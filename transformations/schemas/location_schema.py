"""
location_schema.py
==================
PySpark schema for the FHIR R4 Location resource.
FHIR R4 spec: https://hl7.org/fhir/R4/location.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType,
    StringType, BooleanType, DoubleType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, contact_point, address, coding
)

# Location -- details and position information for a physical place
location_schema = StructType(
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
        StructField("operationalStatus", coding, True),
        StructField("name", StringType(), True),
        StructField("alias", ArrayType(StringType()), True),
        StructField("description", StringType(), True),
        StructField("mode", StringType(), True),
        StructField("type", ArrayType(codeable_concept), True),
        StructField("telecom", ArrayType(contact_point), True),
        StructField("address", address, True),
        StructField("physicalType", codeable_concept, True),
        StructField("position",
                    StructType([
                        StructField("longitude", DoubleType(), False),
                        StructField("latitude", DoubleType(), False),
                        StructField("altitude", DoubleType(), True)
                    ]), True),
        StructField("managingOrganization", reference, True),
        StructField("partOf", reference, True),
        StructField("hoursOfOperation",
                    ArrayType(
                        StructType([
                            StructField("daysOfWeek", ArrayType(StringType()), True),
                            StructField("allDay", BooleanType(), True),
                            StructField("openingTime", StringType(), True),
                            StructField("closingTime", StringType(), True)
                        ])
                    ), True),
        StructField("availabilityExceptions", StringType(), True),
        StructField("endpoint", ArrayType(reference), True)
    ]
)
