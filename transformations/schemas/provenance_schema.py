"""
provenance_schema.py
====================
PySpark schema for the FHIR R4 Provenance resource.
FHIR R4 spec: https://hl7.org/fhir/R4/provenance.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType, StringType, TimestampType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    codeable_concept, reference, period, signature
)

# Provenance -- who, what, when, and where for a set of resources
provenance_schema = StructType(
    [
        StructField("id", id_type, True),
        StructField("meta", meta_type, True),
        StructField("implicitRules", implicitRules_type, True),
        StructField("language", language_type, True),
        StructField("text", text_type, True),
        StructField("contained", contained_type, True),
        StructField("extension", extension_type, True),
        StructField("modifierExtension", modifierExtension_type, True),
        StructField("target", ArrayType(reference), False),
        StructField("occurredPeriod", period, True),
        StructField("occurredDateTime", TimestampType(), True),
        StructField("recorded", StringType(), False),
        StructField("policy", ArrayType(StringType()), True),
        StructField("location", reference, True),
        StructField("reason", ArrayType(codeable_concept), True),
        StructField("activity", codeable_concept, True),
        StructField("agent",
                    ArrayType(
                        StructType([
                            StructField("type", codeable_concept, True),
                            StructField("role", ArrayType(codeable_concept), True),
                            StructField("who", reference, False),
                            StructField("onBehalfOf", reference, True)
                        ])
                    ), False),
        StructField("entity",
                    ArrayType(
                        StructType([
                            StructField("role", StringType(), False),
                            StructField("what", reference, False),
                            StructField("agent",
                                        ArrayType(
                                            StructType([
                                                StructField("type", codeable_concept, True),
                                                StructField("role", ArrayType(codeable_concept), True),
                                                StructField("who", reference, False),
                                                StructField("onBehalfOf", reference, True)
                                            ])
                                        ), True)
                        ])
                    ), True),
        StructField("signature", ArrayType(signature), True)
    ]
)
