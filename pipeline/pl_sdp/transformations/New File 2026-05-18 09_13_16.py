df = spark.read.table("dlt_catalog.dlt_schema.delta_new")
df.count()