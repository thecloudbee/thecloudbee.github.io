# Elasticsearch Cluster Is Red — What Must Be Your Action Plan?
"Elasticsearch cluster is red", that seems like a warning to take a quick action upon. Here is a guide to bring the cluster back to life.

## What is a Red Cluster?

A red (or a yellow) cluster implies the cluster health of Elasticsearch. Let's understand why a red cluster is a big deal and a step-by-step guide to tackling it.

An Elasticsearch index is composed of many shards. A shard is a unit of data that is a little search engine in itself. By default, Elasticsearch has 5 shards and 1 replication factor.

That implies each index is divided into 5 units and each of the 5 units has one replica. In total, we will have 10 shards.

![1.png](https://www.thecloudbee.blog/assets/images/2021-01-26/head.png)

Considering the above arrangement of primary (red) and replica (white) shards across 3 nodes in an ES cluster. Further, the node in the region uswest dies. That implies that shards (1, 5, 2, 4) are not part of the cluster. The cluster has lost some of its primary shards. Hence, the **cluster is Red**.

## Why to worry about the Red cluster?

> Elasticsearch cluster is red ⇒ at-least one index is red ⇒ at-least one primary shard in the index is not allocated.

Remember the above quote. Since we have lost primary shards some of the data in Elasticsearch is not searchable. That implies our search and indexing traffic is experiencing downtime.

What are situations when the above can happen?

- One or many nodes in the cluster were either stopped or restarted.
- One or many nodes lost connection with other nodes in a cluster.
- One or many nodes are not responding.

## The Plan.

We are laser-focused on finding out the reason why some primary shards are not allocated. Watch for the following metrics in Kibana to understand the gap.

### Shards and Nodes

![Elasticsearch%20Cluster%20Is%20Red%20%E2%80%94%20What%20Must%20Be%20Your%20A%2066cdb756f6184c82be9b6ebc2b844a1c/Untitled%201.png](Elasticsearch%20Cluster%20Is%20Red%20%E2%80%94%20What%20Must%20Be%20Your%20A%2066cdb756f6184c82be9b6ebc2b844a1c/Untitled%201.png)

1. **Nodes:** Number of nodes, also the number of failed nodes, if any.
2. **Relocating Shards:** The number of shards moving due to the loss of a node or otherwise.
3. **Unassigned Shards:** The number of shards for which replicas have not been created yet.

### Node Health

![Elasticsearch%20Cluster%20Is%20Red%20%E2%80%94%20What%20Must%20Be%20Your%20A%2066cdb756f6184c82be9b6ebc2b844a1c/Untitled%202.png](Elasticsearch%20Cluster%20Is%20Red%20%E2%80%94%20What%20Must%20Be%20Your%20A%2066cdb756f6184c82be9b6ebc2b844a1c/Untitled%202.png)

1. **Available Disk Space Percentage:** The thumb rule is to fill it max up to 80%. This limit is considered a safe bet.
2. **RAM percentage:** If the RAM percentage is going above 95% or there are peaks in between. This is an alarming situation.
3. **CPU:** Percentage of CPU in use. You can observe the peaks here as-well. You may have to have a look at JVM health i.e. GC metrics to get a better understanding of what might be wrong here.

## How will the cluster recover?

The above dashboards will help you pin down the issue. Further, once you have fixed the cluster, how will it react?

![Elasticsearch%20Cluster%20Is%20Red%20%E2%80%94%20What%20Must%20Be%20Your%20A%2066cdb756f6184c82be9b6ebc2b844a1c/Screen_Shot_2021-01-31_at_4.00.26_PM.png](Elasticsearch%20Cluster%20Is%20Red%20%E2%80%94%20What%20Must%20Be%20Your%20A%2066cdb756f6184c82be9b6ebc2b844a1c/Screen_Shot_2021-01-31_at_4.00.26_PM.png)

When the cluster is red, we can see the shard (Unassigned Replica) in yellow that is not assigned to any node. Further, Elasticsearch starts a process called shard reallocation. After some time, the snapshot on the right depicts the same was assigned to a node `thecloudbee01`.

That implies the primary and replica shards will adjust among the active nodes and hence our service is up again. When node 3 comes up, it will be synced for the data gap.

## Conclusion

A Red cluster in production is a situation of panic. Up to a certain limit, Elasticsearch will help recover from the failed state. In our scenario, we were assuming only one node went down.

What happens when we lose two nodes? In that case, we lose primary as well as replica nodes.