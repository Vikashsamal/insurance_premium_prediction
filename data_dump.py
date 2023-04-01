import pymongo # pip install pymongo
import pandas as pd
import json


#client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.ndlu6.mongodb.net/?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb+srv://Bikash:Loveyoubaby@cluster0.ndlu6.mongodb.net/?retryWrites=true&w=majority")
db = client.test

DATA_FILE_PATH = "/Users/bikashsmac/Desktop/Projects/insurance_premium_prediction/insurance.csv"
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns:{df.shape}")
    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)











