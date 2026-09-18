"""
immunization_schema.py
=======================
PySpark schema for the FHIR R4 Immunization resource.
FHIR R4 spec: https://hl7.org/fhir/R4/immunization.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType,
    StringType, TimestampType, BooleanType, DateType, IntegerType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, annotation
)

# Immunization -- a patient being administered a vaccine or a record of an immunization
immunization_schema = StructType(
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
        StructField("vaccineCode", codeable_concept, False),
        StructField("patient", reference, False),
        StructField("encounter", reference, True),
        StructField("occurrenceDateTime", TimestampType(), True),
        StructField("occurrenceString", StringType(), True),
        StructField("recorded", TimestampType(), True),
        StructField("primarySource", BooleanType(), True),
        StructField("reportOrigin", codeable_concept, True),
        StructField("location", reference, True),
        StructField("manufacturer", reference, True),
        StructField("lotNumber", StringType(), True),
        StructField("expirationDate", DateType(), True),
        StructField("site", codeable_concept, True),
        StructField("route", codeable_concept, True),
        StructField("doseQuantity", StringType(), True),
        StructField("performer",
                    ArrayType(
                        StructType([
                            StructField("function", codeable_concept, True),
                            StructField("actor", reference, False)
                        ])
                    ), True),
        StructField("note", ArrayType(annotation), True),
        StructField("reasonCode", ArrayType(codeable_concept), True),
        StructField("reasonReference", ArrayType(reference), True),
        StructField("isSubpotent", BooleanType(), True),
        StructField("subpotentReason", ArrayType(codeable_concept), True),
        StructField("education",
                    ArrayType(
                        StructType([
                            StructField("documentType", StringType(), True),
                            StructField("reference", StringType(), True),
                            StructField("publicationDate", TimestampType(), True),
                            StructField("presentationDate", TimestampType(), True)
                        ])
                    ), True),
        StructField("programEligibility", ArrayType(codeable_concept), True),
        StructField("fundingSource", codeable_concept, True),
        StructField("reaction",
                    ArrayType(
                        StructType([
                            StructField("date", TimestampType(), True),
                            StructField("detail", reference, True),
                            StructField("reported", BooleanType(), True)
                        ])
                    ), True),
        StructField("protocolApplied",
                    ArrayType(
                        StructType([
                            StructField("series", StringType(), True),
                            StructField("authority", reference, True),
                            StructField("targetDisease", ArrayType(codeable_concept), True),
                            StructField("doseNumberPositiveInt", IntegerType(), True),
                            StructField("doseNumberString", StringType(), True),
                            StructField("seriesDosesPositiveInt", IntegerType(), True),
                            StructField("seriesDosesString", StringType(), True)
                        ])
                    ), True)
    ]
)
