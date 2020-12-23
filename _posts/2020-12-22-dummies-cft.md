---
layout: post
title:  "Steps to write your First CloudFormation Template"
author: amroj
categories: [awscloud, cloudformation, infrascode]
image: assets/images/2020-12-22/head.webp
description: "Dummies guide to create AWS resources with code - CFTs."
featured: true
hidden: true
rating: 0
---

## Why use the CloudFormation Template?

One sure way to create an EC2 is via the AWS Console. You can click on "Create Instance" and enter subnets, security groups, and the instance type. Submit. It's easy.

But, can you do the same steps 20 times over — in order to create a cluster with these instances? 

The answer is, No.

![2020-12-22/1.png]({{ site.baseurl }}/assets/images/2020-12-22/1.webp){: .center-image }

## Hence, CloudFormation.

The CloudFormation template lets you write infra-as-code. Where the JSON (or YAML) configurations define the infra i.e. the EC2 resource in our case. Further, we can replicate the same code for other instances. Run it once to create the required resources.

This article is your first look at CFT and how to write a minimal CFT that is manageable.

The CFT below creates an EC2 Instance in AWS.

{% gist thecloudbee/b35adb2c30d2f2db9a54520128813be1 %}

We can infer from the above YAML file that we are creating an EC2 instance with the Instance type `t2.micro`. 

Run the above CFT in the AWS Console > Goto CloudFormation > Choose the desired region from the top-right corner > Create Stack > Follow intructions.

Once we click on the "create stack" button, we will see an instance was created.

![2020-12-22/2.png]({{ site.baseurl }}/assets/images/2020-12-22/2.webp){: .center-image }

## How to separate the variables?

As per coding practices it makes sense to keep code and variable separate. Let's extract the variables, initialize them, and then use them in the CFT.

{% gist 0641a4b1052cd019f9781c8cbb642fc3 %}

By moving the hard-coding from the configs to parameters it makes a lot of sense. It is easier to have a glance at all the variables, since they are put together.

I don't want to go with a fixed instance type i.e. "t2.micro" in our case. Is it not a better idea to choose instance type as and when I run the CFT?

So the final version of our CFT will look like.

{% gist aa1db06e7a835dd4e3dd6f2ba60fa860 %}

Now, when we put this template into the AWS Console, it will show us the following selection.

![2020-12-22/3.png]({{ site.baseurl }}/assets/images/2020-12-22/3.webp){: .center-image }

## Conclusion

The CloudFormation provides us with the ease to define everything in AWS as a code. The scope of CFTs is not limit to this blog.

How can we change the above YAML file such that we can have different variables - for both prod and lab environment?