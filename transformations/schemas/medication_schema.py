"""
medication_schema.py
====================
PySpark schema for the FHIR R4 Medication resource.
FHIR R4 spec: https://hl7.org/fhir/R4/medication.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType,
    StringType, TimestampType, BooleanType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, ratio
)

# Medication -- a kind of product or substance used in healthcare
medication_schema = StructType(
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
        StructField("code", codeable_concept, True),
        StructField("status", StringType(), True),
        StructField("manufacturer", reference, True),
        StructField("form", codeable_concept, True),
        StructField("amount", ratio, True),
        StructField("ingredient",
                    ArrayType(
                        StructType([
                            StructField("itemCodeableConcept", codeable_concept, True),
                            StructField("itemReference", reference, True),
                            StructField("isActive", BooleanType(), True),
                            StructField("strength", ratio, True)
                        ])
                    ), True),
        StructField("batch",
                    StructType([
                        StructField("lotNumber", StringType(), True),
                        StructField("expirationDate", TimestampType(), True)
                    ]), True)
    ]
)
