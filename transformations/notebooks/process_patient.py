# Databricks notebook source
# DBTITLE 1,Cell 1
import sys
sys.modules.pop('fhir_types', None)
from pyspark.sql.types import *
from fhir_types import identifier, human_name, contact_point, address, codeable_concept, attachment, reference, period, id_type, meta_type, implicitRules_type, language_type, text_type, contained_type, extension_type, modifierExtension_type

# COMMAND ----------

patient_schema = StructType(
    [
        StructField("id", id_type, True),
        StructField("meta", meta_type, True),
        StructField("implicitRules", implicitRules_type, True),
        StructField("language", language_type, True),
        StructField("text", text_type, True),
        StructField("contained", (contained_type), True),
        StructField("extension", (extension_type), True),
        StructField("modifierExtension", (modifierExtension_type), True),
        StructField("identifier", ArrayType(identifier), True),
        StructField("active", BooleanType(), True),
        StructField("name", ArrayType(human_name), True),
        StructField("telecom", ArrayType(contact_point), True),
        StructField("gender", StringType(), True),
        StructField("birthDate", DateType(), True),
        StructField("deceasedBoolean", BooleanType(), True),
        StructField("deceasedDateTime", DateType(), True),
        StructField("address", ArrayType(address), True),
        StructField("maritalStatus", codeable_concept, True),
        StructField("multipleBirthBoolean", BooleanType(), True),
        StructField("multipleBirthInteger", IntegerType(), True),
        StructField("photo", ArrayType(attachment), True),
        StructField("contact", 
                    ArrayType(
                        StructType(
                            [
                                StructField("relationship", ArrayType(codeable_concept), True),
                                StructField("name", human_name, True),
                                StructField("telecom", ArrayType(contact_point), True),
                                StructField("address", address, True),
                                StructField("gender", StringType(), True),
                                StructField("organization", reference, True),
                                StructField("period", period, True)
                            ]
                        )
                    ),True),
        StructField("communication",
                    ArrayType(
                        StructType(
                            [
                                StructField("language", codeable_concept, True),
                                StructField("preferred", BooleanType(), True)
                            ]
                        )
                    ), True),
        StructField("generalPractitioner", ArrayType(reference), True),
        StructField("managingOrganization", reference, True),
        StructField("link", ArrayType(
                        StructType(
                            [
                                StructField("other", reference, True),
                                StructField("type", StringType(), True)
                            ]
                        )
                    ), True)
    ]
)

# COMMAND ----------

df = spark.read.format("json")\
    .option("schema", patient_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/Patient.ndjson")

# COMMAND ----------

df.display()