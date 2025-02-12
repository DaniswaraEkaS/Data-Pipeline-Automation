'''
=================================================
Nama  : Daniswara Eka Saputra

Program ini dibuat untuk melakukan cleaning pada raw data agar nantinya siap dimasukan kedalam database.
=================================================
'''

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

#Creating variable data as spark dataframe for anrgument in tarnsform function
path = '/opt/airflow/dags/'
spark = SparkSession.builder.getOrCreate()
data = spark.read.csv(f'{path}/P2M3_Daniswara_EkaS_data_raw.csv', header=True, inferSchema=True)

def transform(data):

    # Rename columns
    data_cleaning = data.withColumnRenamed('Job Title','job_title')\
            .withColumnRenamed('Salary Estimate','salary_estimate')\
            .withColumnRenamed('Job Description','job_description')\
            .withColumnRenamed('Rating','rating')\
            .withColumnRenamed('Company Name','company_name')\
            .withColumnRenamed('Location','location')\
            .withColumnRenamed('Headquarters','headquarters')\
            .withColumnRenamed('Size','size')\
            .withColumnRenamed('Type of ownership','type_of_ownership')\
            .withColumnRenamed('Industry','industry')\
            .withColumnRenamed('Sector','sector')\
            .withColumnRenamed('Revenue','revenue')\
            .withColumnRenamed('Competitors','competitors')\
            .withColumnRenamed('Easy Apply','easy_apply')\
    
    #drop missing values
    # data_cleaning = data_cleaning.where(col("job_title").isNotNull())
    
    #Convert to pandas dataframe
    data_cleaning = data_cleaning.toPandas()
    
    #Conver dataframe to csv file with specific file path
    data_cleaning.to_csv(f'{path}P2M3_Daniswara_EkaS_data_cleaned.csv', index=False)

    return data_cleaning

if __name__ == '__main__':
    transform(data)