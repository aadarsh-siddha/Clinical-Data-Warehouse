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

# DBTITLE 1,ImagingStudy Schema
imaging_study_schema = StructType(
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
        StructField("modality", ArrayType(coding), True),
        StructField("subject", reference, False),
        StructField("encounter", reference, True),
        StructField("started", TimestampType(), True),
        StructField("basedOn", ArrayType(reference), True),
        StructField("referrer", reference, True),
        StructField("interpreter", ArrayType(reference), True),
        StructField("endpoint", ArrayType(reference), True),
        StructField("numberOfSeries", IntegerType(), True),
        StructField("numberOfInstances", IntegerType(), True),
        StructField("procedureReference", reference, True),
        StructField("procedureCode", ArrayType(codeable_concept), True),
        StructField("location", reference, True),
        StructField("reasonCode", ArrayType(codeable_concept), True),
        StructField("reasonReference", ArrayType(reference), True),
        StructField("note", ArrayType(annotation), True),
        StructField("description", StringType(), True),
        StructField("series",
                    ArrayType(
                        StructType([
                            StructField("uid", StringType(), False),
                            StructField("number", IntegerType(), True),
                            StructField("modality", coding, False),
                            StructField("description", StringType(), True),
                            StructField("numberOfInstances", IntegerType(), True),
                            StructField("endpoint", ArrayType(reference), True),
                            StructField("bodySite", coding, True),
                            StructField("laterality", coding, True),
                            StructField("specimen", ArrayType(reference), True),
                            StructField("started", TimestampType(), True),
                            StructField("performer",
                                        ArrayType(
                                            StructType([
                                                StructField("function", codeable_concept, True),
                                                StructField("actor", reference, False)
                                            ])
                                        ), True),
                            StructField("instance",
                                        ArrayType(
                                            StructType([
                                                StructField("uid", StringType(), False),
                                                StructField("sopClass", coding, False),
                                                StructField("number", IntegerType(), True),
                                                StructField("title", StringType(), True)
                                            ])
                                        ), True)
                        ])
                    ), True)
    ]
)


# COMMAND ----------

# DBTITLE 1,Load DataFrame
df = spark.read.format("json")\
    .schema(imaging_study_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/ImagingStudy.ndjson")

# COMMAND ----------

# DBTITLE 1,Display
df.display()

# COMMAND ----------

