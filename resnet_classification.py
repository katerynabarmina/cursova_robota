import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image

# Завантаження моделі ResNet
model = models.resnet18(pretrained=True)
model.eval()  # Перемикання моделі в режим оцінки

# Список класів ImageNet (завантажте заздалегідь)
imagenet_classes = []
with open("imagenet_classes.txt") as f:
    imagenet_classes = [line.strip() for line in f.readlines()]

# Попередня обробка зображення
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Завантаження та обробка зображення (змініть на шлях до вашого фото)
image = Image.open("sunflower.jpg")
input_tensor = transform(image).unsqueeze(0)  # Додавання batch розміру

# Прогноз
with torch.no_grad():
    output = model(input_tensor)
    predicted_class = torch.argmax(output, dim=1).item()

# Отримання назви класу
predicted_label = imagenet_classes[predicted_class]
print(f"Прогнозований клас: {predicted_label}")