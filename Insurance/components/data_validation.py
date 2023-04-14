'''
Data validation includes:
-> Data type checking.
-> Unwanted data finding.
-> Data cleaning.
'''

import pandas as pd
from typing import Optional
import os,  sys
from Insurance.logger import logging
from Insurance.entity import artifact_entity, config_entity
from Insurance.exception import InsuranceException


class DataValidation:
    def __init__(self,data_validation_config:config_entity.DataValidationConfig, 
                 data_ingestion_artifact: artifact_entity.DataIngestionArtifact) -> None:
        try:
            logging (f"******Data Validation*******")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise InsuranceException(e,sys)
        

    def drop_missing_values_columns(self, df:pd.DataFrame, report_key_name:str)->Optional[pd.DataFrame]:
        try:
            threshold = self.data_validation_config.missing_threshold
            null_report = df.isna().sum() / df.shape[0]
            drop_columns_name = null_report[null_report > threshold].index

            self.validation_error [report_key_name] = list(drop_columns_name)
            df.drop(list(drop_columns_name), axis = 1, inplace = True)

            if len(df.columns) == 0:
                return None
            else:
                return df

        except Exception as e:
            raise InsuranceException(e,sys)

        
    def is_required_columns_exists(self, base_df:pd.DataFrame, current_df:pd.DataFrame, report_key_name:str)->bool:
        try:
            base_columns = base_df
            current_columns = current_df

            missing_columns = []
            for base_columns in base_columns:
                if base_columns not in current_columns:
                    logging.info(f" Columnes: [{base} is not available.]")
                    missing_columns.append(base_columns)
                
                if len(missing_columns)>0:
                    self.validation_error[report_key_name] = missing_columns
                    return False
                return True

        except Exception as e:
            raise InsuranceException(e,sys)


    def data_drift():
        pass
    def initiate_data_validation():
        pass