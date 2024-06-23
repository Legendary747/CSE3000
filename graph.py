import matplotlib.pyplot as plt

# Data for the WER (in percentages)
groups = ['NC7-11', 'NC12-16', 'NN7-16', 'NNA', 'NA']
wer_read_whisper = [20.59, 10.81, 35.68, 36.45, 16.22]
wer_read_mms = [44.79, 29.21, 71.06, 71.35, 39.82]
wer_hmi_whisper = [33.60, 27.78, 47.65, 49.15, 34.89]
wer_hmi_mms = [68.41, 54.03, 82.62, 80.98, 59.04]

# Create a line graph for WER Read and HMI
plt.figure(figsize=(10, 6))
plt.plot(groups, wer_read_whisper, marker='o', label='Whisper-large v3 (Read)')
plt.plot(groups, wer_read_mms, marker='o', label='MMS-1b-All (Read)')
plt.plot(groups, wer_hmi_whisper, marker='o', label='Whisper-large v3 (HMI)')
plt.plot(groups, wer_hmi_mms, marker='o', label='MMS-1b-All (HMI)')
plt.xlabel('Groups')
plt.ylabel('WER (%)')
plt.title('Word Error Rate (WER) for Read and HMI Conditions')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()

# Description of groups
group_description = """
Groups:
NC7-11: native children between 7 and 11
NC12-16: native children between 12 and 16
NN7-16: non-native children between 7 and 16
NNA: non-native adults
NA: native adults above 65
"""

print(group_description)
