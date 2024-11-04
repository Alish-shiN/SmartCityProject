from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def train_model(data):
    X = data[['deviceid', 'direction', 'segment', 'length']]
    y = data['run_time_in_seconds']

    model = LinearRegression()
    model.fit(X, y)

    return model

def make_prediction(model, deviceid, direction, segment, length):
    input_data = np.array([[deviceid, direction, segment, length]])
    prediction = model.predict(input_data)
    return prediction[0]
