import torch

# Check if CUDA is available
if torch.cuda.is_available():
    print(f"CUDA is available. Using GPU: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA is not available. Using CPU.")

# Example tensor operation to verify GPU usage
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.rand(5, 5).to(device)
y = torch.rand(5, 5).to(device)
z = x + y

print(z)

print(torch.__version__)