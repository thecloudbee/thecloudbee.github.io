---
layout: post
title:  "Tailor your ES Indexes for faster queries - define Analyzers"
author: amroj
categories: [elasticsearch]
image: assets/images/2021-01-18/head.png
description: "The default indexing strategy in Elasticsearch is not the best option for you. Understanding how data stored in ES impacts the search performance is trivial."
featured: true
hidden: true
rating: 0
---

## Why default Indexing strategy might not serve well?

During indexing, Elasticsearch extracts keywords from the raw data and stores them. This processing happens inside an analyzers in Elasticsearch. How we trim our data and create "keywords" — rules how efficient our search will be. Analyzers are not very intuitive in Elasticsearch, most of the time left unnoticed. But, they can make a big difference.

Assume we are storing logs in one index and user data in another. We want to split logs on special chars but not the email address of the user. Imagine the two cases going through the same analyzer.

## Inside an Elasticsearch Index

Elasticsearch stores the keywords in something called an Inverted Index. The Inverted Index has keywords and back-references to the raw text. Once you hit a query, the keywords are searched, not the raw data. The raw data is used to display search results, once referenced from the inverted index.

```java
com.cloud.bee ERROR java.lang.RuntimeException.UnsupportedOperationException The operation get is not supported.
```

Assume we have a raw log out of a Java program. We can either split the input on spaces or on — spaces and dots. Below are the two analyzers to do that same. Note that our query changes with what keywords we have.

![2021-01-18/1.png]({{ site.baseurl }}/assets/images/2021-01-18/1.png){: .center-image }

The default Analyzer had split the data at whitespace -- implies a search with wildcards (i.e. `runtimeexception`). In the second case, we configured the index to use a custom analyzer. This analyzer helped us to split the text at whitespaces and punctuation marks. Hence we have a simple query.

> A wildcard search vs a keyword search, you know who is the winner...

## Defining custom Analyzers in Elasticsearch

An analyzer has three parts, a character filter, a tokenizer, and a token filter. While defining a custom analyzer we must specify a tokenizer, the other two are optional.

With the following snippet, we are demonstrating the custom analyzer from our prior discussion.

{% gist aeb2439bf825d22b2a7637723d051464 %}

Note that we have `tcb_special_char_analyser` which calls for a tokenizer in return. The `tcb_special_char_tokenizer` is configured to tokenize on character groups (whitespace and punctations).

{% gist 44e5ad52c586f5f2abbb66c95b94aa2c %}

Keywords result set for the above index request.

```sql
com | cloud | bee | error | java | lang | runtimeexception | unsupportedpperationexception
 | operation | get | supported
```

Notice that in the above keywords the words like `the`, `get`, and `not` are not a part of the result set. This is because we have used a filter called `stop` which has filtered the English stop words.

## Conclusion

Based on the type of queries we are making it is trivial to define the custom analyzers. This can help us boost our query performance and more complications from the system.

The sky is the limit for the number of custom analyzers one can think of. Elasticsearch has defined several for you and they are just a search away...