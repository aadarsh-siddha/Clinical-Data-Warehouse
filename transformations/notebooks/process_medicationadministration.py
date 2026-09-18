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

# DBTITLE 1,MedicationAdministration Schema
medication_administration_schema = StructType(
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
        StructField("instantiates", ArrayType(StringType()), True),
        StructField("partOf", ArrayType(reference), True),
        StructField("status", StringType(), False),
        StructField("statusReason", ArrayType(codeable_concept), True),
        StructField("category", codeable_concept, True),
        StructField("medicationCodeableConcept", codeable_concept, True),
        StructField("medicationReference", reference, True),
        StructField("subject", reference, False),
        StructField("context", reference, True),
        StructField("supportingInformation", ArrayType(reference), True),
        StructField("effectiveDateTime", TimestampType(), True),
        StructField("effectivePeriod", period, True),
        StructField("performer",
                    ArrayType(
                        StructType([
                            StructField("function", codeable_concept, True),
                            StructField("actor", reference, False)
                        ])
                    ), True),
        StructField("reasonCode", ArrayType(codeable_concept), True),
        StructField("reasonReference", ArrayType(reference), True),
        StructField("request", reference, True),
        StructField("device", ArrayType(reference), True),
        StructField("note", ArrayType(annotation), True),
        StructField("dosage",
                    StructType([
                        StructField("text", StringType(), True),
                        StructField("site", codeable_concept, True),
                        StructField("route", codeable_concept, True),
                        StructField("method", codeable_concept, True),
                        StructField("dose", StringType(), True),
                        StructField("rateRatio", ratio, True),
                        StructField("rateQuantity", StringType(), True)
                    ]), True),
        StructField("eventHistory", ArrayType(reference), True)
    ]
)


# COMMAND ----------

# DBTITLE 1,Load DataFrame
df = spark.read.format("json")\
    .schema(medication_administration_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/MedicationAdministration.ndjson")

# COMMAND ----------

# DBTITLE 1,Display
df.display()

# COMMAND ----------

