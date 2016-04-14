# (*) To communicate with Plotly's server, sign in with credentials file
import plotly.plotly as py

# (*) Useful Python/Plotly tools
import plotly.tools as tls

# (*) Graph objects to piece together plots
from plotly.graph_objs import *

import numpy as np  # (*) numpy for math functions and arrays

import matplotlib.pyplot as plt # (*) import matplotlib

# Package all mpl plotting commands inside one function
def plot_mpl_fig():

    # Make two time arrays
    t1 = np.arange(0.0, 2.0, 0.1)
    t2 = np.arange(0.0, 2.0, 0.01)

    # N.B. .plot() returns a list of lines.  
    # The "l1, = plot" usage extracts the first element of the list 
    # into l1 using tuple unpacking.  
    # So, l1 is a Line2D instance, not a sequence of lines
    l1, = plt.plot(t2, np.exp(-t2), label='decaying exp.')
    l2, l3 = plt.plot(t2, np.sin(2 * np.pi * t2), '--go',
                      t1, np.log(1 + t1), '.')
    l4, = plt.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 'rs-.')

    # Add axis labels and title
    plt.xlabel('time')
    plt.ylabel('volts')
    plt.title('Damped oscillation')

    return (l1, l2, l3, l4)  # return line objects (for legend, later)

# Plot it!
plot_mpl_fig()

# N.B. get matplotlib figure object and assign a variable to it
# has to use .gcf()!!!
mpl_fig1 = plt.gcf()

import mpltojson
mpltojson.save_mpl("JSONGraph",mpl_fig1,"/Users/jingnanshi/Documents")

print mpltojson.mpl_to_json(mpl_fig1)
