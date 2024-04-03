# Deep Learning Project 
## Classifying Petrov Space Time Symmetries

This project applies machine learning techniques to the classification of spacetimes in the context of general relativity, specifically addressing the Petrov classification of the Weyl tensor. Utilizing a 5 Layer deep feed-forward neural network, this work showcases the potential of machine learning in identifying and classifying the intricate structures of spacetime, demonstrating a novel approach to a long-standing problem in theoretical physics. With this project we aim at replicating and validating the results obtained by Yang-Hui He and Juan Manuel Perez Ipi in their work titled "Machine-Learning the Classification of Spacetimes"

### Overview
The aim of this project is to model Petrov’s classification of spacetimes using machine learning. By generating numerical data for various spacetime structures and employing a feed-forward neural network, we achieved a high degree of success in classifying spacetimes into distinct Petrov types (I, II, III, D, N, O). This method not only allows for efficient classification but also aids in the analysis of underlying patterns in the structure of different spacetime types.

### Features
Data Generation: Synthetic generation of spacetime data based on the Weyl scalars in the Newman-Penrose formalism, covering all possible Petrov types.
Neural Network Model: Implementation of a 5 layer deep feed-forward neural network with high accuracy in classifying spacetime data into Petrov types.
Visualization: Use of Principal Component Analysis (PCA) to visualize and analyze the patterns in the generated spacetime data.

### Technologies
Python for data generation and neural network implementation.
Libraries: PyTorch for neural network architecture, NumPy for numerical operations, and matplotlib for data visualization.

### Results Summary
The replication study of the machine learning model for the classification of spacetimes based on the Petrov classification showcases a robust performance with nuanced discernibility across the distinct Petrov types. The results are summarized in two key figures: the confusion matrix and the training performance graphs.

#### Confusion Matrix Analysis

![Performance_CM](https://github.com/SatvikVarshney/Deep-Learning-for-Spacetime-Classification/assets/114079530/c8b4f1f1-0910-4601-9f0f-985b58477f33)

The confusion matrix reveals a strong predictive accuracy of the model across all Petrov types with a pronounced diagonal indicating the majority of predictions are correct. Each Petrov class shows substantial true positive rates, with minimal misclassifications. This highlights the model's proficiency in distinguishing the nuanced differences between the spacetime classes, reinforcing the robustness of its learning and classification capabilities

Class 0 (Type O) and Class 5 (Type N) are predicted with near-perfect accuracy.
Class 1 (Type I) and Class 4 (Type D) show a very high number of correct classifications with minimal confusion with other classes.
Class 2 (Type II) and Class 3 (Type III) are accurately identified, though there are a few instances of misclassification, reflecting areas where the model's discernment could be further refined.
Overall, the model displays a strong ability to correctly classify spacetimes, with the confusion matrix underscoring its precision and potential for further optimization.

#### Training Performance Graphs

![Performance_graphs](https://github.com/SatvikVarshney/Deep-Learning-for-Spacetime-Classification/assets/114079530/7b1f9cb6-8443-4044-975e-f95c424b5746)

The training performance graphs depict the model's loss and accuracy over 30 epochs for both the training and validation datasets.

The loss graph shows a steep initial decline in both training and validation loss, which swiftly converges to a plateau, suggesting that the model quickly learned the dominant features in the data required for classification. The convergence of training and validation loss implies good generalization with no significant overfitting.
The accuracy graph indicates a rapid ascension to high accuracy for both datasets within the first few epochs, maintaining a stable level close to 1.0 throughout the remaining epochs. This pattern denotes a high level of consistency and reliability in the model's performance during the training process.

### Conclusion

The results from the replicated study confirm the effectiveness of the machine learning model in classifying spacetimes according to the Petrov classification with high precision and reliability. The performance metrics illustrate a well-tuned model that generalizes well to unseen data while maintaining an exceptional level of accuracy throughout the training and validation phases. These findings reinforce the viability of applying machine learning techniques to theoretical physics problems, offering a promising tool for future explorations in the classification of spacetimes.

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


