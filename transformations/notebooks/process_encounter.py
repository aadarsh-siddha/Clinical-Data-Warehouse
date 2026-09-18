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

# DBTITLE 1,Encounter Schema
encounter_schema = StructType(
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
        StructField("statusHistory",
                    ArrayType(
                        StructType([
                            StructField("status", StringType(), False),
                            StructField("period", period, False)
                        ])
                    ), True),
        StructField("class", coding, False),
        StructField("classHistory",
                    ArrayType(
                        StructType([
                            StructField("class", coding, False),
                            StructField("period", period, False)
                        ])
                    ), True),
        StructField("type", ArrayType(codeable_concept), True),
        StructField("serviceType", codeable_concept, True),
        StructField("priority", codeable_concept, True),
        StructField("subject", reference, True),
        StructField("episodeOfCare", ArrayType(reference), True),
        StructField("basedOn", ArrayType(reference), True),
        StructField("participant",
                    ArrayType(
                        StructType([
                            StructField("type", ArrayType(codeable_concept), True),
                            StructField("period", period, True),
                            StructField("individual", reference, True)
                        ])
                    ), True),
        StructField("appointment", ArrayType(reference), True),
        StructField("period", period, True),
        StructField("length", StringType(), True),
        StructField("reasonCode", ArrayType(codeable_concept), True),
        StructField("reasonReference", ArrayType(reference), True),
        StructField("diagnosis",
                    ArrayType(
                        StructType([
                            StructField("condition", reference, False),
                            StructField("use", codeable_concept, True),
                            StructField("rank", IntegerType(), True)
                        ])
                    ), True),
        StructField("account", ArrayType(reference), True),
        StructField("hospitalization",
                    StructType([
                        StructField("preAdmissionIdentifier", identifier, True),
                        StructField("origin", reference, True),
                        StructField("admitSource", codeable_concept, True),
                        StructField("reAdmission", codeable_concept, True),
                        StructField("dietPreference", ArrayType(codeable_concept), True),
                        StructField("specialCourtesy", ArrayType(codeable_concept), True),
                        StructField("specialArrangement", ArrayType(codeable_concept), True),
                        StructField("destination", reference, True),
                        StructField("dischargeDisposition", codeable_concept, True)
                    ]), True),
        StructField("location",
                    ArrayType(
                        StructType([
                            StructField("location", reference, False),
                            StructField("status", StringType(), True),
                            StructField("physicalType", codeable_concept, True),
                            StructField("period", period, True)
                        ])
                    ), True),
        StructField("serviceProvider", reference, True),
        StructField("partOf", reference, True)
    ]
)


# COMMAND ----------

# DBTITLE 1,Load DataFrame
df = spark.read.format("json")\
    .schema(encounter_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/Encounter.ndjson")

# COMMAND ----------

# DBTITLE 1,Display
df.display()

# COMMAND ----------

