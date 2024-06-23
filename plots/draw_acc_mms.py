import matplotlib.pyplot as plt

# WER, CER, and WIL data for MMS-1b-all
wer_read_mms_1b_all = [44.79, 29.21, 71.04, 71.35, 39.82]
cer_read_mms_1b_all = [20.57, 12.77, 33.46, 31.82, 18.87]
wil_read_mms_1b_all = [63.20, 42.99, 87.03, 87.39, 56.81]

wer_hmi_mms_1b_all = [68.41, 54.03, 82.62, 80.98, 59.04]
cer_hmi_mms_1b_all = [36.75, 25.44, 46.12, 46.41, 31.58]
wil_hmi_mms_1b_all = [85.08, 72.84, 93.90, 93.21, 76.48]

groups = ['NC', 'NT', 'NNT', 'NNA', 'NA']

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Plot for Read Speech
axes[0].plot(groups, wer_read_mms_1b_all, label='WER', marker='o', color='b')
axes[0].plot(groups, cer_read_mms_1b_all, label='CER', marker='s', color='g')
axes[0].plot(groups, wil_read_mms_1b_all, label='WIL', marker='D', color='r')
axes[0].set_title('Read Speech - Error Rates for MMS-1b-all')
axes[0].set_xlabel('Group')
axes[0].set_ylabel('Percentage')
axes[0].legend()
axes[0].grid(True)

# Plot for HMI Speech
axes[1].plot(groups, wer_hmi_mms_1b_all, label='WER', marker='o', color='b')
axes[1].plot(groups, cer_hmi_mms_1b_all, label='CER', marker='s', color='g')
axes[1].plot(groups, wil_hmi_mms_1b_all, label='WIL', marker='D', color='r')
axes[1].set_title('HMI Speech - Error Rates for MMS-1b-all')
axes[1].set_xlabel('Group')
axes[1].set_ylabel('Percentage')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.show()
