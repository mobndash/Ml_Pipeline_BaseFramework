# Transformation related to data like converting categorical features to numerical, handling one - hot enoding, etc
import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

@dataclass
class DataTransformationConfig :
    # Path to save the serialized preprocessor object (as .pkl)
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation :
    def __init__(self) :
        # Initialize the configuration
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self) :
        """
        Creates and returns a ColumnTransformer object that applies:
        - Median imputation and standard scaling to numerical columns
        - Most frequent imputation, one-hot encoding, and scaling to categorical columns
        """
        try :
            # Define the names of numerical and categorical columns
            numerical_columns = ["reading score", "writing score"]
            categorical_columns = ["gender", "race/ethnicity", "parental level of education", "lunch", "test preparation course"]

            numerical_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy = "median")),
                    ("scaler", StandardScaler(with_mean = False))
                ]
            )
            logging.info(f"Numerical pipeline created for columns: {numerical_columns}")

            categorical_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy = "most_frequent")),     # Fill missing values with median
                    ("OneHotEncoder", OneHotEncoder()),                         # Convert categories to binary features
                    ("scaler", StandardScaler(with_mean = False))               # Scale the one-hot encoded values
                ]
            )
            logging.info(f"Categorical pipeline created for columns: {categorical_columns}")

            # Combine both pipelines into a single ColumnTransformer
            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline", numerical_pipeline, numerical_columns),
                    ("categorical_pipeline", categorical_pipeline, categorical_columns)
                ]
            )

            return preprocessor
        
        except Exception as e :
            # Raise a custom exception if something goes wrong
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path) :
        try :
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Reading rain and Test dataset completed")
            logging.info("Fetching pre-processing object")

            preprocessing_obj = self.get_data_transformer_object()

            target_column = "math score"
            numerical_column = ["reading score", "writing score"]

            input_feature_train_df = train_df.drop(columns = [target_column], axis = 1)
            target_feature_train_df = train_df[target_column]

            input_feature_test_df = test_df.drop(columns = [target_column], axis = 1)
            target_feature_test_df = test_df[target_column]

            logging.info(f"Applying preprocessor object on training dataframe and test dataframe")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.fit_transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]

            logging.info("Saving preprocessing object")

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            return (train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file_path)

        except Exception as e :
            raise CustomException(e, sys)