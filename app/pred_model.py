import os

from sklearn.externals import joblib


class PredModel():

    model = None

    def __init__(self, model_file):
        model_file = os.path.join(os.getcwd(), 'ml_models', model_file)
        self.model = joblib.load(model_file)

    def predict(self, ingredients):
        prediction = self.model.predict([ingredients])[0]
        return prediction
