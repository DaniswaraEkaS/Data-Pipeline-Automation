'''
=================================================
Nama  : Daniswara Eka Saputra

Program ini dibuat untuk melakukan extract data dari dataset kemudian mengubahnya kedalam nama file baru.
=================================================
'''
from pyspark.sql import SparkSession


path = '/opt/airflow/dags/'

def extract(path):
    # """
    # Fungsi ini digunakan untuk mengekstrak data dari file lalu mengubah nama file tersebut.
    # parameter:
    #     path : lokasi file yang akan diextract
    # return:
    #     data : dataframe spark
    # contoh penggunaan:
    #     load_data("\Users\ASUS\rmt-002\airflow\dags")
    # """

    
    spark = SparkSession.builder.getOrCreate()

    data = spark.read.csv(f'{path}DataEngineerJob.csv', header=True, inferSchema=True)
    
    data.toPandas().to_csv(f'{path}P2M3_Daniswara_EkaS_data_raw.csv', index=False)
    
    return data


if __name__ == '__main__':
    extract(path)
    