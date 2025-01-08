
## Interview prep quick bytes

- [[Redis persistence]] is the mechanism that enabled redis to survive restarts by saving data to disk. Offers to main persistence options
	- RDB - Redis Database
		- creates point in time snapshot of data at regular intervals
		- compact single file backups, faster restart time and better backup performance
		- but there could be potential data loss between snapshots
	- AOF - Append only file
		- logs every operation received by the server to a file, keeping detailed diary of all changes made to data
		- file can be replayed to rebuild the state
		- better durability guarantees since no data loss, easier to understand and restore
		- but file could grow very large and restarts could be slow
- [[Redis eviction policies]] are used when [[Redis]] reaches it's memory limit
	- No eviction - start returning error when memory limit has been reached
	- LRU based - evict least recently used key
	- Random  - remove keys randomly
	- TTL based - remove keys closest to expiration
	- LFU based - remove least frequently used keys
- Redis offers a variety of [[Redis data structures]] for multiple use cases
	- string - caching, counters, session management
	- list - message queues
	- sets - unique collections
	- sorted set - leaderboard, priority queue
	- hashes - object storage, field value pair management
	- 