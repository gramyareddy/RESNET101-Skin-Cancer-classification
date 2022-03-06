import numpy as np
import pandas as pd
import shutil
import cv2
import os

#put both parts (total images) in a single folder
image_path = "data\\HAM10000_images\\"
basal_cell_carcinoma_path = "data\\segregated_data\\basal_cell_carcinoma"
bowen_disease_path = "data\\segregated_data\\bowen_disease"
benign_keratosis_like_path = "data\\segregated_data\\benign_keratosis_like"
dermatofibroma_path = "data\\segregated_data\\dermatofibroma"
melanocytic_nevi_path = "data\\segregated_data\\melanocytic_nevi"
melanoma_path = "data\\segregated_data\\melanoma"
vascular_path = "data\\segregated_data\\vascular"

df = pd.read_csv("data\\HAM10000_metadata.csv")
print(len(df['image_id']), df['dx'][:10])

for i in range(len(df['image_id'])):
    print(i)
    filename = os.path.join(image_path , df['image_id'][i] + ".jpg")
    type_ = df['dx'][i]
    if(type_ == "bkl"):
        shutil.copy(filename, os.path.join(benign_keratosis_like_path,df['image_id'][i]+".jpg"))
    elif(type_ == "bcc"):
        shutil.copy(filename, basal_cell_carcinoma_path)
    elif(type_ == "akiec"):
        shutil.copy(filename, bowen_disease_path)
    elif(type_ == "df"):
        shutil.copy(filename, dermatofibroma_path)
    elif(type_ == "mel"):
        shutil.copy(filename, melanoma_path)
    elif(type_ == "nv"):
        shutil.copy(filename, melanocytic_nevi_path)
    elif(type_ == "vasc"):
        shutil.copy(filename, vascular_path)

import splitfolders
splitfolders.ratio('data\\segregated_data', output="data\\output", seed=1337, ratio=(.8, 0.2,0)) 