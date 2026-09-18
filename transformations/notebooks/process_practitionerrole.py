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

# DBTITLE 1,PractitionerRole Schema
practitioner_role_schema = StructType(
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
        StructField("active", BooleanType(), True),
        StructField("period", period, True),
        StructField("practitioner", reference, True),
        StructField("organization", reference, True),
        StructField("code", ArrayType(codeable_concept), True),
        StructField("specialty", ArrayType(codeable_concept), True),
        StructField("location", ArrayType(reference), True),
        StructField("healthcareService", ArrayType(reference), True),
        StructField("telecom", ArrayType(contact_point), True),
        StructField("availableTime",
                    ArrayType(
                        StructType([
                            StructField("daysOfWeek", ArrayType(StringType()), True),
                            StructField("allDay", BooleanType(), True),
                            StructField("availableStartTime", StringType(), True),
                            StructField("availableEndTime", StringType(), True)
                        ])
                    ), True),
        StructField("notAvailable",
                    ArrayType(
                        StructType([
                            StructField("description", StringType(), False),
                            StructField("during", period, True)
                        ])
                    ), True),
        StructField("availabilityExceptions", StringType(), True),
        StructField("endpoint", ArrayType(reference), True)
    ]
)


# COMMAND ----------

# DBTITLE 1,Load DataFrame
df = spark.read.format("json")\
    .schema(practitioner_role_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/PractitionerRole.1783319441317.ndjson")

# COMMAND ----------

# DBTITLE 1,Display
df.display()

# COMMAND ----------

