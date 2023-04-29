import numpy as np
import pandas as pd
from Insurance.logger import logging
from typing import Optional
from sklearn.preprocessing import RobustScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from Insurance.entity import artifact_entity, config_entity
from Insurance.exception import InsuranceException
from Insurance.config import TARGET_COLUMN
from Insurance import utils
from sklearn.preprocessing import LabelEncoder
import os, sys
# from sklearn.combine import SMOTE

# Missing values impute.
# Outlaiers Handling.
# Handeling Imbalance data.
# Convert catagorical data into numberical data.

class DataTransformation:
    def __init__(self, data_transformation_config: config_entity.DataTransformationConfig,
                 data_ingestion_artifact: artifact_entity.DataIngestionArtifact):
        
        try:
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact

        except Exception as e:
            raise InsuranceException(e, sys)
        
    @classmethod
    def get_data_transformer_object(cls)->Pipeline: # Create cls class
        try:
            simple_imputer = SimpleImputer(strategy= 'constant', fill_value=0)

            robust_scaler = RobustScaler()
            pipeline = Pipeline(steps = [
                ('Imputer', simple_imputer),
                ('RobustScaler', robust_scaler)
            ])

            return pipeline

        except Exception as e:
            raise InsuranceException(e, sys)


    def initiate_data_transformation(self,)-> artifact_entity.DataTransformationArtifact:        
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            input_feature_train_df = train_df.drop(TARGET_COLUMN, axis =1)
            input_feature_test_df = test_df.drop(TARGET_COLUMN, axis = 1)

            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_test_df = test_df[TARGET_COLUMN]

            label_encoder = LabelEncoder()
            # Fit data
            target_feature_train_arr = target_feature_train_df.squeeze()
            target_feature_test_arr = target_feature_test_df.squeeze()


            for col in input_feature_train_df.columns:
                if input_feature_test_df[col].dtypes == 'O':
                    input_feature_train_df[col] = label_encoder.fit_transform(input_feature_train_df[col])
                    input_feature_test_df[col] = label_encoder.fit_transform(input_feature_test_df[col])
                else:
                    input_feature_train_df[col] = input_feature_train_df[col]
                    input_feature_test_df[col] = input_feature_test_df[col]
            

            # Imbalance data Handling.
            transformation_pipeline = DataTransformation.get_data_transformer_object()
            transformation_pipeline.fit(input_feature_train_df)

            input_feature_train_arr = transformation_pipeline.transform(input_feature_train_df)
            input_feature_test_arr = transformation_pipeline.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, target_feature_train_arr]
            test_arr = np.c_[input_feature_test_arr, target_feature_test_arr]

            utils.save_numpy_array_data(file_path=self.data_transformation_config.transform_train_path,
                                        array= train_arr)
            utils.save_numpy_array_data(file_path=self.data_transformation_config.transform_test_path,
                                        array= test_arr)

            utils.save_object(file_path=self.data_transformation_config.transform_object_path, obj = transformation_pipeline)

            utils.save_object(file_path=self.data_transformation_config.target_encoder_path, obj = label_encoder)

            data_transformation_artifact = artifact_entity.DataTransformationArtifact(
                transform_object_path = self.data_transformation_config.transform_object_path,
                transform_train_path = self.data_transformation_config.transform_train_path,
                transform_test_path = self.data_transformation_config.transform_test_path,
                target_encoder_path = self.data_transformation_config.target_encoder_path
                )
            return data_transformation_artifact
            
        except Exception as e:
            raise InsuranceException(e, sys)




