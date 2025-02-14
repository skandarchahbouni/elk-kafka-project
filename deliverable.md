# Project Deliverable

## Part 1: Data Collection  
- We have created a mock API, **[mock_api](./mock_api/)**, which loads data from a **[data.json](./mock_api/data.json)** file and serves it via the `/data` endpoint, returning the JSON content as a response.  
- The API simulates user activity logs, including logins, logouts, and password changes. Each entry contains details such as user ID, username, activity type, device, browser, location, IP address, timestamp, and a brief description. It provides insights into user authentication and session activities across different devices and locations.  
- The generated data includes a timestamp field, text fields, and a numeric field, which fulfill the requirements for the subsequent questions in this project.  


## Part 2: Kafka  
- The **[producer](./producer/)** fetches user activity data from a mock API and sends it to a Kafka topic (`users_activities`). It uses the Confluent Kafka producer to publish each activity as a JSON message, logging delivery reports. The script runs in a loop, sending one message per second while handling errors and ensuring all messages are flushed before exiting.
- The consumer in our case is Logstash, as you can see in the [Logstash configuration file](./logstash.conf), we are using the Kafka input.
```bash
input {
  kafka {
    bootstrap_servers => "kafka:9093"  # Kafka broker address
    topics => ["users_activities"]     # Kafka topic(s) to read from
    group_id => "my_group"            # Kafka consumer group id
    codec => "json"                        # Optional codec (e.g., json, plain)
    auto_offset_reset => "earliest"         # Read from the earliest message if no offset is found
    consumer_threads => 1                  # Number of consumer threads
  }
}
```

## Part 3: Logstash & Elasticsearch  
- Logstash configuration file: **[logstach.conf](./logstash.conf)**
- Elasticsearch mapping: **[index-mapping.json](./index-mapping.json)** || **[screenshot](./screenshots/indexed_data/mapping.png)**
- Screenshots of indexed data:  **[index-mapping.json](./screenshots/indexed_data/)**
- Five queries: **[example-elasticsearch-queries.md](./example-elasticsearch-queries.md)**

## Part 4: Kibana  
- Screenshots of visualizations and results from advanced Elasticsearch queries: **[logstach.conf](./screenshots/kibana%20dashboard/)**

## Part 5: Hadoop or Spark (Choice-Based)   
- Processing script/configuration: **[spark](./spark/)**
- Calculation results in JSON or CSV format:  **[script output](./spark/example-output/)**
- Screenshot: **[spark screenshots](./screenshots/spark/)**
- Technical explanation of the choices made: 
  1. **Integration with Docker:**
    - **Docker-based Setup:** Since our project is built around Docker, Spark was a more natural choice for integration. Spark has strong support for containerized environments, and it can be easily deployed using Docker images, making the deployment and orchestration process smoother. While Hadoop can run in Docker containers as well, Spark’s lighter architecture and simpler configuration allow for easier management within a Dockerized setup.
    - **Ease of Setup:** Setting up Spark in Docker is relatively straightforward, thanks to its official Docker images. In comparison, deploying Hadoop in Docker can be more complex, as it requires additional configurations for components like HDFS (Hadoop Distributed File System), ResourceManager, NameNode, and more.

  2. **Processing Speed (Performance):**
    - **Faster Data Processing:** Spark outperforms Hadoop in terms of speed, especially for tasks involving iterative algorithms. Spark performs data processing primarily in-memory, reducing the need for disk I/O. This is particularly beneficial when working with large datasets. In contrast, Hadoop’s MapReduce framework requires intermediate data to be written to disk, which can significantly slow down performance, especially during iterative operations.
    - **Advanced Optimizations:** Spark provides advanced optimizations such as DAG (Directed Acyclic Graph) execution for more efficient task scheduling, fault tolerance, and better resource utilization. These optimizations help in speeding up the data processing pipeline, making Spark a preferred choice for many modern big data applications.

  3. **Ease of Use:**
    - **Developer-Friendly APIs:** Spark is easier to use and offers a variety of programming interfaces, including Python, Scala, and SQL. This makes it accessible to a broader range of developers, particularly those familiar with Python and SQL. Hadoop, on the other hand, has a steeper learning curve, particularly for developers who need to write complex Java code for MapReduce tasks.


## Documentation & Organization  
- All the code is Dockerized, so you just need to run `docker-compose up --build` to have the code running on your machine, without any overhead installation guidelines.
- Clear project presentation, including file structure and comments: **[README.md](./README.md)**

