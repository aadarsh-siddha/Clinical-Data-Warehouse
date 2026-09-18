"""
procedure_schema.py
===================
PySpark schema for the FHIR R4 Procedure resource.
FHIR R4 spec: https://hl7.org/fhir/R4/procedure.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType, StringType, TimestampType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, period, annotation, range_type
)

# Procedure -- an action that is or was performed on or for a patient
procedure_schema = StructType(
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
        StructField("instantiatesCanonical", ArrayType(StringType()), True),
        StructField("instantiatesUri", ArrayType(StringType()), True),
        StructField("basedOn", ArrayType(reference), True),
        StructField("partOf", ArrayType(reference), True),
        StructField("status", StringType(), False),
        StructField("statusReason", codeable_concept, True),
        StructField("category", codeable_concept, True),
        StructField("code", codeable_concept, True),
        StructField("subject", reference, False),
        StructField("encounter", reference, True),
        StructField("performedDateTime", TimestampType(), True),
        StructField("performedPeriod", period, True),
        StructField("performedString", StringType(), True),
        StructField("performedAge", StringType(), True),
        StructField("performedRange", range_type, True),
        StructField("recorder", reference, True),
        StructField("asserter", reference, True),
        StructField("performer",
                    ArrayType(
                        StructType([
                            StructField("function", codeable_concept, True),
                            StructField("actor", reference, False),
                            StructField("onBehalfOf", reference, True)
                        ])
                    ), True),
        StructField("location", reference, True),
        StructField("reasonCode", ArrayType(codeable_concept), True),
        StructField("reasonReference", ArrayType(reference), True),
        StructField("bodySite", ArrayType(codeable_concept), True),
        StructField("outcome", codeable_concept, True),
        StructField("report", ArrayType(reference), True),
        StructField("complication", ArrayType(codeable_concept), True),
        StructField("complicationDetail", ArrayType(reference), True),
        StructField("followUp", ArrayType(codeable_concept), True),
        StructField("note", ArrayType(annotation), True),
        StructField("focalDevice",
                    ArrayType(
                        StructType([
                            StructField("action", codeable_concept, True),
                            StructField("manipulated", reference, False)
                        ])
                    ), True),
        StructField("usedReference", ArrayType(reference), True),
        StructField("usedCode", ArrayType(codeable_concept), True)
    ]
)
