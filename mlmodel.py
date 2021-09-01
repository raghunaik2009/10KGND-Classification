import joblib
from preprocess import Preprocess

pre_processing = Preprocess()
class MLModel:
    def __init__(self) -> None:
        self.lsvc_model = None

    def load_model(self):
        print('******loading model*****')
        self.lsvc_model = joblib.load('models/linearsvm_model_pipeline.bz2') #/Users/raghu/vscodeworkspace/10KGND-Classification/

    def text_predict(self, text):
        cleaned_text = pre_processing.clean_text(text)
        prediction = self.lsvc_model.predict([cleaned_text])
        return str(prediction[0])