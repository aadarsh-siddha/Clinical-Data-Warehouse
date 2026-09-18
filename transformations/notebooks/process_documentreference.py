# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,Imports
import sys
sys.modules.pop('fhir_types', None)
from pyspark.sql.types import *
from fhir_types import identifier, human_name, contact_point, address, codeable_concept, attachment, reference, period, timing, annotation, meta_type, id_type, implicitRules_type, language_type, text_type, contained_type, extension_type, modifierExtension_type, range_type, quantity, coding

# COMMAND ----------

# DBTITLE 1,DocumentReference Schema
document_reference_schema = StructType(
    [
        StructField("id", id_type, True),
        StructField("meta", meta_type, True),
        StructField("implicitRules", implicitRules_type, True),
        StructField("language", language_type, True),
        StructField("text", text_type, True),
        StructField("contained", contained_type, True),
        StructField("extension", extension_type, True),
        StructField("modifierExtension", modifierExtension_type, True),
        StructField("masterIdentifier", identifier, True),
        StructField("identifier", ArrayType(identifier), True),
        StructField("status", StringType(), False),
        StructField("docStatus", StringType(), True),
        StructField("type", codeable_concept, True),
        StructField("category", ArrayType(codeable_concept), True),
        StructField("subject", reference, True),
        StructField("date", TimestampType(), True),
        StructField("author", ArrayType(reference), True),
        StructField("authenticator", reference, True),
        StructField("custodian", reference, True),
        StructField("relatesTo",
                    ArrayType(
                        StructType([
                            StructField("code", StringType(), False),
                            StructField("target", reference, False)
                        ])
                    ), True),
        StructField("description", StringType(), True),
        StructField("securityLabel", ArrayType(codeable_concept), True),
        StructField("content",
                    ArrayType(
                        StructType([
                            StructField("attachment", attachment, False),
                            StructField("format", coding, True)
                        ])
                    ), False),
        StructField("context",
                    StructType([
                        StructField("encounter", ArrayType(reference), True),
                        StructField("event", ArrayType(codeable_concept), True),
                        StructField("period", period, True),
                        StructField("facilityType", codeable_concept, True),
                        StructField("practiceSetting", codeable_concept, True),
                        StructField("sourcePatientInfo", reference, True),
                        StructField("related", ArrayType(reference), True)
                    ]), True)
    ]
)


# COMMAND ----------

# DBTITLE 1,Load DataFrame
df = spark.read.format("json")\
    .schema(document_reference_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/DocumentReference.ndjson")

# COMMAND ----------

# DBTITLE 1,Display
df.display()

# COMMAND ----------

