#!/usr/bin/env sh
set -eu
/opt/kafka/bin/kafka-topics.sh --bootstrap-server "${KAFKA_BROKER:-kafka:9092}" --create --if-not-exists --topic "${KAFKA_TOPIC:-earthquake.events.v1}" --partitions 3 --replication-factor 1
/opt/kafka/bin/kafka-topics.sh --bootstrap-server "${KAFKA_BROKER:-kafka:9092}" --create --if-not-exists --topic "${KAFKA_DLQ_TOPIC:-earthquake.dlq.v1}" --partitions 3 --replication-factor 1