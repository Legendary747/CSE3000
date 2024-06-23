import jiwer
import pandas as pd
from jiwer import wer, cer, wil
import os

# Define the base file path and file names
base_path = os.getcwd()
# base_path = os.path.join(base_path, 'Result', 'Whisper', 'beam-5')
base_path = os.path.join(base_path, 'Result', 'MMS', 'mms-1b-all')
# file_names = [
#     "test_read_group1_Whisper_final.xlsx",
#     "test_read_group2_Whisper_final.xlsx",
#     "test_read_group3_Whisper_final.xlsx",
#     "test_read_group4_Whisper_final.xlsx",
#     "test_read_group5_Whisper_final.xlsx"
# ]

# file_names = [
#     "test_hmi_group1_Whisper_final.xlsx",
#     "test_hmi_group2_Whisper_final.xlsx",
#     "test_hmi_group3_Whisper_final.xlsx",
#     "test_hmi_group4_Whisper_final.xlsx",
#     "test_hmi_group5_Whisper_final.xlsx"
# ]

# file_names = [
#     "test_read_group1_MMS_final.xlsx",
#     "test_read_group2_MMS_final.xlsx",
#     "test_read_group3_MMS_final.xlsx",
#     "test_read_group4_MMS_final.xlsx",
#     "test_read_group5_MMS_final.xlsx"
# ]

file_names = [
    "test_hmi_group1_MMS_final.xlsx",
    "test_hmi_group2_MMS_final.xlsx",
    "test_hmi_group3_MMS_final.xlsx",
    "test_hmi_group4_MMS_final.xlsx",
    "test_hmi_group5_MMS_final.xlsx"
]

# Initialize empty lists to hold ground truth and recognized transcriptions
all_ground_truths = []
all_recognized = []

# Loop through each file and concatenate the data
for file_name in file_names:
    file_path = os.path.join(base_path, file_name)
    # Load the Excel file
    data = pd.read_excel(file_path)

    # Remove rows where either 'ground_truth_transformed' or 'transcription_transformed' is 'nan'
    data = data[(data['ground_truth_transformed'] != 'nan') & (data['transcription_transformed'] != 'nan')]

    # Ensure all values are strings
    data['ground_truth_transformed'] = data['ground_truth_transformed'].astype(str)
    data['transcription_transformed'] = data['transcription_transformed'].astype(str)

    # Append to the lists
    all_ground_truths.extend(data['ground_truth_transformed'].tolist())
    all_recognized.extend(data['transcription_transformed'].tolist())

WordOutput = jiwer.process_words(all_ground_truths, all_recognized)

# Calculate and print the WER, CER, and WIL
print("Cumulative WER:", wer(all_ground_truths, all_recognized))
print("Cumulative CER:", cer(all_ground_truths, all_recognized))
print("Cumulative WIL:", wil(all_ground_truths, all_recognized))

print(f"Deletions: {WordOutput.deletions}")
print(f"Insertions: {WordOutput.insertions}")
print(f"Substitutions: {WordOutput.substitutions}")