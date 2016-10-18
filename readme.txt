Title: pyMap v1.0
Author: Daniel Hagquist
Date: 12/13/2015


Note: If downloading from Google Drive, please download the zip file contained within the CCM folder. Google Docs will automatically append file extensions to some unknown file types. For example, downloading the CCM folder, the file “ccm_template.mxd” will be appended with the extension “ccm_template_mxd.doc”, which will cause an error when running the program.


USER MANUAL


Before Running the Program:

You will need the following libraries installed on your computer in order to run this program:
matplotlib (http://matplotlib.org)
osgeo (http://www.osgeo.org/)


Using the program:

To begin, open the file "pyMap.py" and run it.

At the prompt, enter the path and name of a shapefile you would like to process. Press the Enter key to use the default shapefile included in this package*.

Type the attribute of interest. This must be an integer or real number in order to process, as this program currently does not support nominal and categorical classes. The only two usable attributes contained within the default shapefile are "pop_est" (estimated population) and "gdp_md_est" (estimated gross domestic product).

At the next prompt, enter the desired number of classes ranging from 3 to 6**. Press Enter.

Your map will appear in a small window. You are able to maximize the window for a better viewing experience.

The color scheme is from colorbrewer2.org. If you would like to use your own color scheme, it is recommended you use this site. Find the "colors" array in the code and edit the hex codes.


* The shapefile included is this package was obtained from Natural Earth (http://www.naturalearthdata.com/downloads/). It is in the data folder and named "ne_110m_admin_0_countries.shp".

** Using a function borrowed from Daniel J. Lewis, the Jenks natural breaks are then calculated. This is popular method of splitting up data ranges into nicely portioned chunks so that representation (especially on a choropleth map) is more intuitive.


Troubleshooting:

If you get an error at any point in the program, these may be the reasons why:

1. You have not installed the required libraries or they are not  working properly.

2. The shapefile path and/or filename were wrong.

3. The attribute you typed does not exist in the database file for the shapefile.

4. The attribute you typed exists, but it is not an integer, float, or double.


Credit:

References provided by Professor Ningchuan Xiao (OSU)
Natural Breaks (Jenks) code provided by Daniel J. Lewis
