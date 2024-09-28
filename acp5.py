from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

# Create 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.title('3D Scatter Plot')
plt.show()
import plotly.express as px

# Load a sample dataset
df = px.data.iris()

# Create an interactive scatter plot
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', size='petal_length', hover_data=['petal_width'])
fig.update_layout(title='Iris Dataset - Interactive Scatter Plot')
fig.show()
import folium

# Create a map centered around a specific location
map_center = [37.7749, -122.4194]  # San Francisco
m = folium.Map(location=map_center, zoom_start=13)

# Add a marker
folium.Marker(location=[37.7749, -122.4194], popup='San Francisco').add_to(m)

# Display the map
m.save('map.html')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Data for plotting
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
line, = ax.plot(x, y)

def update(frame):
    line.set_ydata(np.sin(x + frame / 10))  # Update the data
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, blit=True)
plt.title('Animated Sine Wave')
plt.show()
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Generate random data
data = np.random.rand(10, 12)

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data, cmap='viridis', annot=True)
plt.title('Heatmap Example')
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
df = sns.load_dataset('iris')

# Create a pair plot
sns.pairplot(df, hue='species')
plt.title('Pair Plot of Iris Dataset')
plt.show()
import plotly.express as px

# Sample data for sunburst
data = {
    'labels': ['A', 'B', 'C', 'D', 'E'],
    'parents': ['', 'A', 'A', 'B', 'B'],
    'values': [10, 20, 30, 40, 50]
}

df = px.data.tips()
fig = px.sunburst(data_frame=data, names='labels', parents='parents', values='values')
fig.update_layout(title='Sunburst Chart Example')
fig.show()
