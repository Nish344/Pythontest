import plotly.express aspx
# Sample data for demonstration
data = {
'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Houston'],
'Lat': [40.7128, 37.7749, 34.0522, 41.8781, 29.7604],
'Lon': [-74.0060, - 122.4194, - 118.2437, -87.6298, -95.3698],
'Population': [8175133, 870887, 3971883, 2716000, 2328000]
}
# Create amap
fig = px.scatter_geo(data, lat='Lat', lon='Lon', text='City', size='Population',
projection='natural earth', title='Population of Cities')
fig.update_traces(textposition='top center')
fig.show()

import plotly.graph_objects as godata = [
{'x': [1, 2, 3, 4, 5], 'y': [6, 7, 2, 4, 5]},
{'x': [6, 7, 8, 9, 10], 'y': [1, 3, 5, 7, 9]}
]
fig = go.Figure()
for i in range(len(data)):
fig.add_trace(go.Scatter(x=data[i]['x'], y=data[i]['y'], mode='lines'))
fig.update_layout(title='Time Series', xaxis_title='Time', yaxis_title='Value')
fig.show()

# Import necessary libraries
import plotly.graph_objects as go
import numpy as npx = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
z = np.random.randn(100, 100)
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])
fig.update_layout(title='3D Scatter Plot', scene=dict(xaxis_title='X Axis', yaxis_title='Y Axis', zaxis_title='Z
Axis'))
fig.show()

# Import the necessary libraries
from bokeh.plotting import figure, show
# Create a line plot
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
line = figure(title="Line Plot", x_axis_label="x", y_axis_label="y")
line.line(x, y, line_width=2)
# Create a bar plot
x = ["a", "b", "c", "d", "e"]
y = [1, 2, 3, 4, 5]
bar = figure(title="Bar Plot", x_range=x)
bar.vbar(x=x, top=y, legend_label="values", width=0.5, bottom=0)
# Create a pie chart
data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
pie = figure(title="Pie Chart")
pie.wedge(x=1, y=1, radius=0.5, start_angle=0.5, end_angle=6.28, line_color="white", fill_color="blue",
legend_label="values")
# Show the plots
show(line)
show(bar)
show(pie)

from bokeh.plotting import figure, output_file, show
from bokeh.models import Label
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
# Output to static HTML file
output_file("line_graph_with_annotations.html")
# Create a figure
p = figure(title="Bokeh Line Graph with Annotations", x_axis_label='X-axis', y_axis_label='Y-axis')
# Plot the line
p.line(x, y, line_width=2, line_color="blue", legend_label="Line Function: y = 2x")
# Add an annotation
annotation = Label(x=3, y=6, text="Important Point", text_font_size="10pt", text_color="red")
p.add_layout(annotation)
# Add legend
p.legend.location = "top_left"
p.legend.click_policy = "hide"
# Show the plot
show(p)

import seaborn as sns
import matplotlib.pyplot asplt
# Load a sample dataset
tips = sns.load_dataset("tips")
# Set the aesthetic style of the plot
sns.set(style="whitegrid")
# Create a scatter plot using Seaborn
sns.scatterplot(x="total_bill", y="tip", style="time", size="size", data=tips)
# Customize the plot further using Seaborn aesthetic functions
sns.despine() # Remove the top and right spines from the plot
# Set custom labels and title
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.title("Scatter Plot of Total Bill vs Tip")
# Show the plot
plt.show()

import matplotlib.pyplot asplt
def formatted_linear_plot():
# Sample data
x = [1, 2, 3, 4, 5, 6]
y = [3, 7, 9, 11, 14, 18]
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Linear Function: y = 2x')
# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Formatted Linear Plot Example')
plt.legend()
plt.grid(True) # Add a grid for better readability
plt.show()
# Call the function to generate the formatted linear plot
formatted_linear_plot()

import matplotlib.pyplot asplt
def linear_plot():
# Sample data
x = [1, 2, 3, 4, 5]
y = [3, 7, 9, 11, 14]
# Plotting the data
plt.plot(x, y, label='Linear Function: y = 2x')
# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Linear Plot Example')
plt.legend()
plt.show()
# Call the function to generate the plot
linear_plot()
