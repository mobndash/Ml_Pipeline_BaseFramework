# Loading dataset w.r.t csv file, from a DB, from a datalake

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformationConfig
from src.components.data_transformation import DataTransformation

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig :
    """
    This dataclass defines file paths for saving:
    - the raw dataset
    - the training data
    - the test data
    """
    train_data_path : str = os.path.join('artifacts', "train.csv")
    test_data_path : str = os.path.join('artifacts', "test.csv")
    raw_data_path : str = os.path.join('artifacts', "raw_data.csv")

class DataIngestion :
    def __init__(self) :
        """
        Initialize ingestion config using the dataclass.
        Creates default paths for train, test, and raw data.
        """
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self) :
        """
        - Reads the input CSV
        - Saves raw copy
        - Splits into train/test sets
        - Saves them into specified file paths
        - Returns the paths for further pipeline usage
        """
        logging.info("Enterd Data Ingestion method")
        
        try:
            # Read the raw dataset
            df = pd.read_csv("notebook/data/StudentsPerformance.csv")
            logging.info("Reading the dataset as DataFrame")

            # Ensure that the 'artifacts' directory exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Split data into training and test sets
            logging.info("Train-Test Split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            # Save test data
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            # Return file paths for use in the next pipeline steps
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )

        except FileNotFoundError as e:
            logging.error("File not found. Please check the dataset path.")
            raise CustomException(e, sys)
        
        except Exception as e:
            logging.error(f"An unexpected error occurred: {str(e)}")
            raise CustomException(e, sys)

if __name__ == "__main__" :
    obj = DataIngestion()
    train_data, test_data, raw_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data, test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))