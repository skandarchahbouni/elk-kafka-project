from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
if spark.version:
    spark.stop()

spark = (
    SparkSession.builder.appName("Read from Elasticsearch")
    .config("spark.es.nodes", "es01")
    .config("spark.es.port", "9200")
    .master("local[*]")
    .getOrCreate()
)

shakespeareDF = spark.read.format("org.elasticsearch.spark.sql").load("fakefriends")

shakespeareDF.show(10)

shakespeareDF.printSchema()
