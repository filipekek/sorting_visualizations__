import plotly.graph_objects as go
import random

# Generate random data for the visualization
def generate_data(bar_count):
    list_data = random.sample(range(1, bar_count + 1), bar_count)
    # data_dict = {position: value for position, value in enumerate(list_data)}
    return list_data

# Create frames for the animation, highlighting compared bars
def create_frames(list_data, comparing_indices=None):
    x_value = [i for i in range(len(list_data))]
    y_value = list_data
    colors = ["#1f77b4"] * len(list_data)  # Default color for all bars

    if comparing_indices:
        for index in comparing_indices:
            colors[index] = "red"  # Highlight bars being compared

    frame = go.Frame(data=[go.Bar(x=x_value, y=y_value, marker_color=colors)])
    return frame

# Selection sort
def selection_sort(data_list):
    frames = []
    n = len(data_list)
    for key in range(n):
        # Find the index of the smallest element in the unsorted part
        minimum_index = key
        for j in range(key + 1, n):
            # Highlight the current and the compared bar
            frames.append(create_frames(data_list, comparing_indices=[key, minimum_index, j]))
            if data_list[j] < data_list[minimum_index]:
                minimum_index = j

        # Swap the found minimum element with the first unsorted element
        data_list[key], data_list[minimum_index] = data_list[minimum_index], data_list[key]

        # Add the frame after swapping
        frames.append(create_frames(data_list, comparing_indices=[key, minimum_index]))
    
    return data_list, frames

# Generate initial data
prime_data = generate_data(10)  # Adjust the number of bars as needed
data_list, frames = selection_sort(prime_data.copy())
x_value = [i for i in range(len(prime_data))]
# Initialize the Plotly chart
chart = go.Figure(
    data=[go.Bar(x=x_value, y=prime_data, marker_color="#1f77b4")],
    layout=go.Layout(
        title="Selection Sort Visualization",
        xaxis=dict(title="<br><br>Selection Sort is a simple algorithm that repeatedly selects the smallest element from the unsorted part of the list and swaps it with the first unsorted element, gradually sorting the list.</sup>", showticklabels=False),  # Hide x-axis values
        yaxis=dict(showticklabels=False),  # Hide y-axis values
        updatemenus=[
            dict(
                type="buttons",
                showactive=False,
                buttons=[
                    dict(label="Play", method="animate", args=[None]),
                    dict(
                        label="Pause",
                        method="animate",
                        args=[
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": True},
                                "mode": "immediate",
                                "transition": {"duration": 0},
                            },
                        ],
                    ),
                ],
            )
        ],
    ),
    frames=frames,
)

chart.update_layout(transition_duration=0)
chart.write_html('selection_sort_visualization.html')
chart.show(config = {'displayModeBar': False})