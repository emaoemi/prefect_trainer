from prefect import flow, get_run_logger, tags, variables
from prefect import task

from datetime import timedelta
import requests

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet

import pandas as pd
import numpy as np
import mlflow

import os


@task
def data_extraction():
    logger = get_run_logger()
    logger.info("Executed data extraction task")
@task
def data_prep():
    logger = get_run_logger()
    logger.info("Executed data preparation task")
@task
def feature_engineering():
    logger = get_run_logger()
    logger.info("Executed data feature engineering task")
@task
def model_training():
    logger = get_run_logger()
    logger.info("Executed model training task")
@task
def model_evaluation():
    logger = get_run_logger()
    logger.info("Executed model avaluation task")
@task
def model_push():
    logger = get_run_logger()
    logger.info("Executed data model push task")

@flow
def MLtraining():
    logger = get_run_logger()
    logger.info("Executing ML Training Flow ...")

    data_extraction()
    data_prep()
    feature_engineering()
    model_training()
    model_evaluation()
    model_push()

    logger.info("ML Flow operations completed")

if __name__ == "__main__":
    MLtraining()
