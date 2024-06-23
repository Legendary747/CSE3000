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

# Calculate total processing time for each model
total_time_mms_1b_all = sum(processing_times_mms_1b_all.values())
total_time_whisper = sum(processing_times_whisper.values())

# Calculate how many times MMS is faster than Whisper
mms_speed_factor = total_time_whisper / total_time_mms_1b_all

print(total_time_mms_1b_all, total_time_whisper, mms_speed_factor)
