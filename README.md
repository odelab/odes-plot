## Open Dynamic Engineering and Scientific Plotting Project @ Harvey Mudd College

![HMC Seal]
(https://www.hmc.edu/about-hmc/wp-content/uploads/sites/2/2013/05/NEW-HMC-SEAL-BLK.png)

This project aims to develop an online publishing platform that enables scientists and engineers to submit paper, data and graph codes, and dynamically interact with plots.

This project is currently in a very preliminary phase. We intend to use d3.js as the front end for data visualization. We would like to add support for multiple languages in the future, possibly through a kind of intermediate data objects.

### Current Progress
- d3 Notebook: A static page with d3 script editor and data editor. User can update the script in the script editor and get live updated d3 graph on the right side.
- Flask d3 Notebook: d3 Notebook served using Flask. We introduce Flask as the backend to enable data file submission feature. The submitted file's URL is generated using SHA256 algorithm using hashlib.

### To-do List:
- Using plotly.js to turn graphs into dynamic ones
- Python language interface: interfacing matplotlib with d3.js
