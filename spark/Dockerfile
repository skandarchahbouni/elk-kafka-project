FROM openjdk:11

# Install wget and download Apache Spark
RUN apt-get update && apt-get install -y wget && \
    wget https://dlcdn.apache.org/spark/spark-3.5.4/spark-3.5.4-bin-hadoop3.tgz

# Extract the downloaded tar file
RUN tar -xvf spark-3.5.4-bin-hadoop3.tgz

# Keep the container running
CMD ["tail", "-f", "/dev/null"]
