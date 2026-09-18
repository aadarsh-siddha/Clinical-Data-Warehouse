"""
base_types.py
=============
Shared PySpark StructType definitions for FHIR R4 data types.

This module provides reusable schema building blocks used across all
FHIR resource notebooks in this project. Types are grouped by their
FHIR specification layer:

  1. Primitive / foundational  -- coding
  2. Resource-level inherited  -- id_type, meta_type, implicitRules_type, language_type
  3. DomainResource inherited  -- text_type, contained_type, extension_type, modifierExtension_type
  4. General-purpose datatypes -- codeable_concept, period, identifier, reference,
                                  human_name, contact_point, address, attachment,
                                  range_type, annotation, element, timing, quantity,
                                  money, ratio, dosage, sampled_data, signature

Usage:
    from schemas.base_types import identifier, reference, codeable_concept, ...

FHIR R4 spec: https://hl7.org/fhir/R4/datatypes.html
"""

from pyspark.sql.types import (
    StructType, StructField,
    StringType, IntegerType, ArrayType,
    BooleanType, FloatType, DoubleType,
    NullType, ShortType, DateType, TimestampType
)


# ===========================================================================
# FOUNDATIONAL PRIMITIVE
# ===========================================================================

# coding -- a reference to a code defined by a terminology system
# FHIR: https://hl7.org/fhir/R4/datatypes.html#Coding
coding = StructType(
    [
        StructField("system", StringType(), True),
        StructField("version", StringType(), True),
        StructField("code", StringType(), True),
        StructField("display", StringType(), True),
        StructField("userSelected", BooleanType(), True)
    ]
)


# ===========================================================================
# RESOURCE TYPE -- fields inherited by every FHIR Resource
# FHIR: https://hl7.org/fhir/R4/resource.html
# ===========================================================================

id_type = StringType()

# meta -- version, timestamps, profiles, security labels, tags
# FHIR: https://hl7.org/fhir/R4/resource.html#Meta
meta_type = StructType([
    StructField("versionId", StringType(), True),
    StructField("lastUpdated", StringType(), True),
    StructField("source", StringType(), True),
    StructField("profile", ArrayType(StringType()), True),
    StructField("security", ArrayType(coding), True),
    StructField("tag", ArrayType(coding), True),
])

implicitRules_type = StringType()

language_type = StringType()


# ===========================================================================
# DOMAINRESOURCE TYPE -- additional fields inherited by most FHIR resources
# FHIR: https://hl7.org/fhir/R4/domainresource.html
# ===========================================================================

# Human-readable narrative summary
# FHIR: https://hl7.org/fhir/R4/narrative.html
text_type = StructType(
    [
        StructField("status", StringType(), False),
        StructField("div", StringType(), False)
    ]
)

# Inline anonymous resource contained within a parent resource
# FHIR: https://hl7.org/fhir/R4/domainresource.html#contained
contained_type = StructType(
    [
        StructField("id", StringType(), True),
        StructField("meta", meta_type, True),
        StructField("implicitRules", StringType(), True),
        StructField("language", StringType(), True)
    ]
)

# FHIR: https://hl7.org/fhir/R4/extensibility.html
extension_type = ArrayType(StructType(
    [
        StructField("url", StringType(), True),
        StructField("value", StringType(), True)
    ]
))

modifierExtension_type = extension_type


# ===========================================================================
# GENERAL-PURPOSE FHIR DATATYPES
# FHIR: https://hl7.org/fhir/R4/datatypes.html
# ===========================================================================

# CodeableConcept -- coded concept with optional free text
# FHIR: https://hl7.org/fhir/R4/datatypes.html#CodeableConcept
codeable_concept = StructType(
    [
        StructField("coding", ArrayType(coding), True),
        StructField("text", StringType(), True)
    ]
)

# Period -- start/end date-time range
# FHIR: https://hl7.org/fhir/R4/datatypes.html#Period
period = StructType(
    [
        StructField("start", StringType(), True),
        StructField("end", StringType(), True)
    ]
)

# Identifier -- a unique identifier within a system
# FHIR: https://hl7.org/fhir/R4/datatypes.html#Identifier
identifier = StructType(
    [
        StructField("use", StringType(), True),
        StructField("type", codeable_concept, True),
        StructField("system", StringType(), True),
        StructField("value", StringType(), True),
        StructField("period", period, True),
        StructField("assigner", StringType(), True)
    ]
)

# Reference -- a reference from one resource to another
# FHIR: https://hl7.org/fhir/R4/references.html
reference = StructType(
    [
        StructField("reference", StringType(), True),
        StructField("type", StringType(), True),
        StructField("identifier", identifier, True),
        StructField("display", StringType(), True)
    ]
)

# HumanName -- name with text, parts, and usage
# FHIR: https://hl7.org/fhir/R4/datatypes.html#HumanName
human_name = StructType(
    [
        StructField("use", StringType(), True),
        StructField("text", StringType(), True),
        StructField("family", StringType(), True),
        StructField("given", StringType(), True),
        StructField("prefix", StringType(), True),
        StructField("suffix", StringType(), True),
        StructField("period", period, True)
    ]
)

# ContactPoint -- phone, fax, email, etc.
# FHIR: https://hl7.org/fhir/R4/datatypes.html#ContactPoint
contact_point = StructType(
    [
        StructField("system", StringType(), True),
        StructField("value", StringType(), True),
        StructField("use", StringType(), True),
        StructField("rank", IntegerType(), True),
        StructField("period", period, True)
    ]
)

# Address -- postal address
# FHIR: https://hl7.org/fhir/R4/datatypes.html#Address
address = StructType(
    [
        StructField("use", StringType(), True),
        StructField("type", StringType(), True),
        StructField("text", StringType(), True),
        StructField("line", StringType(), True),
        StructField("city", StringType(), True),
        StructField("district", StringType(), True),
        StructField("state", StringType(), True),
        StructField("postalCode", StringType(), True),
        StructField("country", StringType(), True),
        StructField("period", period, True)
    ]
)

# Attachment -- binary content (image, document, etc.)
# FHIR: https://hl7.org/fhir/R4/datatypes.html#Attachment
attachment = StructType(
    [
        StructField("contentType", StringType(), True),
        StructField("language", StringType(), True),
        StructField("data", StringType(), True),
        StructField("url", StringType(), True),
        StructField("size", IntegerType(), True),
        StructField("hash", StringType(), True),
        StructField("title", StringType(), True),
        StructField("creation", TimestampType(), True)
    ]
)

# Range -- low/high quantity limits
# FHIR: https://hl7.org/fhir/R4/datatypes.html#Range
range_type = StructType(
    [
        StructField("low", StringType(), True),
        StructField("high", StringType(), True)
    ]
)

# Annotation -- text note with author and timestamp
# FHIR: https://hl7.org/fhir/R4/datatypes.html#Annotation
annotation = StructType(
    [
        StructField("authorReference", reference, True),
        StructField("authorString", StringType(), True),
        StructField("time", TimestampType(), True),
        StructField("text", StringType(), True)
    ]
)

# extension_element -- key/value pair used inside element
extension_element = StructType(
    [
        StructField("url", StringType(), True),
        StructField("value", StringType(), True)
    ]
)

# Element -- base definition for all elements in a resource
# FHIR: https://hl7.org/fhir/R4/types.html#Element
element = StructType(
    [
        StructField("id", StringType(), True),
        StructField("extension", ArrayType(extension_element), True)
    ]
)

# Timing -- an event that may occur multiple times
# FHIR: https://hl7.org/fhir/R4/datatypes.html#Timing
timing = StructType(
    [
        StructField("event", ArrayType(TimestampType()), True),
        StructField("repeat",
                    StructType(
                        [
                            StructField("boundsDuration", StringType(), True),
                            StructField("boundsPeriod", StringType(), True),
                            StructField("boundsRange", StringType(), True),
                            StructField("count", IntegerType(), True),
                            StructField("countMax", IntegerType(), True),
                            StructField("duration", FloatType(), True),
                            StructField("durationMax", FloatType(), True),
                            StructField("durationUnit", StringType(), True),
                            StructField("frequency", IntegerType(), True),
                            StructField("frequencyMax", IntegerType(), True),
                            StructField("period", FloatType(), True),
                            StructField("periodMax", FloatType(), True),
                            StructField("dayOfWeek", ArrayType(StringType()), True),
                            StructField("timeOfDay", ArrayType(StringType()), True),
                            StructField("when", ArrayType(StringType()), True),
                            StructField("offset", IntegerType(), True)
                        ]
                    ), True),
        StructField("code", codeable_concept, True)
    ]
)

# Quantity -- a measured amount
# FHIR: https://hl7.org/fhir/R4/datatypes.html#Quantity
quantity = StructType(
    [
        StructField("value", FloatType(), True),
        StructField("comparator", StringType(), True),
        StructField("unit", StringType(), True),
        StructField("system", StringType(), True),
        StructField("code", StringType(), True)
    ]
)

# Money -- monetary value with currency
# FHIR: https://hl7.org/fhir/R4/datatypes.html#Money
money = StructType(
    [
        StructField("value", FloatType(), True),
        StructField("currency", StringType(), True)
    ]
)

# Ratio -- numerator/denominator relationship between quantities
# FHIR: https://hl7.org/fhir/R4/datatypes.html#Ratio
ratio = StructType(
    [
        StructField("numerator", quantity, True),
        StructField("denominator", quantity, True)
    ]
)

# Dosage -- how a medication is/was taken
# FHIR: https://hl7.org/fhir/R4/dosage.html
dosage = StructType(
    [
        StructField("sequence", IntegerType(), True),
        StructField("text", StringType(), True),
        StructField("additionalInstruction", ArrayType(codeable_concept), True),
        StructField("patientInstruction", StringType(), True),
        StructField("timing", timing, True),
        StructField("asNeededBoolean", BooleanType(), True),
        StructField("asNeededCodeableConcept", codeable_concept, True),
        StructField("site", codeable_concept, True),
        StructField("route", codeable_concept, True),
        StructField("method", codeable_concept, True),
        StructField("doseAndRate",
                    ArrayType(
                        StructType([
                            StructField("type", codeable_concept, True),
                            StructField("doseRange", range_type, True),
                            StructField("doseQuantity", quantity, True),
                            StructField("rateRatio", ratio, True),
                            StructField("rateRange", range_type, True),
                            StructField("rateQuantity", quantity, True)
                        ])
                    ), True),
        StructField("maxDosePerPeriod", ratio, True),
        StructField("maxDosePerAdministration", StringType(), True),
        StructField("maxDosePerLifetime", StringType(), True)
    ]
)

# SampledData -- a series of measurements taken by a device
# FHIR: https://hl7.org/fhir/R4/datatypes.html#SampledData
sampled_data = StructType(
    [
        StructField("origin", StringType(), False),
        StructField("period", FloatType(), False),
        StructField("factor", FloatType(), True),
        StructField("lowerLimit", FloatType(), True),
        StructField("upperLimit", FloatType(), True),
        StructField("dimensions", IntegerType(), False),
        StructField("data", StringType(), True)
    ]
)

# Signature -- digital signature with context
# FHIR: https://hl7.org/fhir/R4/datatypes.html#Signature
signature = StructType(
    [
        StructField("type", ArrayType(coding), False),
        StructField("when", StringType(), False),
        StructField("who", reference, False),
        StructField("onBehalfOf", reference, True),
        StructField("targetFormat", StringType(), True),
        StructField("sigFormat", StringType(), True),
        StructField("data", StringType(), True)
    ]
)
