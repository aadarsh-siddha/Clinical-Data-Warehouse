from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType, BooleanType, FloatType, DoubleType, NullType, ShortType, DateType, TimestampType

coding = StructType(
    [
        StructField("system", StringType(), True),
        StructField("version", StringType(), True),
        StructField("code", StringType(), True),
        StructField("display", StringType(), True),
        StructField("userSelected", BooleanType(), True)
    ]
)

#---------------------------------------------------------------#
#                  Resource Type Inherited
#---------------------------------------------------------------#

id_type = StringType()


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

#---------------------------------------------------------------#
#               DomainResource Type Inherited
#---------------------------------------------------------------#

text_type = StructType(
    [
        StructField("status", StringType(), False),
        StructField("div", StringType(), False)
    ]
)

contained_type = StructType(
    [
        StructField("id", StringType(), True),
        StructField("meta", meta_type, True),
        StructField("implicitRules", StringType(), True),
        StructField("language", StringType(), True)
    ]
)



extension_type = ArrayType(StructType(
    [
        StructField("url", StringType(), True),
        StructField("value", StringType(), True)
    ]
))

modifierExtension_type = extension_type


#----------------------------------------------------------------------------------------------------------------------------------#



codeable_concept = StructType(
    [
        StructField("coding", ArrayType(coding), True),
        StructField("text", StringType(), True)
    ]
)

period = StructType(
    [
        StructField("start", StringType(), True),
        StructField("end", StringType(), True)
    ]
)

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

reference = StructType(
    [
        StructField("reference", StringType(), True),
        StructField("type", StringType(), True),
        StructField("identifier", identifier, True),
        StructField("display", StringType(), True)
    ]
)

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

contact_point = StructType(
    [
        StructField("system", StringType(), True),
        StructField("value", StringType(), True),
        StructField("use", StringType(), True),
        StructField("rank", IntegerType(), True),
        StructField("period", period, True)
    ]
)

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

range_type = StructType(
    [
        StructField("low", StringType(), True),
        StructField("high", StringType(), True)
    ]
)

annotation = StructType(
    [
        StructField("authorReference", reference, True),
        StructField("authorString", StringType(), True),
        StructField("time", TimestampType(), True),
        StructField("text", StringType(), True)
    ]
)
extension_element = StructType(
    [
        StructField("url", StringType(), True),
        StructField("value", StringType(), True)
    ]
)

element = StructType(
    [
        StructField("id", StringType(), True),
        StructField("extension", ArrayType(extension_element), True)
    ]
)
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

quantity = StructType(
    [
        StructField("value", FloatType(), True),
        StructField("comparator", StringType(), True),
        StructField("unit", StringType(), True),
        StructField("system", StringType(), True),
        StructField("code", StringType(), True)
    ]
)

money = StructType(
    [
        StructField("value", FloatType(), True),
        StructField("currency", StringType(), True)
    ]
)

 
ratio = StructType(
    [
        StructField("numerator", quantity, True),
        StructField("denominator", quantity, True)
    ]
)

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
        