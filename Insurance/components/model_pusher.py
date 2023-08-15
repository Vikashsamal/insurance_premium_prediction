from Insurance.predictor import ModelResolver
from Insurance.entity import config_entity,artifact_entity
from Insurance.exception import InsuranceException
from Insurance.logger import logging
from Insurance.utils import load_object, save_object
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import pandas  as pd
import sys,os
from Insurance.config import TARGET_COLUMN
from Insurance.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact,ModelPusherArtifact
from Insurance.entity.config_entity import ModelPusherConfig


class ModelPusher:
    