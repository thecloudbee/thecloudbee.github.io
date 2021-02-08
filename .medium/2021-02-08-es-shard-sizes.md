# Control the Size of Shards — Supercharge Elasticsearch for Performance

Shards are the heart of Elasticsearch. This blog takes the understanding of shards further to link it with performance.

![2021-02-08/head.png](https://www.thecloudbee.blog/assets/images/2021-02-08/head.png)

## Why Shard Size matters?

The search power of Elasticsearch revolves around the shard size. An index has many shards and a shard is a "search engine" in itself. Whenever a query is hit on an index, it is sent to all the shards inside that index. Further the results are aggregated to show you the query response.

- More shards (small-sized) means less time on searching inside a shard. But **more time in aggregation**.
- Less shards (large-sized) means more time spent on searching inside a shard. But there is **less aggregation time**.

> One shard is searched by a single thread.

![2021-02-08/1.png](https://www.thecloudbee.blog/assets/images/2021-02-08/1.png)

Both the indexes are storing the same amount of data but with different shard sizes. The left index has smaller shards as compared to the right one. More aggregations have to perform on the left one. But in the later index, search time per shard is greater, as it is storing double the amount of data.

## Where will things become problematic?

When the data size that is being indexed doesn't follow a fixed pattern.

If we are indexing data that has a constant rate (e.g. service logs), we can have one index each day. This way we have similar data sizes in indexes -- and hence in shards. This takes the pain away to go into complex shard tailoring exercises. Also, the index management, for example, deleting data older than 7 days, becomes easy in this case. All we have to do is — delete index that is dated 7 days from now in the past. 

On the contrary, given an irregular data stream we will end up creating indexes with varied sizes. So, the shard size across the cluster is not comparable. Some shards are smaller that will respond quickly -- while the overloaded ones will be slower.

## The Solution

Elasticsearch provides us with options to optimise our ES shards. We can control the size of indexes using the following strategies.

## Rollover Index API

The idea is to create a new index when the current index has exceeded a particular threshold. Define the number of documents, size, or time and Elasticsearch will automatically Rollover the index by creating a new index.

An Index-alias is required to keep things simple for the client. Whenever an index is created, the index alias is pointed to the new index. The client can continue indexing using the alias without worrying about the index change.

[https://gist.github.com/thecloudbee/d41e716bf94202683bfef4cd29d1da91](https://gist.github.com/thecloudbee/d41e716bf94202683bfef4cd29d1da91)

The API defines a Rollover index at 2 GB or 2M docs, with an index alias `tcb-views-alias`.

## Shrink Index API

In the Rollover index, the ES is creating indexes with names, tcb-views-000001, tcb-views-000002, and so on. Think of index management in the above case.

Another strategy that can be adopted in ES to reduce the number of shards is the Shrink Index. An additional demerit with this technique is that a shrunk index can't be updated anymore. Though that is a lot to ask, but the concept is interesting. As the data gets older it is less likely to be searched. Shrink a large number of primary shards to save on fore said aggregations. Also, you can choose to reduce replicas to save a lot of disk space.

[https://gist.github.com/thecloudbee/1f1c352aa23fd939bf2afa9d8b33e1bd](https://gist.github.com/thecloudbee/1f1c352aa23fd939bf2afa9d8b33e1bd)

A notable point is that the Rollover index is a configuration. But, the later is an API and has to be performed on demand on the indexes to be optimised.

## Conclusion

Understanding the role shards has to play in search performance is crucial. We can use Rollover and Shrink API to make a perfect balance of shards inside the cluster. 

This will not only save on compute power but also the memory. ES keeps index and shard metadata in the main memory. Hence, we are saving on that as well. With a lot of savings, book a beach holiday this year. 🏖
