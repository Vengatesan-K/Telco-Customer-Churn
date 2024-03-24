from CustomerChurn.config.configuration import ConfigurationManager
from CustomerChurn.components.model_evaluation import ModelEvaluation
from CustomerChurn.logging import logger

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager().get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config)
        model_evaluation.log_into_mlflow()
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

