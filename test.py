import torch

print("GPU:", torch.cuda.is_available())
print(torch.rand(3, 4))