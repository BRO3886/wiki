![[Pasted image 20250108160046.png]]

1. **ZooKeeper Ensemble**
   - Consists of multiple ZooKeeper nodes (typically 3 or 5)
   - Manages broker coordination
   - Stores metadata about partitions and brokers
   - Handles leader election
   - Tracks broker health through heartbeats

2. **Kafka Brokers**
   - Each broker hosts multiple partitions
   - One broker acts as the cluster controller (Broker 1 in our diagram)
   - Partitions are distributed across brokers for load balancing
   - Each partition has one leader and multiple replicas

3. **Topics and Partitions**
   - Each topic (Topic1, Topic2) is split into multiple partitions
   - Partitions are the unit of parallelism
   - Each partition is an ordered, immutable log
   - Replicas are distributed across different brokers for fault tolerance

4. **Producers**
   - Send messages to specific topics
   - Can choose partition assignment strategy:
     - Round-robin
     - Key-based
     - Custom partitioning

5. **Consumer Groups**
   - Multiple consumers work together to process messages
   - Each partition is consumed by exactly one consumer within a group
   - Multiple consumer groups can read the same topic independently
   - Automatic rebalancing when consumers join/leave

Key Interactions:
- Producers write to partition leaders
- Followers replicate data from leaders
- ZooKeeper manages metadata and coordinates cluster
- Consumers read from partition leaders
- Consumer groups enable parallel processing

