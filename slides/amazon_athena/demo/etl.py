import sys
from pyspark.sql import SparkSession

spark = SparkSession.builder\
    .appName("Word Count") \
    .getOrCreate()


input_path= 's3://mydevbucket/db/continents_countries.csv'
# input_path = sys.argv[1]

df = spark.read.format("csv").option("header","true")\
    .option("inferSchema", "true")\
    .load(input_path)

df.show(100, truncate=False)
df.printSchema()

output_path = "s3://mydevbucket/output/cc1"
# output_path = sys.argv[2]

df.repartition("continent", "country")\
    .write.mode("append")\
    .partitionBy("continent", "country")\
    .parquet(output_path)

spark.stop()
