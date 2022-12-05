# Satvik Varshney 
## PHYS449 Main project 

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
