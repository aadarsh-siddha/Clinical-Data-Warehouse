# Databricks notebook source
# DBTITLE 1,Cell 1
import sys
sys.modules.pop('fhir_types', None)
from pyspark.sql.types import *
from fhir_types import identifier, human_name, contact_point, address, codeable_concept, attachment, reference, period, timing, annotation, meta_type, id_type, implicitRules_type, language_type, text_type, contained_type, extension_type, modifierExtension_type

# COMMAND ----------

careplan_schema = StructType(
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
        StructField("replaces", ArrayType(reference), True),
        StructField("partOf", ArrayType(reference), True),
        StructField("status", StringType(), False),
        StructField("intent", StringType(), False),
        StructField("category", ArrayType(codeable_concept), True),
        StructField("title", StringType(), True),
        StructField("description", StringType(), True),
        StructField("subject", reference, False),
        StructField("encounter", reference, True),
        StructField("period", period, True),
        StructField("created", TimestampType(), True),
        StructField("author", reference, True),
        StructField("contributor", ArrayType(reference), True),
        StructField("careTeam", ArrayType(reference), True),
        StructField("addresses", ArrayType(reference), True),
        StructField("supportingInfo", ArrayType(reference), True),
        StructField("goal", ArrayType(reference), True),
        StructField("activity", 
                    ArrayType(
                        StructType(
                            [
                                StructField("outcomeCodeableConcept", ArrayType(codeable_concept), True),
                                StructField("outcomeReference", ArrayType(reference), True),
                                StructField("progress", ArrayType(annotation), True),
                                StructField("reference", reference, True),
                                StructField("detail", StructType(
                                    [          
                                        StructField("kind", StringType(), True),
                                        StructField("instantiatesCanonical", ArrayType(StringType()), True),
                                        StructField("instantiatesUri", ArrayType(StringType()), True),
                                        StructField("code", codeable_concept, True),
                                        StructField("reasonCode", ArrayType(codeable_concept), True),
                                        StructField("reasonReference", ArrayType(reference), True),
                                        StructField("goal", ArrayType(reference), True),
                                        StructField("status", StringType(), True),
                                        StructField("statusReason", codeable_concept, True),
                                        StructField("doNotPerform", BooleanType(), True),
                                        StructField("scheduledTiming", timing, True),
                                        StructField("scheduledPeriod", period, True),
                                        StructField("scheduledString", StringType(), True),
                                        StructField("location", reference, True),
                                        StructField("performer", ArrayType(reference), True),
                                        StructField("productCodeableConcept", codeable_concept, True),
                                        StructField("productReference", reference, True),
                                        StructField("quantity", StringType(), True),
                                        StructField("description", StringType(), True),
                                    ]           
                            ), True),
                        ])
                    ), True)                
    ]
)

# COMMAND ----------

df = spark.read.format("json")\
    .option("schema", careplan_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/CarePlan.ndjson")

# COMMAND ----------

df.display()