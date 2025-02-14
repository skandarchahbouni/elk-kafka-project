from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Initialize or get an existing SparkSession
spark = (
    SparkSession.builder.appName("Read from Elasticsearch")
    .config("spark.es.nodes", "es01")
    .config("spark.es.port", "9200")
    .master("local[*]")
    .getOrCreate()
)

# Load the data from Elasticsearch
shakespeareDF = spark.read.format("org.elasticsearch.spark.sql").load(
    "users-activities"
)

# Show the first 10 rows (original unprocessed data)
shakespeareDF.show(10)

# Show the schema of the dataframe to see the structure of the data
shakespeareDF.printSchema()

# Processing Example 1: Filter out only "Login" activities and group them by location to count logins per location
login_activities = (
    shakespeareDF.filter(col("activity_type") == "Login")
    .groupBy("location")
    .agg(count("activity_id").alias("login_count"))
)

# Show the result of the login activity processing
login_activities.show(10)

# Save the login activities result to a CSV file
login_activities.write.option("header", "true").csv("output/login_activities.csv")

# Processing Example 2: Select specific columns (user_id, username, location, timestamp) and show the first 10 rows
selected_columns = shakespeareDF.select("user_id", "username", "location", "timestamp")
selected_columns.show(10)

# Save the selected columns result to a CSV file
selected_columns.write.option("header", "true").csv("output/selected_columns.csv")

# Processing Example 3: Count the number of activities per user_id
user_activity_count = shakespeareDF.groupBy("user_id").agg(
    count("activity_id").alias("activity_count")
)
user_activity_count.show(10)

# Save the user activity count result to a CSV file
user_activity_count.write.option("header", "true").csv("output/user_activity_count.csv")
