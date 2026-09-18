# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,Imports
import sys
sys.modules.pop('fhir_types', None)
from pyspark.sql.types import *
from fhir_types import identifier, human_name, contact_point, address, codeable_concept, attachment, reference, period, timing, annotation, meta_type, id_type, implicitRules_type, language_type, text_type, contained_type, extension_type, modifierExtension_type, range_type, quantity, ratio, sampled_data

# COMMAND ----------

# DBTITLE 1,Observation Schema
observation_schema = StructType(
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
        StructField("status", StringType(), False),
        StructField("category", ArrayType(codeable_concept), True),
        StructField("code", codeable_concept, False),
        StructField("subject", reference, True),
        StructField("focus", ArrayType(reference), True),
        StructField("encounter", reference, True),
        StructField("effectiveDateTime", TimestampType(), True),
        StructField("effectivePeriod", period, True),
        StructField("effectiveTiming", timing, True),
        StructField("effectiveInstant", StringType(), True),
        StructField("issued", StringType(), True),
        StructField("performer", ArrayType(reference), True),
        StructField("valueQuantity", quantity, True),
        StructField("valueCodeableConcept", codeable_concept, True),
        StructField("valueString", StringType(), True),
        StructField("valueBoolean", BooleanType(), True),
        StructField("valueInteger", IntegerType(), True),
        StructField("valueRange", range_type, True),
        StructField("valueRatio", ratio, True),
        StructField("valueSampledData", sampled_data, True),
        StructField("valueTime", StringType(), True),
        StructField("valueDateTime", TimestampType(), True),
        StructField("valuePeriod", period, True),
        StructField("dataAbsentReason", codeable_concept, True),
        StructField("interpretation", ArrayType(codeable_concept), True),
        StructField("note", ArrayType(annotation), True),
        StructField("bodySite", codeable_concept, True),
        StructField("method", codeable_concept, True),
        StructField("specimen", reference, True),
        StructField("device", reference, True),
        StructField("referenceRange",
                    ArrayType(
                        StructType([
                            StructField("low", StringType(), True),
                            StructField("high", StringType(), True),
                            StructField("type", codeable_concept, True),
                            StructField("appliesTo", ArrayType(codeable_concept), True),
                            StructField("age", range_type, True),
                            StructField("text", StringType(), True)
                        ])
                    ), True),
        StructField("hasMember", ArrayType(reference), True),
        StructField("derivedFrom", ArrayType(reference), True),
        StructField("component",
                    ArrayType(
                        StructType([
                            StructField("code", codeable_concept, False),
                            StructField("valueQuantity", quantity, True),
                            StructField("valueCodeableConcept", codeable_concept, True),
                            StructField("valueString", StringType(), True),
                            StructField("valueBoolean", BooleanType(), True),
                            StructField("valueInteger", IntegerType(), True),
                            StructField("valueRange", range_type, True),
                            StructField("valueRatio", ratio, True),
                            StructField("valueSampledData", sampled_data, True),
                            StructField("valueTime", StringType(), True),
                            StructField("valueDateTime", TimestampType(), True),
                            StructField("valuePeriod", period, True),
                            StructField("dataAbsentReason", codeable_concept, True),
                            StructField("interpretation", ArrayType(codeable_concept), True),
                            StructField("referenceRange", ArrayType(StringType()), True)
                        ])
                    ), True)
    ]
)


# COMMAND ----------

# DBTITLE 1,Load DataFrame
df = spark.read.format("json")\
    .schema(observation_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/Observation.ndjson")

# COMMAND ----------

# DBTITLE 1,Display
df.display()

# COMMAND ----------

