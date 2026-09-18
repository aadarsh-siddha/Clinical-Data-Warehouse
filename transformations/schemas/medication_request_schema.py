"""
medication_request_schema.py
==============================
PySpark schema for the FHIR R4 MedicationRequest resource.
FHIR R4 spec: https://hl7.org/fhir/R4/medicationrequest.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType,
    StringType, TimestampType, BooleanType, IntegerType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, period,
    annotation, dosage, quantity
)

# MedicationRequest -- an order or request for supply of medication and administration to a patient
medication_request_schema = StructType(
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
        StructField("status", StringType(), False),
        StructField("statusReason", codeable_concept, True),
        StructField("intent", StringType(), False),
        StructField("category", ArrayType(codeable_concept), True),
        StructField("priority", StringType(), True),
        StructField("doNotPerform", BooleanType(), True),
        StructField("reportedBoolean", BooleanType(), True),
        StructField("reportedReference", reference, True),
        StructField("medicationCodeableConcept", codeable_concept, True),
        StructField("medicationReference", reference, True),
        StructField("subject", reference, False),
        StructField("encounter", reference, True),
        StructField("supportingInformation", ArrayType(reference), True),
        StructField("authoredOn", TimestampType(), True),
        StructField("requester", reference, True),
        StructField("performer", reference, True),
        StructField("performerType", codeable_concept, True),
        StructField("recorder", reference, True),
        StructField("reasonCode", ArrayType(codeable_concept), True),
        StructField("reasonReference", ArrayType(reference), True),
        StructField("instantiatesCanonical", ArrayType(StringType()), True),
        StructField("instantiatesUri", ArrayType(StringType()), True),
        StructField("basedOn", ArrayType(reference), True),
        StructField("groupIdentifier", identifier, True),
        StructField("courseOfTherapyType", codeable_concept, True),
        StructField("insurance", ArrayType(reference), True),
        StructField("note", ArrayType(annotation), True),
        StructField("dosageInstruction", ArrayType(dosage), True),
        StructField("dispenseRequest",
                    StructType([
                        StructField("initialFill",
                                    StructType([
                                        StructField("quantity", quantity, True),
                                        StructField("duration", StringType(), True)
                                    ]), True),
                        StructField("dispenseInterval", StringType(), True),
                        StructField("validityPeriod", period, True),
                        StructField("numberOfRepeatsAllowed", IntegerType(), True),
                        StructField("quantity", StringType(), True),
                        StructField("expectedSupplyDuration", StringType(), True),
                        StructField("performer", reference, True)
                    ]), True),
        StructField("substitution",
                    StructType([
                        StructField("allowedBoolean", BooleanType(), True),
                        StructField("allowedCodeableConcept", codeable_concept, True),
                        StructField("reason", codeable_concept, True)
                    ]), True),
        StructField("priorPrescription", reference, True),
        StructField("detectedIssue", ArrayType(reference), True),
        StructField("eventHistory", ArrayType(reference), True)
    ]
)
