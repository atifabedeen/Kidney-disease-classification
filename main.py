from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01 import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02 import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03 import ModelTrainingPipeline



STAGE_NAME = "DATA INGESTION"
try:
   logger.info(f">>>>>> STAGE {STAGE_NAME} STARTED <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> STAGE {STAGE_NAME} STARTED <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e