import matplotlib.pyplot as plt

# Define the processing times for each group and model
processing_times_mms_1b_all = {
    'hmi_NC': 283.84,
    'hmi_NT': 174.92,
    'hmi_NNT': 220.91,
    'hmi_NNA': 701.20,
    'hmi_NA': 784.40,
    'read_NC': 811.98,
    'read_NT': 562.48,
    'read_NNT': 763.87,
    'read_NNA': 785.72,
    'read_NA': 778.46
}

processing_times_mms_1b_l1107 = {
    'hmi_NC': 310.41,
    'hmi_NT': 193.20,
    'hmi_NNT': 253.28,
    'hmi_NNA': 844.77,
    'hmi_NA': 896.16,
    'read_NC': 907.11,
    'read_NT': 586.74,
    'read_NNT': 811.58,
    'read_NNA': 947.02,
    'read_NA': 916.77
}

processing_times_mms_1b_fl102 = {
    'hmi_NC': 290.27,
    'hmi_NT': 178.38,
    'hmi_NNT': 242.11,
    'hmi_NNA': 764.01,
    'hmi_NA': 823.37,
    'read_NC': 933.92,
    'read_NT': 600.67,
    'read_NNT': 853.97,
    'read_NNA': 921.97,
    'read_NA': 930.59
}

processing_times_whisper = {
    'hmi_NC': 1864.48,
    'hmi_NT': 1235.53,
    'hmi_NNT': 1389.33,
    'hmi_NNA': 3222.57,
    'hmi_NA': 4355.76,
    'read_NC': 6364.53,
    'read_NT': 4890.55,
    'read_NNT': 5507.21,
    'read_NNA': 5244.84,
    'read_NA': 6064.87
}

# Plot the processing times for MMS models
groups = list(processing_times_mms_1b_all.keys())
times_mms_1b_all = list(processing_times_mms_1b_all.values())
times_mms_1b_l1107 = list(processing_times_mms_1b_l1107.values())
times_mms_1b_fl102 = list(processing_times_mms_1b_fl102.values())

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(groups, times_mms_1b_all, marker='o', label='MMS-1b-all')
ax.plot(groups, times_mms_1b_l1107, marker='s', label='MMS-1b-l1107')
ax.plot(groups, times_mms_1b_fl102, marker='^', label='MMS-1b-fl102')
ax.set_xlabel('Group')
ax.set_ylabel('Processing Time (seconds)')
ax.set_title('Processing Time for Different MMS Models by Group')
ax.legend(title="Model", loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot the processing times for Whisper and MMS-1b-all
times_whisper = list(processing_times_whisper.values())

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(groups, times_mms_1b_all, marker='o', label='MMS-1b-all')
ax.plot(groups, times_whisper, marker='s', label='Whisper-large-v3')
ax.set_xlabel('Group')
ax.set_ylabel('Processing Time (seconds)')
ax.set_title('Processing Time for Whisper-large-v3 and MMS-1b-all by Group')
ax.legend(title="Model", loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
