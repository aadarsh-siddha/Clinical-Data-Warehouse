# Databricks notebook source
# DBTITLE 1,Cell 1
import sys
sys.modules.pop('fhir_types', None)
from pyspark.sql.types import *
from fhir_types import identifier, human_name, contact_point, address, codeable_concept, attachment, reference, period, timing, annotation, meta_type, id_type, implicitRules_type, language_type, text_type, contained_type, extension_type, modifierExtension_type

# COMMAND ----------

careteam_schema = StructType(
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
        StructField("status", StringType(), True),
        StructField("category", ArrayType(codeable_concept), True),
        StructField("name", StringType(), True),
        StructField("subject", reference, True),
        StructField("period", period, True),
        StructField("participant", 
                    ArrayType(
                        StructType(
                            [
                                StructField("role", ArrayType(codeable_concept), True),
                                StructField("member", reference, True),
                                StructField("onBehalfOf", reference, True),
                                StructField("period", period, True)
                            ]
                        )
                    ), True),
        StructField("reasonCode", ArrayType(codeable_concept), True),
        StructField("reasonReference", ArrayType(reference), True),
        StructField("managingOrganization", ArrayType(reference), True),
        StructField("telecom", ArrayType(contact_point), True),
        StructField("note", ArrayType(annotation), True)  
    ]
)

# COMMAND ----------

df = spark.read.format("json")\
    .option("schema", careteam_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/CareTeam.ndjson")

# COMMAND ----------

df.display()

# COMMAND ----------

