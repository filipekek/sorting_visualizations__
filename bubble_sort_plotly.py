import plotly.graph_objects as go
import random

# Generate random data for the visualization
def generate_data(bar_count):
    list_data = random.sample(range(1, bar_count + 1), bar_count)
    data_dict = {position: value for position, value in enumerate(list_data)}
    return data_dict

# Create frames for the animation, highlighting compared bars
def create_frames(data_dict, comparing_indices=None):
    x_value = list(data_dict.keys())
    y_value = list(data_dict.values())
    colors = ["#1f77b4"] * len(data_dict)  # Default color for all bars

    if comparing_indices:
        for index in comparing_indices:
            colors[index] = "red"  # Highlight bars being compared

    frame = go.Frame(data=[go.Bar(x=x_value, y=y_value, marker_color=colors)])
    return frame

# Bubble sort logic with visualization frames
def bubble_sort(data_dict):
    n = len(data_dict)
    frames = []
    data_list = list(data_dict.values())  # Convert dict values to a list for sorting

    for i in range(n):
        for j in range(0, n - i - 1):
            frames.append(create_frames({k: v for k, v in enumerate(data_list)}, comparing_indices=[j, j + 1]))
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
                updated_dict = {k: v for k, v in enumerate(data_list)}  # Update dict to match the sorted list
                frames.append(create_frames(updated_dict, comparing_indices=[j, j + 1]))
    return data_list, frames

# Generate initial data
prime_data = generate_data(10)  # Adjust the number of bars as needed
data_list, frames = bubble_sort(prime_data)

# Initialize the Plotly chart
chart = go.Figure(
    data=[go.Bar(x=list(prime_data.keys()), y=list(prime_data.values()), marker_color="#1f77b4")],
    layout=go.Layout(
        title="Bubble Sort Visualization",
        xaxis=dict(title="<br><br>Bubble Sort is a simple algorithm that repeatedly compares and swaps adjacent elements if they are in the wrong order, gradually sorting the list.</sup>", showticklabels=False),  # Hide x-axis values
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
chart.write_html('bubble_sort_visualization.html')
chart.show(config = {'displayModeBar': False})