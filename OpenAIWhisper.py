import time
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import soundfile as sf
import os
import jiwer  # Ensure jiwer is installed: pip install jiwer
import pandas as pd  # Add pandas for handling data and exporting to Excel

# Set up device and data types
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3"

# Load model and processor
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)
processor = AutoProcessor.from_pretrained(model_id)

# Create the pipeline
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)

# Define base paths
base_path = os.getcwd()
audio_base_paths = {
    'test_hmi_group': os.path.join(base_path, "Jasmin1.0/Data/data/audio/wav/comp-p/nl"),
    # 'test_read_group': os.path.join(base_path, "Jasmin1.0/Data/data/audio/wav/comp-q/nl")
}

text_file_paths = ([
                      os.path.join(base_path, f"JASMIN-Kaldi_processed/nl/test_hmi_group{i}", "text") for i in
                      range(1, 6)
                  ]
                  #  + [
                  #     os.path.join(base_path, f"JASMIN-Kaldi_processed/nl/test_read_group{i}", "text") for i in
                  #     range(1, 6)
                  # ]
                   )


def save_to_excel(data_records, iteration, group_name):
    df = pd.DataFrame(data_records)
    output_dir = os.path.join(base_path, group_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = os.path.join(output_dir, f"{group_name}_Whisper_{iteration}.xlsx")
    df.to_excel(output_path, index=False)
    print(f"Data saved to Excel file at: {output_path}")
    return output_path

print(text_file_paths)
print(audio_base_paths)

# Initialize log file
log_file_path = os.path.join(base_path, "processing_log_Whisper.txt")
with open(log_file_path, 'w') as log_file:
    log_file.write("Processing Log\n")
    log_file.write("=" * 30 + "\n")

for text_file_path in text_file_paths:
    startT = time.time()

    all_ground_truths = []
    all_transcriptions = []
    data_records = []

    # Determine the group name from the path
    group_name = os.path.basename(os.path.dirname(text_file_path))
    print(group_name)
    group_type = 'test_hmi_group' if 'test_hmi_group' in text_file_path else 'test_read_group'
    audio_base_path = audio_base_paths[group_type]

    with open(text_file_path, 'r') as file:
        lines = file.readlines()

    for idx, line in enumerate(lines, 1):  # Start index from 1
        if idx % 100 == 0:
            print(f"Processing line {idx}/{len(lines)}")

        parts = line.strip().split(' ', 1)
        if len(parts) != 2:
            continue

        audio_info, ground_truth = parts
        speaker_id, audio_name, start_time, end_time = audio_info.split('-')
        start_time = float(start_time)
        end_time = float(end_time)

        # Construct audio path
        audio_path = os.path.join(audio_base_path, f"{audio_name}.wav")

        # Check if the file exists
        if not os.path.exists(audio_path):
            print(f"Audio file does not exist: {audio_path}")
            continue

        try:
            # Read the entire audio file to get sample rate
            audio_input, sample_rate = sf.read(audio_path)

            # Calculate start and end samples
            start_sample = int(start_time * sample_rate)
            end_sample = int(end_time * sample_rate)

            # Slice the audio
            audio_segment = audio_input[start_sample:end_sample]

            # Ensure the audio is resampled to 16,000 Hz if not already
            if sample_rate != 16000:
                raise ValueError(f"Unexpected sample rate: {sample_rate}")

            # Convert stereo to mono if necessary
            if audio_segment.ndim > 1:
                # Keep only the left channel (channel 0)
                audio_segment = audio_segment[:, 0]

            # Process the audio input
            inputs = processor(audio_segment, sampling_rate=sample_rate, return_tensors="pt").to(device)

            # Perform speech recognition with specified temperature and beam size
            result = pipe(audio_segment, generate_kwargs={"num_beams": 7, "language": "dutch"})
            transcription = result["text"]

            # Define transformation for WER calculation
            transformation = jiwer.Compose([
                jiwer.ToLowerCase(),
                jiwer.RemovePunctuation(),
                jiwer.Strip(),
                jiwer.RemoveMultipleSpaces()
            ])

            # Ensure transformations do not result in empty strings
            ground_truth_transformed = transformation(ground_truth)
            transcription_transformed = transformation(transcription)
            if not ground_truth_transformed.strip() or not transcription_transformed.strip():
                print(f"Skipping empty transformation result for index {idx}, due to too short audio segment.")
                continue

            # Append ground truth and transcription to lists
            all_ground_truths.append(ground_truth_transformed)
            all_transcriptions.append(transcription_transformed)

            # Store the data for Excel output
            data_records.append({
                "speaker_id": speaker_id,
                "audio_name": audio_name,
                "ground_truth_transformed": ground_truth_transformed,
                "transcription_transformed": transcription_transformed
            })

            # Save every 1000 lines
            if idx % 1000 == 0:
                save_to_excel(data_records, idx // 1000, group_name)

        except Exception as e:
            print(f"Error at index {idx}, audio file: {audio_path}")
            print(e)
            continue

    try:
        # Calculate cumulative WER with transformations
        cumulative_wer = jiwer.wer(all_ground_truths, all_transcriptions)
        print(f"Cumulative WER: {cumulative_wer}")
    except Exception as e:
        print(e)

    # Note the time taken for the process
    endT = time.time()
    total_time = endT - startT
    print(f"Total processing time: {total_time:.2f} seconds")

    # Create a DataFrame and save to Excel
    output_path = save_to_excel(data_records, "final", group_name)

    # Log the results
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"Text file processed: {text_file_path}\n")
        log_file.write(f"Output saved to: {output_path}\n")
        log_file.write(f"Cumulative WER: {cumulative_wer}\n")
        log_file.write(f"Total processing time: {total_time:.2f} seconds\n")
        log_file.write("=" * 30 + "\n")

print(f"All processing complete. Log file saved at: {log_file_path}")
