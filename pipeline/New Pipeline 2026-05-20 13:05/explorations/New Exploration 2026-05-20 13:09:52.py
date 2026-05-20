# Databricks notebook source
# MAGIC %sql
# MAGIC select * from dlt_catalog.dlt_schema.customer

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into dlt_catalog.dlt_schema.customer
# MAGIC values (1, 'John', 1000), (2, 'Mary', 2000),(3, 'Jane', 3000)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from dlt_catalog.dlt_schema.dlt_bronze

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from catalog_dab.schema_dab.dlt_bronze
