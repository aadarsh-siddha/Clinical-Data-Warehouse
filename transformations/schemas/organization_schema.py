"""
organization_schema.py
=======================
PySpark schema for the FHIR R4 Organization resource.
FHIR R4 spec: https://hl7.org/fhir/R4/organization.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType, StringType, BooleanType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, contact_point, address, human_name
)

# Organization -- a formally or informally recognized grouping of people or organizations
organization_schema = StructType(
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
        StructField("type", ArrayType(codeable_concept), True),
        StructField("name", StringType(), True),
        StructField("alias", ArrayType(StringType()), True),
        StructField("telecom", ArrayType(contact_point), True),
        StructField("address", ArrayType(address), True),
        StructField("partOf", reference, True),
        StructField("contact",
                    ArrayType(
                        StructType([
                            StructField("purpose", codeable_concept, True),
                            StructField("name", human_name, True),
                            StructField("telecom", ArrayType(contact_point), True),
                            StructField("address", address, True)
                        ])
                    ), True),
        StructField("endpoint", ArrayType(reference), True)
    ]
)
