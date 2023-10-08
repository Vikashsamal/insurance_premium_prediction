# This file was created for Batchprediction and Training pipeline

from Insurance.pipeline.batch_prediction import start_batch_prediction
from Insurance.exception import InsuranceException
import os, sys

file_path = r"/Users/bikashsmac/Desktop/Projects/insurance_premium_prediction/insurance.csv"
print(__name__)
if __name__ == "__main__":
    try:
        output_file = start_batch_prediction(input_file_path=file_path)
        print(output_file)
    except Exception as e:
        raise InsuranceException (e,sys)