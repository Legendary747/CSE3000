import jiwer
import pandas as pd
from jiwer import wer, cer, wil
import os

# # Define the file path
# file_path = os.path.join(os.getcwd(), "MMS_Result", "test_read_group1_MMS.xlsx")
# Define the file path
# file_path = os.path.join(os.getcwd(), "test_read_group4_MMS_final.xlsx")
file_path = os.path.join(os.getcwd(), "test_hmi_group4_Whisper_final.xlsx")
# Load the Excel file
data = pd.read_excel(file_path)

# Remove rows where either 'ground_truth_transformed' or 'transcription_transformed' is 'nan'
data = data[(data['ground_truth_transformed'] != 'nan') & (data['transcription_transformed'] != 'nan')]

# Ensure all values are strings
data['ground_truth_transformed'] = data['ground_truth_transformed'].astype(str)
data['transcription_transformed'] = data['transcription_transformed'].astype(str)

# Get the lists of ground truth and recognized transcriptions
ground_truth_list = data['ground_truth_transformed'].tolist()
recognized_list = data['transcription_transformed'].tolist()


# Calculate and print the WER
print("Cumulative WER:", wer(ground_truth_list, recognized_list))
print("Cumulative CER:", cer(ground_truth_list, recognized_list))
print("Cumulative WIL:", wil(ground_truth_list, recognized_list))
WordOutput = jiwer.process_words(ground_truth_list, recognized_list)
print(f"Deletions: {WordOutput.deletions}")
print(f"Insertions: {WordOutput.insertions}")
print(f"Substitutions: {WordOutput.substitutions}")
