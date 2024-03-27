# Satvik Varshney 
## PHYS449 Main project 

This project applies machine learning techniques to the classification of spacetimes in the context of general relativity, specifically addressing the Petrov classification of the Weyl tensor. Utilizing a feed-forward neural network, this work showcases the potential of machine learning in identifying and classifying the intricate structures of spacetime, demonstrating a novel approach to a long-standing problem in theoretical physics. With this project aim at replicating and validating the results obtained by Yang-Hui He and Juan Manuel Perez Ipi in their work titled "Machine-Learning the Classication of Spacetimes"

### Overview
The aim of this project is to model Petrov’s classification of spacetimes using machine learning. By generating numerical data for various spacetime structures and employing a feed-forward neural network, we achieved a high degree of success in classifying spacetimes into distinct Petrov types (I, II, III, D, N, O). This method not only allows for efficient classification but also aids in the analysis of underlying patterns in the structure of different spacetime types.

### Features
Data Generation: Synthetic generation of spacetime data based on the Weyl scalars in the Newman-Penrose formalism, covering all possible Petrov types.
Neural Network Model: Implementation of a 5 layer deep feed-forward neural network with high accuracy in classifying spacetime data into Petrov types.
Visualization: Use of Principal Component Analysis (PCA) to visualize and analyze the patterns in the generated spacetime data.

### Technologies
Python for data generation and neural network implementation.
Libraries: PyTorch for neural network architecture, NumPy for numerical operations, and matplotlib for data visualization.##


#### Command line syntax to run main.py
```
python main.py param/param_file_name.json petrov_data.csv result/performance.html
```

#### Command line parameters description
```
Parameter 1 = param/param_file_name.json
Parameter 1 description = JSON file to keep the hyper parameters (e.g. learning rate, batch size, etc.
Parameter 1 default value = param/param_file_name.json
Parameter 1 file type = JSON

Parameter 2 = even_mnist.csv 
Parameter 2 description = Petrov Input dataset file name with path
Parameter 2 default value = petrov_data.csv
Parameter 2 file type = csv

Parameter 3 = performance.html
Parameter 3 description = html file name with path to record the output.This report summarizes the final results and performance.
Parameter 3 default value = result/Performance.html
Parameter 3 file type = html

```

#### Parameter Json file description
```
learning rate = [float] learning rate 
num iter = [interger] number of epochs
num_input = [interger] number of neurons in input layer
num_hidden = [interger] number of neurons in hidden layer
batch_size = [interger] number of data in a batch
num_classes = [interger] number of neurons in output layer
```
