import pymongo
import os
from dataclasses import dataclass


@dataclass
class EnvironmentVariable:
    mongo_db_url: str = os.getenv("MONGO_DB_URL") # type: ignore


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "expenses"
print(env_var.mongo_db_url)
