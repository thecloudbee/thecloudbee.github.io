---
slug: es-metrics-part-1-3
tags: [elasticsearch, monitoring]
...

# Elasticsearch Metrics to Watch — Cluster Health — Part 1

An introduction to setting up metrics in Elasticsearch [Part 1 of 3].

![2021-02-22/head.png](https://www.thecloudbee.blog/assets/images/2021-02-22/head.png)

We talked about Elasticsearch going red in a recent post at [https://thecloudbee.blog](https://medium.com/thecloudbee/elasticsearch-cluster-is-red-what-must-be-your-action-plan-7432fdbcf281).

But we must act proactively on such possibilities and never have downtime in ES. But, how to read the Elasticsearch metrics to predict the cluster behavior?

## **Monitoring the ES Cluster Health**

To keep Elasticsearch Green we must keep an eye on the following metrics. These metrics are responsible for everything starting from search to indexing.

1. Number of Nodes and Shards
2. CPU, Disk, and Memory Stats

## Number of Nodes and Shards

Regardless of the number of nodes in an cluster -- an index must have a fixed number of shards. If we scale-up, the shards will rearrange themselves across new nodes. This provides better parallel processing. This process is **Shard Allocation**.

When a node is out of a cluster, below is how the cluster tries to recover from it.

- Since there are some missing shards from the cluster (primary/replicas) — the Shard Allocation kicks in.
- The Shard Allocation will search for lost primary shards. The Replica shards in this process are promoted to act as primary shards.
- To maintain the replication factor the shard replication will start.

There is a lot of activity going on inside a data node during recovery. Which takes a toll at CPU and Memory.

![2021-02-22/1.png](https://www.thecloudbee.blog/assets/images/2021-02-22/1.png)

We understand the risk of losing a node and having unassigned shards. Below is the list of metrics to watch for.

- The number of nodes.
- The number of active shards.
- The number of unassigned shards — if there are unassigned shards it means the cluster health will be yellow/red.

## Node Stats — CPU, Disk, and Memory

There are a number of reasons by which we can have unassigned shards in Elasticsearch. A node restart or stop, disk usage, or memory limits can cause the aforesaid scenario.

So, it becomes vital to monitor these parameters for each node in the cluster. 

- CPU Utilization
- Free Disk Space
- JVM Heap

![2021-02-22/2.png](https://www.thecloudbee.blog/assets/images/2021-02-22/2.png)

## Conclusion

Unassigned shards have a direct connection to the ES cluster health. Having a quick look at the above metrics will allow us to decide our further actions.

Look this space for series 2 and 3 of this article.

---

*Originally published at [https://www.thecloudbee.blog](https://www.thecloudbee.blog/es-metrics-part-1-3/) on .*