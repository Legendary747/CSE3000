import matplotlib.pyplot as plt
import numpy as np

# Processing times extracted from the log files
processing_times_beam_5 = {
    'hmi_NC': 1864.48,
    'hmi_NT': 1339.21,
    'hmi_NNT': 1550.55,
    'hmi_NNA': 3168.51,
    'hmi_NA': 4661.74,
    'read_NC': 6364.53,
    'read_NT': 5537.89,
    'read_NNT': 5685.79,
    'read_NNA': 5981.94,
    'read_NA': 6053.17
}

processing_times_beam_6 = {
    'hmi_NC': 1881.10,
    'hmi_NT': 1401.84,
    'hmi_NNT': 1640.57,
    'hmi_NNA': 3665.37,
    'hmi_NA': 4996.96,
    'read_NC': 6795.95,
    'read_NT': 5483.23,
    'read_NNT': 6104.24,
    'read_NNA': 6080.63,
    'read_NA': 7105.20
}

processing_times_beam_7 = {
    'hmi_NC': 2084.79,
    'hmi_NT': 1397.56,
    'hmi_NNT': 1600.69,
    'hmi_NNA': 3806.60,
    'hmi_NA': 5163.95,
    'read_NC': 7558.11,
    'read_NT': 5836.04,
    'read_NNT': 6560.40,
    'read_NNA': 6260.24,
    'read_NA': 7234.59
}

# Combine the processing times into a single dictionary
groups = list(processing_times_beam_5.keys())
processing_times = {group: [processing_times_beam_5[group], processing_times_beam_6[group], processing_times_beam_7[group]] for group in groups}

# Create a line chart to visualize the processing times with groups as x-axis
fig, ax = plt.subplots(figsize=(14, 8))

# Define colors and markers for better distinction
colors = ['b', 'g', 'r']
markers = ['o', 's', 'D']

# Plot each beam size's processing times
for i, beam_size in enumerate(['Beam size = 5', 'Beam size = 6', 'Beam size = 7']):
    times = [processing_times[group][i] for group in groups]
    ax.plot(groups, times, label=beam_size, color=colors[i], linewidth=3, markersize=8, marker=markers[i])

# Set the x-axis labels
ax.set_xlabel('Group')
ax.set_ylabel('Processing Time (seconds)')
ax.set_title('Processing Time for Different Groups by Beam Size')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add grid lines for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add a legend outside of the plot area
ax.legend(title="Beam Size", loc='upper left')

# Tight layout for better spacing
plt.tight_layout()

plt.show()
