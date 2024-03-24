import os
import pandas as pd
from sklearn.metrics import f1_score,precision_score,accuracy_score,recall_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn 
import numpy as np
import joblib
from CustomerChurn.entity.config_entity import ModelEvaluationConfig
from pathlib import Path
from CustomerChurn.utils.common import save_json


class ModelEvaluation:
    def __init__(self,config: ModelEvaluationConfig):
        self.config = config
        
    def evaluate_metrics(self,actual,pred):
        f1 = f1_score(actual,pred)
        precision = precision_score(actual,pred)
        recall = recall_score(actual,pred)
        accuracy = accuracy_score(actual,pred)
        return f1,precision,recall,accuracy
    
    
    def log_into_mlflow(self):
        
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_x = test_data.drop([self.config.target_column], axis = 1)
        test_y = test_data[self.config.target_column]
        
        mlflow.set_registry_uri = (self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
           
           predicted_qualities = model.predict(test_x)
           
           (precision, recall, f1, accuracy) = self.evaluate_metrics(test_y,predicted_qualities)
           
           scores = {
               "f1":f1,
               "precision":precision,
               "recall":recall,
               "accuracy":accuracy
           }
           save_json(path=Path(self.config.metric_file_name), data = scores)
           
           mlflow.log_params(self.config.all_params)
           mlflow.log_metric("accuracy", accuracy)
           mlflow.log_metric("f1", f1)
           mlflow.log_metric("precision", precision)
           mlflow.log_metric("recall", recall)
           
           
           
           if tracking_url_type_store != "file":
               mlflow.sklearn.log_model(model, "model", registered_model_name="Telco Customer Churn")
           else:
               mlflow.sklearn.log_model(model, "model")