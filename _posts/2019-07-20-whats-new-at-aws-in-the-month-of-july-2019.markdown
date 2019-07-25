---
layout: post
title: "AWS Weekly"
date: 2019-07-20
author: omps
comments: true
published: true
featured: true
---

  Now use AWS Systems Manager Maintenance Windows to select resource groups as targets
======================================================================================

[  AWS Systems Manager Maintenance Windows enable you to define a time window for performing potentially disruptive actions on your instances. You can now use maintenance windows to select a resource group as the target. Resource groups make it easier to organize, manage, and automate tasks on large numbers of resources at one time. By selecting a resource group as the target of a maintenance window, you can perform routine tasks across different resources such as Amazon Elastic Compute Cloud (Amazon EC2) instances, Amazon Elastic Block Store (Amazon EBS) volumes, and Amazon Simple Storage Service (Amazon S3) buckets within the same recurring time window.

  ,   Previously, targets for maintenance windows were limited to Amazon EC2 instances, which were selected manually or through tags. With the support of resource groups, the targets can be any resource [supported by AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html#supported-resources-console). For example, by selecting a resource group that represents your application as the target, you can schedule a Systems Manager Automation task to back up the application EBS volumes, and then run a Systems Manager RunCommand task to patch the EC2 instances that host the application within the same maintenance window. You can also execute an AWS Lambda function or AWS Step Functions task that targets the resources belonging to the resource group.

  ,   Maintenance Windows is a feature of Systems Manager. Systems Manager enables visibility and control of your cloud and on-premises infrastructure. It simplifies resource and application management, shortens the time to detect and resolve operational problems, and makes it easier to operate and manage your infrastructure securely at scale.

  ,   This feature is available in all AWS Regions where AWS Resource Groups is available. For more details about this feature, see our [Documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html). To learn more about AWS Systems Manager Maintenance Windows, visit our [Product Page](https://aws.amazon.com/systems-manager/features/).

  ]  Configuration update for Amazon EFS encryption of data in transit
===================================================================

[  We’ve updated the default configuration for the [Amazon Elastic File System (Amazon EFS)](/efs/) mount helper package when using encryption of data in transit. Starting today, use of the Online Certificate Status Protocol (OCSP) is not enabled by default.

  ,   The Amazon EFS mount helper provides the option to encrypt data in transit for EFS file systems using Transport Layer Security version 1.2 (TLS v1.2). EFS uses an [Amazon certificate authority](https://www.amazontrust.com/) (CA) to issue and sign its TLS certificates, as well as to check for certificate revocation using OCSP. The OCSP endpoint must be accessible over the Internet from your Virtual Private Cloud (VPC) in order to check for certificate revocation. To maximize file system availability in the event that the CA is not reachable from your VPC, the EFS mount helper no longer enables OCSP by default. Within the service, EFS continuously monitors for certificate revocation status and will issue new certificates if a revoked certificate is detected.

  ,   You can still choose to enable OCSP to have your clients check for revoked certificates, providing the strongest possible security. OCSP protects against malicious use of revoked certificates, which is unlikely to occur within your VPC. In the event that an EFS TLS certificate is revoked, Amazon will publish a [security bulletin](/security/security-bulletins/) and make a new version of the EFS mount helper available that explicitly rejects the revoked certificate. This will require you to update the EFS mount helper manually.

  ,   The updated EFS mount helper is available within [Amazon Linux](/amazon-linux-ami/) and [Amazon Linux 2](/amazon-linux-2/) AMIs, and can also be found on [GitHub](https://github.com/aws/efs-utils). To get started with the Amazon EFS mount helper and EFS encryption of data in transit, see the [documentation](https://docs.aws.amazon.com/efs/latest/ug/encryption.html#encryption-in-transit).[](/amazon-linux-2/)

  ]

Introducing Amazon EC2 Resource Optimization Recommendations
==============================================================

[  Starting today, you can access custom-generated Amazon EC2 resource optimization recommendations in AWS Cost Explorer. These recommendations identify idle and underutilized instances across your accounts and regions. To generate these recommendations, AWS analyzes your historical EC2 resource usage, your Amazon CloudWatch metrics, and your existing reservation footprint to identify opportunities for cost savings (e.g., by terminating idle instances or downsizing active instances to lower-cost options). For example, if your m5.2xlarge has a maximum utilization of 20% over the last 14 days, AWS may recommended downsizing that instance to m5.xlarge or m5.large and show you how much you can save based on your usage and your applicable m5 family reservations.

  ,   To get started, just click on the Recommendations summary link on the AWS Cost Explorer sidebar to view your resource- and reservation-related recommendations. From the Resource Optimization page, you can dive deeper into your individual resource recommendations, download them in CSV form, and take action accordingly. Resource optimization recommendations can also be accessed via the [AWS Cost Explorer API](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-api.html).

 To learn more about getting started with Amazon EC2 resource optimization recommendations, please visit this [blog post](https://aws.amazon.com/blogs/aws-cost-management/launch-resource-optimization-recommendations/) or the [Optimizing your Costs with Rightsizing Recommendations](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-rightsizing.html) user guide.



  ]  AWS Backup will Automatically Copy Tags from Resource to Recovery Point
=========================================================================

[  AWS Backup now provides customers a more seamless way to manage their backups, by automatically copying tags from their resources to their backups. For customers using tags to manage their AWS resources, AWS Backup will enable them to more effectively search for source resources or conduct billing for their backups. See [AWS Tagging Strategies](/answers/account-management/aws-tagging-strategies/) for tagging best practices.

  ,   [AWS Backup](/backup/) offers a centralized, managed service to back up data across AWS services in the cloud as well as on premises using Storage Gateway. AWS Backup serves as a single dashboard for backup, restore, and policy-based retention of different AWS resources, including Amazon EBS volumes, Amazon RDS databases, Amazon DynamoDB tables, Amazon EFS file systems, and AWS Storage Gateway volumes.

  ,   To learn more about AWS Backup, please see our [product page](/backup/) and [documentation](https://docs.aws.amazon.com/aws-backup/).

  ]  Amazon EC2 P3 Instances Featuring NVIDIA Volta V100 GPUs now Support NVIDIA Quadro Virtual Workstation
========================================================================================================

[   Customers can now use Amazon EC2 P3 and P3dn instances for graphics applications such as remote workstations and 3D visualization using NVIDIA Quadro Virtual Workstation software made available using new Amazon Machine Images (AMIs) accessible on the AWS Marketplace.

  ,   As more and more customers migrate graphics intensive workloads to the cloud to take advantage of increased agility and ease of management, they also continually look for increased compute power to support complex use cases. NVIDIA Quadro Virtual Workstation AMIs deliver high graphics performance using the powerful NVIDIA Volta V100 GPUs running in the AWS cloud. These AMIs have the latest NVIDIA GPU graphics software preinstalled along with the latest Quadro drivers and Quadro ISV certifications with support for up to four 4K desktop resolutions and 8K video encoding capabilities. NVIDIA V100 combined with Quadro vWS delivers fast ray tracing, advanced simulations, and AI-powered rendering. Also look for our upcoming release of EC2 G4 instances featuring NVIDIA T4 GPUs which leverage the NVIDIA Turing architecture and RTX platform enhancements, enabling support for real-time photorealistic rendering and AI-enhanced graphics, video and image processing from the cloud.

  ,   The new AMIs are available on the AWS Marketplace with support for Windows Server:

  * NVIDIA Quadro Virtual Workstation - WinServer 2016 - <https://aws.amazon.com/marketplace/pp/B07TV59ZQK>
 * NVIDIA Quadro Virtual Workstation - WinServer 2019 - <https://aws.amazon.com/marketplace/pp/B07TS3S3ZH>
   ,    To learn more about EC2 P3 and P3dn instances, visit the [P3 product page](https://aws.amazon.com/ec2/instance-types/p3/).

  ]  Amazon MQ Adds Support for AWS Key Management Service (AWS KMS), Improving Encryption Capabilities
====================================================================================================

[  Amazon MQ now supports the AWS Key Management Service (AWS KMS) to create and manage keys for at-rest encryption of customer data in Amazon MQ. Amazon MQ handles the encryption and decryption seamlessly, so you don’t have to change your applications to access your data. When you create a broker, you can now select the KMS key used to encrypt your data from the following three options: a KMS key in the Amazon MQ service account, a KMS key in your account that Amazon MQ creates and manages, or a KMS key in your account that you create and manage. In addition to encryption at rest, all data transferred between Amazon MQ and client applications is securely transmitted using TLS/SSL.

  ,   [Amazon MQ](/amazon-mq/) is a managed message broker service for Apache ActiveMQ that makes it easy to set up and operate message brokers in the cloud. Message brokers allow different software systems–often using different programming languages, and on different platforms–to communicate and exchange information. With Amazon MQ, you can use industry standard APIs and protocols for messaging, including JMS, NMS, AMQP, STOMP, MQTT, and WebSocket. You can easily move from any message broker that uses these standards to Amazon MQ because you don’t have to rewrite any messaging code in your applications.

  ,   KMS support is available in all AWS regions where [Amazon MQ is available](/about-aws/global-infrastructure/regional-product-services/). To learn more see [Amazon MQ Encryption](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-encryption.html) in the Amazon MQ Developer Guide.

  ]  Introducing AI-Driven Social Media Dashboard
==============================================

[  [AI-Driven Social Media Dashboard](/solutions/ai-driven-social-media-dashboard/) is a solution that monitors and ingests specified tweets using stream processing and leverages a serverless architecture and machine learning services to translate and extract insights from those tweets. The solution is easy to deploy and contains a data lake you can use to quickly and easily perform additional analytics on tweet data.


  ,   The solution uses [Amazon EC2](/ec2/), [Amazon VPC](/vpc/), [Amazon Kinesis Data Firehose](/kinesis/data-firehose/), [Amazon S3](/s3/), [AWS Lambda](/lambda/), [Amazon Translate](/translate/), [Amazon Comprehend](/comprehend/), [AWS Glue](/glue/), [Amazon Athena](/athena/), and [Amazon QuickSight](/quicksight/). To learn more about the AI-Driven Social Media Dashboard solution, see the [solution webpage](/solutions/ai-driven-social-media-dashboard/).

  ,   Additional AWS Solutions offerings are available on the [AWS Solutions webpage](/solutions/), where customers can browse solutions by product category or industry to find AWS-vetted, automated, turnkey reference implementations that address specific business needs.[](/solutions/)

  ]  AWS Systems Manager Distributor makes it easier to create distributable software packages
===========================================================================================

[  AWS Systems Manager Distributor provides simplified package creation, enabling you to deploy your software packages across instances quickly. Distributor will package your installers so they can be easily used to install and update your software across multiple operating systems.

  ,   With Distributor, you can securely store and manage software packages, such as software agents, from a centralized, version-controlled repository. With the simplified package creation experience, you select the installable files you want, and Distributor automates creating installation and uninstallation scripts, uploading the installable files, and zipping everything into a package. These packages can then be shared across AWS accounts and distributed to instances on demand or on a schedule. You can also report on compliance of your software distribution from the Systems Manager compliance dashboard.

  ,   Distributor is a feature in Systems Manager. Systems Manager enables visibility and control of your cloud and on-premise infrastructure. It simplifies resource and application management, shortens the time to detect and resolve operational problems, and makes it easier to operate and manage your infrastructure securely at scale.

  ,   The AWS Systems Manager Distributor feature is available in [all GovCloud (US) and commercial Regions](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) (excluding China Regions). This feature is priced on a pay-per-use model. See the AWS Systems Manager [Pricing page](https://aws.amazon.com/systems-manager/pricing/) for details.

  ,   For more information about Distributor, visit the AWS Systems Manager [Product page](https://aws.amazon.com/systems-manager/features/) and [Documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html).

  ]  AWS Direct Connect support for AWS Transit Gateway is Now Available in AWS EU (Ireland) region
================================================================================================

[  AWS Direct Connect support for AWS Transit Gateway is now available in AWS EU (Ireland) region. With this feature, customers can connect thousands of Amazon Virtual Private Clouds (Amazon VPCs) in multiple AWS Regions to their on-premises networks using 1/2/5/10 Gbps AWS Direct Connect connections.

  ,   AWS Direct Connect gateway allows you to access any AWS Region (except China) using your AWS Direct Connect connections. You can associate up to three Transit Gateways from any AWS Region with each Direct Connect gateway. AWS Direct Connect is introducing a new type of virtual interface called the transit virtual interface to support connectivity to AWS Transit Gateway. You can create a transit virtual interface using your 1/2/5/10 Gbps AWS Direct Connect connections at any AWS Direct Connect locations, with the exception of AWS Direct Connect locations in China. To increase the resiliency of your connectivity, we recommend that you attach at least two transit virtual interfaces from different AWS Direct Connect locations, to the Direct Connect gateway. For more information, please refer to the AWS Direct Connect resiliency [recommendation](/directconnect/resiliency-recommendation/).

  ,   With this announcement, AWS Direct Connect support for AWS Transit Gateway is now available in a total of eight AWS Regions. Support for other AWS Regions is coming soon. For more information about AWS Direct Connect support for AWS Transit Gateway, please read the [user guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html).

  ]  Amazon ECS Console now enables simplified AWS App Mesh integration
====================================================================

[  When creating or updating an ECS task definition in the ECS console, you now have the ability to add the task to a mesh in AWS App Mesh. AWS App Mesh is a service mesh that provides application-level networking to make it easy for your services to communicate with each other across multiple types of compute infrastructure.


  ,   App Mesh uses the open-source Envoy proxy as a sidecar container for service-to-service communication. The ECS console can now automatically add the Envoy container to your task definition, set up the proxy configuration parameters, add the Envoy container to your mesh, and configure container startup ordering for you.


  ,   The simplified App Mesh integration in the ECS console is available in [all regions where ECS and App Mesh are available](/about-aws/global-infrastructure/regional-product-services/). To get started with App Mesh and ECS, visit our [documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/mesh-gs-ecs.html).


  ]  AWS IoT Device Tester v1.3.0 is Now Available for Amazon FreeRTOS 201906.00 Major
===================================================================================

[  [AWS IoT Device Tester,](https://aws.amazon.com/freertos/device-tester/) a Windows/Linux/Mac test automation tool for connected devices, is now available for [Amazon FreeRTOS 201906.00 Major.](https://aws.amazon.com/about-aws/whats-new/2019/06/bluetooth-low-energy-support-amazon-freertos-now-available/)

  ,   You can use AWS IoT Device Tester to easily determine if your microcontroller based devices running Amazon FreeRTOS can be authenticated by and interoperate with AWS IoT. AWS IoT Device Tester runs end-to-end tests with AWS IoT Core to give you confidence that your devices meet the security and functional requirements to interoperate with AWS IoT services.

  ,   AWS IoT Device Tester is required to qualify as part of the [AWS Device Qualification Program](https://aws.amazon.com/partners/dqp/). Qualified devices are listed in the [AWS Partner Device Catalog](https://devices.amazonaws.com/). You can learn more about AWS IoT Device Tester for Amazon FreeRTOS [here](https://aws.amazon.com/freertos/device-tester/), and download the latest release [here](https://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html).


  ]  Amazon Comprehend Custom Entities now supports multiple entity types
======================================================================

[  [Amazon Comprehend](/comprehend/) is a natural language processing (NLP) service that uses machine learning to find insights and relationships in text. With Comprehend’s Custom Entity Recognition API, you can easily build models to extract custom entities (policy numbers, part codes, serial numbers, etc.) that are tailored to your organization’s needs.

  ,   Starting today, Amazon Comprehend Custom Entity Recognition supports multiple entity types per model. With multi entity support, you can create a single custom entity recognition model to identify up to twelve entity types. You can now reduce cost and complexity by detecting multiple entity types in your documents using a single detection job.

  ,   Amazon Comprehend multi entity type support is now available in all AWS regions where Amazon Comprehend is available. For additional information, please visit the [documentation](https://docs.aws.amazon.com/comprehend/latest/dg/custom-entity-recognition.html).

  ]  AWS Device Farm improves device start up time to enable instant access to devices
===================================================================================

[  AWS Device Farm is an app testing service that lets you test your Android, iOS, and web apps , on a massive collection of real mobile devices hosted in the AWS Cloud. You can use one of the supported automation test frameworks to parallelly test your app on many devices, or you can use Device Farm’s Remote Access (manual testing) feature to gesture, swipe, and interact, with the device in real time directly from your web browser.

  ,   With today’s launch, Device Farm is reducing the device start up time by 90% so you get instant access to real iOS and Android devices. If you have selected a device that is available, Device Farm will now setup the device for your test within thirty seconds of your request. To ensure you always select an available device, make sure to update your Device Pool to include the *availability* rule.

  ,   To learn more about AWS Device Farm see the [documentation](https://docs.aws.amazon.com/devicefarm/?id=docs_gateway) or visit the [product page](/device-farm/).

  ]
