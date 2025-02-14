# ELK + Kafka + Mock API Project 🚀

This project sets up a Docker environment with the following components:

- **Kafka**: Message broker for data streaming 🐱‍🏍.
- **Elasticsearch (ES)**: Search and analytics engine 🔍.
- **Kibana**: Visualization tool for Elasticsearch data 📊.
- **Logstash**: Log processing pipeline 🔄.
- **Mock API**: A simulated API to serve data to Kafka producers 🤖.
- **Producer**: A service that consumes data from the Mock API and sends it to Kafka 🎬.
- **Spark**: A processing engine for real-time analytics ⚡ (integrated with Elasticsearch via ES-Hadoop).


## Requirements 📋

- Docker 🐳
- Docker Compose 📦

## Setup ⚙️

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2. Build and start the containers:
    ```bash
    docker-compose up --build
    ```

## Configuration 🔧

- **Kafka** is configured with a KRaft (Kubernetes Raft) mode for managing cluster metadata.
- **Elasticsearch** and **Kibana** are set to work in a single-node mode.
- **Logstash** ingests data from Kafka and sends it to Elasticsearch.
- **Mock API** runs on port 8000, providing mock data for the producer service.
- **Spark** is integrated with **ES-Hadoop** for real-time analytics, if needed.

## Endpoints 🌐

- **Kibana**: `localhost:<KIBANA_PORT>` (default: 5601)
- **Mock API**: `localhost:8000/docs` (Swagger UI)

## Spark ⚡

To run Spark with Elasticsearch integration, you can connect to the Spark container and run the following command:

```bash
./spark-3.5.4-bin-hadoop3/bin/pyspark --packages org.elasticsearch:elasticsearch-spark-30_2.12:8.17.1
```

or 

```bash
./spark-3.5.4-bin-hadoop3/bin/spark-submit \
  --packages org.elasticsearch:elasticsearch-spark-30_2.12:8.17.1 \
  your_script.py
```
