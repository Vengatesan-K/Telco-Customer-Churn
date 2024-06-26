from CustomerChurn.config.configuration import ConfigurationManager
from CustomerChurn.components.model_trainer import ModelTrainer
from CustomerChurn.logging import logger

STAGE_NAME = "Model Training stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager().get_model_trainer_config()
        model_trainer = ModelTrainer(config)
        model_trainer.train()
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e