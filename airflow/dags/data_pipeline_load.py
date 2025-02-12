from pymongo import MongoClient
import pandas as pd 

path = '/opt/airflow/dags/'

def load(data):
    # connect to MongoDB
    mongodb_uri = ''
    client = MongoClient(mongodb_uri)
    db = client['']
    collection = db['']
    
    # Convert dataframe to a list of dictionaries
    
    data = data.to_dict(orient="records")
    
    # insert data into the colection
    
    if data:
        collection.insert_many(data)
    else:
        print("No data to insert.")
    
    # close the connection
    client.close()
    
if __name__ == '__main__':
    df = pd.read_csv(f'{path}P2M3_Daniswara_EkaS_data_cleaned.csv')
    load(df) 