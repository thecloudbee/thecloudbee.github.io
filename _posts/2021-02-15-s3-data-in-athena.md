---
layout: post
title:  "How to Smartly Query Your Data in S3 Using Athena?"
author: amroj
categories: [athena, awscloud]
image: assets/images/2021-02-15/head.png
description: "Take decisions using your big data stored in S3 without running ETL jobs. Save cost by SMARTLY partitioning the data."
featured: true
hidden: true
rating: 0
---

## AWS Athena Pricing

Athena is a powerful service built to query the data in S3. It suites to data that is semi or unstructured. You only pay for the amount of data that was scanned during the query execution.

Since we are paying for the amount of data scanned, we can make a difference by — compressing, partitioning, or using smart formats to store the data.

It goes without saying that if we are storing big data in an S3 it must be compressed. Further, we can save the data in Columnar format such as Parquet, which makes Athena faster and cheaper. But a problem with the latter approach is that we must have a defined schema.

Lastly, partitions are the game-changers. Think of querying a data set that has several months of data vs the one which is partitioned into days.

## Partitioning Data in Athena

Inorder to run a query on Athena. We must defined a table with several columns and partitions. Athena supports different types of data, semi-structured data (like JSON and XML) and unstructured data( like CSV, logs, and text with delimiters).

It is ideal to save data daywise in S3. This way we can partition on a date and query any subset with fewer resources.

{% gist thecloudbee/d98a0883167e923c892db9d12d855764 %}

{% gist thecloudbee/00edec18d88d9e87c6f92cb52e62c34e %}

Consider the above folder structure and a sample log for the DHCP IP allocation logs. We can define a create table query as follows.

{% gist thecloudbee/a0337c1a3c2c08ad0ccb29198ca1fabe %}

`RegexSerDe` uses regular expression (regex) to serialize/deserialize.

Finally, we can create partitions using the below query.

{% gist thecloudbee/af6486d4fd161124d558b39c33bd62fc %}

## Querying the Data

Let's write a query to get all the IPs assigned to a Mac address for the given date.

{% gist thecloudbee/f45a109f69022afed0b1d2252701db0a %}

This is a simple SQL like query, note that where clause has the partition `date`. This implies we have limited the data that has to be scanned by querying inside the firewall folder with a specified date. 

All types of queries like JOIN, GROUP BY, and so on are supported by Athena.

## Conclusion

Athena is a powerful yet simple tool that can help you query your data in S3. It might not the fastest way to query big data but it has its own upsides of being able to query raw data.

Athena is using Presto behind the scenes — which is an interesting distributed query engine for big data.