from pyspark import pipelines as dp
from pyspark.sql.functions import *

@dp.materialized_view(
    name = "mv_customer"
)
def mv_customer():
    # lld = spark.sql("select max(order_date) from dlt_catalog.dlt_schema.customer").collect()[0][0]
    lld = "2022-01-04"
    df = spark.read.table("dlt_catalog.dlt_schema.customer")
    # df1 = df.filter(col("order_date") >= lit(lld))
    df1 = df.where(f"order_date >= '{lld}'")
    return df1

@dp.temporary_view(
    name = "sv_customer"
)
def sv_customer():    
    df = spark.readStream.option('skipChangeCommits', True).table("mv_customer")
    return df

@dp.table(
    name = "customer_streaming"
)
def customer_streaming():
    df = spark.readStream.option('skipChangeCommits', True).table("sv_customer")
    return df

dp.create_streaming_table(
    name = "st_customer"
)
@dp.append_flow(target="st_customer")
def append_customer():
    df = spark.readStream.table("sv_customer")
    return df
