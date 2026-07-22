#Databricks notebook source
dbutils.widgets.text("catalog_name", "dev_catalog")
catalog = dbutils.widgets.get("catalog_name")

df= (spark.read.format("csv")
                .option("header", "true")
                .load("/databricks-datasets/retail-org/customers/customers.csv")
)

dbutils.widgets.text("storage_location", "")
storage_location = dbutils.widgets.get("storage_location")

# spark.sql(f"CREATE CATALOG IF NOT EXISTS {catalog} MANAGED LOCATION '{storage_location}/{catalog}' COMMENT 'Managed catalog'")
# spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.bronze")

df.write.mode("overwrite").format("delta").saveAsTable(f"{catalog}.bronze.customers")

print(f"Loaded {df.count()} customer rows into {catalog}.bronze.customers")

