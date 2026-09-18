"""
careteam_schema.py
==================
PySpark schema for the FHIR R4 CareTeam resource.
FHIR R4 spec: https://hl7.org/fhir/R4/careteam.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType, StringType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, period, contact_point, annotation
)

# CareTeam -- planned participants in the coordination and delivery of care
careteam_schema = StructType(
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
        StructField("status", StringType(), True),
        StructField("category", ArrayType(codeable_concept), True),
        StructField("name", StringType(), True),
        StructField("subject", reference, True),
        StructField("period", period, True),
        StructField("participant",
                    ArrayType(
                        StructType(
                            [
                                StructField("role", ArrayType(codeable_concept), True),
                                StructField("member", reference, True),
                                StructField("onBehalfOf", reference, True),
                                StructField("period", period, True)
                            ]
                        )
                    ), True),
        StructField("reasonCode", ArrayType(codeable_concept), True),
        StructField("reasonReference", ArrayType(reference), True),
        StructField("managingOrganization", ArrayType(reference), True),
        StructField("telecom", ArrayType(contact_point), True),
        StructField("note", ArrayType(annotation), True)
    ]
)
