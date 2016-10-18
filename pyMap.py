"""
PyMap v1.0
Author: Daniel Hagquist
Date:12/13/2015
"""

import sys
import matplotlib.pyplot as plt
from osgeo import ogr
from jenks import *

## PRINT TITLE SCREEN
print 'pyMap v1.0'
print 'Author: Daniel Hagquist'
print 'Date: 12/13/2015'
print

# LOAD SHAPEFILE
driver = ogr.GetDriverByName("ESRI Shapefile")
print 'Type the path of the shapefile (e.g. data/shapefile.shp) or press'
print 'Enter to use the default shapefile (ne_110m_admin_0_countries.shp).'
input = raw_input('--> ')
if len(input) > 4: fname = input
else: fname = 'data/ne_110m_admin_0_countries.shp'
vector = driver.Open(fname, 0)
if vector is None: print 'Error loading shapefile.'
else: print 'Shapefile successfully loaded.'
print

## LOAD DATA INFORMATION
layer = vector.GetLayer(0)
total_records = layer.GetFeatureCount()

## GET ATTRIBUTE FROM USER
print 'Type the attribute of interest (e.g. gdp_md_est) or press Enter'
print 'to use the default attribute (pop_est).'
input = raw_input('--> ')
if len(input) > 0: field = input
else: field = 'pop_est'
print

## GET NUMBER OF CLASSES FROM USER AND INITIALIZE COLOR SCHEME
input = raw_input('Enter the desired number of classes (3 - 6): ')
num_classes = int(input)
while num_classes < 3 or num_classes > 6:
    print 'Invalid input.'
    input = raw_input('Enter the desired number of classes (3 - 6): ')
    num_classes = int(input)
print 'Using ' + str(num_classes) + '.'
colors = [ '#eff3ff', '#c6dbef', '#9ecae1', '#6baed6', '#3182bd', '#08519c' ]
print

# CALCULATE JENKS INTERVALS
values = []
for i in range(total_records):
    feature = layer.GetFeature(i)
    if feature.GetField(field) > 0:
        values.append(feature.GetField(field))
breaks = getJenksBreaks(values, num_classes)
print 'Producing choropleth map...'

# DISPLAY GEOMETRY
def plot_lines(geom, plt):
    points = geom.GetPoints()
    line = [[p[0], p[1]] for p in points]
    l = plt.Polygon(line, closed=False, fill=False, edgecolor='blue')
    plt.gca().add_line(l)

def plot_rings(geom, plt, colors, num_classes, feature):
    poly = []
    color = 'white'
    for ring in geom:
        points = ring.GetPoints()
        poly += [[p[0], p[1]] for p in points]
    # There must be a more elegant way to do this, but this will work for now.
    if num_classes == 3:
        if feature.GetField(field) >  breaks[0] and feature.GetField(field) < breaks[1]: color = colors[0]
        if feature.GetField(field) >= breaks[1] and feature.GetField(field) < breaks[2]: color = colors[2]
        if feature.GetField(field) >= breaks[2]: color = colors[4]
    if num_classes == 4:
        if feature.GetField(field) >  breaks[0] and feature.GetField(field) < breaks[1]: color = colors[0]
        if feature.GetField(field) >= breaks[1] and feature.GetField(field) < breaks[2]: color = colors[2]
        if feature.GetField(field) >= breaks[2] and feature.GetField(field) < breaks[3]: color = colors[4]
        if feature.GetField(field) >= breaks[3]: color = colors[5]
    if num_classes == 5:
        if feature.GetField(field) >  breaks[0] and feature.GetField(field) < breaks[1]: color = colors[1]
        if feature.GetField(field) >= breaks[1] and feature.GetField(field) < breaks[2]: color = colors[2]
        if feature.GetField(field) >= breaks[2] and feature.GetField(field) < breaks[3]: color = colors[3]
        if feature.GetField(field) >= breaks[3] and feature.GetField(field) < breaks[4]: color = colors[4]
        if feature.GetField(field) >= breaks[4]: color = colors[5]
    if num_classes == 6:
        if feature.GetField(field) >  breaks[0] and feature.GetField(field) < breaks[1]: color = colors[0]
        if feature.GetField(field) >= breaks[1] and feature.GetField(field) < breaks[2]: color = colors[1]
        if feature.GetField(field) >= breaks[2] and feature.GetField(field) < breaks[3]: color = colors[2]
        if feature.GetField(field) >= breaks[3] and feature.GetField(field) < breaks[4]: color = colors[3]
        if feature.GetField(field) >= breaks[4] and feature.GetField(field) < breaks[5]: color = colors[4]
        if feature.GetField(field) >= breaks[5]: color = colors[5]
    l = plt.Polygon(poly, closed=True, fill=True, facecolor=color, edgecolor='black', alpha=0.5)
    plt.gca().add_line(l)

def draw_layer(layer, plt):
    i = 0
    for f in layer:
        feature = layer.GetFeature(i)
        geom = f.GetGeometryRef()
        geomtype = geom.GetGeometryName()
        if geomtype == "MULTIPOLYGON":
            for geom1 in geom:
                plot_rings(geom1, plt, colors, num_classes, feature)
        elif geomtype == "POLYGON":
            plot_rings(geom, plt, colors, num_classes, feature)
        elif geomtype == "LINESTRING":
            plot_lines(geom, plt)
            pass
        i = i + 1

draw_layer(layer, plt)
vector.Destroy()
plt.axis('equal')
plt.show()
