"""
imaging_study_schema.py
========================
PySpark schema for the FHIR R4 ImagingStudy resource.
FHIR R4 spec: https://hl7.org/fhir/R4/imagingstudy.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType, StringType, TimestampType, IntegerType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, annotation, coding
)

# ImagingStudy -- representation of the content produced in a DICOM imaging study
imaging_study_schema = StructType(
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
        StructField("modality", ArrayType(coding), True),
        StructField("subject", reference, False),
        StructField("encounter", reference, True),
        StructField("started", TimestampType(), True),
        StructField("basedOn", ArrayType(reference), True),
        StructField("referrer", reference, True),
        StructField("interpreter", ArrayType(reference), True),
        StructField("endpoint", ArrayType(reference), True),
        StructField("numberOfSeries", IntegerType(), True),
        StructField("numberOfInstances", IntegerType(), True),
        StructField("procedureReference", reference, True),
        StructField("procedureCode", ArrayType(codeable_concept), True),
        StructField("location", reference, True),
        StructField("reasonCode", ArrayType(codeable_concept), True),
        StructField("reasonReference", ArrayType(reference), True),
        StructField("note", ArrayType(annotation), True),
        StructField("description", StringType(), True),
        StructField("series",
                    ArrayType(
                        StructType([
                            StructField("uid", StringType(), False),
                            StructField("number", IntegerType(), True),
                            StructField("modality", coding, False),
                            StructField("description", StringType(), True),
                            StructField("numberOfInstances", IntegerType(), True),
                            StructField("endpoint", ArrayType(reference), True),
                            StructField("bodySite", coding, True),
                            StructField("laterality", coding, True),
                            StructField("specimen", ArrayType(reference), True),
                            StructField("started", TimestampType(), True),
                            StructField("performer",
                                        ArrayType(
                                            StructType([
                                                StructField("function", codeable_concept, True),
                                                StructField("actor", reference, False)
                                            ])
                                        ), True),
                            StructField("instance",
                                        ArrayType(
                                            StructType([
                                                StructField("uid", StringType(), False),
                                                StructField("sopClass", coding, False),
                                                StructField("number", IntegerType(), True),
                                                StructField("title", StringType(), True)
                                            ])
                                        ), True)
                        ])
                    ), True)
    ]
)
