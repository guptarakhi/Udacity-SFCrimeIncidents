# Udacity-SFCrimeIncidents
#Use of Kafka and Spark on San Francisco Crime Statistics

Step 1:
Screenshot provided in the zip file

Step 2:
Screenshots provided in the zip file

Step 3:

Q: How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

A: Sparksession property parameters will influence the scheduling and processing times for a spark job. As a user we look for drive down the processing times which means low latency and high throughput.


Q: What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

A: To find the most optimal values, we can test multiple variations and see which provides the best processing times. Below are some of the parameters which can influence the processing times:
    * spark.default.parallelism: total number of cores on all executor nodes.
    * spark.streaming.kafka.maxRatePerPartition: maximum rate at which data will be read from each Kafka partition.
    * spark.streaming.kafka.maxOffsetsPerTrigger: limit the number of records to fetch per trigger.
