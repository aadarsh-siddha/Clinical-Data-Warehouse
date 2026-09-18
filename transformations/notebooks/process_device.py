# Databricks notebook source
# DBTITLE 1,Cell 1
import sys
sys.modules.pop('fhir_types', None)
from pyspark.sql.types import *
from fhir_types import identifier, human_name, contact_point, address, codeable_concept, attachment, reference, period, timing, annotation, meta_type, id_type, implicitRules_type, language_type, text_type, contained_type, extension_type, modifierExtension_type, range_type, quantity

# COMMAND ----------

device_schema = StructType(
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
        StructField("definition", reference, True),
        StructField("udiCarrier", 
                    ArrayType(
                        StructType([
                            StructField("deviceIdentifier", StringType(), True),
                            StructField("issuer", StringType(), True),
                            StructField("jurisdiction", StringType(), True),
                            StructField("carrierAIDC", StringType(), True),
                            StructField("carrierHRF", StringType(), True),
                            StructField("entryType", StringType(), True)
                        ])
                    ), True),
        StructField("status", StringType(), True),
        StructField("statusReason", ArrayType(codeable_concept), True),
        StructField("distinctIdentifier", StringType(), True),
        StructField("manufacturer", StringType(), True),
        StructField("manufactureDate", TimestampType(), True),
        StructField("expirationDate", TimestampType(), True),
        StructField("lotNumber", StringType(), True),
        StructField("serialNumber", StringType(), True),
        StructField("deviceName", 
                    ArrayType(
                        StructType([
                            StructField("name", StringType(), True),
                            StructField("type", StringType(), True)
                        ])
                    ), True),
        StructField("modeNumber", StringType(), True),
        StructField("partNumber", StringType(), True),
        StructField("type", codeable_concept, True),
        StructField("specialization", 
                    ArrayType(
                        StructType([
                            StructField("systemType", codeable_concept, False),
                            StructField("version", StringType(), True)
                        ])
                    ), True),
        StructField("version", 
                    ArrayType(
                        StructType([
                            StructField("type", codeable_concept, True),
                            StructField("component", identifier, True),
                            StructField("value", StringType(), False)                            
                        ])
                    ), True),
        StructField("property", 
                    ArrayType(
                        StructType([
                            StructField("type", codeable_concept, False),
                            StructField("valueQuantity", ArrayType(quantity), True),
                            StructField("valueCode", ArrayType(codeable_concept), True)
                        ])
                    ), True),
        StructField("patient", reference, True),
        StructField("owner", reference, True),
        StructField("contact", ArrayType(contact_point), True),
        StructField("location", reference, True),
        StructField("url", StringType(), True),
        StructField("note", ArrayType(annotation), True),
        StructField("safety", ArrayType(codeable_concept), True),
        StructField("parent", reference, True)
    ]
)


# COMMAND ----------

df = spark.read.format("json")\
    .option("schema", device_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/Device.ndjson")

# COMMAND ----------

df.display()

# COMMAND ----------

