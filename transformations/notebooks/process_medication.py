# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,Imports
import sys
sys.modules.pop('fhir_types', None)
from pyspark.sql.types import *
from fhir_types import identifier, human_name, contact_point, address, codeable_concept, attachment, reference, period, timing, annotation, meta_type, id_type, implicitRules_type, language_type, text_type, contained_type, extension_type, modifierExtension_type, range_type, quantity, ratio

# COMMAND ----------

# DBTITLE 1,Medication Schema
medication_schema = StructType(
    [
        StructField("id", id_type, True),
        StructField("meta", meta_type, True),
        StructField("implicitRules", implicitRules_type, True),
        StructField("language", language_type, True),
        StructField("text", text_type, True),
        StructField("contained", contained_type, True),
        StructField("extension", extension_type, True),
        StructField("modifierExtension", modifierExtension_type, True),
        StructField("identifier", ArrayType(identifier), True),
        StructField("code", codeable_concept, True),
        StructField("status", StringType(), True),
        StructField("manufacturer", reference, True),
        StructField("form", codeable_concept, True),
        StructField("amount", ratio, True),
        StructField("ingredient",
                    ArrayType(
                        StructType([
                            StructField("itemCodeableConcept", codeable_concept, True),
                            StructField("itemReference", reference, True),
                            StructField("isActive", BooleanType(), True),
                            StructField("strength", ratio, True)
                        ])
                    ), True),
        StructField("batch",
                    StructType([
                        StructField("lotNumber", StringType(), True),
                        StructField("expirationDate", TimestampType(), True)
                    ]), True)
    ]
)


# COMMAND ----------

# DBTITLE 1,Load DataFrame
df = spark.read.format("json")\
    .schema(medication_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/Medication.ndjson")

# COMMAND ----------

# DBTITLE 1,Display
df.display()

# COMMAND ----------

