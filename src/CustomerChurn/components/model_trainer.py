import pandas as pd
import os
from CustomerChurn.logging import logger
from sklearn.ensemble import RandomForestClassifier
import joblib
from CustomerChurn.entity.config_entity import ModelTrainerconfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerconfig):
        self.config = config
        
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]
        
        train_x = train_data.drop([self.config.target_column], axis = 1)
        test_x = test_data.drop([self.config.target_column], axis = 1)
        
        model = RandomForestClassifier(
            n_estimators = self.config.n_estimators,
            max_features = self.config.max_features,
            min_samples_leaf = self.config.min_samples_leaf,
            criterion = self.config.criterion
        )
        
        model.fit(train_x, train_y)
        
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))
        
        