# Using functions provided by Plotly.py
# Plotly is a great ploting library. It's amazing how extensive this library
# is.

from __future__ import absolute_import

import json
import os

# potential python compatibility issue; using six to fix that
import six
import six.moves

from plotly import exceptions, tools, utils, version, files

def panda_to_json(figure, resize = True, strip_style = False):
    """ Turn the Panda Series into a JSON data object using tools
        provided by plotly.py

        Positional Arguments:
            fig -- a series from Panda

        Keywords Arguments:
            resize (default is True) -- allow the plotly backend to choose the size
            strip_style (default is False) -- allow plotly to choose style options
    """
    fig = tools.panda_to_plotly(figure, resize=resize, strip_style=strip_style)

    # get the json scheme
    data = json.dumps(fig['data'] if 'data' in fig else [],
                      cls=utils.PlotlyJSONEncoder)
    layout = json.dumps(fig['layout'] if 'layout' in fig else [],
                        cls=utils.PlotlyJSONEncoder)
    # make the total json object
    return str(fig)

def panda_to_plotly(figure, resize = True, strip_style = False):
    """ wrapper function for plotly.tools.mpl_to_plotly
    """
    return tools.panda_to_plotly(figure, resize=resize, strip_style=strip_style)


