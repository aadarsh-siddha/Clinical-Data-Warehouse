"""
allergy_intolerance_schema.py
==============================
PySpark schema for the FHIR R4 AllergyIntolerance resource.
FHIR R4 spec: https://hl7.org/fhir/R4/allergyintolerance.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType,
    StringType, IntegerType, TimestampType, BooleanType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, period, range_type, annotation
)

# AllergyIntolerance -- record of a clinical assessment of an allergy or intolerance
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
        StructField("category", ArrayType(StringType()), True),
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
