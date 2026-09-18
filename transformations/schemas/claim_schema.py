"""
claim_schema.py
===============
PySpark schema for the FHIR R4 Claim resource.
FHIR R4 spec: https://hl7.org/fhir/R4/claim.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType,
    StringType, IntegerType, TimestampType, BooleanType,
    FloatType, DateType, DataType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, period,
    quantity, money, address, attachment
)

# Claim -- a provider-side request for adjudication of healthcare-related charges
claim_schema = StructType(
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
        StructField("type", codeable_concept, False),
        StructField("subType", codeable_concept, True),
        StructField("use", StringType(), False),
        StructField("patient", reference, False),
        StructField("billablePeriod", period, True),
        StructField("created", TimestampType(), False),
        StructField("enterer", reference, True),
        StructField("insurer", reference, True),
        StructField("provider", reference, False),
        StructField("priority", codeable_concept, False),
        StructField("fundsReserve", codeable_concept, True),
        StructField("related",
                    ArrayType(
                        StructType([
                            StructField("claim", reference, True),
                            StructField("relationship", codeable_concept, True),
                            StructField("reference", StringType(), True)
                        ])
                    ), True),
        StructField("prescription", reference, True),
        StructField("originalPrescription", reference, True),
        StructField("payee",
                    StructType([
                        StructField("type", codeable_concept, True),
                        StructField("party", reference, True)
                    ]), True),
        StructField("referral", reference, True),
        StructField("facility", reference, True),
        StructField("careTeam",
                    ArrayType(
                        StructType([
                            StructField("sequence", IntegerType(), False),
                            StructField("provider", reference, False),
                            StructField("responsible", BooleanType(), True),
                            StructField("role", codeable_concept, True),
                            StructField("qualification", codeable_concept, True)
                        ])
                    ), True),
        StructField("supportingInfo",
                    ArrayType(
                        StructType([
                            StructField("sequence", IntegerType(), False),
                            StructField("category", codeable_concept, False),
                            StructField("code", codeable_concept, True),
                            StructField("timingDate", DateType(), True),
                            StructField("timingPeriod", period, True),
                            StructField("valueBoolean", BooleanType(), True),
                            StructField("valueString", StringType(), True),
                            StructField("valueQuantity", quantity, True),
                            StructField("valueAttachment", attachment, True),
                            StructField("valueReference", reference, True),
                            StructField("reason", codeable_concept, True)
                        ])
                    ), True),
        StructField("diagnosis",
                    ArrayType(
                        StructType([
                            StructField("sequence", IntegerType(), False),
                            StructField("diagnosisCodeableConcept", codeable_concept, True),
                            StructField("diagnosisReference", reference, True),
                            StructField("type", ArrayType(codeable_concept), True),
                            StructField("onAdmission", codeable_concept, True),
                            StructField("packageCode", codeable_concept, True)
                        ])
                    ), True),
        StructField("procedure",
                    ArrayType(
                        StructType([
                            StructField("sequence", IntegerType(), False),
                            StructField("type", ArrayType(codeable_concept), True),
                            StructField("date", TimestampType(), True),
                            StructField("procedureCodeableConcept", codeable_concept, True),
                            StructField("procedureReference", reference, True),
                            StructField("udi", ArrayType(reference), True)
                        ])
                    ), True),
        StructField("insurance",
                    ArrayType(
                        StructType([
                            StructField("sequence", IntegerType(), False),
                            StructField("focal", BooleanType(), False),
                            StructField("identifier", identifier, True),
                            StructField("coverage", reference, False),
                            StructField("businessAgreement", StringType(), True),
                            StructField("preAuthRef", ArrayType(StringType()), True),
                            StructField("claimResponse", reference, True)
                        ])
                    ), False),
        StructField("accident",
                        StructType([
                            StructField("date", DateType(), False),
                            StructField("type", codeable_concept, True),
                            StructField("locationAddress", address, True),
                            StructField("locationReference", reference, True)
                        ]), True),
        StructField("item",
                    ArrayType(
                        StructType([
                            StructField("sequence", IntegerType(), False),
                            StructField("careTeamSequence", ArrayType(IntegerType()), True),
                            StructField("diagnosisSequence", ArrayType(IntegerType()), True),
                            StructField("procedureSequence", ArrayType(IntegerType()), True),
                            StructField("informationSequence", ArrayType(IntegerType()), True),
                            StructField("revenue", codeable_concept, True),
                            StructField("category", codeable_concept, True),
                            StructField("productOrService", codeable_concept, False),
                            StructField("modifier", ArrayType(codeable_concept), True),
                            StructField("programCode", ArrayType(codeable_concept), True),
                            StructField("servicedDate", DateType(), True),
                            StructField("servicedPeriod", period, True),
                            StructField("locationCodeableConcept", codeable_concept, True),
                            StructField("locationAddress", address, True),
                            StructField("locationReference", reference, True),
                            StructField("quantity", StringType(), True),
                            StructField("unitPrice", money, True),
                            StructField("factor", FloatType(), True),
                            StructField("net", money, True),
                            StructField("udi", ArrayType(reference), True),
                            StructField("bodySite", codeable_concept, True),
                            StructField("subSite", ArrayType(codeable_concept), True),
                            StructField("encounter", ArrayType(reference), True),
                            StructField("detail",
                                        ArrayType(
                                            StructType([
                                                StructField("sequence", IntegerType(), False),
                                                StructField("revenue", codeable_concept, True),
                                                StructField("category", codeable_concept, True),
                                                StructField("productOrService", codeable_concept, False),
                                                StructField("modifier", ArrayType(codeable_concept), True),
                                                StructField("programCode", ArrayType(codeable_concept), True),
                                                StructField("quantity", StringType(), True),
                                                StructField("unitPrice", money, True),
                                                StructField("factor", FloatType(), True),
                                                StructField("net", money, True),
                                                StructField("udi", ArrayType(reference), True),
                                                StructField("subDetail",
                                                            ArrayType(
                                                                StructType([
                                                                    StructField("sequence", IntegerType(), False),
                                                                    StructField("revenue", codeable_concept, True),
                                                                    StructField("category", codeable_concept, True),
                                                                    StructField("productOrService", codeable_concept, True),
                                                                    StructField("modifier", ArrayType(codeable_concept), True),
                                                                    StructField("programCode", ArrayType(codeable_concept), True),
                                                                    StructField("quantity", StringType(), True),
                                                                    StructField("unitPrice", money, True),
                                                                    StructField("factor", FloatType(), True),
                                                                    StructField("net", money, True),
                                                                    StructField("udi", ArrayType(reference), True)
                                                                ])
                                                            ), True)
                                            ])
                                        ), True)
                        ])
                    ), True)
    ]
)
