# Databricks notebook source
# DBTITLE 1,Cell 1
import sys
sys.modules.pop('fhir_types', None)
from pyspark.sql.types import *
from fhir_types import identifier, human_name, contact_point, address, codeable_concept, attachment, reference, period, timing, annotation, meta_type, id_type, implicitRules_type, language_type, text_type, contained_type, extension_type, modifierExtension_type, range_type, quantity

# COMMAND ----------

# DBTITLE 1,Cell 2
diagnostic_report_schema = StructType(
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
        StructField("status", StringType(), False),
        StructField("category", ArrayType(codeable_concept), True),
        StructField("code", codeable_concept, False),
        StructField("subject", reference, True),
        StructField("encounter", reference, True),
        StructField("effectiveDateTime", TimestampType(), True),
        StructField("effectivePeriod", period, True),
        StructField("issued", TimestampType(), True),
        StructField("performer", ArrayType(reference), True),
        StructField("resultsInterpreter", ArrayType(reference), True),
        StructField("specimen", ArrayType(reference), True),
        StructField("result", ArrayType(reference), True),
        StructField("imagingStudy", ArrayType(reference), True),
        StructField("media", 
                    ArrayType(
                        StructType([
                            StructField("comment", StringType(), True),
                            StructField("link", reference, False)
                        ])
                    ), True),
        StructField("conclusion", StringType(), True),
        StructField("conclusionCode", ArrayType(codeable_concept), True),
        StructField("presentedForm", ArrayType(attachment), True)
    ]
)


# COMMAND ----------

# DBTITLE 1,Cell 3
df = spark.read.format("json")\
    .schema(diagnostic_report_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/DiagnosticReport.ndjson")

# COMMAND ----------

df.display()

# COMMAND ----------

