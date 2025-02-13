import time
from confluent_kafka import Producer
import logging
import sys
import json
import requests

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


# Define a callback for delivery reports (optional)
def delivery_report(err, msg):
    if err is not None:
        logging.info(f"Message delivery failed: {err}")
    else:
        logging.info(
            f"Message delivered to {msg.topic} [{msg.partition}] with offset {msg.offset()}."
        )


# Configuration for the Kafka producer
conf = {
    "bootstrap.servers": "kafka:9093",  # Kafka server address
}

# Create the Producer instance
producer = Producer(conf)

# Public API URL
api_url = "http://mock_api:8000/data"

try:
    # Fetch data from the API
    response = requests.get(api_url)
    if response.status_code != 200:
        logging.error(
            f"Failed to fetch data from API. Status code: {response.status_code}"
        )
        sys.exit(1)

    # Parse the JSON response
    posts = response.json()
    logging.info(f"Fetched {len(posts)} posts from the API.")

    # Iterate over the posts and produce to Kafka
    for post in posts:
        # Convert post to a JSON string
        message = json.dumps(post)

        # Produce a message to the Kafka topic
        producer.produce(
            "users_activities",
            key=str(post["activity_id"]),
            value=message,
            callback=delivery_report,
        )

        # Wait for the delivery report to be sent
        producer.flush()

        logging.info(f"Sent post with ID {post['activity_id']} to Kafka.")

        # Sleep for 1 second
        time.sleep(1)

except KeyboardInterrupt:
    logging.error("Producer interrupted, exiting...")
finally:
    # Ensure all messages are flushed before exiting
    producer.flush()
