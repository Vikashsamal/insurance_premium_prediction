# This file was created for Batchprediction and Training pipeline

from Insurance.pipeline.batch_prediction import start_batch_prediction
from Insurance.pipeline.training_pipeline import start_training_pipeline
from Insurance.exception import InsuranceException
import sys

file_path = r"/Users/bikashsmac/Desktop/Projects/insurance_premium_prediction/insurance.csv"
print(__name__)
if __name__ == "__main__":
    try:
        output_file = start_batch_prediction(input_file_path=file_path)
        #output_file = start_training_pipeline()
        print(output_file)
    except Exception as e:
        raise InsuranceException(e, sys)
