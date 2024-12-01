import torch
import torch.nn as nn

# Перевірка наявності GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Створення простої моделі
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc = nn.Linear(100, 10)  # Лінійний шар

    def forward(self, x):
        return self.fc(x)

# Ініціалізація моделі та перенесення на GPU
model = SimpleNN().to(device)

# Створення даних і перенесення на GPU
input_data = torch.rand(32, 100).to(device)  # 32 зразки, кожен з 100 ознак
output_data = model(input_data)  # Вихід моделі

print(output_data)

