"""
medication_administration_schema.py
======================================
PySpark schema for the FHIR R4 MedicationAdministration resource.
FHIR R4 spec: https://hl7.org/fhir/R4/medicationadministration.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType, StringType, TimestampType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, period, annotation, ratio
)

# MedicationAdministration -- event of a patient consuming or being administered a medication
medication_administration_schema = StructType(
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
        StructField("instantiates", ArrayType(StringType()), True),
        StructField("partOf", ArrayType(reference), True),
        StructField("status", StringType(), False),
        StructField("statusReason", ArrayType(codeable_concept), True),
        StructField("category", codeable_concept, True),
        StructField("medicationCodeableConcept", codeable_concept, True),
        StructField("medicationReference", reference, True),
        StructField("subject", reference, False),
        StructField("context", reference, True),
        StructField("supportingInformation", ArrayType(reference), True),
        StructField("effectiveDateTime", TimestampType(), True),
        StructField("effectivePeriod", period, True),
        StructField("performer",
                    ArrayType(
                        StructType([
                            StructField("function", codeable_concept, True),
                            StructField("actor", reference, False)
                        ])
                    ), True),
        StructField("reasonCode", ArrayType(codeable_concept), True),
        StructField("reasonReference", ArrayType(reference), True),
        StructField("request", reference, True),
        StructField("device", ArrayType(reference), True),
        StructField("note", ArrayType(annotation), True),
        StructField("dosage",
                    StructType([
                        StructField("text", StringType(), True),
                        StructField("site", codeable_concept, True),
                        StructField("route", codeable_concept, True),
                        StructField("method", codeable_concept, True),
                        StructField("dose", StringType(), True),
                        StructField("rateRatio", ratio, True),
                        StructField("rateQuantity", StringType(), True)
                    ]), True),
        StructField("eventHistory", ArrayType(reference), True)
    ]
)
