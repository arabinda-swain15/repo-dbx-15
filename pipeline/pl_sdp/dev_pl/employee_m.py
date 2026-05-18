from pyspark import pipelines as dp

@dp.materialized_view(
    name = "bronze_m"
)
def bronze_m():
    df = spark.read.table("dlt_catalog.dlt_schema.dlt_table_m")
    return df

@dp.temporary_view(
    name = "stream_view"
)
def stream_view():
    df = spark.readStream.table("bronze_table")
    return df

dp.create_streaming_table("stream_bronze_append")

@dp.append_flow(target = "stream_bronze_append")
def stream_bronze_append():
    df = spark.readStream.table("stream_view")
    return df

dp.create_sink(
    name = "delta_new1",
    format="delta",
    options={"tableName": "dlt_catalog.dlt_schema.delta_new"}
)
@dp.append_flow(target = "delta_new1")
def delta_sync():
    df = spark.readStream.table("stream_view")
    return df