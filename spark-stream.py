from pyspark.sql import SparkSession
#from pyspark.sql.functions import explode
#from pyspark.sql.functions import split

val spark = SparkSession
      .builder
      .master("local[*]")
      .config("spark.redis.host", "localhost")
      .config("spark.redis.port", "6379")
      .getOrCreate()

val sensors = spark
      .readStream
      .format("redis")                          # read from Redis
      .option("stream.keys", "myKey")         #stream key
      #.schema(StructType(Array(                 # stream fields 
       # StructField("sensor-id", StringType),
       # StructField("temperature", FloatType)
      #)))
      #.load()

val query = sensors
  .writeStream
  .format("console")
  .start()

query.awaitTermination()
