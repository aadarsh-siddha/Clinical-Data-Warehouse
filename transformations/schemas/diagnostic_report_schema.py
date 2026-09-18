"""
diagnostic_report_schema.py
============================
PySpark schema for the FHIR R4 DiagnosticReport resource.
FHIR R4 spec: https://hl7.org/fhir/R4/diagnosticreport.html
"""

from pyspark.sql.types import (
    StructType, StructField, ArrayType, StringType, TimestampType
)

from base_types import (
    id_type, meta_type, implicitRules_type, language_type,
    text_type, contained_type, extension_type, modifierExtension_type,
    identifier, codeable_concept, reference, period, attachment
)

# DiagnosticReport -- findings and interpretation of diagnostic tests performed on patients
diagnostic_report_schema = StructType(
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
        StructField("status", StringType(), False),
        StructField("category", ArrayType(codeable_concept), True),
        StructField("code", codeable_concept, False),
        StructField("subject", reference, True),
        StructField("encounter", reference, True),
        StructField("effectiveDateTime", TimestampType(), True),
        StructField("effectivePeriod", period, True),
        StructField("issued", TimestampType(), True),
        StructField("performer", ArrayType(reference), True),
        StructField("resultsInterpreter", ArrayType(reference), True),
        StructField("specimen", ArrayType(reference), True),
        StructField("result", ArrayType(reference), True),
        StructField("imagingStudy", ArrayType(reference), True),
        StructField("media",
                    ArrayType(
                        StructType([
                            StructField("comment", StringType(), True),
                            StructField("link", reference, False)
                        ])
                    ), True),
        StructField("conclusion", StringType(), True),
        StructField("conclusionCode", ArrayType(codeable_concept), True),
        StructField("presentedForm", ArrayType(attachment), True)
    ]
)
