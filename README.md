**Project Title: CIFAR-10 Image Classification with Convolutional Neural Network**

**Description:**
In this project, a Convolutional Neural Network (CNN) was implemented to classify images from the CIFAR-10 dataset into ten different classes: airplane, automobile, bird, cat, deerdog, frog, horse, ship, and truck. The CNN architecture was designed using the functional API in TensorFlow/Keras.

**Architecture:**
The CNN architecture consists of several layers:
1. Input layer: Accepts 32x32 color images.
2. Convolutional layers: Two sets of Conv2D layers with 32, 64, and 128 filters respectively, followed by batch normalization and ReLU activation.
3. Max Pooling layers: MaxPooling2D layers are used after each set of convolutional layers to reduce spatial dimensions.
4. Flatten layer: Flattens the output from the convolutional layers for input into the fully connected layers.
5. Fully connected layers: Two dense layers with 1024 neurons and ReLU activation are used as hidden layers.
6. Output layer: A dense layer with softmax activation to predict the probability of each class.

**Training and Tuning:**
The model was trained using the Adam optimizer with sparse categorical cross-entropy loss. The initial training was performed for 55 epochs on the original training dataset. Data augmentation techniques, such as width shift, height shift, and horizontal flip, were applied to generate augmented training data.

**Results:**
The model achieved an impressive test accuracy of approximately 86.38%. The use of data augmentation enhanced the model's robustness and generalization capability. 

**Graphs:**
Below are the graphs of loss and accuracy on training and validation data over the epochs:

![Graph Loss and Accuracy](/img/graph_loss_accuracy.png)

**Conclusion:**
The CNN architecture, along with data augmentation, proved to be effective in accurately classifying CIFAR-10 images. The model achieved good accuracy and demonstrated resilience to variations in the input data. The project provides a comprehensive understanding of the image classification process using CNNs and data augmentation techniques.