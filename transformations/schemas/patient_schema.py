"""
patient_schema.py
=================
PySpark schema for the FHIR R4 Patient resource.
FHIR R4 spec: https://hl7.org/fhir/R4/patient.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType,
    StringType, BooleanType, IntegerType, TimestampType, DateType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, period,
    human_name, contact_point, address, attachment
)

# Patient -- demographics and administrative information about a person receiving care
patient_schema = StructType(
    [
        StructField("id", id_type, True),
        StructField("meta", meta_type, True),
        StructField("implicitRules", implicitRules_type, True),
        StructField("language", language_type, True),
        StructField("text", text_type, True),
        StructField("contained", (contained_type), True),
        StructField("extension", (extension_type), True),
        StructField("modifierExtension", (modifierExtension_type), True),
        StructField("identifier", ArrayType(identifier), True),
        StructField("active", BooleanType(), True),
        StructField("name", ArrayType(human_name), True),
        StructField("telecom", ArrayType(contact_point), True),
        StructField("gender", StringType(), True),
        StructField("birthDate", DateType(), True),
        StructField("deceasedBoolean", BooleanType(), True),
        StructField("deceasedDateTime", TimestampType(), True),
        StructField("address", ArrayType(address), True),
        StructField("maritalStatus", codeable_concept, True),
        StructField("multipleBirthBoolean", BooleanType(), True),
        StructField("multipleBirthInteger", IntegerType(), True),
        StructField("photo", ArrayType(attachment), True),
        StructField("contact",
                    ArrayType(
                        StructType(
                            [
                                StructField("relationship", ArrayType(codeable_concept), True),
                                StructField("name", human_name, True),
                                StructField("telecom", ArrayType(contact_point), True),
                                StructField("address", address, True),
                                StructField("gender", StringType(), True),
                                StructField("organization", reference, True),
                                StructField("period", period, True)
                            ]
                        )
                    ), True),
        StructField("communication",
                    ArrayType(
                        StructType(
                            [
                                StructField("language", codeable_concept, True),
                                StructField("preferred", BooleanType(), True)
                            ]
                        )
                    ), True),
        StructField("generalPractitioner", ArrayType(reference), True),
        StructField("managingOrganization", reference, True),
        StructField("link",
                    ArrayType(
                        StructType(
                            [
                                StructField("other", reference, True),
                                StructField("type", StringType(), True)
                            ]
                        )
                    ), True)
    ]
)
