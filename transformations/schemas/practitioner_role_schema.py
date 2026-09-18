"""
practitioner_role_schema.py
=============================
PySpark schema for the FHIR R4 PractitionerRole resource.
FHIR R4 spec: https://hl7.org/fhir/R4/practitionerrole.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType, StringType, BooleanType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, period, contact_point
)

# PractitionerRole -- roles/locations/specialties/services a practitioner may perform
practitioner_role_schema = StructType(
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
        StructField("period", period, True),
        StructField("practitioner", reference, True),
        StructField("organization", reference, True),
        StructField("code", ArrayType(codeable_concept), True),
        StructField("specialty", ArrayType(codeable_concept), True),
        StructField("location", ArrayType(reference), True),
        StructField("healthcareService", ArrayType(reference), True),
        StructField("telecom", ArrayType(contact_point), True),
        StructField("availableTime",
                    ArrayType(
                        StructType([
                            StructField("daysOfWeek", ArrayType(StringType()), True),
                            StructField("allDay", BooleanType(), True),
                            StructField("availableStartTime", StringType(), True),
                            StructField("availableEndTime", StringType(), True)
                        ])
                    ), True),
        StructField("notAvailable",
                    ArrayType(
                        StructType([
                            StructField("description", StringType(), False),
                            StructField("during", period, True)
                        ])
                    ), True),
        StructField("availabilityExceptions", StringType(), True),
        StructField("endpoint", ArrayType(reference), True)
    ]
)
