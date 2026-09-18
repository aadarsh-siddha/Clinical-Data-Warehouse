from pyspark.sql.types import *
from fhir_types import identifier, human_name, contact_point, address, codeable_concept, attachment, reference, period, timing, annotation, meta_type, id_type, implicitRules_type, language_type, text_type, contained_type, extension_type, modifierExtension_type, range_type

condition_schema = StructType(
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
        StructField("clinicalStatus", codeable_concept, True),
        StructField("verificationStatus", codeable_concept, True),
        StructField("category", ArrayType(codeable_concept), True),
        StructField("severity", codeable_concept, True),
        StructField("code", codeable_concept, True),
        StructField("bodySite", ArrayType(codeable_concept), True),
        StructField("subject", reference, False),
        StructField("encounter", reference, True),
        StructField("onsetDateTime", TimestampType(), True),
        StructField("onsetAge", StringType(), True),
        StructField("onsetPeriod", period, True),
        StructField("onsetRange", range_type, True),
        StructField("onsetString", StringType(), True),
        StructField("abatementDateTime", TimestampType(), True),
        StructField("abatementAge", StringType(), True),
        StructField("abatementPeriod", period, True),
        StructField("abatementRange", range_type, True),
        StructField("abatementString", StringType(), True),
        StructField("recordedDate", TimestampType(), True),
        StructField("recorder", reference, True),
        StructField("asserter", reference, True),
        StructField("stage", 
                    ArrayType(
                        StructType(
                            [
                                StructField("summary", codeable_concept, True),
                                StructField("assessment", ArrayType(codeable_concept), True),
                                StructField("type", codeable_concept, True)
                            ]
                        )
                    ), True),
        StructField("evidence", 
                    ArrayType(
                        StructType(
                            [
                                StructField("code", ArrayType(codeable_concept), True),
                                StructField("detail", ArrayType(reference), True)
                            ]
                        )
                    ), True),
        StructField("note", ArrayType(annotation), True)
    ]
)