from pyspark import pipelines as dp

@dp.table(
    name = "dlt_catalog.dlt_schema.dlt_bronze"
)
def bronze():
    df = spark.readStream.table("dlt_catalog.dlt_schema.customer")
    return df