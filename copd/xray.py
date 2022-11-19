import os

import numpy as np
import pandas as pd
import cv2
import glob
from tqdm import tqdm
from keras.models import model_from_json
from keras.models import load_model
from keras.utils import to_categorical
import time
from sklearn.model_selection import train_test_split
seed = 333
np.random.seed(seed)

#Reading the model from JSON file

from PIL import Image
from numpy import asarray
import cv2


modulepath = os.path.dirname(__file__)
xrayModelJsonPath = os.path.join(modulepath, 'mlmodels/model_4.json')
xrayModelH5Path = os.path.join(modulepath, 'mlmodels/model_4.h5')


def test_xray(path):
    with open(xrayModelJsonPath, 'r') as json_file:
        json_saved_model = json_file.read()
    model_j = model_from_json(json_saved_model)
    model_j.load_weights(xrayModelH5Path)
    img = cv2.imread(path)
    img = cv2.resize(img, (100, 100))
    print(img.shape)
    pred = model_j.predict(img.reshape(-1, 100, 100, 3))
    classes_x = np.argmax(pred, axis=1)
    return classes_x[0]
