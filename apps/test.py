import pyspark.sql  
from pyspark.sql.functions import *

print('hello world')

#important replace spark information below

spark = pyspark.sql.SparkSession.builder\
    .master("spark://cedc9cd97516:7077") \
    .config("spark.app.name", "JasonTest") \
    .getOrCreate()

data = [("Jason", "Adrian", "Andrew")]


df = spark.createDataFrame(data=data)

df.show()
