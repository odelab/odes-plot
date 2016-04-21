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

I think I'll use d3.js as my graphing library.

## General Graph Data Abstraction

To garantee modularity, the main ploting library will use a general graph data abstraction format. 

We need to first design the methods and values for the abstracted data format. The abstracted graph object will certainly have a lot of getters and setters. We also need to contain format options in the abstracted data object.

Some example format options include: title, axes, fonts, etc..

This data abstraction format will be compatitble with Plotly's.

## Compatibility with Multiple Languages

Similar to Plotly, we need to write a different parser for each different language. Right now I plan to provide compatibility for Matlab, Python (matlplotlib), and R. Since I am most familiar with Python, I will right the parser for Python first. 

One choice for the parser design is that I use Javascript to write parsers for all the languages. The parser will not need server support. I am not sure about whether to use node.js or jquery. I need to learn more about the Javascript string manipulation library.

Another choice will be to write parser for that language in that language. For examle, write the Python parser in Python; write the Matlab parser in Matlab and so on. 

I suspect the second method will be easier. I think most of the graphing libraries will be OOP. So writing the parser in that specific language will be easier, as the parser can directly access the methods of that graph object.











