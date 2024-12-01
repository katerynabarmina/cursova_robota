

---

# PyTorch Image Classification with ResNet-18

This project demonstrates how to use a pre-trained ResNet-18 model in PyTorch for two tasks:

1. **Simple Neural Network (SimpleNN)**: A basic feed-forward neural network with a single fully connected layer.
2. **Image Classification with ResNet-18**: A more advanced example using a pre-trained ResNet-18 model from `torchvision` to classify an image.

The project also includes GPU support, meaning the model can run on either the CPU or GPU depending on availability.

## Requirements

To run this project, you need the following Python packages:

- `torch`: PyTorch library for tensor computations and deep learning.
- `torchvision`: PyTorch's computer vision library, used for image classification and pre-trained models.
- `Pillow`: Python Imaging Library (PIL) used to open and process images.

### Install dependencies

You can install the required libraries by running:

```bash
pip install -r requirements.txt
```

## Files

- **`requirements.txt`**: A list of Python dependencies for the project.
- **`imagenet_classes.txt`**: A text file containing ImageNet class labels. This file is needed for mapping model predictions to human-readable class names.
- **`sunflower.jpg`**: A sample image for classification. Replace this with your own image for testing.
- **`simple_nn.py`**: A script implementing a simple neural network (SimpleNN) with a fully connected layer.
- **`resnet_classification.py`**: A script using the pre-trained ResNet-18 model for image classification.

## How to Use

### 1. **Clone the repository:**

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

### 3. **Download ImageNet class labels:**

Download the ImageNet class labels from the following URL:

- [ImageNet classes file](https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt)

Save this file as `imagenet_classes.txt` in the same directory as the script.

### 4. **Prepare your image:**

Ensure the image you want to classify is available in the same directory as the script or provide the correct file path in the code. Replace `"sunflower.jpg"` in the script with the path to your own image.

### 5. **Running the scripts:**

- **For Simple Neural Network (`simple_nn.py`)**:
  This script demonstrates how to create a simple feed-forward neural network in PyTorch.

  Run the script:

  ```bash
  python simple_nn.py
  ```

  This script will create a simple neural network, initialize it, and process random input data.

- **For Image Classification (`resnet_classification.py`)**:
  This script uses the pre-trained ResNet-18 model to classify an image.

  Run the script:

  ```bash
  python resnet_classification.py
  ```

  The script will load an image, preprocess it, and classify it using the ResNet-18 model. The predicted class name will be printed out.

### 6. **Output:**

For the `resnet_classification.py` script, you should see the predicted class printed out in the terminal, for example:

```bash
Прогнозований клас: sunflower
```

---

## Explanation

### **1. Simple Neural Network (`simple_nn.py`)**

This script demonstrates the creation of a very simple neural network (SimpleNN) with a single fully connected layer. It generates random input data, passes it through the model, and prints the output. While simple, this example helps familiarize you with PyTorch’s basic functionality.

### **2. Image Classification with ResNet-18 (`resnet_classification.py`)**

The `resnet_classification.py` script uses a pre-trained ResNet-18 model from `torchvision` for image classification. It loads an image, preprocesses it (resizing, normalization), and then feeds it into the model to predict the class. The model's output is the index of the predicted class, which is then mapped to a human-readable label using the `imagenet_classes.txt` file.

### **GPU Support**

Both scripts support running on either the CPU or GPU. The model will automatically run on the GPU if available, otherwise, it will run on the CPU.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Explanation of Changes:

- **`requirements.txt`** now includes all the necessary libraries.
- **`README`** is updated to mention two distinct scripts (`simple_nn.py` and `resnet_classification.py`), explaining both their purposes.
- Each script has clear instructions on how to run it and what kind of output to expect.
