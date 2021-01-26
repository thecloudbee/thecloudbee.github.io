---
layout: post
title:  "How to Structure Your Ansible Playbook? - the Minimalistic Guide"
author: amroj
categories: ansible
image: assets/images/2021-01-26/head.png
description: "Ansible helps us to setup or configure 100s of machines in an agent-less manner. This guide will help you structure the Ansible Playbook such that it is more intuitive — the team will love to collaborate."
featured: true
hidden: true
rating: 0
---

## Why a structure is important in Ansible?

Ansible is the one destination for all IT automation. With time, the complexity of a system increases and so does the number of components involved. It becomes important to isolate the components in your automation scripts. These scripts work independently of each other -- called roles in Ansible.

The Single Responsibility principle when applied to an Ansible folder structure makes a lot of sense. There are different ways to separate your components. Below is the one that always works for me.

## Ansible Roles to define the limits

Roles help you define a directory structure such that — everything under a single role can share variables and tasks. Once you group the content into roles, it can be reused.

Let's dive into the Ansible structure. Consider a typical scenario where we are creating a Kafka cluster with several Kafka and Zookeeper nodes.

![2021-01-26/1.png]({{ site.baseurl }}/assets/images/2021-01-26/1.png){: .center-image }

Keeping in mind the above deployment plan, we can point out that Java must be a different role altogether. The Java role will be included both in Zookeeper and Kafka playbooks.

The minimal folder structure to contain the above requirements.

```
group-vars/
├── all.yml
roles/
├── java/
	├── defaults
	│   └── main.yml
	├── files
	├── tasks
	│   └── main.yml
	├── templates
├── kafka/
	├── defaults
	│   └── main.yml
	├── files
	├── tasks
	│   └── main.yml
	├── templates
├── zookeeper/
	├── defaults
	│   └── main.yml
		....
hosts/
│   └── hosts
playbook_kafka_cluster.yml
```

We have three different roles Java, Kafka and Zookeeper. Each of the roles acts as an independent entity and can run in isolation.

## Ansible Host Inventory

Ansible works with a spectrum of systems in infrastructure at the same time. Consider the below two use cases.

1. A change to be applied just to the Zookeeper nodes in production.
2. A change to be applied to all the staging nodes.

Ansible `hosts` inventory enables you to group your resources. Further the `:children` postfix in the hosts file lets you have groups of groups.

{% gist thecloudbee/0e53b158bab8aeb70c932e6b8e9e7f2b %}

We have grouped Kafka and Zookeeper hosts based on the services we want to install and the flavors.

## Ansible Playbook to put everything together

Playbook helps you out together the roles and hosts.

{% gist thecloudbee/cc68fde22e1855cb7a8eddce0b6e93bb %}

The below command gives us a clearer picture of how everything can be put together. We can use the `--limit` argument to limit the groups to run the Ansible.

{% gist thecloudbee/6ec2e67d28e4f246d6ac47004762a2a5 %}

Or we can say `--limit 'production'` to deploy the cluster on the production environment.

## Conclusion

A complex infra can lead to complicating our Ansible scripts. It is trivial to define a directory structure that is scalable. By having a folder structure and a host inventory we can make the best out of our Ansible automation.