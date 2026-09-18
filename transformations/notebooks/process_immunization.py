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

# DBTITLE 1,Immunization Schema
immunization_schema = StructType(
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
        StructField("status", StringType(), False),
        StructField("statusReason", codeable_concept, True),
        StructField("vaccineCode", codeable_concept, False),
        StructField("patient", reference, False),
        StructField("encounter", reference, True),
        StructField("occurrenceDateTime", TimestampType(), True),
        StructField("occurrenceString", StringType(), True),
        StructField("recorded", TimestampType(), True),
        StructField("primarySource", BooleanType(), True),
        StructField("reportOrigin", codeable_concept, True),
        StructField("location", reference, True),
        StructField("manufacturer", reference, True),
        StructField("lotNumber", StringType(), True),
        StructField("expirationDate", DateType(), True),
        StructField("site", codeable_concept, True),
        StructField("route", codeable_concept, True),
        StructField("doseQuantity", StringType(), True),
        StructField("performer",
                    ArrayType(
                        StructType([
                            StructField("function", codeable_concept, True),
                            StructField("actor", reference, False)
                        ])
                    ), True),
        StructField("note", ArrayType(annotation), True),
        StructField("reasonCode", ArrayType(codeable_concept), True),
        StructField("reasonReference", ArrayType(reference), True),
        StructField("isSubpotent", BooleanType(), True),
        StructField("subpotentReason", ArrayType(codeable_concept), True),
        StructField("education",
                    ArrayType(
                        StructType([
                            StructField("documentType", StringType(), True),
                            StructField("reference", StringType(), True),
                            StructField("publicationDate", TimestampType(), True),
                            StructField("presentationDate", TimestampType(), True)
                        ])
                    ), True),
        StructField("programEligibility", ArrayType(codeable_concept), True),
        StructField("fundingSource", codeable_concept, True),
        StructField("reaction",
                    ArrayType(
                        StructType([
                            StructField("date", TimestampType(), True),
                            StructField("detail", reference, True),
                            StructField("reported", BooleanType(), True)
                        ])
                    ), True),
        StructField("protocolApplied",
                    ArrayType(
                        StructType([
                            StructField("series", StringType(), True),
                            StructField("authority", reference, True),
                            StructField("targetDisease", ArrayType(codeable_concept), True),
                            StructField("doseNumberPositiveInt", IntegerType(), True),
                            StructField("doseNumberString", StringType(), True),
                            StructField("seriesDosesPositiveInt", IntegerType(), True),
                            StructField("seriesDosesString", StringType(), True)
                        ])
                    ), True)
    ]
)


# COMMAND ----------

# DBTITLE 1,Load DataFrame
df = spark.read.format("json")\
    .schema(immunization_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/Immunization.ndjson")

# COMMAND ----------

# DBTITLE 1,Display
df.display()

# COMMAND ----------

