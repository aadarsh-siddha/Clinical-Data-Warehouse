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

# DBTITLE 1,Procedure Schema
procedure_schema = StructType(
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
        StructField("instantiatesCanonical", ArrayType(StringType()), True),
        StructField("instantiatesUri", ArrayType(StringType()), True),
        StructField("basedOn", ArrayType(reference), True),
        StructField("partOf", ArrayType(reference), True),
        StructField("status", StringType(), False),
        StructField("statusReason", codeable_concept, True),
        StructField("category", codeable_concept, True),
        StructField("code", codeable_concept, True),
        StructField("subject", reference, False),
        StructField("encounter", reference, True),
        StructField("performedDateTime", TimestampType(), True),
        StructField("performedPeriod", period, True),
        StructField("performedString", StringType(), True),
        StructField("performedAge", StringType(), True),
        StructField("performedRange", range_type, True),
        StructField("recorder", reference, True),
        StructField("asserter", reference, True),
        StructField("performer",
                    ArrayType(
                        StructType([
                            StructField("function", codeable_concept, True),
                            StructField("actor", reference, False),
                            StructField("onBehalfOf", reference, True)
                        ])
                    ), True),
        StructField("location", reference, True),
        StructField("reasonCode", ArrayType(codeable_concept), True),
        StructField("reasonReference", ArrayType(reference), True),
        StructField("bodySite", ArrayType(codeable_concept), True),
        StructField("outcome", codeable_concept, True),
        StructField("report", ArrayType(reference), True),
        StructField("complication", ArrayType(codeable_concept), True),
        StructField("complicationDetail", ArrayType(reference), True),
        StructField("followUp", ArrayType(codeable_concept), True),
        StructField("note", ArrayType(annotation), True),
        StructField("focalDevice",
                    ArrayType(
                        StructType([
                            StructField("action", codeable_concept, True),
                            StructField("manipulated", reference, False)
                        ])
                    ), True),
        StructField("usedReference", ArrayType(reference), True),
        StructField("usedCode", ArrayType(codeable_concept), True)
    ]
)


# COMMAND ----------

# DBTITLE 1,Load DataFrame
df = spark.read.format("json")\
    .schema(procedure_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/Procedure.ndjson")

# COMMAND ----------

# DBTITLE 1,Display
df.display()

# COMMAND ----------

