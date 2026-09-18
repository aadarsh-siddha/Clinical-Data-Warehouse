# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,Imports
import sys
sys.modules.pop('fhir_types', None)
from pyspark.sql.types import *
from fhir_types import identifier, human_name, contact_point, address, codeable_concept, attachment, reference, period, timing, annotation, meta_type, id_type, implicitRules_type, language_type, text_type, contained_type, extension_type, modifierExtension_type, range_type, quantity, coding, signature

# COMMAND ----------

# DBTITLE 1,Provenance Schema
provenance_schema = StructType(
    [
        StructField("id", id_type, True),
        StructField("meta", meta_type, True),
        StructField("implicitRules", implicitRules_type, True),
        StructField("language", language_type, True),
        StructField("text", text_type, True),
        StructField("contained", contained_type, True),
        StructField("extension", extension_type, True),
        StructField("modifierExtension", modifierExtension_type, True),
        StructField("target", ArrayType(reference), False),
        StructField("occurredPeriod", period, True),
        StructField("occurredDateTime", TimestampType(), True),
        StructField("recorded", StringType(), False),
        StructField("policy", ArrayType(StringType()), True),
        StructField("location", reference, True),
        StructField("reason", ArrayType(codeable_concept), True),
        StructField("activity", codeable_concept, True),
        StructField("agent",
                    ArrayType(
                        StructType([
                            StructField("type", codeable_concept, True),
                            StructField("role", ArrayType(codeable_concept), True),
                            StructField("who", reference, False),
                            StructField("onBehalfOf", reference, True)
                        ])
                    ), False),
        StructField("entity",
                    ArrayType(
                        StructType([
                            StructField("role", StringType(), False),
                            StructField("what", reference, False),
                            StructField("agent",
                                        ArrayType(
                                            StructType([
                                                StructField("type", codeable_concept, True),
                                                StructField("role", ArrayType(codeable_concept), True),
                                                StructField("who", reference, False),
                                                StructField("onBehalfOf", reference, True)
                                            ])
                                        ), True)
                        ])
                    ), True),
        StructField("signature", ArrayType(signature), True)
    ]
)


# COMMAND ----------

# DBTITLE 1,Load DataFrame
df = spark.read.format("json")\
    .schema(provenance_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/Provenance.ndjson")

# COMMAND ----------

# DBTITLE 1,Display
df.display()

# COMMAND ----------

