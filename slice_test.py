import soundfile as sf
import os

# Define paths
base_path = os.getcwd()
audio_base_path = os.path.join(base_path, "Jasmin1.0/Data/data/audio/wav/comp-q/nl")

# Example data from the script for the first slice
audio_name = "fn000049"
start_time = 100.2178
end_time = 101.7831

# Construct audio path
audio_path = os.path.join(audio_base_path, f"{audio_name}.wav")

# Check if the file exists
if not os.path.exists(audio_path):
    print(f"Audio file does not exist: {audio_path}")
else:
    # Read the entire audio file to get sample rate
    audio_input, sample_rate = sf.read(audio_path)

    # Calculate start and end samples
    start_sample = int(start_time * sample_rate)
    end_sample = int(end_time * sample_rate)

    # Slice the audio
    audio_segment = audio_input[start_sample:end_sample]

    # Define output path
    output_path = os.path.join(base_path, "human_try.wav")

    # Save the sliced audio segment
    sf.write(output_path, audio_segment, sample_rate)
    print(f"Audio segment saved to: {output_path}")
