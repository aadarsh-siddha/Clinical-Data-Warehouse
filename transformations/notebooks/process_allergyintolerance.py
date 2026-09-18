# Databricks notebook source
# DBTITLE 1,Cell 1
import sys
sys.modules.pop('fhir_types', None)
from pyspark.sql.types import *
from fhir_types import identifier, human_name, contact_point, address, codeable_concept, attachment, reference, period, range_type, annotation, id_type, meta_type, implicitRules_type, language_type, text_type, contained_type, extension_type, modifierExtension_type

# COMMAND ----------

allergy_intolerance_schema = StructType(
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
        StructField("clinicalStatus", codeable_concept, True),
        StructField("verificationStatus", codeable_concept, True),
        StructField("type", StringType(), True),
        StructField("category", StringType(), True),
        StructField("criticality", StringType(), True),
        StructField("code", codeable_concept, True),
        StructField("patient", reference, False),
        StructField("encounter", reference, True),
        StructField("onsetDateTime", TimestampType(), True),
        StructField("onsetAge", IntegerType(), True),
        StructField("onsetPeriod", period, True),
        StructField("onsetRange", range_type, True),
        StructField("onsetString", StringType(), True),
        StructField("recordedDate", TimestampType(), True),
        StructField("recorder", reference, True),
        StructField("asserter", reference, True),
        StructField("lastOccurrence", TimestampType(), True),
        StructField("note", ArrayType(annotation), True),
        StructField("reaction", 
                    ArrayType(
                        StructType(
                            [
                                StructField("substance", codeable_concept, True),
                                StructField("manifestation", ArrayType(codeable_concept), False),
                                StructField("description", StringType(), True),
                                StructField("onset", TimestampType(), True),
                                StructField("severity", StringType(), True),
                                StructField("exposureRoute", codeable_concept, True),
                                StructField("note", ArrayType(annotation), True)
                            ]       
                        )
                    ), True)            
    ]
)

# COMMAND ----------

df = spark.read.format("json")\
    .option("schema", allergy_intolerance_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/AllergyIntolerance.ndjson")

# COMMAND ----------

df.display()

# COMMAND ----------

