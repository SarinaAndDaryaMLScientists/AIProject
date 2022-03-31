# importing the modules
from bokeh.plotting import figure, output_file, show
import numpy as np
import pandas as pd
from bokeh.io import curdoc
from bokeh.io import curdoc, show
from bokeh.models import ColumnDataSource, Grid, HexTile, LinearAxis, Plot

# file to save the model
output_file("gfg.html")

# instantiating the figure object
graph = figure(title="Bokeh Hexagon Bin Graph")
curdoc().theme = 'night_sky'

# the points to be plotted
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# plotting the graph for all of these
graph.hexbin(x, y, size=1, fill_color='#4292c6')
# a = HexTile()
# displaying the model
show(graph)
