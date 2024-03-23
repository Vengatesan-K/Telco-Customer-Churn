import os
from CustomerChurn.logging import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from CustomerChurn.entity.config_entity import DataTransformationConfig



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        
        train, test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info(f"Train and test data saved in {self.config.root_dir}")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)
        
        