import torch
from transformers import AutoProcessor, AutoModelForCTC
from datasets import load_dataset
import jiwer

# Load the processor and model
model_name = "facebook/mms-1b-all"
processor = AutoProcessor.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCTC.from_pretrained(model_name)

# Check for GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
if torch.cuda.is_available():
    print(f"Using GPU: {torch.cuda.get_device_name(0)}")
else:
    print("Using CPU")

model.to(device)

# Load the Dutch FLEUR dataset and specify the test split
dataset = load_dataset("google/fleurs", "nl_nl", split='test')

# Initialize variables for WER calculation
transform = jiwer.Compose([
    jiwer.RemovePunctuation(),
    jiwer.ToLowerCase()
])
total_wer = 0
sample_count = 0

# Iterate through the test dataset and compute WER for each sample
for i, sample in enumerate(dataset):
    # Preprocess the audio data
    inputs = processor(sample["audio"]["array"], sampling_rate=sample["audio"]["sampling_rate"], return_tensors="pt", padding=True)
    input_values = inputs.input_values.to(device)

    # Run inference
    with torch.no_grad():
        logits = model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)

    # Get the predicted text
    predicted_text = processor.batch_decode(predicted_ids)[0]

    # Calculate WER for the current sample
    transcription = sample["raw_transcription"]
    wer = jiwer.wer(transform(transcription), transform(predicted_text))

    # Update cumulative WER
    total_wer += wer
    sample_count += 1
    cumulative_wer = total_wer / sample_count

    # Print the results for the current sample
    print(f"Sample {i + 1}:")
    print(f"Original Text: {transcription}")
    print(f"Predicted Text: {predicted_text}")
    print(f"WER: {wer}")
    print(f"Cumulative WER: {cumulative_wer}\n")

# Final cumulative WER
print(f"Final Cumulative WER: {cumulative_wer}")
