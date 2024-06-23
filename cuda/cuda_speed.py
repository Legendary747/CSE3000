import torch
import time


# Function to measure time for tensor operation on a given device
def measure_time(device, iterations=10):
    # Create random tensors
    x = torch.rand(10000, 10000, device=device)
    y = torch.rand(10000, 10000, device=device)

    # Warm up
    _ = torch.matmul(x, y)
    torch.cuda.synchronize() if device.type == 'cuda' else None

    # Measure time for tensor operation
    start_time = time.time()
    for _ in range(iterations):
        z = torch.matmul(x, y)
        torch.cuda.synchronize() if device.type == 'cuda' else None  # Wait for GPU to finish
    end_time = time.time()

    return (end_time - start_time) / iterations


# Measure time on CPU
cpu_device = torch.device("cpu")
cpu_time = measure_time(cpu_device)
print(f"Average time taken on CPU: {cpu_time:.4f} seconds")

# Measure time on GPU
if torch.cuda.is_available():
    gpu_device = torch.device("cuda")
    gpu_time = measure_time(gpu_device)
    print(f"Average time taken on GPU: {gpu_time:.4f} seconds")
else:
    print("CUDA is not available. Using CPU only.")
