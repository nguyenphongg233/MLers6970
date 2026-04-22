import torch

# Kiểm tra xem CUDA có sẵn không (tương đương với việc check GPU runtime)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Đang sử dụng thiết bị: {device}")

# # Khi tạo model hoặc dữ liệu, bạn phải đẩy nó lên GPU
# model = MyCNN().to(device)