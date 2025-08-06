# Common functions like model saving, connecting with mongoDB

import os
import sys

from src.exception import CustomException
from src.logger import logging

import pandas as pd
import numpy as np

import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

# dave preprocessing file as preprocessor object


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

# Function to evaluate models and calculate best hyperparamater using GridSearchCV


def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            # retrieve the models
            model = list(models.values())[i]
            # retrieve the model names
            para = param[list(models.keys())[i]]

            # GridSearch calculate the best parameters
            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            # sets the best parameters for the model
            model.set_params(**gs.best_params_)

            logging.info("Model Training started")

            model.fit(X_train, y_train)

            # model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            # saves and returns the report with model namees and r2 score above 60%
            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
