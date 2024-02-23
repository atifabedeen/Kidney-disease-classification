from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01 import DataIngestionTrainingPipeline




STAGE_NAME = "DATA INGESTION"
try:
   logger.info(f">>>>>> STAGE {STAGE_NAME} STARTED <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
