"""
observation_schema.py
======================
PySpark schema for the FHIR R4 Observation resource.
FHIR R4 spec: https://hl7.org/fhir/R4/observation.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType,
    StringType, TimestampType, BooleanType, IntegerType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, period, timing,
    quantity, range_type, ratio, sampled_data, annotation
)

# Observation -- measurements and assertions about a patient, device, or other subject
observation_schema = StructType(
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
        StructField("basedOn", ArrayType(reference), True),
        StructField("partOf", ArrayType(reference), True),
        StructField("status", StringType(), False),
        StructField("category", ArrayType(codeable_concept), True),
        StructField("code", codeable_concept, False),
        StructField("subject", reference, True),
        StructField("focus", ArrayType(reference), True),
        StructField("encounter", reference, True),
        StructField("effectiveDateTime", TimestampType(), True),
        StructField("effectivePeriod", period, True),
        StructField("effectiveTiming", timing, True),
        StructField("effectiveInstant", StringType(), True),
        StructField("issued", StringType(), True),
        StructField("performer", ArrayType(reference), True),
        StructField("valueQuantity", quantity, True),
        StructField("valueCodeableConcept", codeable_concept, True),
        StructField("valueString", StringType(), True),
        StructField("valueBoolean", BooleanType(), True),
        StructField("valueInteger", IntegerType(), True),
        StructField("valueRange", range_type, True),
        StructField("valueRatio", ratio, True),
        StructField("valueSampledData", sampled_data, True),
        StructField("valueTime", StringType(), True),
        StructField("valueDateTime", TimestampType(), True),
        StructField("valuePeriod", period, True),
        StructField("dataAbsentReason", codeable_concept, True),
        StructField("interpretation", ArrayType(codeable_concept), True),
        StructField("note", ArrayType(annotation), True),
        StructField("bodySite", codeable_concept, True),
        StructField("method", codeable_concept, True),
        StructField("specimen", reference, True),
        StructField("device", reference, True),
        StructField("referenceRange",
                    ArrayType(
                        StructType([
                            StructField("low", StringType(), True),
                            StructField("high", StringType(), True),
                            StructField("type", codeable_concept, True),
                            StructField("appliesTo", ArrayType(codeable_concept), True),
                            StructField("age", range_type, True),
                            StructField("text", StringType(), True)
                        ])
                    ), True),
        StructField("hasMember", ArrayType(reference), True),
        StructField("derivedFrom", ArrayType(reference), True),
        StructField("component",
                    ArrayType(
                        StructType([
                            StructField("code", codeable_concept, False),
                            StructField("valueQuantity", quantity, True),
                            StructField("valueCodeableConcept", codeable_concept, True),
                            StructField("valueString", StringType(), True),
                            StructField("valueBoolean", BooleanType(), True),
                            StructField("valueInteger", IntegerType(), True),
                            StructField("valueRange", range_type, True),
                            StructField("valueRatio", ratio, True),
                            StructField("valueSampledData", sampled_data, True),
                            StructField("valueTime", StringType(), True),
                            StructField("valueDateTime", TimestampType(), True),
                            StructField("valuePeriod", period, True),
                            StructField("dataAbsentReason", codeable_concept, True),
                            StructField("interpretation", ArrayType(codeable_concept), True),
                            StructField("referenceRange", ArrayType(StringType()), True)
                        ])
                    ), True)
    ]
)
