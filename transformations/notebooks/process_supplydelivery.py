# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,Imports
import sys
sys.modules.pop('fhir_types', None)
from pyspark.sql.types import *
from fhir_types import identifier, human_name, contact_point, address, codeable_concept, attachment, reference, period, timing, annotation, meta_type, id_type, implicitRules_type, language_type, text_type, contained_type, extension_type, modifierExtension_type, range_type, quantity

# COMMAND ----------

# DBTITLE 1,SupplyDelivery Schema
supply_delivery_schema = StructType(
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
        StructField("basedOn", ArrayType(reference), True),
        StructField("partOf", ArrayType(reference), True),
        StructField("status", StringType(), True),
        StructField("patient", reference, True),
        StructField("type", codeable_concept, True),
        StructField("suppliedItem",
                    StructType([
                        StructField("quantity", quantity, True),
                        StructField("itemCodeableConcept", codeable_concept, True),
                        StructField("itemReference", reference, True)
                    ]), True),
        StructField("occurrenceDateTime", TimestampType(), True),
        StructField("occurrencePeriod", period, True),
        StructField("occurrenceTiming", timing, True),
        StructField("supplier", reference, True),
        StructField("destination", reference, True),
        StructField("receiver", ArrayType(reference), True)
    ]
)


# COMMAND ----------

# DBTITLE 1,Load DataFrame
df = spark.read.format("json")\
    .schema(supply_delivery_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/SupplyDelivery.ndjson")

# COMMAND ----------

# DBTITLE 1,Display
df.display()

# COMMAND ----------

