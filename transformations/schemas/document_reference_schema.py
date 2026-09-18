"""
document_reference_schema.py
==============================
PySpark schema for the FHIR R4 DocumentReference resource.
FHIR R4 spec: https://hl7.org/fhir/R4/documentreference.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType, StringType, TimestampType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, period, attachment, coding
)

# DocumentReference -- a reference to a document of any kind for any purpose
document_reference_schema = StructType(
    [
        StructField("id", id_type, True),
        StructField("meta", meta_type, True),
        StructField("implicitRules", implicitRules_type, True),
        StructField("language", language_type, True),
        StructField("text", text_type, True),
        StructField("contained", contained_type, True),
        StructField("extension", extension_type, True),
        StructField("modifierExtension", modifierExtension_type, True),
        StructField("masterIdentifier", identifier, True),
        StructField("identifier", ArrayType(identifier), True),
        StructField("status", StringType(), False),
        StructField("docStatus", StringType(), True),
        StructField("type", codeable_concept, True),
        StructField("category", ArrayType(codeable_concept), True),
        StructField("subject", reference, True),
        StructField("date", TimestampType(), True),
        StructField("author", ArrayType(reference), True),
        StructField("authenticator", reference, True),
        StructField("custodian", reference, True),
        StructField("relatesTo",
                    ArrayType(
                        StructType([
                            StructField("code", StringType(), False),
                            StructField("target", reference, False)
                        ])
                    ), True),
        StructField("description", StringType(), True),
        StructField("securityLabel", ArrayType(codeable_concept), True),
        StructField("content",
                    ArrayType(
                        StructType([
                            StructField("attachment", attachment, False),
                            StructField("format", coding, True)
                        ])
                    ), False),
        StructField("context",
                    StructType([
                        StructField("encounter", ArrayType(reference), True),
                        StructField("event", ArrayType(codeable_concept), True),
                        StructField("period", period, True),
                        StructField("facilityType", codeable_concept, True),
                        StructField("practiceSetting", codeable_concept, True),
                        StructField("sourcePatientInfo", reference, True),
                        StructField("related", ArrayType(reference), True)
                    ]), True)
    ]
)
