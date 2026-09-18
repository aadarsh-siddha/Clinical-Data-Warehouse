# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,Imports
import sys
sys.modules.pop('fhir_types', None)
from pyspark.sql.types import *
from fhir_types import identifier, human_name, contact_point, address, codeable_concept, attachment, reference, period, timing, annotation, meta_type, id_type, implicitRules_type, language_type, text_type, contained_type, extension_type, modifierExtension_type, range_type, quantity, dosage

# COMMAND ----------

# DBTITLE 1,MedicationRequest Schema
medication_request_schema = StructType(
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
        StructField("statusReason", codeable_concept, True),
        StructField("intent", StringType(), False),
        StructField("category", ArrayType(codeable_concept), True),
        StructField("priority", StringType(), True),
        StructField("doNotPerform", BooleanType(), True),
        StructField("reportedBoolean", BooleanType(), True),
        StructField("reportedReference", reference, True),
        StructField("medicationCodeableConcept", codeable_concept, True),
        StructField("medicationReference", reference, True),
        StructField("subject", reference, False),
        StructField("encounter", reference, True),
        StructField("supportingInformation", ArrayType(reference), True),
        StructField("authoredOn", TimestampType(), True),
        StructField("requester", reference, True),
        StructField("performer", reference, True),
        StructField("performerType", codeable_concept, True),
        StructField("recorder", reference, True),
        StructField("reasonCode", ArrayType(codeable_concept), True),
        StructField("reasonReference", ArrayType(reference), True),
        StructField("instantiatesCanonical", ArrayType(StringType()), True),
        StructField("instantiatesUri", ArrayType(StringType()), True),
        StructField("basedOn", ArrayType(reference), True),
        StructField("groupIdentifier", identifier, True),
        StructField("courseOfTherapyType", codeable_concept, True),
        StructField("insurance", ArrayType(reference), True),
        StructField("note", ArrayType(annotation), True),
        StructField("dosageInstruction", ArrayType(dosage), True),
        StructField("dispenseRequest",
                    StructType([
                        StructField("initialFill",
                                    StructType([
                                        StructField("quantity", quantity, True),
                                        StructField("duration", StringType(), True)
                                    ]), True),
                        StructField("dispenseInterval", StringType(), True),
                        StructField("validityPeriod", period, True),
                        StructField("numberOfRepeatsAllowed", IntegerType(), True),
                        StructField("quantity", StringType(), True),
                        StructField("expectedSupplyDuration", StringType(), True),
                        StructField("performer", reference, True)
                    ]), True),
        StructField("substitution",
                    StructType([
                        StructField("allowedBoolean", BooleanType(), True),
                        StructField("allowedCodeableConcept", codeable_concept, True),
                        StructField("reason", codeable_concept, True)
                    ]), True),
        StructField("priorPrescription", reference, True),
        StructField("detectedIssue", ArrayType(reference), True),
        StructField("eventHistory", ArrayType(reference), True)
    ]
)


# COMMAND ----------

# DBTITLE 1,Load DataFrame
df = spark.read.format("json")\
    .schema(medication_request_schema)\
    .load("s3://healthcare-analytics-bucket-042740341370-us-east-1-an/bulk-fhir-data/7-7-2026/MedicationRequest.ndjson")

# COMMAND ----------

# DBTITLE 1,Display
df.display()

# COMMAND ----------

