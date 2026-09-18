"""
device_schema.py
================
PySpark schema for the FHIR R4 Device resource.
FHIR R4 spec: https://hl7.org/fhir/R4/device.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType, StringType, TimestampType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, annotation, contact_point, quantity
)

# Device -- an item used in the provision of healthcare without substantial human intervention
device_schema = StructType(
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
        StructField("definition", reference, True),
        StructField("udiCarrier",
                    ArrayType(
                        StructType([
                            StructField("deviceIdentifier", StringType(), True),
                            StructField("issuer", StringType(), True),
                            StructField("jurisdiction", StringType(), True),
                            StructField("carrierAIDC", StringType(), True),
                            StructField("carrierHRF", StringType(), True),
                            StructField("entryType", StringType(), True)
                        ])
                    ), True),
        StructField("status", StringType(), True),
        StructField("statusReason", ArrayType(codeable_concept), True),
        StructField("distinctIdentifier", StringType(), True),
        StructField("manufacturer", StringType(), True),
        StructField("manufactureDate", TimestampType(), True),
        StructField("expirationDate", TimestampType(), True),
        StructField("lotNumber", StringType(), True),
        StructField("serialNumber", StringType(), True),
        StructField("deviceName",
                    ArrayType(
                        StructType([
                            StructField("name", StringType(), True),
                            StructField("type", StringType(), True)
                        ])
                    ), True),
        StructField("modelNumber", StringType(), True),
        StructField("partNumber", StringType(), True),
        StructField("type", codeable_concept, True),
        StructField("specialization",
                    ArrayType(
                        StructType([
                            StructField("systemType", codeable_concept, False),
                            StructField("version", StringType(), True)
                        ])
                    ), True),
        StructField("version",
                    ArrayType(
                        StructType([
                            StructField("type", codeable_concept, True),
                            StructField("component", identifier, True),
                            StructField("value", StringType(), False)
                        ])
                    ), True),
        StructField("property",
                    ArrayType(
                        StructType([
                            StructField("type", codeable_concept, False),
                            StructField("valueQuantity", ArrayType(quantity), True),
                            StructField("valueCode", ArrayType(codeable_concept), True)
                        ])
                    ), True),
        StructField("patient", reference, True),
        StructField("owner", reference, True),
        StructField("contact", ArrayType(contact_point), True),
        StructField("location", reference, True),
        StructField("url", StringType(), True),
        StructField("note", ArrayType(annotation), True),
        StructField("safety", ArrayType(codeable_concept), True),
        StructField("parent", reference, True)
    ]
)
