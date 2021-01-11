---
layout: post
title:  "CloudFormation vs Terraform: My Experience With Both"
author: amroj
categories: [cloudformation, infrascode, terraform]
image: assets/images/2021-01-11/head.webp
description: "Infra-as-code is the backbone for any cloud. But, why should one look beyond CloudFormation Templates?"
featured: true
hidden: true
rating: 0
---

## Why Infrastructure as Code?

Infra-as-code implies we are provisioning infrastructure by writing a code. As in the case of AWS CloudFormation, we input `.yaml` files and AWS resources are generated.

We are inclined towards using infra as code due to two reasons.

1. Speed - Quick and Consistent changes across different environments.
2. Accountability - Who changed and what changed?

## Terraform was impressive.

I have been writing CloudFormation Templates (CFTs) for 4 years. But once I wrote my first Terraform, I never looked back. The first impression of terraform was.
- Less code
- Environments made easy
- Terraform makes the changes more visual

## Terraform means Manageable Code

Terraform understands the Abstraction. One can build a database module separated from the functions module. On the other hand, doing this through CFT means one CFTs for database and another one for functions.

![2021-01-11/1.webp]({{ site.baseurl }}/assets/images/2021-01-11/1.webp){: .center-image }

The Terraform modules provide a light-weight abstraction. We can leverage this abstraction to make our code understandable and easy to navigate. As in the above example we have different modules for app and data.

## Environments made easy in Terraform

Let's say you have a CFT that you have tested on the lab environment. Further, it is desired to run the same CFT on the staging environment. One can manage environments in CFT as follows.

{% gist thecloudbee/abbdfdb5e421cd6361d68e8663691276 %}

Now, switching between the argument in `FindInMap`, one can get different flavors.

Comparing the above scenario with Terraform. We can leverage Terraform variables to reuse the code for different deployment plans. The `terraform init` command creates a working directory with the Terraform Configuration Files. 

![2021-01-11/2.webp]({{ site.baseurl }}/assets/images/2021-01-11/2.webp){: .center-image }

The above folder structure in Terraform makes it easy to switch between the lab and staging flavours. Example is the following command.

{% gist 59c7d12ab56bb2f1af95723a31d195a2 %}

## Terraform makes the changes more visual

Both CloudFormation and Terraform have state management in-built. Both of these create a changeset before deployment and one can validate before deploying.

This is how the AWS CloudFormation changeset looks like when you create a change over an existing CFT.

![2021-01-11/3.webp]({{ site.baseurl }}/assets/images/2021-01-11/3.webp){: .center-image }

Now compare the above with the extra details provided by terraform when we are over-writing a change.

![2021-01-11/4.webp]({{ site.baseurl }}/assets/images/2021-01-11/4.webp){: .center-image }

The above snippet shows the details Terraform plan provides in comparison to AWS CloudFormation. We can make out that only the tags are changing for the Instance in Terraform. But in AWS CloudFormation no details are provided -- only the resources that are changing are listed.

## Conclusion

Terraform is more flexible and easy to learn. So, if you're starting the journey of infra-as-code, Terraform is the answer.

This is not a full list of comparisons between AWS CloudFormation and Terraform, but a part of that.