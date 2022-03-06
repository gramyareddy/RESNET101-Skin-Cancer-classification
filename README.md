# RESNET101-Skin-Cancer-classification
 Using dataset from Kaggle to classify the type of skin cancer from the images
 
 In data_segregate.py (data preprocessing)
------------------------------------------
1. Use the metadata csv to seperate all the data into 7 different folders (7 classes)
2. Used splitfolders pip package to split it to train,val data


In skin_cancer_classification.py(Model training)
-------------------------------------------------
1. Downloaded a RESNET101 Pretrained model and used SGD optimiser nd cross entropy loss and trained for 17 epochs (Couldnt train more as I dont have a local GPU and Colalb (nonpro) was taking top long per epoch)
Achieved 92% train and 88% test accuracy, if trained for a longer duration another 2% increase is possible 
2.Can also try other models like EfficientB6,B7 models
3. Visualisation : Confusion matrix and metrics are printe to a text file

Inference
==========
There is a bit of confusion between melanoma nd melanocytic_nevi as they might be kinda similar, it makes sense we can resolve with more training data or trying out more intricate models but at the moment I do not have GPU resources to train it up well.
