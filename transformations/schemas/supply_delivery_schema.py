"""
supply_delivery_schema.py
==========================
PySpark schema for the FHIR R4 SupplyDelivery resource.
FHIR R4 spec: https://hl7.org/fhir/R4/supplydelivery.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType, StringType, TimestampType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, period, quantity, timing
)

# SupplyDelivery -- delivery of bulk supplies to a patient or practitioner
supply_delivery_schema = StructType(
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
        StructField("status", StringType(), True),
        StructField("patient", reference, True),
        StructField("type", codeable_concept, True),
        StructField("suppliedItem",
                    StructType([
                        StructField("quantity", quantity, True),
                        StructField("itemCodeableConcept", codeable_concept, True),
                        StructField("itemReference", reference, True)
                    ]), True),
        StructField("occurrenceDateTime", TimestampType(), True),
        StructField("occurrencePeriod", period, True),
        StructField("occurrenceTiming", timing, True),
        StructField("supplier", reference, True),
        StructField("destination", reference, True),
        StructField("receiver", ArrayType(reference), True)
    ]
)
