import torch

# 检查是否有 CUDA 设备
if torch.cuda.is_available():
    print(f"CUDA is available. cuDNN version: {torch.backends.cudnn.version()}")
else:
    print("CUDA is not available")
