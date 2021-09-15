---
slug: intro-influxdb
tags: [influxdb, monitoring]
...

# Why I love this Monitoring Stack so much? - InfluxData

Being a part of mission-critical services and managing our monitoring stacks has given me exposure to various such tools. But this monitoring stack is the hero.

![2021-09-16/head.png](https://www.thecloudbee.blog/assets/images/2021-09-16/head.png)

![Untitled](Why%20I%20love%20this%20Monitoring%20Stack%20so%20much%20-%20InfluxD%20a8f902952e8f4bef88333f102bea025c/Untitled.png)

InfluxDB has been the highest rated time-series database since 2016.

So what makes it so popular? The single word can is simplicity. 

The InfluxDB an opensource time-series database — is used to store metrics for monitoring and alerting purposes. The time series implies we are getting data for each second and we store it in no predefined structure. The latter is the definition of schema-less design.

But what proves my strong claims?

1. Ease of Data Collection
2. Faster and Cheaper
3. A Fancy UI

## Ease of Data Collection

Meet the TICK stack — a toolkit provided by InfluxDB for data collection, storage, visualization, and alerting. 

T in TICK stands for Telegraf. This component is the one that collects data. The Telegraf runs as a daemon and can collect any type of data, not confining itself to CPU and memory usage.

A simple example would be to collect Kafka stats, for example, the number of messages coming in/going out for a broker. All you have to do is install Telegraf on all the Kafka instances and add a plugin to the Telegraf service. There [is a plugin]() for most of the services presents out there.

Above all, InfluxDB is not confined to Telegraf, it works well with Graphite or Collectd as well.

## Faster and Cheaper

To optimise storage and performance, InfluxDB makes sure that data inserted into the storage is aggregated on its own. This aggregation makes sense as it is the summarized data that we are looking at in our dashboards. They call it, Downsampling.

As an example, the CPU values that are beyond 24 hours need not be granular at the second level. Why not take a mean and store these values at minute intervals?

## Visualising the data stored in InfluxDB

Coming back to the TICK terminology. What we are interested in here is C and K, namely Chrongraf and Kapacitor. The Chrongraf is a data visualization interface and the latter one is an alerting system.

Can anything be fancier than this dashboard over here.

![2021-09-16/1.png](https://www.thecloudbee.blog/assets/images/2021-09-16/1.png)

## Conclusion

The monitoring stack has to be the most simple piece of technology in a micro-service ecosystem. At the same time, it should make a hole in your pocket. InfluxDB is the answer.

Migration to InfluxData is seamless, as all you have to do is install a metrics forwarding service on your machine. Or you can configure your current forwarders like graphite to leverage InfluxDB as the storage.

*Do you experience same feeling as me for InfluxData?*

---

*Originally published at [https://www.thecloudbee.blog](https://www.thecloudbee.blog/intro-influxdb/) on [September 16, 2021].*