# Overview

This project contains a Python script/library for converting Matplotlib objects into Plotly JSON objects, and a Python Flask server program that accepts d3.js code, Plotly JSON objects and data files for plotting graphs on browsers. 

The website does every rendering things on the client site. Chrome browser is tested and the website works fine. Haven't tested compatibility with other browsers yet.

# Design

## Web Client-side based

The website accepts 

### Submission of Manuscript

Users submit their manuscript including the corresponding data and code for plotting the data. The submitted code and data should be minimal: the least required amount of code and data required to plot the graph shown in the manuscript main body.

Supporting the dependencies used by different users would be potentially troublesome. 

### Viewing Graphs & Data Dynamically

Users can view already submitted manucript. Users have options to dynamically view the data and plot graphs. Users can interact with graphs, i.e., change scales, focus, etc.. Graph and data are separated.

During the semester, d3.js and Plotly.js are used separately to achieve the graphing function. Using d3.js can achieve basic graphing functions, where as plotly.js can achieve dynamic interation easier than d3.js. 

## General Graph Data Abstraction

To garantee modularity, the ploting Python script uses a general graph data abstraction format. (in accordance with Plotly.js's JSON format)

Some example format options include: title, axes, fonts, etc..

This data abstraction format will be compatitble with Plotly's.

## Compatibility with Multiple Languages

A Python library is written to convert matplotlib object into JSON file that the website JS can recognize and plot the graph. The Python library written is essentially a wrapper for some of the core functions of Plotly.js. The difference is that this library doesn't require login into Plotly website, unlike the original Plotly library.







