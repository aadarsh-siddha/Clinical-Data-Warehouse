"""
practitioner_schema.py
=======================
PySpark schema for the FHIR R4 Practitioner resource.
FHIR R4 spec: https://hl7.org/fhir/R4/practitioner.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType,
    StringType, BooleanType, DateType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, period,
    human_name, contact_point, address, attachment
)

# Practitioner -- a person who is directly or indirectly involved in providing healthcare
practitioner_schema = StructType(
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
        StructField("active", BooleanType(), True),
        StructField("name", ArrayType(human_name), True),
        StructField("telecom", ArrayType(contact_point), True),
        StructField("address", ArrayType(address), True),
        StructField("gender", StringType(), True),
        StructField("birthDate", DateType(), True),
        StructField("photo", ArrayType(attachment), True),
        StructField("qualification",
                    ArrayType(
                        StructType([
                            StructField("identifier", ArrayType(identifier), True),
                            StructField("code", codeable_concept, False),
                            StructField("period", period, True),
                            StructField("issuer", reference, True)
                        ])
                    ), True),
        StructField("communication", ArrayType(codeable_concept), True)
    ]
)
