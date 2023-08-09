# Project Title: CIFAR-10 Image Classification with Convolutional Neural Network

# Docker Hub:
```
docker push icoderp/irecognition:tagname
```

## Description:
In this project, we have implemented a Convolutional Neural Network (CNN) to classify images from the CIFAR-10 dataset into ten distinct classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, and truck. Leveraging the power of deep learning and computer vision, our CNN architecture demonstrates efficient image recognition and classification.

## Web Interface for Image Classification:
Our project goes beyond the backend implementation of a CNN. We have created a captivating web interface using Django, enabling users to interact with our image classifier seamlessly. The intuitive design and user-friendly interface allow anyone to upload an image and receive real-time predictions about the object contained in the image.

![Web Interface Screenshot](/img/web-i.png)
![Web Interface Screenshot](/img/web-i-upload.png)

## Getting Started:

To run this project locally, follow these steps:

### Prerequisites:

- Python (3.10 or higher)
- Docker (if you want to use Docker for deployment)

### Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/ihor-vt/Web-Based-Image-Classification-with-CIFAR-10-Datase.git
   cd your-repo
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Rename `.env.example` to `.env` in the project root.
   - Replace the placeholder values in `.env` with your actual secrets and configurations.

### Running the Application:

1. Change you dir to irecognition:
   ```bash
   cd irecognition
   ```

2. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

3. Start the development server:
   ```bash
   python manage.py runserver
   ```

4. Access the web interface in your browser at http://localhost:8000.

### Running with Docker:

1. Build the Docker image:
   ```bash
   docker build -t cifar-10-image-classifier .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 --env-file .env cifar-10-image-classifier
   ```

3. Access the web interface in your browser at http://localhost:8000.

Happy coding and image classification!

## Architecture:
The CNN architecture consists of a well-structured sequence of layers, each contributing to accurate image classification:

1. Input Layer: Accepts 32x32 color images.
2. Convolutional Layers: Two sets of Conv2D layers (32, 64, and 128 filters) with batch normalization and ReLU activation.
3. Max Pooling Layers: Spatial dimensions are reduced using MaxPooling2D after convolutional layers.
4. Flatten Layer: Converts the convolutional output into a format suitable for fully connected layers.
5. Fully Connected Layers: Two hidden dense layers (1024 neurons) with ReLU activation.
6. Output Layer: A dense layer with softmax activation to predict class probabilities.

## Training and Tuning:
We trained our model using the Adam optimizer and sparse categorical cross-entropy loss. Initial training was conducted for 55 epochs on the original training dataset. To enhance the model's robustness, we applied data augmentation techniques like width shift, height shift, and horizontal flip, thereby generating augmented training data.

## Results:
The model has demonstrated impressive performance, achieving a test accuracy of approximately 86.38%. Data augmentation has substantially contributed to improving the model's resilience and its ability to generalize well to unseen data.

## Graphs:
Here are visual representations of the training and validation progress over the epochs:

![Graph Loss and Accuracy](/img/graph_loss_accuracy.png)

## Conclusion:
Our CNN architecture, coupled with strategic data augmentation, showcases the efficacy of deep learning in image classification. The model's accuracy and adaptability are noteworthy, making it a robust solution for classifying CIFAR-10 images. Moreover, our user-friendly web interface brings the power of this model to your fingertips, enabling easy and intuitive image classification.

By exploring this project, you gain valuable insights into CNNs, data augmentation, and the practical implementation of image classification in real-world scenarios.