from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01 import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02 import PrepareBaseModelTrainingPipeline



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