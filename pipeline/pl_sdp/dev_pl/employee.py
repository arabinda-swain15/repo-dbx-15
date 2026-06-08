from pyspark import pipelines as dp

@dp.table(
    name = "bronze_table"
)
def bronze_table():
    df = spark.readStream.table("dlt_catalog.dlt_schema.dlt_table")
    return df




  