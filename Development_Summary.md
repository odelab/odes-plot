# Overview

This project contains a Python script/library for converting Matplotlib objects into Plotly JSON objects, and a Python Flask server program that accepts d3.js code, Plotly JSON objects and data files for plotting graphs on browsers. 

The website does every rendering things on the client site. Chrome browser is tested and the website works fine. Haven't tested compatibility with other browsers yet.

# Design of the Website

## Web Client-side based

The website accepts Plotly JSON objects and d3.script. You can input the d3 scripts in the browser, and you can run the code on the website, and the graph will be shown on the right.

### Submission of data, script and JSON files

Users can upload the data file, d3.js scripts and Plotly JSON objects to the website. 

After user uploads the data file, an unique URL for the data file will be displayed on the screen. The user can use that URL in the d3.js script for accessing the data.

After user uploads either the d3.js script or the Plotly JSON objects, the editor on the left will also be filled with the script content, so that users can have an idea on what the script contains.

If users generated multiple graphs, the graphs will be appended below the pervious graphs, so that users can compare the effects of different scripts on the same data.

### Viewing Graphs & Data Dynamically using Plotly 

Because the website uses Plotly, the users have options to dynamically play with the data. Users can interact with graphs, i.e., change scales, domain, ranges, etc.. The graph will display tooltips of the data.

# Design of the Python matplotlib-to-plotly script

## Plotly JSON Standard

To garantee modularity, the Python-side code library will use the Plotly general graph data JSON abstraction format. A full explanaion of the scheme is here: [Plotly JSON chart schema](http://help.plot.ly/json-chart-schema/).

The script uses Plotly's helper methods to read the mpl objects, and use Python JSON library to turn the Plotly format to JSON objects. It also provides functions to save JSON to files.

This data abstraction format is compatitble with any Plotly library.











