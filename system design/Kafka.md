# Interview Prep Quick bytes

## Broker

A broker is a server which runs in a kafka cluster, managing message storage and transmission.

Key Responsibilities:
- Message storage and replication
- Topic and partition management
- Client request handling
- Leader election participation
- Consumer group coordination

Broker can handle thousands of topics and partition. It is generally limited by available disk space, network bandwidth, memory, CPU resources.

## Partition

Partitions are the foundation of kafka's scalability.

Key Concepts:
- Each topic is divided into one or more partitions
- Partitions are ordered, immutable logs
- Messages in partition get sequential id, or offset
- Partitions are distributed across brokers - enabling horizontal scalability

## Message Delivery

Kafka ensures message delivery through multiple mechanisms

Producer acks

```
acks = 0 -> fire and forget
acks = 1 -> leader ack (partial guarantee)
acks = all -> all replicas ack (strongest guarantee)
```

Consumer Guarantees

```
at-most once
Think of it like reading a book and moving your bookmark forward before you've finished reading the page – if you get interrupted, you might miss some content

at-least once
Think of this like a postal service with delivery confirmation. If the postal service isn't sure whether a package was delivered, they'll try delivering it again. This means you might get the same package twice, but you'll never miss a package

exactly-once semantics
This works like a banking transaction - if you deposit money, the bank ensures the amount is credited exactly once, no matter what technical issues might occur
```

## Consumer Groups

Consumer groups enable parallel processing while maintaining order.

Key points
- Multiple consumers share processing load
- Each partition is read by one consumer in a group
- Automatic rebalancing on consumer changes
- Offset tracking per group
- Multiple groups can read the same topic

## Fault Tolerance

Kafka has a robust failure handling mechanism

Detection:
- ZooKeeper tracks broker heartbeats
- Controller broker monitors health
- Configurable failure detection timeouts

Recovery Process:
- Controller detects failure
- New leader election for affected partitions
- Metadata update across cluster
- Client connection re-establishment
- Consumer group rebalancing


Refer to [[Kafka Architecture Diagram]] for the complete architecture diagram
