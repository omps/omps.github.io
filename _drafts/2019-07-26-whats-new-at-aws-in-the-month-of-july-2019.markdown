<h1 id="AWS_Secrets_Manager_now_supports_VPC_endpoint_policies"> <a name="AWS_Secrets_Manager_now_supports_VPC_endpoint_policies"> AWS Secrets Manager now supports VPC endpoint policies</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Secrets Manager now supports VPC endpoint policies, making it easier for you to restrict egress of secrets from your Amazon VPC. When you create a VPC endpoint for Secrets Manager, you can attach an endpoint policy to define the Secrets Manager actions that can be performed, the secrets these actions can be performed on, the IAM users or roles that can perform these actions, and the accounts that can be accessed via the VPC endpoint. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS Secrets Manager enables you to retrieve and manage secrets throughout their lifecycle. AWS Secrets Manager also makes it easier to follow the security best practice of using short-term secrets by <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html">rotating secrets safely</a> on a schedule that you determine. For example, you can <a href="https://aws.amazon.com/blogs/security/how-to-use-aws-secrets-manager-rotate-credentials-amazon-rds-database-types-oracle/">configure AWS Secrets Manager to rotate a database credential daily</a>, turning a typical long-term secret in to a short-term secret that is rotated automatically. By using Secrets Manager with Amazon VPC endpoint policies, you can now keep secrets-related, encrypted communication within the AWS network and help meet your compliance and regulatory requirements by granularly controlling access to Secrets Manager APIs. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS Secrets Manager is available in the Asia Pacific (Mumbai, Seoul, Singapore, Sydney, Tokyo), Canada (Central), EU (Frankfurt, Ireland, London, Paris, Stockholm), GovCloud (US-West), South America (São Paulo), US West (N. California, Oregon), and US East (N. Virginia, Ohio) regions. To learn more about AWS Secrets Manager, visit the <a href="https://docs.aws.amazon.com/secretsmanager/index.html">documentation</a>. To get started, visit the <a href="/secrets-manager/">AWS Secrets Manager home page</a>. </p>
</div>
</div>]<h1 id="Temporary_Queue_Client_Now_Available_for_Amazon_SQS"> <a name="Temporary_Queue_Client_Now_Available_for_Amazon_SQS"> Temporary Queue Client Now Available for Amazon SQS</a> </h1>[<div class="aws-text-box">
<div class="">
<p>The <a href="https://github.com/awslabs/amazon-sqs-java-temporary-queues-client">Temporary Queue Client</a> for Amazon Simple Queue Service (SQS) is now available. The client supports common messaging patterns such as request-response, and helps you save development time and deployment costs when creating application-managed temporary queues.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>The client maps multiple temporary queues onto a single Amazon SQS queue automatically, allowing your application to make fewer API calls and achieve higher throughput. When a temporary queue is no longer in use, the client cleans up the temporary queue automatically. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Amazon SQS is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. Amazon SQS eliminates the complexity and overhead associated with managing and operating message-oriented middleware, and empowers developers to focus on differentiating work. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>For more information about <a href="/sqs/">Amazon SQS</a>, see Amazon SQS and <a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-temporary-queues.html">Temporary Queues</a> in the <i>Amazon SQS Developer Guide</i>.<i></i> To get started with the new <a href="https://github.com/awslabs/amazon-sqs-java-temporary-queues-client">Temporary Queues Client</a>, download the library from <a href="https://github.com/awslabs">AWS Labs on GitHub</a> and read the <a href="https://aws.amazon.com/blogs/compute/simple-two-way-messaging-using-the-amazon-sqs-temporary-queue-client">AWS blog</a>.</p>
</div>
</div>]<h1 id="AWS_IoT_Events_actions_now_support_AWS_Lambda,_SQS,_Kinesis_Firehose,_and_IoT_Events_as_targets"> <a name="AWS_IoT_Events_actions_now_support_AWS_Lambda,_SQS,_Kinesis_Firehose,_and_IoT_Events_as_targets"> AWS IoT Events actions now support AWS Lambda, SQS, Kinesis Firehose, and IoT Events as targets</a> </h1>[<div class="aws-text-box">
<div class="">
<p>When using <a href="/iot-events/">AWS IoT Events</a>, you now have the option to define actions to invoke AWS Lambda functions, publish messages to the Amazon Simple Queue Service (SQS) queue or an Amazon Kinesis Data Firehose delivery stream, and republish messages to IoT Events. Previously, you could only define actions to publish messages to SNS and MQTT. These expanded actions make it easier to build monitoring applications that help you quickly understand the state of your devices by providing more options to process messages created by IoT Events.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>You can define a Lambda action to invoke a specific Lambda function with the message payload. The Lambda function receives the message payload as an input parameter and can further process the information in the message. Similarly, you can define an SQS action to send the message payload to a SQS queue that other services could read from. You can send the message payload to a Firehose delivery stream to display alerts in applications such as real-time dashboards. Finally, by defining IoT Events as an action, you send the message payload as an input to another detector model which can help simplify complex detector models into a hierarchy of simple ones. <br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p> These new actions are available in <a href="/about-aws/global-infrastructure/regional-product-services/">all regions where AWS IoT Events</a> is available. To get started, open the <a href="https://console.aws.amazon.com/iotevents">IoT Events console</a> and select a state for a detector model. Add an event to the state, and select from the <a href="https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-with-others.html">list of available actions</a>. <br/> </p>
</div>
</div>]<h1 id="Amazon_EC2_Spot_Now_Available_for_Red_Hat_Enterprise_Linux_(RHEL)"> <a name="Amazon_EC2_Spot_Now_Available_for_Red_Hat_Enterprise_Linux_(RHEL)"> Amazon EC2 Spot Now Available for Red Hat Enterprise Linux (RHEL)</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Starting today, you can launch <a href="/ec2/spot/">Amazon EC2 Spot Instances</a> running Red Hat Enterprise Linux (RHEL) on base Red Hat Enterprise Linux Images (AMIs). Previously, only customers with existing Red Hat Enterprise Linux Premium subscriptions could launch Amazon EC2 Spot Instances running RHEL (i.e. the bring your own license model). Spot Instances can now be launched through RHEL’s basic subscription model and are included in the hourly Spot Instance price.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p><a href="/ec2/spot/">Amazon EC2 Spot Instances</a> let you take advantage of unused EC2 capacity available in the AWS cloud. Spot Instances are available at up to a 90% discount compared to On-Demand prices. You can use Spot Instances for various stateless, fault-tolerant, or flexible applications such as big data, containerized workloads, CI/CD, web servers, high-performance computing (HPC), and other test &amp; development workloads. Spot Instances are easy to launch, scale and manage through AWS services like Amazon ECS and Amazon EMR, or integrated third parties like Terraform and Jenkins.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Spot Instances can be launched via RunInstances API with a single additional parameter. You can also provision compute capacity across Spot Instances, RIs and On-Demand instances to optimize performance and cost using EC2 Fleet and Spot Fleet APIs.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more about Amazon EC2 Spot Instances, visit <a href="/ec2/spot/">Amazon EC2 Spot page</a> or <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html">technical documentation</a>.</p>
</div>
</div>]<h1 id="Amazon_S3_adds_support_for_percentiles_on_Amazon_CloudWatch_Metrics"> <a name="Amazon_S3_adds_support_for_percentiles_on_Amazon_CloudWatch_Metrics"> Amazon S3 adds support for percentiles on Amazon CloudWatch Metrics</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon S3 announced support for percentiles on Amazon CloudWatch Metrics. This feature allows customers to visualize and alarm on p90, p95, p99, p99.9 or any other percentile (including p100) of an S3 request metric. This provides customers with more granularity about their request patterns on S3 and helps them observe and diagnose anomalies in request patterns on S3. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>S3 request metrics already support statistics such as average, minimum or maximum, which are useful for many metrics. Percentiles are particularly useful when applied to metrics that exhibit large variances. They also help customers understand the distribution of a metric, and can be critical to understand outliers or unusual metric behaviors. Percentiles help customers observe and diagnose anomalies in request patterns on S3, avoid false alarms and save costs spent in monitoring and tracking requests. This feature is included with Amazon S3 CloudWatch Metrics for no additional charge. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To get started, customers can turn on request metrics from the S3 console by navigating to the management tab of their S3 bucket. Once the metrics are turned on, customers can view and set up alarms on any percentile of a metric in their CloudWatch console by selecting a percentile from the drop-down list or entering a percentile of their choice, in 0.1% increments. Customers who already have request metrics turned on can skip the first step and directly go to the CloudWatch console to view percentiles of their metrics. These metrics can also be accessed using the SDK or API. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Percentile support for S3 request metrics is available in all <a href="/about-aws/global-infrastructure/regional-product-services/">AWS commercial regions</a> and <a href="/govcloud-us/">AWS GovCloud (US) Regions</a>.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>For information about CloudWatch pricing, see <a href="/cloudwatch/pricing/">Amazon CloudWatch Pricing</a>.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more about Amazon S3 CloudWatch Metrics, visit <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html">Monitoring Metrics with Amazon CloudWatch</a> in the Amazon S3 Developer Guide.</p>
</div>
</div>]<h1 id="Lumberyard_Beta_1.20_Now_Available"> <a name="Lumberyard_Beta_1.20_Now_Available"> Lumberyard Beta 1.20 Now Available</a> </h1>[<div class="aws-text-box">
<div class="">
<p>We’re excited to announce Lumberyard Beta 1.20, which reduces the time it takes Amazon Lumberyard to scan assets by 90%. This release contains over 200 improvements, fixes, and features.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>This release includes:</p>
<ul>
<li> Asset Processor scan time improvements. In <a href="https://aws.amazon.com/blogs/gametech/1-18/" target="_blank">Lumberyard 1.18</a>, we reduced the time it took to launch the Lumberyard editor by introducing Fast Scanning Mode to the Asset Processor. In Lumberyard 1.20, we improved Fast Scanning Mode even more. Now Lumberyard’s Asset Processor only scans asset files that have been modified since the last Lumberyard launch. A faster scan means a faster editor start up. This feature is on by default.</li>
<li> EBus performance improvements. We’ve reduced the overhead of using the Event Bus (EBus for short) messaging system so game systems and components can send and receive events faster (by at least 20% in most cases and up to 80% in others.) Using EBuses to send events between different game systems and components now performs closer to that of calling the event as a raw function. These low-level improvements don’t require you to make any changes – all of the APIs are staying the same.</li>
</ul>
<p> You can read about all of the Lumberyard 1.20 features and improvements in the full release notes <a href="https://docs.aws.amazon.com/lumberyard/latest/releasenotes/lumberyard-v1.20.html" target="_blank">here</a>.</p>
<p> To get started with Amazon Lumberyard, please visit the <a href="https://aws.amazon.com/lumberyard/" target="_blank">Lumberyard website</a> to download Lumberyard. You can learn more about Lumberyard’s new features by watching <a href="https://tinyurl.com/LumberyardTutorials" target="_blank">our Tutorials</a>, visiting the <a href="https://gamedev.amazon.com/forums/index.html" target="_blank">Forums</a>, or reading through our <a href="https://docs.aws.amazon.com/lumberyard/index.html" target="_blank">Documentation</a>.</p>
<p> Visit the <a href="https://aws.amazon.com/blogs/gametech/1-20" target="_blank">Game Tech blog</a> to learn more.</p>
</div>
</div>]<h1 id="Amazon_GuardDuty_Now_Available_in_AWS_Asia_Pacific_(Hong_Kong)_Region"> <a name="Amazon_GuardDuty_Now_Available_in_AWS_Asia_Pacific_(Hong_Kong)_Region"> Amazon GuardDuty Now Available in AWS Asia Pacific (Hong Kong) Region</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon GuardDuty is now available in the AWS Asia Pacific (Hong Kong) region. You can now continuously monitor and detect security threats in the Asia Pacific (Hong Kong) region to help protect your AWS accounts and workloads.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p> Available globally, Amazon GuardDuty continuously monitors for malicious or unauthorized behavior to help protect your AWS resources, including your AWS accounts and access keys. GuardDuty identifies unusual or unauthorized activity, like crypto-currency mining or infrastructure deployments in a region that has never been used. Powered by threat intelligence and machine learning anomaly detections, GuardDuty is continuously evolving to help you protect your AWS environment.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>You can enable your 30-day free trial of Amazon GuardDuty with a single-click in the AWS Management console. Please see the <a href="/about-aws/global-infrastructure/regional-product-services/">AWS Regions page</a> for all the regions where GuardDuty is available. To learn more, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html">Amazon GuardDuty Findings</a> and to start your 30-day free trial, see <a href="/guardduty/pricing/">Amazon GuardDuty Free Trial</a>.</p>
</div>
</div>]<h1 id="AWS_Glue_now_supports_additional_configuration_options_for_memory-intensive_jobs_submitted_through_development_endpoints"> <a name="AWS_Glue_now_supports_additional_configuration_options_for_memory-intensive_jobs_submitted_through_development_endpoints"> AWS Glue now supports additional configuration options for memory-intensive jobs submitted through development endpoints</a> </h1>[<div class="aws-text-box">
<div class="">
<p>You can now specify additional worker types when you use AWS Glue development endpoints. An AWS Glue <a href="https://docs.aws.amazon.com/glue/latest/dg/console-development-endpoint.html">development endpoint</a> is a serverless Apache Spark environment that you can use to develop, debug, and test your AWS Glue ETL scripts in an interactive manner.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Previously, you were able to specify the additional worker types only for Apache Spark jobs in AWS Glue. You can now pick from two new configurations, G.1X and G.2X, that provide more memory per executor. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more about these configuration options, please visit our <a href="https://docs.aws.amazon.com/glue/latest/dg/console-development-endpoint.html">documentation</a>. These options are now available in all the AWS regions where AWS Glue is available except AWS GovCloud (US-East) and AWS GovCloud (US-West). </p>
</div>
</div>]<h1 id="AWS_Glue_now_supports_the_ability_to_run_ETL_jobs_on_Apache_Spark_2.4.3_(with_Python_3)_"> <a name="AWS_Glue_now_supports_the_ability_to_run_ETL_jobs_on_Apache_Spark_2.4.3_(with_Python_3)_"> AWS Glue now supports the ability to run ETL jobs on Apache Spark 2.4.3 (with Python 3) </a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Glue has updated its Apache Spark infrastructure to support <a href="https://spark.apache.org/releases/spark-release-2-4-3.html">Apache Spark 2.4.3</a> (in addition to <a href="https://spark.apache.org/releases/spark-release-2-2-1.html">Apache Spark 2.2.1</a>) for ETL jobs, enabling you to take advantage of stability fixes and new features available in this version of Apache Spark.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>You can pick the Apache Spark infrastructure that you want your Glue jobs to run on by choosing a Glue version in job properties. Your existing Glue ETL jobs that were created without specifying a Glue version will be defaulted to a Glue version of <a href="https://docs.aws.amazon.com/glue/latest/dg/release-notes.html">0.9</a>. Glue jobs with a Glue version of <a href="https://docs.aws.amazon.com/glue/latest/dg/release-notes.html">1.0</a> will run on Apache Spark 2.4.3. In addition to supporting the latest version of Spark, you will also have the ability to choose between Python 2 and Python 3 for your ETL jobs. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more about how you can take advantage of this feature, please visit our <a href="https://docs.aws.amazon.com/en_us/glue/latest/dg/add-job.html">documentation</a> and <a href="https://docs.aws.amazon.com/glue/latest/dg/release-notes.html">release notes</a>.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>This feature is now available in all the AWS regions where AWS Glue is available except AWS GovCloud (US-East) and AWS GovCloud (US-West).  </p>
</div>
</div>]<h1 id="AWS_Amplify_Console_adds_support_for_automatically_deploying_branches_that_match_a_specific_pattern"> <a name="AWS_Amplify_Console_adds_support_for_automatically_deploying_branches_that_match_a_specific_pattern"> AWS Amplify Console adds support for automatically deploying branches that match a specific pattern</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amplify Console now supports branch pattern deployments, allowing developers to automatically deploy branches that match a specific pattern without any extra configuration. <br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Product teams using feature branch or GitFlow workflows for their releases, can now define patterns such as ‘release*/**’ to automatically deploy Git branches that begin with ‘release’ to a shareable URL. For apps with a backend, the Amplify Console automatically deploys a staging version of a backend so testers can make changes without impacting production.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more, visit our <a href="https://dev.to/kkemple/branch-based-deployment-strategies-with-aws-amplify-console-1n3c">launch blog.</a><br/> </p>
</div>
</div>]<h1 id="AWS_Snowball_and_AWS_Snowball_Edge_are_available_in_Asia_Pacific_(Seoul)_Region"> <a name="AWS_Snowball_and_AWS_Snowball_Edge_are_available_in_Asia_Pacific_(Seoul)_Region"> AWS Snowball and AWS Snowball Edge are available in Asia Pacific (Seoul) Region</a> </h1>[<div class="aws-text-box">
<div class="">
<p><a href="/snowball/">AWS Snowball</a> and <a href="/snowball-edge/">AWS Snowball Edge</a> are now available in the Asia Pacific (Seoul) region. Snowball and Snowball Edge are data transfer services that use secure, ruggedized devices to move up to petabytes of data into and out of Amazon S3 for migration, edge computing, machine learning and analytics.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS Snowball and AWS Snowball Edge help overcome the challenges to of moving large data sets to the cloud when you do not have adequate network bandwidth for transfers. For edge computing in remote, disconnected and harsh environments, AWS Snowball Edge also enables you to run specific Amazon EC2 instances. You can develop and test applications in AWS, and then deploy them on Snowball Edge devices, to collect and pre-process data for image analysis or machine learning. You can then ship the data back to AWS for storage and further processing.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS Snowball and AWS Snowball Edge are available in AWS regions worldwide. For a complete list, see the <a href="/about-aws/global-infrastructure/regional-product-services/">AWS Region table</a>. To learn more, visit the following resources:</p>
<ul>
<li><a href="/snowball/">Snowball product page</a></li>
<li><a href="http://docs.aws.amazon.com/snowball/latest/ug/whatissnowball.html">Snowball documentation</a></li>
<li><a href="/snowball-edge/">Snowball Edge product page</a></li>
<li><a href="https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html">Snowball Edge documentation</a></li>
<li><a href="https://console.aws.amazon.com/importexport/home">AWS Console</a><br/> </li>
</ul>
</div>
</div>, <div class="aws-text-box section">
<div class="">
</div>
</div>]<h1 id="Introducing_AWS_Chatbot_(beta):_ChatOps_for_AWS_in_Amazon_Chime_and_Slack_Chat_Rooms"> <a name="Introducing_AWS_Chatbot_(beta):_ChatOps_for_AWS_in_Amazon_Chime_and_Slack_Chat_Rooms"> Introducing AWS Chatbot (beta): ChatOps for AWS in Amazon Chime and Slack Chat Rooms</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Chatbot is a new service that makes it easy to set up ChatOps for AWS in your <a href="/chime/">Amazon Chime</a> or <a href="https://slack.com/" target="_blank">Slack</a> chat rooms. AWS Chatbot provides an interactive agent that enables you to monitor and interact with your AWS resources from team chat rooms. You can receive alerts and execute commands to return diagnostic information so your team can collaborate and respond to events faster. AWS Chatbot is in beta with support for receiving notifications in your chat room.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To get started with AWS Chatbot, go to the console, perform an authorization with Slack or Amazon Chime, and add AWS Chatbot to your chat room. The launch announcement <a href="/blogs/devops/introducing-aws-chatbot-chatops-for-aws/" target="_blank">blog post</a> provides a step-by-step guide to help you set up AWS Chatbot. Please visit the <a href="/chatbot/">AWS Chatbot homepage</a> to learn more.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS Chatbot is available at no additional charge. You pay for only the underlying AWS resources needed to run you applications. You can use AWS Chatbot in any public AWS Region.</p>
</div>
</div>]<h1 id="Introducing_Predictive_Maintenance_Using_Machine_Learning"> <a name="Introducing_Predictive_Maintenance_Using_Machine_Learning"> Introducing Predictive Maintenance Using Machine Learning</a> </h1>[<div class="aws-text-box">
<div class="">
<p><a href="/solutions/predictive-maintenance-using-machine-learning/" target="_blank">Predictive Maintenance Using Machine Learning</a> is a solution that automates the detection of potential equipment failures, and provides recommended actions to take. The solution is easy to deploy and contains an example dataset of a <a href="https://data.nasa.gov/dataset/Turbofan-engine-degradation-simulation-data-set/vrks-gjie" target="_blank">turbofan degradation simulation</a> from NASA. But, you can modify the solution to use your own dataset.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>The solution deploys <a href="/sagemaker/" target="_blank">Amazon SageMaker</a>, <a href="/lambda/" target="_blank">AWS Lambda</a>, <a href="/s3/" target="_blank">Amazon S3</a>, and <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html" target="_blank">Amazon CloudWatch Events</a>. To learn more about Predictive Maintenance Using Machine Learning, see the <a href="/solutions/predictive-maintenance-using-machine-learning/" target="_blank">solution webpage</a>.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p> Additional AWS Solutions offerings are available on the <a href="/solutions/" target="_blank">AWS Solutions webpage</a>, where customers can browse solutions by product category or industry to find AWS-vetted, automated, turnkey reference implementations that address specific business needs.</p>
</div>
</div>]<h1 id="AWS_Budgets_Announces_AWS_Chatbot_Integration_"> <a name="AWS_Budgets_Announces_AWS_Chatbot_Integration_"> AWS Budgets Announces AWS Chatbot Integration </a> </h1>[<div class="aws-text-box">
<div class="">
<p>Starting today, you can leverage AWS Budgets’ integration with the newly released AWS Chatbot service to receive AWS Budgets alerts via Slack and Amazon Chime. To enable AWS Chatbot integration, simply configure an Amazon Simple Notification Service (Amazon SNS) topic during the budget alert creation process. From there, navigate to the AWS Chatbot console and map your Amazon SNS topic to the appropriate Slack channel or Chime room. Once configured, your AWS Budgets alerts will be sent directly to the Slack channel or Chime room of your choice.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Please note that all AWS Budgets functionality can be accessed programmatically via the <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Operations_AWS_Budgets.html" target="_blank">AWS Budgets API</a>.</p>
<p>To get started using this feature, refer to the <a href="https://aws.amazon.com/chatbot/" target="_blank">AWS Chatbot</a> webpage. To learn about setting budgets, refer to the <a href="https://aws.amazon.com/aws-cost-management/aws-budgets/" target="_blank">AWS Budgets</a> webpage or the <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/sns-alert-chime.html" target="_blank">Receiving Budget Alerts in Amazon Chime and Slack</a> section of the <i>Managing Your Costs With Budgets</i> user guide.</p>
<p> </p>
</div>
</div>]<h1 id="AWS_RoboMaker_Expands_to_the_EU_(Frankfurt),_Asia_Pacific_(Singapore),_US_East_(Ohio)_Regions"> <a name="AWS_RoboMaker_Expands_to_the_EU_(Frankfurt),_Asia_Pacific_(Singapore),_US_East_(Ohio)_Regions"> AWS RoboMaker Expands to the EU (Frankfurt), Asia Pacific (Singapore), US East (Ohio) Regions</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS RoboMaker, a service that makes it easy to develop, simulate, and deploy intelligent robotics applications at scale, is now available in the EU (Frankfurt), Asia Pacific (Singapore), US East (Ohio) regions. With these additions, RoboMaker is now available in <a href="/about-aws/global-infrastructure/regional-product-services/">seven regions globally</a>.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS RoboMaker extends the most widely used open-source robotics software framework, Robot Operating System (ROS), with connectivity to cloud services. RoboMaker provides a robotics development environment for application development, a robotics simulation service to accelerate application testing, and a robotics fleet management service for remote application deployment, update, and management. Features include AWS machine learning services, monitoring services, and analytics services that enable a robot to stream data, navigate, communicate, comprehend, and learn. To get started, one can explore the <a href="/robomaker/">RoboMaker webpage</a> or run a sample simulation job in the <a href="http://console.aws.amazon.com/robomaker">RoboMaker console</a>. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>The regional expansion furthers our customers' ability to build highly-available robotic applications, simulations and deployments. The pricing for the new region can be found on the <a href="/robomaker/pricing/">AWS RoboMaker pricing page</a>. </p>
</div>
</div>]<h1 id="New_AWS_Certification_Exam_Vouchers_Make_Certifying_Groups_Easier"> <a name="New_AWS_Certification_Exam_Vouchers_Make_Certifying_Groups_Easier"> New AWS Certification Exam Vouchers Make Certifying Groups Easier</a> </h1>[<div class="aws-text-box">
<div class="">
<p>It’s now easier than ever for organizations to develop and validate their teams’ skills by providing them with <a href="https://aws.amazon.com/certification/bulk-voucher/" target="_blank">AWS Certification exam vouchers</a>. These vouchers conveniently eliminate the need for candidates to pay when registering for their exam.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Exam vouchers are easy to purchase. Buy anytime online in any quantity from Xvoucher, an authorized AWS Training and Certification distributor. Pay with a credit card, wire/PO, or prepaid funds, which allows you to commit your training budget and draw upon it when you need it. Efficiently distribute and track exam vouchers in one centralized place online and eliminate manual tracking. Enjoy the flexibility of purchasing exam vouchers by exam level, as well as the option to choose vouchers for use at Pearson VUE or PSI testing centers. You may also let candidates decide the exam delivery provider. Candidates have 12 months from purchase to sit for their exam. <br/> <br/> Learn more about <a href="https://aws.amazon.com/certification/bulk-voucher/" target="_blank">AWS Certification exam vouchers</a> today!</p>
</div>
</div>]<h1 id="Amazon_SNS_Adds_Support_for_AWS_X-Ray"> <a name="Amazon_SNS_Adds_Support_for_AWS_X-Ray"> Amazon SNS Adds Support for AWS X-Ray</a> </h1>[<div class="aws-text-box">
<div class="">
<p>You can now enable AWS X-Ray for your messages passing through Amazon SNS, making it easier to trace and analyze messages as they travel through to the downstream services. AWS X-Ray provides more insights to developers troubleshooting performance issues and errors for their distributed applications and microservices. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>With support of AWS X-Ray, you can see the map view of connections between Amazon SNS and other services used by your application from the AWS X-Ray console. You can gain visibility into metrics such as average latency and failure rates. For example, you can now trace messages published to a SNS topic for distribution to Amazon SQS queues or AWS Lambda functions.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Amazon SNS support for AWS X-Ray trace is available in all AWS X-Ray <a href="/about-aws/global-infrastructure/regional-product-services/">regions</a>.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p><a href="/sns/">Amazon SNS</a> is a simple, reliable, scalable, and fully managed pub/sub and mobile messaging service. With Amazon SNS, you can use topics to simultaneously distribute messages to multiple subscribing endpoints such as mobile devices (SMS and push notifications), email addresses, Amazon SQS queues, AWS Lambda functions and HTTP webhooks.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more see:</p>
<ul>
<li> Amazon SNS and AWS X-Ray in the <a href="https://docs.aws.amazon.com/xray/latest/devguide/xray-services-sns.html">Amazon X-Ray Developer Guide.</a><br/> </li>
</ul>
</div>
</div>]<h1 id="AWS_Well-Architected_Tool_is_now_available_in_AWS_Europe_(London)_region"> <a name="AWS_Well-Architected_Tool_is_now_available_in_AWS_Europe_(London)_region"> AWS Well-Architected Tool is now available in AWS Europe (London) region</a> </h1>[<div class="aws-text-box">
<div class="">
<p>The AWS Well-Architected Tool is now available in AWS Europe (London) region. The AWS Well-Architected Tool helps you review your workloads against the latest AWS architectural best practices, and get guidance on how to improve your cloud architectures.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p> With this regional expansion, the tool is available in US East (N. Virginia, Ohio), US West (Oregon), Europe (Ireland), Europe (London), and Asia Pacific (Sydney) Regions.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To get started, visit the <a href="https://console.aws.amazon.com/">AWS Management Console</a>. To learn more, visit the <a href="https://docs.aws.amazon.com/wellarchitected/index.html">Documentation</a> and the <a href="/well-architected-tool/">Product page</a>.</p>
</div>
</div>]<h1 id="Amazon_FSx_for_Windows_File_Server_is_Now_Available_in_the_US_West_(N._California)_Region"> <a name="Amazon_FSx_for_Windows_File_Server_is_Now_Available_in_the_US_West_(N._California)_Region"> Amazon FSx for Windows File Server is Now Available in the US West (N. California) Region</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon FSx for Windows File Server is now available in the AWS US West (N. California) Region.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Amazon FSx for Windows File Server provides a fully managed native Microsoft Windows file system so you can easily move your Windows-based applications that require shared file storage to AWS. Built on Windows Server, Amazon FSx natively supports the SMB protocol, Windows NTFS, and Active Directory (AD). To meet a broad spectrum of needs, Amazon FSx delivers high levels of throughput and IOPs, and provides consistent sub-millisecond latencies.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>For more information, please visit the <a href="/fsx/windows/" target="_blank">Amazon FSx for Windows File Server</a> product page, and see the <a href="/about-aws/global-infrastructure/regional-product-services/" target="_blank">AWS Region Table</a> for complete regional availability information.</p>
</div>
</div>]<h1 id="Amazon_FSx_for_Lustre_is_Now_Available_in_the_US_West_(N._California)_Region"> <a name="Amazon_FSx_for_Lustre_is_Now_Available_in_the_US_West_(N._California)_Region"> Amazon FSx for Lustre is Now Available in the US West (N. California) Region</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon FSx for Lustre is now available in the AWS US West (N. California) Region. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Amazon FSx for Lustre provides a high-performance file system optimized for fast processing of workloads such as machine learning, high performance computing (HPC), video processing, financial modeling, and electronic design automation (EDA). Amazon FSx for Lustre file systems can be configured as standalone file systems or can be linked to an Amazon S3 bucket. When linked to an S3 bucket, an FSx for Lustre file system transparently presents S3 objects as files and allows you to write results back to S3, making it easy for you to process cloud data sets on S3 using a high-performance file system. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>For more information, please visit the <a href="/fsx/lustre/" target="_blank">Amazon FSx for Lustre</a> product page, and see the <a href="/about-aws/global-infrastructure/regional-product-services/" target="_blank">AWS Region Table</a> for complete regional availability information.</p>
</div>
</div>]<h1 id="AWS_Client_VPN_now_adds_support_for_Split-tunnel"> <a name="AWS_Client_VPN_now_adds_support_for_Split-tunnel"> AWS Client VPN now adds support for Split-tunnel</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Client VPN now supports split-tunnel, which gives customers the flexibility to cherry pick the traffic that traverses over the VPN tunnel.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>From their on-premises network, employees often access both AWS and on-premises resources. With a full-tunnel, the traffic irrespective of the destination is always sent over the VPN tunnel. If the destination resource is in the network on premises, the traffic is routed over the VPN tunnel to AWS and then back to the premises. This is an unnecessary hairpin from the premises, to AWS, and back to the network on premises.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Split-tunnel provides customers the ability to configure which traffic gets routed over the VPN tunnel. With split-tunnel, customers can optimize the routing of traffic from the client, by having only the AWS destined traffic traverse the VPN tunnel. By optimizing the traffic, customers also reduce the volume of egress traffic from AWS, therefore reducing the data transfer cost.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>For more information on split-tunnel, refer to the AWS Client VPN product page. To learn on how to use split-tunnel on AWS Client VPN endpoints, refer to the AWS Client VPN User Guide. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS Client VPN provides customers with the ability to securely access their AWS and on-premises networks from anywhere, on any device using OpenVPN-based clients. AWS Client VPN is available in US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), EU (London), Asia Pacific (Sydney), Asia Pacific (Singapore), Asia Pacific (Mumbai) and Asia Pacific (Tokyo). </p>
</div>
</div>]<h1 id="AWS_Certificate_Manager_Private_Certificate_Authority_is_now_available_in_the_Asia_Pacific_(Hong_Kong)_Region"> <a name="AWS_Certificate_Manager_Private_Certificate_Authority_is_now_available_in_the_Asia_Pacific_(Hong_Kong)_Region"> AWS Certificate Manager Private Certificate Authority is now available in the Asia Pacific (Hong Kong) Region</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Certificate Manager (ACM) Private Certificate Authority (CA) is now available in the Asia Pacific (Hong Kong) region. This regional expansion extends the global availability of ACM Private CA, increasing the number of regions to 18.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>ACM Private CA is a managed private CA service that helps you easily and securely manage the lifecycle of your private certificates. ACM Private CA provides you a highly-available private CA service without the upfront investment and ongoing maintenance costs of operating your own private CA. CA administrators can create a complete CA hierarchy, including online root and subordinate CAs, with no need for external CAs. ACM Private CA extends ACM’s certificate management capabilities to private certificates, enabling you to manage public and private certificates centrally. <br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>For a list of regions where ACM Private CA is available, see <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html">AWS Regions and Endpoints</a>. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To get started, first time ACM Private CA customers can try the service for 30 days with no charge for the operation of their first CA. Visit the <a href="/certificate-manager/private-certificate-authority/">ACM Private CA website</a> to learn more about ACM Private CA. </p>
</div>
</div>]<h1 id="Amazon_EC2_Now_Supports_Tagging_Launch_Templates_on_Creation"> <a name="Amazon_EC2_Now_Supports_Tagging_Launch_Templates_on_Creation"> Amazon EC2 Now Supports Tagging Launch Templates on Creation</a> </h1>[<div class="aws-text-box">
<div class="">
<p>You can now tag launch templates at the time they are created, eliminating the need to run custom tagging scripts after creation. In addition, you can now set resource-level permissions on the <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html">CreateLaunchTemplate</a> API, allowing you to implement stronger security policies by giving more granular control over who has access to that API. Resource-level permissions and tagging your launch templates on creation simplifies management and ensures that your launch templates are secured upon creation.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Launch templates templatize EC2 instance launch requests in order to streamline and simplify the instance launch process. They can be used for On-Demand instance launches as well as with EC2 Auto Scaling, EC2 Fleet, AWS Batch, and AWS CloudFormation. When used as an authorization vehicle, launch templates simplify IAM policies and ensure that organizational best practices are used for every instance launch. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Launch templates are available in all AWS regions. You can manage resource tags for your launch templates using the console, CLI, or SDK. To learn more, read the <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#create-launch-template">launch templates documentation</a>.</p>
</div>
</div>]<h1 id="Now_use_AWS_Systems_Manager_Maintenance_Windows_to_select_resource_groups_as_targets"> <a name="Now_use_AWS_Systems_Manager_Maintenance_Windows_to_select_resource_groups_as_targets"> Now use AWS Systems Manager Maintenance Windows to select resource groups as targets</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Systems Manager Maintenance Windows enable you to define a time window for performing potentially disruptive actions on your instances. You can now use maintenance windows to select a resource group as the target. Resource groups make it easier to organize, manage, and automate tasks on large numbers of resources at one time. By selecting a resource group as the target of a maintenance window, you can perform routine tasks across different resources such as Amazon Elastic Compute Cloud (Amazon EC2) instances, Amazon Elastic Block Store (Amazon EBS) volumes, and Amazon Simple Storage Service (Amazon S3) buckets within the same recurring time window.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Previously, targets for maintenance windows were limited to Amazon EC2 instances, which were selected manually or through tags. With the support of resource groups, the targets can be any resource <a href="https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html#supported-resources-console" target="_blank">supported by AWS Resource Groups</a>. For example, by selecting a resource group that represents your application as the target, you can schedule a Systems Manager Automation task to back up the application EBS volumes, and then run a Systems Manager RunCommand task to patch the EC2 instances that host the application within the same maintenance window. You can also execute an AWS Lambda function or AWS Step Functions task that targets the resources belonging to the resource group. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Maintenance Windows is a feature of Systems Manager. Systems Manager enables visibility and control of your cloud and on-premises infrastructure. It simplifies resource and application management, shortens the time to detect and resolve operational problems, and makes it easier to operate and manage your infrastructure securely at scale. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>This feature is available in all AWS Regions where AWS Resource Groups is available. For more details about this feature, see our <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html" target="_blank">Documentation</a>. To learn more about AWS Systems Manager Maintenance Windows, visit our <a href="https://aws.amazon.com/systems-manager/features/" target="_blank">Product Page</a>. </p>
</div>
</div>]<h1 id="Configuration_update_for_Amazon_EFS_encryption_of_data_in_transit"> <a name="Configuration_update_for_Amazon_EFS_encryption_of_data_in_transit"> Configuration update for Amazon EFS encryption of data in transit</a> </h1>[<div class="aws-text-box">
<div class="">
<p>We’ve updated the default configuration for the <a href="/efs/">Amazon Elastic File System (Amazon EFS)</a> mount helper package when using encryption of data in transit. Starting today, use of the Online Certificate Status Protocol (OCSP) is not enabled by default. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>The Amazon EFS mount helper provides the option to encrypt data in transit for EFS file systems using Transport Layer Security version 1.2 (TLS v1.2). EFS uses an <a href="https://www.amazontrust.com/">Amazon certificate authority</a> (CA) to issue and sign its TLS certificates, as well as to check for certificate revocation using OCSP. The OCSP endpoint must be accessible over the Internet from your Virtual Private Cloud (VPC) in order to check for certificate revocation. To maximize file system availability in the event that the CA is not reachable from your VPC, the EFS mount helper no longer enables OCSP by default. Within the service, EFS continuously monitors for certificate revocation status and will issue new certificates if a revoked certificate is detected. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>You can still choose to enable OCSP to have your clients check for revoked certificates, providing the strongest possible security. OCSP protects against malicious use of revoked certificates, which is unlikely to occur within your VPC. In the event that an EFS TLS certificate is revoked, Amazon will publish a <a href="/security/security-bulletins/">security bulletin</a> and make a new version of the EFS mount helper available that explicitly rejects the revoked certificate.  This will require you to update the EFS mount helper manually.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>The updated EFS mount helper is available within <a href="/amazon-linux-ami/">Amazon Linux</a> and <a href="/amazon-linux-2/">Amazon Linux 2</a> AMIs, and can also be found on <a href="https://github.com/aws/efs-utils">GitHub</a>. To get started with the Amazon EFS mount helper and EFS encryption of data in transit, see the <a href="https://docs.aws.amazon.com/efs/latest/ug/encryption.html#encryption-in-transit">documentation</a>.<a href="/amazon-linux-2/"></a></p>
</div>
</div>]<h1 id="Introducing_Amazon_EC2_Resource_Optimization_Recommendations_"> <a name="Introducing_Amazon_EC2_Resource_Optimization_Recommendations_"> Introducing Amazon EC2 Resource Optimization Recommendations </a> </h1>[<div class="aws-text-box">
<div class="">
<p>Starting today, you can access custom-generated Amazon EC2 resource optimization recommendations in AWS Cost Explorer. These recommendations identify idle and underutilized instances across your accounts and regions. To generate these recommendations, AWS analyzes your historical EC2 resource usage, your Amazon CloudWatch metrics, and your existing reservation footprint to identify opportunities for cost savings (e.g., by terminating idle instances or downsizing active instances to lower-cost options). For example, if your m5.2xlarge has a maximum utilization of 20% over the last 14 days, AWS may recommended downsizing that instance to m5.xlarge or m5.large and show you how much you can save based on your usage and your applicable m5 family reservations.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To get started, just click on the Recommendations summary link on the AWS Cost Explorer sidebar to view your resource- and reservation-related recommendations. From the Resource Optimization page, you can dive deeper into your individual resource recommendations, download them in CSV form, and take action accordingly.<br/> </p>
<p>To learn more about getting started with Amazon EC2 resource optimization recommendations, please visit this <a href="https://aws.amazon.com/blogs/aws-cost-management/launch-resource-optimization-recommendations/" target="_blank">blog post</a> or the <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-rightsizing.html" target="_blank">Optimizing your Costs with Rightsizing Recommendations</a> user guide.</p>
<p> </p>
</div>
</div>]<h1 id="AWS_Backup_will_Automatically_Copy_Tags_from_Resource_to_Recovery_Point"> <a name="AWS_Backup_will_Automatically_Copy_Tags_from_Resource_to_Recovery_Point"> AWS Backup will Automatically Copy Tags from Resource to Recovery Point</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Backup now provides customers a more seamless way to manage their backups, by automatically copying tags from their resources to their backups. For customers using tags to manage their AWS resources, AWS Backup will enable them to more effectively search for source resources or conduct billing for their backups. See <a href="/answers/account-management/aws-tagging-strategies/">AWS Tagging Strategies</a> for tagging best practices.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p><a href="/backup/">AWS Backup</a> offers a centralized, managed service to back up data across AWS services in the cloud as well as on premises using Storage Gateway. AWS Backup serves as a single dashboard for backup, restore, and policy-based retention of different AWS resources, including Amazon EBS volumes, Amazon RDS databases, Amazon DynamoDB tables, Amazon EFS file systems, and AWS Storage Gateway volumes.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more about AWS Backup, please see our <a href="/backup/">product page</a> and <a href="https://docs.aws.amazon.com/aws-backup/">documentation</a>.</p>
</div>
</div>]<h1 class="aws-orange" id="AWS_Elemental_MediaConvert_Expands_Audio_Support_and_Improves_Performance"> <a name="AWS_Elemental_MediaConvert_Expands_Audio_Support_and_Improves_Performance"> AWS Elemental MediaConvert Expands Audio Support and Improves Performance</a> </h1>[<div class="aws-text-box">
<div class="">
<p><a href="https://aws.amazon.com/mediaconvert/">AWS Elemental MediaConvert</a> has expanded support for audio formats and improved overall transcode performance. With new audio-only outputs for HLS, AAC with MP4, and WAV with PCM, you have more options for delivering audio-only content to users for music, podcasting, radio, audio books, and more. In addition, MediaConvert has significantly improved performance for non-accelerated jobs, reducing the time required for creating VOD assets so you can make your media available to end users even faster and start monetizing new content sooner.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Using AWS Elemental MediaConvert, video providers with any size content library can easily and reliably transcode on-demand content for broadcast and multiscreen delivery. MediaConvert functions independently or as part of <a href="https://aws.amazon.com/media-services/">AWS Elemental Media Services</a>, a family of services that form the foundation of cloud-based workflows and offer the capabilities needed to transport, transcode, package, and deliver video.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Visit the <a href="https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/" target="_blank">AWS region table</a> for a full list of AWS Regions where AWS Elemental MediaConvert is available. To learn more about MediaConvert, please visit <a href="https://aws.amazon.com/mediaconvert/">https://aws.amazon.com/mediaconvert/</a>.</p>
</div>
</div>]<h1 id="Amazon_EC2_P3_Instances_Featuring_NVIDIA_Volta_V100_GPUs_now_Support_NVIDIA_Quadro_Virtual_Workstation"> <a name="Amazon_EC2_P3_Instances_Featuring_NVIDIA_Volta_V100_GPUs_now_Support_NVIDIA_Quadro_Virtual_Workstation"> Amazon EC2 P3 Instances Featuring NVIDIA Volta V100 GPUs now Support NVIDIA Quadro Virtual Workstation</a> </h1>[<div class="aws-text-box">
<div class="">
<p> Customers can now use Amazon EC2 P3 and P3dn instances for graphics applications such as remote workstations and 3D visualization using NVIDIA Quadro Virtual Workstation software made available using new Amazon Machine Images (AMIs) accessible on the AWS Marketplace.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>As more and more customers migrate graphics intensive workloads to the cloud to take advantage of increased agility and ease of management, they also continually look for increased compute power to support complex use cases. NVIDIA Quadro Virtual Workstation AMIs deliver high graphics performance using the powerful NVIDIA Volta V100 GPUs running in the AWS cloud. These AMIs have the latest NVIDIA GPU graphics software preinstalled along with the latest Quadro drivers and Quadro ISV certifications with support for up to four 4K desktop resolutions and 8K video encoding capabilities. NVIDIA V100 combined with Quadro vWS delivers fast ray tracing, advanced simulations, and AI-powered rendering. Also look for our upcoming release of EC2 G4 instances featuring NVIDIA T4 GPUs which leverage the NVIDIA Turing architecture and RTX platform enhancements, enabling support for real-time photorealistic rendering and AI-enhanced graphics, video and image processing from the cloud.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>The new AMIs are available on the AWS Marketplace with support for Windows Server:</p>
<ul>
<li>NVIDIA Quadro Virtual Workstation - WinServer 2016 - <a href="https://aws.amazon.com/marketplace/pp/B07TV59ZQK" target="_blank">https://aws.amazon.com/marketplace/pp/B07TV59ZQK</a></li>
<li>NVIDIA Quadro Virtual Workstation - WinServer 2019 - <a href="https://aws.amazon.com/marketplace/pp/B07TS3S3ZH" target="_blank">https://aws.amazon.com/marketplace/pp/B07TS3S3ZH</a></li>
</ul>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p> To learn more about EC2 P3 and P3dn instances, visit the <a href="https://aws.amazon.com/ec2/instance-types/p3/" target="_blank">P3 product page</a>.</p>
</div>
</div>]<h1 id="Amazon_MQ_Adds_Support_for_AWS_Key_Management_Service_(AWS_KMS),_Improving_Encryption_Capabilities"> <a name="Amazon_MQ_Adds_Support_for_AWS_Key_Management_Service_(AWS_KMS),_Improving_Encryption_Capabilities"> Amazon MQ Adds Support for AWS Key Management Service (AWS KMS), Improving Encryption Capabilities</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon MQ now supports the AWS Key Management Service (AWS KMS) to create and manage keys for at-rest encryption of customer data in Amazon MQ. Amazon MQ handles the encryption and decryption seamlessly, so you don’t have to change your applications to access your data. When you create a broker, you can now select the KMS key used to encrypt your data from the following three options: a KMS key in the Amazon MQ service account, a KMS key in your account that Amazon MQ creates and manages, or a KMS key in your account that you create and manage. In addition to encryption at rest, all data transferred between Amazon MQ and client applications is securely transmitted using TLS/SSL. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p><a href="/amazon-mq/">Amazon MQ</a> is a managed message broker service for Apache ActiveMQ that makes it easy to set up and operate message brokers in the cloud. Message brokers allow different software systems–often using different programming languages, and on different platforms–to communicate and exchange information. With Amazon MQ, you can use industry standard APIs and protocols for messaging, including JMS, NMS, AMQP, STOMP, MQTT, and WebSocket. You can easily move from any message broker that uses these standards to Amazon MQ because you don’t have to rewrite any messaging code in your applications.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>KMS support is available in all AWS regions where <a href="/about-aws/global-infrastructure/regional-product-services/">Amazon MQ is available</a>. To learn more see <a href="https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-encryption.html">Amazon MQ Encryption</a> in the Amazon MQ Developer Guide.</p>
</div>
</div>]<h1 id="Introducing_AI-Driven_Social_Media_Dashboard"> <a name="Introducing_AI-Driven_Social_Media_Dashboard"> Introducing AI-Driven Social Media Dashboard</a> </h1>[<div class="aws-text-box">
<div class="">
<p><a href="/solutions/ai-driven-social-media-dashboard/" target="_blank">AI-Driven Social Media Dashboard</a> is a solution that monitors and ingests specified tweets using stream processing and leverages a serverless architecture and machine learning services to translate and extract insights from those tweets. The solution is easy to deploy and contains a data lake you can use to quickly and easily perform additional analytics on tweet data.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>The solution uses <a href="/ec2/" target="_blank">Amazon EC2</a>, <a href="/vpc/" target="_blank">Amazon VPC</a>, <a href="/kinesis/data-firehose/" target="_blank">Amazon Kinesis Data Firehose</a>, <a href="/s3/" target="_blank">Amazon S3</a>, <a href="/lambda/" target="_blank">AWS Lambda</a>, <a href="/translate/" target="_blank">Amazon Translate</a>, <a href="/comprehend/" target="_blank">Amazon Comprehend</a>, <a href="/glue/" target="_blank">AWS Glue</a>, <a href="/athena/" target="_blank">Amazon Athena</a>, and <a href="/quicksight/" target="_blank">Amazon QuickSight</a>. To learn more about the AI-Driven Social Media Dashboard solution, see the <a href="/solutions/ai-driven-social-media-dashboard/" target="_blank">solution webpage</a>.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Additional AWS Solutions offerings are available on the <a href="/solutions/" target="_blank">AWS Solutions webpage</a>, where customers can browse solutions by product category or industry to find AWS-vetted, automated, turnkey reference implementations that address specific business needs.<a href="/solutions/" target="_blank"></a></p>
</div>
</div>]<h1 id="AWS_Systems_Manager_Distributor_makes_it_easier_to_create_distributable_software_packages"> <a name="AWS_Systems_Manager_Distributor_makes_it_easier_to_create_distributable_software_packages"> AWS Systems Manager Distributor makes it easier to create distributable software packages</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Systems Manager Distributor provides simplified package creation, enabling you to deploy your software packages across instances quickly. Distributor will package your installers so they can be easily used to install and update your software across multiple operating systems.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>With Distributor, you can securely store and manage software packages, such as software agents, from a centralized, version-controlled repository. With the simplified package creation experience, you select the installable files you want, and Distributor automates creating installation and uninstallation scripts, uploading the installable files, and zipping everything into a package. These packages can then be shared across AWS accounts and distributed to instances on demand or on a schedule. You can also report on compliance of your software distribution from the Systems Manager compliance dashboard. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Distributor is a feature in Systems Manager. Systems Manager enables visibility and control of your cloud and on-premise infrastructure. It simplifies resource and application management, shortens the time to detect and resolve operational problems, and makes it easier to operate and manage your infrastructure securely at scale.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>The AWS Systems Manager Distributor feature is available in <a href="https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/" target="_blank">all GovCloud (US) and commercial Regions</a> (excluding China Regions). This feature is priced on a pay-per-use model. See the AWS Systems Manager <a href="https://aws.amazon.com/systems-manager/pricing/" target="_blank">Pricing page</a> for details.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>For more information about Distributor, visit the AWS Systems Manager <a href="https://aws.amazon.com/systems-manager/features/" target="_blank">Product page</a> and <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html" target="_blank">Documentation</a>.  </p>
</div>
</div>]<h1 id="AWS_Direct_Connect_support_for_AWS_Transit_Gateway_is_Now_Available_in_AWS_EU_(Ireland)_region"> <a name="AWS_Direct_Connect_support_for_AWS_Transit_Gateway_is_Now_Available_in_AWS_EU_(Ireland)_region"> AWS Direct Connect support for AWS Transit Gateway is Now Available in AWS EU (Ireland) region</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Direct Connect support for AWS Transit Gateway is now available in AWS EU (Ireland) region. With this feature, customers can connect thousands of Amazon Virtual Private Clouds (Amazon VPCs) in multiple AWS Regions to their on-premises networks using 1/2/5/10 Gbps AWS Direct Connect connections.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS Direct Connect gateway allows you to access any AWS Region (except China) using your AWS Direct Connect connections. You can associate up to three Transit Gateways from any AWS Region with each Direct Connect gateway. AWS Direct Connect is introducing a new type of virtual interface called the transit virtual interface to support connectivity to AWS Transit Gateway. You can create a transit virtual interface using your 1/2/5/10 Gbps AWS Direct Connect connections at any AWS Direct Connect locations, with the exception of AWS Direct Connect locations in China. To increase the resiliency of your connectivity, we recommend that you attach at least two transit virtual interfaces from different AWS Direct Connect locations, to the Direct Connect gateway. For more information, please refer to the AWS Direct Connect resiliency <a href="/directconnect/resiliency-recommendation/">recommendation</a>.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>With this announcement, AWS Direct Connect support for AWS Transit Gateway is now available in a total of eight AWS Regions. Support for other AWS Regions is coming soon. For more information about AWS Direct Connect support for AWS Transit Gateway, please read the <a href="https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html">user guide</a>. </p>
</div>
</div>]<h1 id="Amazon_ECS_Console_now_enables_simplified_AWS_App_Mesh_integration"> <a name="Amazon_ECS_Console_now_enables_simplified_AWS_App_Mesh_integration"> Amazon ECS Console now enables simplified AWS App Mesh integration</a> </h1>[<div class="aws-text-box">
<div class="">
<p>When creating or updating an ECS task definition in the ECS console, you now have the ability to add the task to a mesh in AWS App Mesh. AWS App Mesh is a service mesh that provides application-level networking to make it easy for your services to communicate with each other across multiple types of compute infrastructure.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>App Mesh uses the open-source Envoy proxy as a sidecar container for service-to-service communication. The ECS console can now automatically add the Envoy container to your task definition, set up the proxy configuration parameters, add the Envoy container to your mesh, and configure container startup ordering for you. <br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>The simplified App Mesh integration in the ECS console is available in <a href="/about-aws/global-infrastructure/regional-product-services/">all regions where ECS and App Mesh are available</a>. To get started with App Mesh and ECS, visit our <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/mesh-gs-ecs.html">documentation</a>.<br/> </p>
</div>
</div>]<h1 id="AWS_IoT_Device_Tester_v1.3.0_is_Now_Available_for_Amazon_FreeRTOS_201906.00_Major"> <a name="AWS_IoT_Device_Tester_v1.3.0_is_Now_Available_for_Amazon_FreeRTOS_201906.00_Major"> AWS IoT Device Tester v1.3.0 is Now Available for Amazon FreeRTOS 201906.00 Major</a> </h1>[<div class="aws-text-box">
<div class="">
<p><a href="https://aws.amazon.com/freertos/device-tester/" target="_blank">AWS IoT Device Tester,</a> a Windows/Linux/Mac test automation tool for connected devices, is now available for <a href="https://aws.amazon.com/about-aws/whats-new/2019/06/bluetooth-low-energy-support-amazon-freertos-now-available/" target="_blank">Amazon FreeRTOS 201906.00 Major.</a></p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>You can use AWS IoT Device Tester to easily determine if your microcontroller based devices running Amazon FreeRTOS can be authenticated by and interoperate with AWS IoT. AWS IoT Device Tester runs end-to-end tests with AWS IoT Core to give you confidence that your devices meet the security and functional requirements to interoperate with AWS IoT services. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS IoT Device Tester is required to qualify as part of the <a href="https://aws.amazon.com/partners/dqp/" target="_blank">AWS Device Qualification Program</a>. Qualified devices are listed in the <a href="https://devices.amazonaws.com/" target="_blank">AWS Partner Device Catalog</a>. You can learn more about AWS IoT Device Tester for Amazon FreeRTOS <a href="https://aws.amazon.com/freertos/device-tester/" target="_blank">here</a>, and download the latest release <a href="https://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html" target="_blank">here</a>.<br/> </p>
</div>
</div>]<h1 id="Amazon_Comprehend_Custom_Entities_now_supports_multiple_entity_types"> <a name="Amazon_Comprehend_Custom_Entities_now_supports_multiple_entity_types"> Amazon Comprehend Custom Entities now supports multiple entity types</a> </h1>[<div class="aws-text-box">
<div class="">
<p><a href="/comprehend/">Amazon Comprehend</a> is a natural language processing (NLP) service that uses machine learning to find insights and relationships in text. With Comprehend’s Custom Entity Recognition API, you can easily build models to extract custom entities (policy numbers, part codes, serial numbers, etc.) that are tailored to your organization’s needs.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Starting today, Amazon Comprehend Custom Entity Recognition supports multiple entity types per model. With multi entity support, you can create a single custom entity recognition model to identify up to twelve entity types. You can now reduce cost and complexity by detecting multiple entity types in your documents using a single detection job. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Amazon Comprehend multi entity type support is now available in all AWS regions where Amazon Comprehend is available. For additional information, please visit the <a href="https://docs.aws.amazon.com/comprehend/latest/dg/custom-entity-recognition.html">documentation</a>.</p>
</div>
</div>]<h1 id="AWS_Device_Farm_improves_device_start_up_time_to_enable_instant_access_to_devices"> <a name="AWS_Device_Farm_improves_device_start_up_time_to_enable_instant_access_to_devices"> AWS Device Farm improves device start up time to enable instant access to devices</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Device Farm is an app testing service that lets you test your Android, iOS, and web apps , on a massive collection of real mobile devices hosted in the AWS Cloud. You can use one of the supported automation test frameworks to parallelly test your app on many devices, or you can use Device Farm’s Remote Access (manual testing) feature to gesture, swipe, and interact, with the device in real time directly from your web browser.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>With today’s launch, Device Farm is reducing the device start up time by 90% so you get instant access to real iOS and Android devices. If you have selected a device that is available, Device Farm will now setup the device for your test within thirty seconds of your request. To ensure you always select an available device, make sure to update your Device Pool to include the *availability* rule.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more about AWS Device Farm see the <a href="https://docs.aws.amazon.com/devicefarm/?id=docs_gateway">documentation</a> or visit the <a href="/device-farm/">product page</a>.</p>
</div>
</div>]<h1 id="Elastic_Fabric_Adapter_is_officially_integrated_into_Libfabric_Library"> <a name="Elastic_Fabric_Adapter_is_officially_integrated_into_Libfabric_Library"> Elastic Fabric Adapter is officially integrated into Libfabric Library</a> </h1>[<div class="aws-text-box">
<div class="">
<p>The <a href="/hpc/efa/">Elastic Fabric Adapter (EFA)</a> provider is officially integrated into the Libfabric 1.8 release. Customers can directly use Libfabric 1.8 without needing to install the EFA provider separately.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>EFA is a network interface for Amazon EC2 instances that enables customers to run applications requiring high levels of inter-node communications at scale on AWS. With EFA, High Performance Computing (HPC) applications using the Message Passing Interface (MPI) and Machine Learning (ML) applications using NVIDIA Collective Communications Library (NCCL) can scale to thousands of CPUs or GPUs.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>The Libfabric library is the preferred interface for accessing the EFA hardware. <a href="https://ofiwg.github.io/libfabric/">Libfabric</a> is a core component of OpenFabrics Interfaces (OFI) and the library that defines and exports the user-space API of OFI. It is typically the only software that applications deal with directly.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more about EFA, please visit <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html">EFA documentation</a>. To launch a HPC cluster with EFA, check out <a href="https://aws.amazon.com/blogs/opensource/scale-hpc-workloads-elastic-fabric-adapter-and-aws-parallelcluster/">here</a>.  </p>
</div>
</div>]<h1 id="SageMaker_Batch_Transform_now_enables_associating_prediction_results_with_input_attributes_"> <a name="SageMaker_Batch_Transform_now_enables_associating_prediction_results_with_input_attributes_"> SageMaker Batch Transform now enables associating prediction results with input attributes </a> </h1>[<div class="aws-text-box">
<div class="">
<p><a href="https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html">Amazon SageMaker Batch Transform</a> enables you to run predictions on datasets stored in <a href="/s3/">Amazon S3</a>. It is ideal for scenarios where you are working with large batches of data and don’t need sub-second latency. You can now configure your Batch Transform Jobs to exclude certain data attributes from prediction requests, and to join some or all of the input data attributes with prediction results. As a result, you no longer need additional pre-processing or post-processing when running batch predictions on data that is in CSV or JSON format.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p> For example, consider a dataset that includes three attributes: ID, age, and height. The ID attribute is a randomly generated or sequential number that carries no signal for the ML problem and was not used when training the ML model. You can now configure your Batch Transform jobs to exclude the ID attribute from each record, and pass only the age and height attributes in the prediction requests sent to the model. You can also configure your Batch Transform jobs to associate the ID attribute with the prediction results in the final S3 output of the job. Retaining record-level attributes in this way can be useful for analyzing the prediction results.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>This new capability is available in <a href="/about-aws/global-infrastructure/regional-product-services/">all regions where Amazon SageMaker is available</a>. To learn more about this feature, see the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html">Amazon SageMaker Developer Guide</a>. </p>
</div>
</div>]<h1 id="Amazon_DocumentDB_(with_MongoDB_compatibility)_is_Now_Available_in_EU_(London)_Region"> <a name="Amazon_DocumentDB_(with_MongoDB_compatibility)_is_Now_Available_in_EU_(London)_Region"> Amazon DocumentDB (with MongoDB compatibility) is Now Available in EU (London) Region</a> </h1>[<div class="aws-text-box">
<div class="">
<p><a href="/documentdb/">Amazon DocumentDB (with MongoDB compatibility)</a> is now available in the EU (London) region. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Amazon DocumentDB is a fast, scalable, highly available, and fully managed document database service that supports MongoDB workloads.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>You can use Amazon DocumentDB in the following AWS regions: US East (N. Virginia, Ohio), US West (Oregon), Europe (Ireland, Frankfurt, London), and Asia Pacific (Sydney, Tokyo, Seoul). For more information on AWS regions and services, please visit the <a href="/about-aws/global-infrastructure/regional-product-services/">AWS global region table</a>.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more about Amazon DocumentDB, please see our <a href="/documentdb/">product page</a> and <a href="https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html">documentation</a>.</p>
</div>
</div>]<h1 id="Amazon_ECR_now_supports_increased_repository_and_image_limits"> <a name="Amazon_ECR_now_supports_increased_repository_and_image_limits"> Amazon ECR now supports increased repository and image limits</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon Elastic Container Registry (ECR) now supports increased number of repositories per region and images per repository. Previously, the default limit was 1,000 repositories per region and 1,000 images per repository, and required an extra step to increase limits. Now, the default limit has been increased to 10,000 repositories per region and 10,000 images per repository to better align with your requirements and growth.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Getting started is easy. The new limit increases are available in all ECR supported regions, and are already applied to current repositories. To see where ECR is available, please visit the <a href="/about-aws/global-infrastructure/regional-product-services/">AWS region table</a> and more information on default ECR service limits can be found in our documentation. You can learn more about storing, managing and deploying Docker container images with Amazon ECR, including how to get started, from our <a href="/ecr/">product page</a> and <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html">User Guide</a>.</p>
</div>
</div>]<h1 id="Amazon_Inspector_is_now_available_in_the_Europe_(Stockholm)_Region"> <a name="Amazon_Inspector_is_now_available_in_the_Europe_(Stockholm)_Region"> Amazon Inspector is now available in the Europe (Stockholm) Region</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Starting today, Amazon Inspector is available to customers in the Europe (Stockholm) region. With the addition of this region, Inspector is available in US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), EU (Frankfurt), EU (Ireland), EU (London), EU (Stockholm), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Sydney), Asia Pacific (Tokyo), AWS GovCloud (US-West), and AWS GovCloud (US-East).  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Amazon Inspector is an on-demand security assessment service that helps AWS customers validate the security configurations of the applications and operating systems deployed in their Amazon EC2 environments. Inspector security assessments can also help customers check for unintended network accessibility of EC2 instances. Inspector gives customers the flexibility to check EC2 instances for vulnerabilities and evaluate their instance configurations against security benchmarks any time they need. Inspector offers rules packages that allow customers to choose the type of security assessment they wish to run and provides a detailed evaluation of the findings along with recommendations to improve the security of their instances.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more about Amazon Inspector or to start your free trial, please visit <a href="/inspector/">Amazon Inspector</a>. See the <a href="/about-aws/global-infrastructure/regional-product-services/">AWS Region Table</a> for the list of regions where Amazon Inspector is currently available.</p>
</div>
</div>]<h1 id="AWS_CodePipeline_Achieves_HIPAA_Eligibility"> <a name="AWS_CodePipeline_Achieves_HIPAA_Eligibility"> AWS CodePipeline Achieves HIPAA Eligibility</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS CodePipeline is now a <a href="/compliance/hipaa-eligible-services-reference/" target="_blank">HIPAA Eligible Service</a>. If you have a HIPAA Business Associate Addendum (BAA) in place with AWS, you can now start using AWS CodePipeline for your HIPAA eligible workloads. If you do not have a BAA in place with AWS or have any other questions about running HIPAA-regulated workloads on AWS, please <a href="/compliance/contact/" target="_blank">contact us</a>.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>HIPAA Eligibility applies to all <a href="/about-aws/global-infrastructure/regional-product-services/">AWS Regions</a> where AWS CodePipeline is available. See the <a href="https://d0.awsstatic.com/whitepapers/compliance/AWS_HIPAA_Compliance_Whitepaper.pdf" target="_blank">Architecting for HIPAA Security and Compliance on Amazon Web Services Whitepaper</a> for information and best practices about how to configure AWS HIPAA Eligible Services to store, process, and transmit PHI. To learn more about CodePipeline please visit the CodePipeline <a href="/codepipeline/" target="_blank">homepage</a>.</p>
</div>
</div>]<h1 id="Discovering_Documents_Made_Easy_in_AWS_Systems_Manager_Automation"> <a name="Discovering_Documents_Made_Easy_in_AWS_Systems_Manager_Automation"> Discovering Documents Made Easy in AWS Systems Manager Automation</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Today, AWS Systems Manager updated the layout for the documents selection screen. Now, documents published by AWS are organized by use case so you can easily navigate and discover them. This update also includes the ability to view custom documents owned by you or shared with you, allowing you to quickly find your custom documents.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Document categories can be found on the document selection page, after selecting <b>Execute Automation</b>. For example, you can find security-related documents, such as documents to encrypt S3 buckets, in the <b>Security</b> category. Similarly, remediation documents to rescue Amazon Elastic Compute Cloud (Amazon EC2) instances can be found in the <b>Remediation </b>category. Other categories include documents for AMI management, data backup, and instance-based documents. Go to the Systems Manager console to see all available categories. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>This update is live in all AWS Regions where Systems Manager is <a href="/about-aws/global-infrastructure/regional-product-services/" target="_blank">available</a>. To learn more about AWS Systems Manager Automation, visit our <a href="/systems-manager/" target="_blank">product page</a>.</p>
</div>
</div>]<h1 id="Amazon_EC2_AMD_Instances_are_Now_Available_in_additional_regions"> <a name="Amazon_EC2_AMD_Instances_are_Now_Available_in_additional_regions"> Amazon EC2 AMD Instances are Now Available in additional regions</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Starting today, Amazon EC2 M5a, M5ad, R5a, R5ad, and T3a instances are available in additional regions.</p>
<p>• M5a and R5a instances are now available in AWS Europe (Paris), US West (San Francisco), Canada (Montreal) and AWS GovCloud (US) Regions<br/> • M5ad and R5ad instances are now available in AWS Asia Pacific (Sydney), Canada (Montreal) and AWS GovCloud(US-West) Regions<br/> • T3a instances are now available in AWS Asia Pacific (Seoul, Sydney, Tokyo), Europe (Paris, London, Frankfurt), US West (San Francisco), Canada (Montreal) and AWS GovCloud (US) Regions</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Both M5a and R5a instances were first <a href="/about-aws/whats-new/2018/11/introducing_amazon_ec2_instances_featuring_amd_epyc_processors/">introduced</a> in November of 2018. M5ad and R5ad instances were <a href="https://aws.amazon.com/blogs/aws/new-amd-epyc-powered-amazon-ec2-m5ad-and-r5ad-instances/">launched</a> in March of 2019, <a href="https://aws.amazon.com/blogs/aws/new-amd-epyc-powered-amazon-ec2-m5ad-and-r5ad-instances/">followed</a> by T3a in April of 2019. All the AMD instances feature 2.5 GHz AMD EPYC 7000 series processors, and are variants of Amazon EC2’s general purpose (<a href="/ec2/instance-types/m5/">M5</a>), memory optimized (<a href="/ec2/instance-types/r5/">R5</a>), and burstable general-purpose (<a href="/ec2/instance-types/t3/">T3</a>) instance families.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p> The AMD-based instances provide additional options for customers who are looking to achieve a 10% cost savings on their Amazon EC2 compute environment for a variety of workloads. M5a and M5ad instances are ideal for business-critical applications, web and application servers, back-end servers for enterprise applications, gaming servers, caching fleets, and app development environments. R5a and R5ad instances are ideal for high performance databases, distributed web scale in-memory caches, mid-size in-memory databases, real time big data analytics, and other enterprise applications. T3a instances offer a balance of compute, memory, and network resources for a broad spectrum of general purpose workloads including micro-services, low-latency interactive applications, small and medium databases, virtual desktops, development environments, code repositories, and business-critical applications.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>With these regional expansions, M5a and R5a instances are available today in US East (N. Virginia, Ohio), US West (Oregon, San Francisco), Europe (Ireland, Frankfurt, Paris), Asia Pacific (Singapore, Tokyo, Sydney), China (Beijing and Ningxia), Canada (Montreal) and AWS GovCloud (US). M5ad, and R5ad instances are available today in US East (N. Virginia, Ohio), US West (Oregon), Asia Pacific (Singapore, Sydney), Canada (Montreal) and AWS GovCloud (US-West). In addition, T3a instances are available today in US East (N. Virginia, Ohio), US West (Oregon, San Francisco), Europe (Ireland, Frankfurt, London, Paris), Asia Pacific (Singapore, Sydney, Tokyo, Seoul), China (Beijing and Ningxia), Canada (Montreal) and AWS GovCloud (US) Regions. M5a, M5ad, R5a and R5ad instances are available in 8 sizes, with 2, 4, 8, 16, 32, 48, 64, and 96 vCPUs, and T3a instances are available in 7 sizes, with 2, 4 and 8 vCPUs. These new instances can be purchased as On-Demand, Reserved or Spot Instances. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To get started, visit the <a href="https://console.aws.amazon.com/">AWS Management Console</a>, <a href="/cli/">AWS Command Line Interface (CLI)</a>, and <a href="https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/EC2.html">AWS SDKs</a>. To learn more, visit the <a href="/ec2/amd/">AMD Instances Page</a>. </p>
</div>
</div>]<h1 id="AWS_Migration_Hub_Now_Supports_Import_of_On-Premises_Server_and_Application_Data_From_RISC_Networks_to_Plan_and_Track_Migration_Progress"> <a name="AWS_Migration_Hub_Now_Supports_Import_of_On-Premises_Server_and_Application_Data_From_RISC_Networks_to_Plan_and_Track_Migration_Progress"> AWS Migration Hub Now Supports Import of On-Premises Server and Application Data From RISC Networks to Plan and Track Migration Progress</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Migration Hub now supports import of on-premises server and application data exported directly from RISC Networks, an AWS Migration Competency Partner.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Migration Hub provides a single location to discover, plan, and track the progress of application migrations. You can now import information discovered by RISC Networks, including server specifications, utilization data, and application and server dependencies, to Migration Hub.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more about AWS Migration Hub, click <a href="/migration-hub/">here</a> or refer to the <a href="https://docs.aws.amazon.com/migrationhub/latest/ug/whatishub.html">documentation</a>.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more about RISC Networks, visit their <a href="https://www.riscnetworks.com/">website</a>.</p>
<p> </p>
</div>
</div>]<h1 id="AWS_Cost_Explorer_now_Supports_Usage-Based_Forecasts_"> <a name="AWS_Cost_Explorer_now_Supports_Usage-Based_Forecasts_"> AWS Cost Explorer now Supports Usage-Based Forecasts </a> </h1>[<div class="aws-text-box">
<div class="">
<p> Starting today, you can create custom usage forecasts using AWS Cost Explorer to gain a line of sight into your future usage patterns. Cost Explorer’s usage forecasts use a machine learning algorithm that learns your historical usage trends and uses that information to provide a forecast of your future usage. Using these forecasts, you can better understand your expected cost trends and monitor your key usage patterns (for example, storage, data transfer, or running hours). Please note that you can generate your usage forecasts and explore your cost and usage data programmatically via the <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetUsageForecast.html" target="_blank">AWS Cost Explorer API</a>. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p> From there, you can use these forecasted amounts to define custom usage budgets (using <a href="https://aws.amazon.com/aws-cost-management/aws-budgets/" target="_blank">AWS Budgets</a>) that will help you monitor these patterns and proactively alert you if changes in your usage patterns are detected.</p>
<p> To learn more about AWS Cost Explorer capabilities, refer to the <a href="https://aws.amazon.com/aws-cost-management/aws-cost-explorer/" target="_blank">AWS Cost Explorer</a> webpage or the <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-forecast.html" target="_blank">Forecasting with Cost Explorer</a> user guide. To get started with AWS Cost Explorer, please refer to this <a href="https://aws.amazon.com/blogs/aws-cost-management/getting-started-with-aws-cost-explorer-part-1/" target="_blank">blog post</a>.</p>
</div>
</div>]<h1 id="EC2_Hibernation_feature_is_now_available_to_customers_in_the_Europe_(Stockholm)_and_Asia_Pacific_(Hong_Kong)_AWS_Regions"> <a name="EC2_Hibernation_feature_is_now_available_to_customers_in_the_Europe_(Stockholm)_and_Asia_Pacific_(Hong_Kong)_AWS_Regions"> EC2 Hibernation feature is now available to customers in the Europe (Stockholm) and Asia Pacific (Hong Kong) AWS Regions</a> </h1>[<div class="aws-text-box">
<div class="">
<p>The EC2 Hibernation feature is now available in the Europe (Stockholm) and Asia Pacific (Hong Kong) AWS Regions. Hibernation gives you the ability to launch EC2 instances, set them up as desired, hibernate them, and then quickly bring them back to life when you need them. Applications pick up exactly where they left off instead of rebuilding their memory footprint. Using hibernate, you can maintain a fleet of pre-warmed instances that can get to a productive state faster, and you can do this without modifying your existing applications.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Hibernation requires an EC2 instance to be an encrypted <a href="/ebs/">Amazon EBS-</a>backed instance. This ensures protection of sensitive contents in memory (RAM) as they get copied to EBS upon hibernation. You can now enable Amazon EBS <a href="/about-aws/whats-new/2019/05/with-a-single-setting-you-can-encrypt-all-new-amazon-ebs-volumes/">Encryption by Default</a>, to ensure all new EBS volumes created in your account are encrypted. You no longer have to create an encrypted copy of the Amazon Machine Image (AMI) before launching an instance. Alternatively, you can also now specify encryption intent at launch (with unencrypted AMI or snapshot) and enable hibernation at the same time (see <a href="https://aws.amazon.com/about-aws/whats-new/2019/05/enable-hibernation-on-ec2-instances-when-launching-with-an-ami-without-an-encrypted-ebs-snapshot/">link</a>).  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Hibernation is available for On-Demand and Reserved Instances running on newly launched M3, M4, M5, C3, C4, C5, R3, R4, and R5 instances running Amazon Linux (1). With this expansion, EC2 Hibernation feature is now available in the US East (N. Virginia, Ohio), US West (N. California, Oregon), Canada (Central), South America (Sao Paulo), Asia Pacific (Hong Kong, Mumbai, Seoul, Singapore, Sydney, Tokyo), and Europe (Frankfurt, London, Ireland, Paris, Stockholm) AWS Regions. <br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>This feature is available through <a href="/cli/">AWS Command Line Interface (CLI)</a>, <a href="/tools/">AWS SDKs,</a> or the <a href="https://console.aws.amazon.com/console/home">AWS Management Console</a> at no extra charge. To learn more about hibernation, visit this <a href="/blogs/aws/new-hibernate-your-ec2-instances/">blog</a>. For information about enabling hibernation for your EC2 instances, visit our <a href="/ec2/faqs/#Hibernate">FAQs</a> or technical <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html">documentation</a>. For more information about EBS Encryption by Default, visit <a href="/about-aws/whats-new/2019/05/with-a-single-setting-you-can-encrypt-all-new-amazon-ebs-volumes/">this link</a> or <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html">technical documentation</a>. <br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
</div>
</div>]<h1 id="AWS_Direct_Connect_Now_Supports_Resource_Based_Authorization,_Tag_Based_Authorization,_and_Tag_on_Resource_Creation"> <a name="AWS_Direct_Connect_Now_Supports_Resource_Based_Authorization,_Tag_Based_Authorization,_and_Tag_on_Resource_Creation"> AWS Direct Connect Now Supports Resource Based Authorization, Tag Based Authorization, and Tag on Resource Creation</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Direct Connect is a cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS. Using AWS Direct Connect, you can establish private connectivity between AWS and your data center, office, or colocation environment, which in many cases can reduce your network costs, increase bandwidth throughput, and provide a more consistent network experience than Internet-based connections. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS Direct Connect now supports resource based authorization, tag based authorization, and tag on resource creation.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>You can now define <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html">AWS Identity and Access Management (IAM)</a> policies to specify fine-grained permissions for AWS Direct Connect Dedicated and Hosted connection(s), Interconnects, Link Aggregation Groups, virtual interfaces, Direct Connect gateways based on resource names and tags, improving the security through these two granular access control features.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>With resource-level authorization, you can configure IAM policies that reference AWS Direct Connect Dedicated and Hosted connection(s), Interconnects, Link Aggregation Groups, virtual interfaces, Direct Connect gateways using Amazon Resource Names (ARNs) or wildcards, and specify the users and actions that are permitted on the resources. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Using tag-based permissions, you can define IAM policies that specify permissions for tagged AWS Direct Connect Dedicated and Hosted connection(s), Interconnects, Link Aggregation Groups, virtual interfaces. For example, you can tag a Dedicated connection based on business units and limit control over those resources to the members of that business unit.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Using tag on resource creation, you can tag AWS Direct Connect Dedicated and Hosted connection(s), Interconnects, Link Aggregation Groups, virtual interfaces resources at the time of creation. When new resources are created with tags, the corresponding IAM permissions are automatically applied. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more, see <a href="https://docs.aws.amazon.com/directconnect/latest/UserGuide/using-tags.html">Tagging AWS Direct Connect Resources</a> in the AWS Direct Connect User Guide.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Visit our <a href="/directconnect/getting-started/">Getting Started</a> page. Sign in to your <a href="/console/">AWS Management Console</a> to order AWS Direct Connect today!</p>
</div>
</div>]<h1 id="Introducing_the_Amazon_Corretto_Crypto_Provider_(ACCP)_for_Improved_Cryptography_Performance"> <a name="Introducing_the_Amazon_Corretto_Crypto_Provider_(ACCP)_for_Improved_Cryptography_Performance"> Introducing the Amazon Corretto Crypto Provider (ACCP) for Improved Cryptography Performance</a> </h1>[<div class="aws-text-box">
<div class="">
<p>The Amazon Corretto Crypto Provider (ACCP), a cryptography performance improvement for <a href="/corretto/" target="_blank">Amazon Corretto</a>, is now available. Historically, Java cryptography has been CPU-intensive resulting in slow performance and elevated operational costs. ACCP updates dozens of cryptographic algorithms, accelerating cryptographic workloads.<br/> <br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>You can now optimize your own environments with ACCP. The ACCP is open source and available on Maven and GitHub, so that non-Corretto Java 8 and Java 11 users can improve their cryptographic performance. To learn more about ACCP and observed benchmarking improvements, please read the <a href="https://aws.amazon.com/blogs/opensource/introducing-amazon-corretto-crypto-provider-accp/" target="_blank">blog post</a>. </p>
</div>
</div>]<h1 id="AWS_Resource_Groups_and_AWS_Resource_Groups_Tag_Editor_Now_Supports_Additional_AWS_Resources"> <a name="AWS_Resource_Groups_and_AWS_Resource_Groups_Tag_Editor_Now_Supports_Additional_AWS_Resources"> AWS Resource Groups and AWS Resource Groups Tag Editor Now Supports Additional AWS Resources</a> </h1>[<div class="aws-text-box">
<div class="">
<p> AWS Resource Groups makes it easier to manage and automate tasks on large numbers of AWS resources at one time. AWS Resource Groups Tag Editor allows you to add tags to – or edit or delete tags of – multiple AWS resources at once. With Tag Editor, you can search for the resources that you want to tag, and then manage tags for the resources in your search results. Starting today, AWS Resource Groups supports 26 additional AWS resources including AWS Config Rules, AWS ElasticBeanstalk Applications, and AWS Resource Groups Tag Editor supports 6 additional AWS resources including AWS CloudWatch Alarms, AWS CloudFormation Stacks.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Both AWS Resource Groups, and AWS Resource Groups Tag Editor are available in all commercial AWS Regions except the Asia Pacific (Osaka) Local and China Regions. With this release, AWS Resource Groups supports over 140 AWS Resources, and AWS Resource Groups Tag Editor supports over 50 AWS Resources. To view the complete list of supported AWS Resources, visit <a href="https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html" target="_blank">Resource Groups Supported Resources documentation</a>.</p>
</div>
</div>]<h1 id="AWS_VPC_CNI_Version_1.5.0_Now_Default_for_Amazon_EKS_Clusters"> <a name="AWS_VPC_CNI_Version_1.5.0_Now_Default_for_Amazon_EKS_Clusters"> AWS VPC CNI Version 1.5.0 Now Default for Amazon EKS Clusters</a> </h1>[<div class="aws-text-box">
<div class="">
<p><a href="https://github.com/aws/amazon-vpc-cni-k8s">AWS VPC Container Networking Interface (CNI) Plugin</a> version 1.5 is now the default CNI for new Kubernetes clusters launched by Amazon EKS.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Version 1.5 of the AW VPC CNI plugin improves the behavior of the WARM_IP_TARGET parameter so that any IPs not assigned to pods will be returned back to the subnet. This lowers overall IP address utilization across the cluster. Additionally, a number of bug fixes improve the overall reliability and performance of the CNI for Amazon EKS clusters. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more, visit the <a href="https://docs.aws.amazon.com/eks/latest/userguide/pod-networking.html">Amazon EKS documentation</a> and <a href="https://github.com/aws/amazon-vpc-cni-k8s/releases/tag/v1.5.0">AWS VPC CNI v1.5 release notes on GitHub</a>. You can upgrade your existing clusters to use version 1.5 of the AWS VPC CNI plugin by following the instructions in the <a href="https://docs.aws.amazon.com/eks/latest/userguide/cni-upgrades.html">Amazon EKS documentation</a>.</p>
</div>
</div>]<h1 id="Kinesis_Video_Streams_adds_support_for_Dynamic_Adaptive_Streaming_over_HTTP_(DASH)_and_H.265_video"> <a name="Kinesis_Video_Streams_adds_support_for_Dynamic_Adaptive_Streaming_over_HTTP_(DASH)_and_H.265_video"> Kinesis Video Streams adds support for Dynamic Adaptive Streaming over HTTP (DASH) and H.265 video</a> </h1>[<div class="aws-text-box">
<div class="">
<p><a href="/kinesis/video-streams/">Amazon Kinesis Video Streams</a> Dynamic Adaptive Streaming over HTTP (DASH) capability enables developers to playback their ingested video streams using the industry-standard, HTTP-based media streaming protocol.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>As devices stream their video into Kinesis Video Streams, developers can use the fully-managed DASH capability to playback live and recorded video from their streams. Developers can now also stream, store, and process H.265 video for playback and Machine Leaning based processing. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p> The DASH-based playback capability is fully managed, so you do not have to build any cloud-based infrastructure or software to playback the media captured by Amazon Kinesis Video streams. You can simply create a streaming session using the new APIs and leverage webplayers such as VideoJS or GoogleShaka player, modern web browsers, or video players for mobile platforms such as Android (Exoplayer) and iOS (AVMediaPlayer), that are compatible with the fragmented MP4 (FMP4) format.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>H.265 video offers superior compression over H.264 encoded video allowing developers to deliver high quality video at lower bitrates. Developers can stream and store H.265 video generated by compatible edge devices into Kinesis Video streams and then process it for generating machine learning based insights or playback the video using Amazon Kinesis Video Streams’ HTTP Live Streaming (HLS) or DASH capabilities.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more, please refer to the <a href="https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html">developer documentation</a>. </p>
<p>Refer to the <a href="/about-aws/global-infrastructure/regional-product-services/">AWS global region table</a> for Amazon Kinesis Video Streams availability.<br/> </p>
</div>
</div>]<h1 id="New_AWS_Public_Datasets_Available_from_Facebook,_Yale,_Allen_Institute_for_Brain_Science,_NOAA,_and_others"> <a name="New_AWS_Public_Datasets_Available_from_Facebook,_Yale,_Allen_Institute_for_Brain_Science,_NOAA,_and_others"> New AWS Public Datasets Available from Facebook, Yale, Allen Institute for Brain Science, NOAA, and others</a> </h1>[<div class="aws-text-box">
<div class="">
<p>New AWS Public Datasets Available from Facebook, Yale, Allen Institute for Brain Science, NOAA, and others. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>9 new or updated AWS Public Datasets are now available in the following categories:</p>
<p>Biology:</p>
<ul>
<li>The <a href="https://registry.opendata.aws/allen-brain-observatory/" target="_blank">Allen Brain Observatory</a> has been expanded to include 100TB of neurophysiology data representing tens of thousands of neurons in the mouse visual system from Allen Institute for Brain Science.</li>
</ul>
<p>Environmental:</p>
<ul>
<li><a href="https://registry.opendata.aws/noaa-goes/" target="_blank">Geostationary Operational Environmental Satellite (GOES) 16 &amp; 17 Fire Detection and Characterization data</a> from the National Oceanic and Atmospheric Administration (NOAA).<br/> </li>
<li><a href="https://registry.opendata.aws/noaa-ghe/" target="_blank">Global Hydro Estimator (GHE) Instantaneous Rain Rate product</a> from NOAA.</li>
</ul>
<p>Geospatial:</p>
<ul>
<li><a href="https://registry.opendata.aws/dc-lidar/" target="_blank">2018 Classified Point Cloud LiDAR of Washington, DC</a> from the District of Columbia Office of the Chief Technology Officer.<br/> </li>
<li><a href="https://registry.opendata.aws/dataforgood-fb-hrsl/" target="_blank">High Resolution Population Density Maps + Demographic Estimates</a> by the Center for International Earth Science Information Network (CIESIN) at Columbia University and Facebook.</li>
</ul>
<p>Meteorological:</p>
<ul>
<li><a href="https://registry.opendata.aws/noaa-isd/" target="_blank">Integrated Surface Database (ISD)</a> from the NOAA.<br/> </li>
<li><a href="https://registry.opendata.aws/noaa-ghcnh/" target="_blank">Global Historical Climatology Network Hourly (GHCN-H)</a> from NOAA.<br/> </li>
<li><a href="https://registry.opendata.aws/noaa-nwm-pds/" target="_blank">National Water Model Short Range Forecast</a> and <a href="https://registry.opendata.aws/nwm-archive/" target="_blank">Reanalysis</a> version 2.0 from NOAA.</li>
</ul>
<p>Robotics:</p>
<ul>
<li><a href="https://registry.opendata.aws/ycb-benchmarks/" target="_blank">Yale-Carnegie Mellon University-Berkeley (YCB) Object and Model Set</a>.</li>
</ul>
<p>The AWS Public Dataset Program covers the cost of storage for publicly available high-value cloud-optimized datasets. We work with data providers who seek to:</p>
<ul>
<li>Democratize access to data by making it available for analysis on AWS.<br/> </li>
<li>Develop new cloud-native techniques, formats, and tools that lower the cost of working with data.<br/> </li>
<li>Encourage the development of communities that benefit from access to shared datasets.</li>
</ul>
<div>
              
          </div>
<div>
            Learn how to propose your dataset to the 
           <a href="https://aws.amazon.com/opendata/public-datasets/" style="outline-width: 0px !important; user-select: auto !important;">AWS Public Dataset Program</a>. 
          </div>
</div>
</div>]<h1 id="Amazon_EC2_I3en_Instances_are_Now_Available_in_US_West_(N._California)_and_Asia_Pacific_(Seoul)_AWS_Regions"> <a name="Amazon_EC2_I3en_Instances_are_Now_Available_in_US_West_(N._California)_and_Asia_Pacific_(Seoul)_AWS_Regions"> Amazon EC2 I3en Instances are Now Available in US West (N. California) and Asia Pacific (Seoul) AWS Regions</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Starting today, Amazon EC2 I3en instances are available in US West (N. California) and Asia Pacific (Seoul) AWS Regions. I3en global availability now includes the Asia Pacific (Tokyo, Seoul), Europe (Frankfurt, Ireland), US East (N. Virginia, Ohio), and US West (Oregon, N. California) AWS regions. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>I3en instances offer up to 60 TB of low latency NVMe SSD instance storage and up to 50% lower cost per GB over I3 instances. These instances are designed for data-intensive workloads such as relational and NoSQL databases, distributed file systems, search engines, and data warehouses that require high random I/O access to large amounts of data residing on instance storage. I3en instances also provide up to 100 Gbps of networking bandwidth and come in seven instance sizes, with storage options from 1.25 to 60 TB. For more information, visit our <a href="/ec2/instance-types/i3en/">product page</a>.</p>
</div>
</div>]<h1 id="Announcing_the_availability_of_Amazon_Kinesis_Video_Producer_SDK_in_C"> <a name="Announcing_the_availability_of_Amazon_Kinesis_Video_Producer_SDK_in_C"> Announcing the availability of Amazon Kinesis Video Producer SDK in C</a> </h1>[<div class="aws-text-box">
<div class="">
<p><a href="/kinesis/video-streams/">Amazon Kinesis Video Streams</a> producer SDKs are free and open software libraries for building applications that can stream audio and video data directly from an edge device to the AWS cloud for durable storage, playback, and machine learning based processing. Amazon Kinesis Video Streams producer SDK is now available in C. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>With the addition of producer SDK in C, developers can now choose among C, C++, and JAVA SDKs to build streaming applications that best suits their edge device platform. Producer SDK in C is specifically useful for building applications for edge devices with limited flash storage such as cameras used in home or enterprise security. An application built with the producer SDK in C can be deployed to an edge device with as low as 500KB of available flash storage. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p> Producer SDK in C is available for Linux, MacOS, Windows, and Raspbian platforms; and is also available as a Docker container for easy deployment. To learn more, please refer to the <a href="https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk.html">developer documentation</a>.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Refer to the <a href="/about-aws/global-infrastructure/regional-product-services/">AWS global region table</a> for Amazon Kinesis Video Streams availability. </p>
</div>
</div>]<h1 id="AWS_RoboMaker_announces_support_for_Robot_Operating_System_(ROS)_Melodic"> <a name="AWS_RoboMaker_announces_support_for_Robot_Operating_System_(ROS)_Melodic"> AWS RoboMaker announces support for Robot Operating System (ROS) Melodic</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS RoboMaker, a service that makes it easy to develop, simulate, and deploy intelligent robotics applications at scale, announces the support for ROS-Melodic Morenia, which is the latest long term support (LTS) release for ROS. Now with AWS RoboMaker, customers can build robotics applications with ROS-Melodic, in addition to the existing ROS-Kinetic distribution. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Customers can choose the ROS version they would like to be pre-installed and configured in RoboMaker’s integrated development environment so that they can start coding right away. ROS Melodic is compatible with the Gazebo 9 simulation engine and with the Ubuntu 18.04 (Bionic) operating system.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS RoboMaker extends the most widely used open-source robotics software framework, Robot Operating System (ROS), with connectivity to cloud services. This includes AWS machine learning services, monitoring services, and analytics services that enable a robot to stream data, navigate, communicate, comprehend, and learn. AWS RoboMaker provides each of these cloud service extensions as open source ROS packages, so you can build functions on your robot by taking advantage of cloud APIs, all in a familiar software framework. To get started, one can explore the <a href="/robomaker/">RoboMaker webpage</a> or run a sample simulation job in the <a href="http://console.aws.amazon.com/robomaker">RoboMaker console</a>. </p>
</div>
</div>]<h1 id="AWS_Elemental_MediaConvert_Now_Ingests_Files_from_HTTPS_Sources"> <a name="AWS_Elemental_MediaConvert_Now_Ingests_Files_from_HTTPS_Sources"> AWS Elemental MediaConvert Now Ingests Files from HTTPS Sources</a> </h1>[<div class="aws-text-box">
<div class="">
<p><a href="https://aws.amazon.com/mediaconvert/">AWS Elemental MediaConvert</a> can now ingest video files from HTTP and HTTPS sources. With the ability to transcode content from sources other than Amazon S3, you are no longer required to build logic to copy files into S3 in order to use MediaConvert. This feature is available at no additional charge. To learn, more please <a href="https://docs.aws.amazon.com/mediaconvert/latest/ug/upload-input-files.html#http-input-requirements">read the documentation</a>.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Using AWS Elemental MediaConvert, video providers with any size content library can easily and reliably transcode on-demand content for broadcast and multiscreen delivery. MediaConvert functions independently or as part of <a href="https://aws.amazon.com/media-services/">AWS Elemental Media Services</a>, a family of services that form the foundation of cloud-based workflows and offer the capabilities needed to transport, transcode, package, and deliver video.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Visit the <a href="https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/">AWS region table</a> for a full list of AWS Regions where AWS Elemental MediaConvert is available. To learn more about MediaConvert, please visit <a href="https://aws.amazon.com/mediaconvert/">https://aws.amazon.com/mediaconvert/</a>.</p>
</div>
</div>]<h1 id="AWS_Glue_is_now_available_in_the_AWS_South_America_(Sao_Paulo)_Region"> <a name="AWS_Glue_is_now_available_in_the_AWS_South_America_(Sao_Paulo)_Region"> AWS Glue is now available in the AWS South America (Sao Paulo) Region</a> </h1>[<div class="aws-text-box">
<div class="">
<p>You can now use AWS Glue in the AWS South America (Sao Paulo) Region.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p><a href="/glue/">AWS Glue</a> automates much of the effort to build, maintain, and run extract, transform, and load (ETL) jobs. AWS Glue crawls your data sources, identifies data formats, and suggests schemas and transformations. AWS Glue automatically generates the code to execute your data transformations and loading processes. AWS Glue is serverless, so there is no infrastructure to provision or manage. AWS Glue runs your ETL jobs on a fully managed Apache Spark environment. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>For a list of regions where AWS Glue is available, see the <a href="/about-aws/global-infrastructure/regional-product-services/">AWS Region Table</a>. </p>
</div>
</div>]<h1 id="New_AWS_Competency_Partners_to_migrate_Microsoft_Workloads_to_AWS"> <a name="New_AWS_Competency_Partners_to_migrate_Microsoft_Workloads_to_AWS"> New AWS Competency Partners to migrate Microsoft Workloads to AWS</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Customers have been running Windows workloads on AWS for over a decade. We run nearly 2x more Windows Server instances than the next largest cloud provider, according to an <a href="https://pages.awscloud.com/IDC-Windows-Server-Market-Update.html?trk=ar_card" target="_blank">IDC report.</a> Our <a href="/windows/?analyst-reports-windows.sort-by=item.additionalFields.datePublished&amp;analyst-reports-windows.sort-order=desc" target="_blank">experience running Windows applications</a> has earned our customers’ trust and the number of AWS enterprise customers using Amazon EC2 for Windows Server has grown 5x since 2015.</p>
<p>Today, we are excited to announce the AWS Microsoft Workloads Competency for APN Advanced Technology Partners, offering products based on varying phases of a customer’s journey to the AWS Cloud including migration assessment, migration, post-migration operational optimization, enhancement through analytics and Machine Learning, and modernization. The AWS Microsoft Workloads Competency reduces a customer’s time and effort in finding a capable and trusted APN Technology Partner for their Microsoft Workloads environment on AWS.</p>
<p>Interested in becoming an AWS Microsoft Workloads Competency Partner? <a href="/partners/competencies/" target="_blank">See the requirements and next steps here</a>.</p>
<p>Interested in working with an AWS Microsoft Workloads Technology Partner? <a href="/windows/partner-solutions/" target="_blank">See the validated AWS Microsoft Workload Technology Partners here</a>.  </p>
<p><a href="https://aws.amazon.com/blogs/apn/more-reasons-for-customers-to-migrate-their-microsoft-workloads-to-aws/" target="_blank">Learn more on the APN Blog</a>. </p>
</div>
</div>]<h1 id="The_AWS_Cloud_Development_Kit_(AWS_CDK)_is_Now_Generally_Available"> <a name="The_AWS_Cloud_Development_Kit_(AWS_CDK)_is_Now_Generally_Available"> The AWS Cloud Development Kit (AWS CDK) is Now Generally Available</a> </h1>[<div class="aws-text-box">
<div class="">
<p> The AWS Cloud Development Kit (AWS CDK) is now generally available in TypeScript and Python. AWS CDK is an open source software development framework to model and provision your cloud application resources using familiar programming languages. With AWS CDK, you can define your infrastructure as code and provision it through AWS CloudFormation. AWS CDK is also available in Java and C# in developer preview.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS CDK provides high-level components that preconfigure cloud resources with proven defaults, so you can build cloud applications without needing to be an expert. It also enables you to compose and share your own custom components that incorporate your organization's requirements, helping teams start new projects faster. AWS CDK is available to use in all regions.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more about <a href="/cdk/">AWS CDK</a>, visit our <a href="/blogs/aws/aws-cloud-development-kit-cdk-typescript-and-python-are-now-generally-available/">blog post</a>.<br/> </p>
</div>
</div>]<h1 id="Introducing_Amazon_EventBridge"> <a name="Introducing_Amazon_EventBridge"> Introducing Amazon EventBridge</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon EventBridge is a serverless event bus that makes it easy to connect applications together using data from your own applications, Software-as-a-Service (SaaS) applications, and AWS services. EventBridge delivers a stream of real-time data from event sources, such Zendesk, Datadog, or Pagerduty, and routes that data to targets like AWS Lambda. You can set up routing rules to determine where to send your data to build application architectures that react in real time to all of your data sources. EventBridge allows you to build event-driven architectures, which are loosely coupled and distributed. This improves developer agility as well as application resiliency. EventBridge makes it easy to build event-driven applications because it takes care of event ingestion and delivery, security, authorization, and error-handling for you. EventBridge leverages the CloudWatch Events API, so CloudWatch Events users can access their existing default bus, rules, and events in the new EventBridge console, as well as in the CloudWatch Events console.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>EventBridge supports 10 SaaS application partners and 90+ AWS Services as event sources. To become an EventBridge SaaS integration partner, please visit the <a href="https://aws.amazon.com/eventbridge/partners/">EventBridge partner page</a>.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>There is no up-front cost commitment or minimum fee for using EventBridge, and you pay only for the events published to your event bus. All state change events published by AWS services are free.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>You can get started with EventBridge using the <a href="https://console.aws.amazon.com/events/home">AWS Management Console</a>, <a href="/cli/">Command Line Interface</a> (CLI), or <a href="/tools/">SDK</a>. You can create a new event bus and receive events from SaaS applications in minutes; then simply create a rule to match events from a list of AWS services or SaaS applications and proceed to set up targets for your events.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>EventBridge is generally available today in the following regions: US East (Ohio and N. Virginia), US West (Oregon and N. California), Canada (Central), EU (Stockholm, Paris, Ireland, Frankfurt, and London), Asia Pacific (Mumbai, Tokyo, Hong Kong, Seoul, Singapore, and Sydney), and South America (Sao Paulo).<br/> </p>
<p>To learn more about EventBridge:</p>
<ul>
<li>Read the <a href="https://aws.amazon.com/blogs/aws/amazon-eventbridge-event-driven-aws-integration-for-your-saas-applications/">AWS News blog post</a></li>
<li>Visit the <a href="/eventbridge/">Amazon EventBridge product page</a><br/> </li>
<li>Read the <a href="https://docs.aws.amazon.com/eventbridge/index.html">Amazon EventBridge Developer Guide</a></li>
</ul>
</div>
</div>]<h1 id="The_AWS_Toolkit_for_Visual_Studio_Code_is_Now_Generally_Available"> <a name="The_AWS_Toolkit_for_Visual_Studio_Code_is_Now_Generally_Available"> The AWS Toolkit for Visual Studio Code is Now Generally Available</a> </h1>[<div class="aws-text-box">
<div class="">
<p>The AWS Toolkit for Visual Studio Code, an open source plug-in that makes it easier to create, step-through debug, build, and deploy applications, is now Generally Available. The toolkit supports .NET, node.js and Python applications and provides deep support for serverless applications at launch with other AWS services planned for the future. The toolkit had previously been in developer preview. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>The AWS Toolkit for Visual Studio Code provides an integrated experience for developing serverless applications. You can get started fast with built-in project templates that leverage the AWS Serverless Application Model (AWS SAM) to define and configure resources. The toolkit also includes an integrated experience for step-through debugging of serverless applications with the AWS SAM CLI and makes it easy to deploy your applications from the IDE. Check out this <a href="https://aws.amazon.com/blogs/developer/announcing-aws-toolkit-for-visual-studio-code/">blog post</a> to learn about developing serverless applications with Visual Studio Code. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Please visit the <a href="/visualstudiocode/">AWS Toolkit for Visual Studio Code homepage</a> for more information on how to get started.  </p>
</div>
</div>]<h1 id="AWS_Direct_Connect_launches_third_location_in_New_York_Metro_Area"> <a name="AWS_Direct_Connect_launches_third_location_in_New_York_Metro_Area"> AWS Direct Connect launches third location in New York Metro Area</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Direct Connect is now live at Equinix NY5, Secaucus, NJ. This location offers logical redundancy over a single virtual interface (VIF) on a Direct Connect connection. <a href="/about-aws/whats-new/2018/11/aws-direct-connect-launches-logical-redundancy-over-a-single-vir/">Logical redundancy</a> can reduce downtime when a BGP peering session goes down due to a device failure or maintenance activity on the AWS side. With global access for AWS Direct Connect, you can reach AWS resources in any global AWS region using global public VIFs and Direct Connect gateway. When connecting to any AWS region, your data will not hairpin via the home region if it is not in the shortest path to your desired AWS region.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>As with any AWS Direct Connect location, this locations conforms to the standard resiliency model that includes two customer facing devices per location that allow customers to establish locally resilient and redundant physical connectivity to the Amazon backbone network. Please take a look at our <a href="/directconnect/resiliency-recommendation/">resiliency recommendations</a> when planning your connectivity. Using AWS Direct Connect, you can establish private connectivity between AWS and your datacenter, office, or colocation environment, which in many cases can reduce your network costs, increase bandwidth throughput, and provide a more consistent network experience than Internet-based connections.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Please see the AWS Direct Connect website for details on our <a href="/directconnect/details/">locations</a>, their associated home regions, the support of logical redundancy and <a href="/directconnect/pricing/">pricing</a>. All AWS Direct Connect locations give access to all global AWS Regions (except China) as shown in our <a href="/about-aws/global-infrastructure/regional-product-services/">region table</a>. Customers can get 1Gbps or 10Gbps Dedicated Connections or work with an approved partner for Hosted Connections with capacities ranging from 50Mbps to 10Gbps. To get started with planning your connectivity to AWS, visit our <a href="/directconnect/getting-started/">Getting Started page</a>. Sign in to your <a href="/console/">AWS Management Console</a> to order AWS Direct Connect today!</p>
</div>
</div>]<h1 id="AWS_Resource_Groups_is_Now_SOC_Compliant"> <a name="AWS_Resource_Groups_is_Now_SOC_Compliant"> AWS Resource Groups is Now SOC Compliant</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Resource Groups, a service that makes it easier to manage and automate tasks on large numbers of AWS resources at one time, is now a Service Organization Control (SOC) compliant service. This compliance certification applies to all AWS Regions where AWS Resource Groups is available.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p> AWS SOC (System and Organization Controls) reports are independent third-party examination reports that demonstrate how AWS achieves key compliance controls and objectives. SOC reporting provides customers and users with an independent assessment of AWS' control environment relevant to system security, availability, and confidentiality.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>You can get more information about AWS Compliance programs by visiting AWS Compliance Programs, or by going to the <a href="/compliance/services-in-scope/" target="_blank">Services in Scope by Compliance Program</a> page to see a full list of services covered by each compliance program. AWS Resource Groups is available in all commercial AWS Regions except the Asia Pacific (Osaka-Local) and China Regions. To learn more about AWS Resource Groups, please see our <a href="https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html" target="_blank">documentation</a>.</p>
</div>
</div>]<h1 id="Amazon_ECS_now_offers_improved_capabilities_for_local_testing"> <a name="Amazon_ECS_now_offers_improved_capabilities_for_local_testing"> Amazon ECS now offers improved capabilities for local testing</a> </h1>[<div class="aws-text-box">
<div class="">
<p>The open source ecs-cli tool now has improved capabilities for testing ECS task definitions locally. Using the ecs-cli, you can run ECS task definitions in a local development environment, such as a laptop or virtual machine.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>The ecs-cli converts your task definition to a Docker compose file, and enables you to test network modes, volumes, secrets, and credentials without having to deploy your task to ECS on AWS. This allows you to more fully test and debug your application locally without deploying, saving you time and shortening the development iteration loop. The new capabilities build on the existing ecs-cli capability for local testing that was <a href="/about-aws/whats-new/2019/03/new-local-testing-tools-now-available-for-amazon-ecs/">previously launched</a>.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To see a full list of capabilities and commands, see the documentation available on Github <a href="https://github.com/aws/amazon-ecs-cli/tree/master#running-tasks-locally">here</a> or the AWS documentation <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cmd-ecs-cli-local.html">here</a>.</p>
</div>
</div>]<h1 id="Large_Match_Support_for_Amazon_GameLift_Now_Available_"> <a name="Large_Match_Support_for_Amazon_GameLift_Now_Available_"> Large Match Support for Amazon GameLift Now Available </a> </h1>[<div class="aws-text-box">
<div class="">
<p>Players expect multiplayer game sessions to be fast and full. But with the rise of Battle Royale games and other player-intensive games, ensuring a consistent and fulfilling matchmaking experience can be a challenge for developers.</p>
<p>That’s why today we’re excited to announce Large Match Support for Amazon GameLift. With this update, you can now match and connect up to 200 players to a single game session on the lowest latency server instance available—all based upon a custom rule you define. We’ve also added some other new functionality that makes it even easier to support games with larger player counts, including:</p>
<ul>
<li><b>Create multiple teams from one definition.</b> Rather than defining team compositions separately, you can now easily create teams by specifying one team template for creating as many teams as needed for your game.</li>
</ul>
<div>
             
         </div>
<ul>
<li><b>Easier backfilling of open player slots.</b> We’ve automated backfilling, so you can keep matches full without causing long player wait times. Matchmaking backfill will automatically add a new player to a match even after a game has started and will prioritize filling a match before creating a new match.</li>
</ul>
<p>GameLift is available in the following 15 AWS Regions: US East (N. Virginia and Ohio), US West (Oregon and N. California), Central Canada (Montreal), EU Central (Frankfurt), EU West (London and Ireland), Asia Pacific South (Mumbai), Asia Pacific Northeast (Seoul and Tokyo), Asia Pacific Southeast (Singapore and Sydney), South America East (São Paulo), and China (Beijing).</p>
<p>To learn more about GameLift and Large Match Support, visit the <a href="https://aws.amazon.com/gamelift/" target="_blank">Amazon GameLift Product detail page</a> and read the <a href="https://aws.amazon.com/blogs/gametech/large-match-support/">Game Tech blog</a>. </p>
</div>
</div>]<h1 id="AWS_Cloud_Map_Available_in_AWS_South_America_(São_Paulo)_Region"> <a name="AWS_Cloud_Map_Available_in_AWS_South_America_(São_Paulo)_Region"> AWS Cloud Map Available in AWS South America (São Paulo) Region</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Cloud Map is now available in the AWS South America (São Paulo) Region. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS Cloud Map is a cloud resource discovery service. With AWS Cloud Map, you can define custom names for your application resources, such as Amazon ECS tasks, Amazon EC2 instances, Amazon S3 buckets, Amazon DynamoDB tables, Amazon SQS queues, or any other cloud resource. You can then use these custom names to discover the location and metadata of cloud resources from your applications using AWS SDK and authenticated API queries. AWS Cloud Map is a highly available, managed service with rapid change propagation.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Visit the <a href="/about-aws/global-infrastructure/regional-product-services/">AWS Region Table</a> to see all AWS Regions where AWS Cloud Map is available. Please visit our <a href="/cloud-map/">product page</a> to learn more about AWS Cloud Map.</p>
</div>
</div>]<h1 id="AWS_Container_Services_launches_Fluent_Bit_Plugins_for_AWS"> <a name="AWS_Container_Services_launches_Fluent_Bit_Plugins_for_AWS"> AWS Container Services launches Fluent Bit Plugins for AWS</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Container Services launches AWS Fluent Bit, a container image pre-installed with <a href="/cloudwatch/">Amazon CloudWatch</a> and <a href="/kinesis/data-firehose/">Amazon Kinesis Data Firehose</a> plugins that helps customers route container logs to multiple destinations such as CloudWatch, <a href="/s3/">Amazon S3</a>, <a href="/redshift/">Amazon Redshift</a>, and <a href="/elasticsearch-service/">Amazon Elasticsearch Service</a>.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p><a href="https://fluentbit.io/" target="_blank">Fluent Bit</a> is an open source and multi-platform Log Processor and Forwarder which allows you to collect data and logs from different sources, unify and send them to multiple destinations. It's fully compatible with <a href="https://www.docker.com/" target="_blank">Docker</a> and <a href="https://kubernetes.io/" target="_blank">Kubernetes</a> environments. Using the newly launched AWS Fluent Bit image, you can send container logs to the breadth of services for logs storage and analytics at AWS. You've been requesting for ways to send container logs to multiple destinations and the AWS Fluent Bit image enables integrations with Cloudwatch, S3, <a href="/athena/">Amazon Athena</a>, Elasticsearch Service, and Redshift.<br/> <br/> Read our <a href="https://aws.amazon.com/blogs/opensource/centralized-container-logging-fluent-bit/" target="_blank">blog</a> to learn more about how to use the Fluent Bit image on both <a href="/ecs/">Amazon Elastic Container Service (ECS)</a> and <a href="/eks/">Amazon Elastic Kubernetes Service (EKS)</a>.<br/> </p>
</div>
</div>]<h1 id="AWS_License_Manager_is_now_available_in_the_Asia_Pacific_(Hong_Kong)_Region"> <a name="AWS_License_Manager_is_now_available_in_the_Asia_Pacific_(Hong_Kong)_Region"> AWS License Manager is now available in the Asia Pacific (Hong Kong) Region</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS License Manager is now available in the Asia Pacific (Hong Kong) region. See the <a href="/about-aws/global-infrastructure/regional-product-services/">AWS Region Table</a> for the list of regions where License Manager is currently available. AWS License Manager is offered at no additional charges. To learn more about this service, visit the <a href="https://docs.aws.amazon.com/license-manager/index.html#lang/en_us">product documentation</a>, and <a href="/license-manager/faqs/">FAQ page</a>.</p>
</div>
</div>]<h1 id="Amplify_Framework_now_Supports_Adding_AWS_Lambda_Triggers_for_events_in_Auth_and_Storage_categories"> <a name="Amplify_Framework_now_Supports_Adding_AWS_Lambda_Triggers_for_events_in_Auth_and_Storage_categories"> Amplify Framework now Supports Adding AWS Lambda Triggers for events in Auth and Storage categories</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Starting today, the Amplify CLI (part of the open source <a href="https://aws-amplify.github.io/">Amplify Framework</a>) includes support for adding and configuring AWS Lambda triggers for events when using Amazon Cognito, Amazon Simple Storage Service, and Amazon DynamoDB as event sources. This enables developers to setup customized authentication flows for their mobile and web applications from the Amplify CLI using Amazon Cognito User Pool as an authentication provider.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p> Developers can easily configure capabilities such as adding Google reCAPTCHA challenge, account verification using email, adding user to a Cognito User Pools group, and email domain filtering through templates provided in the CLI. Previously, developers had to manually add and configure the AWS Lambda function from the Lambda console or using CloudFormation.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p> In addition, with this release developers can use the Amplify CLI to easily configure an AWS Lambda function for events when using Amazon S3 and Amazon DynamoDB as storage resources for their mobile and web applications. This also gives developers the ability to grant permissions for interacting with AWS resources from a Lambda function. This updates associated IAM execution role policies without needing to perform manual IAM policy updates.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>For more details about these features, refer to our <a href="https://aws.amazon.com/blogs/mobile/amplify-framework-adds-supports-for-aws-lambda-triggers-in-auth-and-storage-categories/">blog post</a>. To learn more about Amplify Framework, please visit our <a href="https://aws-amplify.github.io/docs/">documentation</a>.  </p>
</div>
</div>]<h1 id="Introducing_Amazon_CloudWatch_Container_Insights_for_Amazon_ECS_and_AWS_Fargate_-_Now_in_Preview"> <a name="Introducing_Amazon_CloudWatch_Container_Insights_for_Amazon_ECS_and_AWS_Fargate_-_Now_in_Preview"> Introducing Amazon CloudWatch Container Insights for Amazon ECS and AWS Fargate - Now in Preview</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon CloudWatch Container Insights is now available in preview to monitor, isolate, and diagnose your containerized applications and microservices environments. With this preview, DevOps and systems engineers have access to automated dashboards summarizing the performance and health of their <a href="/ecs/">Amazon Elastic Container Service (ECS)</a> and <a href="/fargate/">AWS Fargate</a> clusters by tasks, containers, and services.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>You can get started collecting detailed performance metrics, logs, and meta-data from your containers and clusters in just a few clicks from the ECS Management Console or from the AWS CLI. To learn more, follow these steps in the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html">CloudWatch Container Insights documentation</a>. </p>
</div>
</div>]<h1 id="AWS_CodeBuild_adds_Support_for_Polyglot_Builds"> <a name="AWS_CodeBuild_adds_Support_for_Polyglot_Builds"> AWS CodeBuild adds Support for Polyglot Builds</a> </h1>[<div class="aws-text-box">
<div class="">
<p><a href="https://aws.amazon.com/codebuild/" target="_blank">AWS CodeBuild</a> now supports polyglot builds in <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html" target="_blank">CodeBuild’s managed images</a>. Previously, you could only specify a single programming language runtime in these CodeBuild managed images. In order to perform a polyglot build, you either had to rely on a self-managed build images with various runtimes pre-installed or you had to install these additional runtimes inline in your buildspec.</p>
<p>Now, you can simply <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runtime-versions.html#sample-runtime-two-major-version-runtimes" target="_blank">specify one or more programming language versions</a> in your buildspec for your build needs. This is made possible by a concept called "runtime-versions". With runtime-versions, you can also <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runtime-versions.html#sample-runtime-update-version" target="_blank">specify which major version</a> of the runtime should be enabled for your builds.</p>
<p>To learn more about "runtime-versions" please visit our <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runtime-versions.html" target="_blank">documentation</a>. Please visit our <a href="https://aws.amazon.com/codebuild/" target="_blank">product page</a> or <a href="https://console.aws.amazon.com/codebuild" target="_blank">the console</a> to learn more about how to get started with AWS CodeBuild. </p>
</div>
</div>]<h1 id="AWS_Amplify_Console_announces_Manual_Deploys_for_Static_Web_Hosting"> <a name="AWS_Amplify_Console_announces_Manual_Deploys_for_Static_Web_Hosting"> AWS Amplify Console announces Manual Deploys for Static Web Hosting</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amplify Console now provides developers the ability to host a web app by simply uploading a folder from their desktop, or linking to a zip file stored in an S3 bucket or external server.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Developers managing their own CI/CD pipelines can now use the Amplify Console to host their static web app and leverage all the hosting benefits offered such as instant CDN cache invalidation, atomic deploys, password protection, and redirects. Additionally, developers building proof-of-concepts get a shareable URL for their app in seconds without the overhead of connecting a Git repository. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Checkout our launch <a href="https://aws.amazon.com/blogs/mobile/deploy-files-s3-dropbox-amplify-console">blog</a> to learn more, or visit the <a href="http://console.amplify.aws">Amplify Console</a> to get started. </p>
</div>
</div>]<h1 id="Optimize_Cost_with_Amazon_EFS_Infrequent_Access_Lifecycle_Management_"> <a name="Optimize_Cost_with_Amazon_EFS_Infrequent_Access_Lifecycle_Management_"> Optimize Cost with Amazon EFS Infrequent Access Lifecycle Management </a> </h1>[<div class="aws-text-box">
<div class="">
<p>You can now choose from four Amazon Elastic File System (Amazon EFS) Lifecycle Management policies to automatically move files into the EFS Infrequent Access (EFS IA) storage class and save up to 85% as your access patterns change. Additionally, you can now enable Lifecycle Management for all EFS file systems. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>EFS IA provides price/performance that’s cost-optimized for files not accessed every day, enabling you to save up to 85% on file storage costs compared to the Amazon EFS Standard storage class. To get started with EFS IA, you enable Lifecycle Management for your file system, which automatically moves files to the lower-cost storage class based on the last time they were accessed. You can now choose age-off policies of 14, 30, 60, or 90 days. Previously, EFS Lifecycle Management used a pre-defined policy to move files into EFS IA. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>These enhancements are immediately available in all EFS regions. For EFS regional availability, see the <a href="/about-aws/global-infrastructure/regional-product-services/">AWS Region Table</a>. To get started with EFS IA and <a href="/efs/features/infrequent-access/">EFS Lifecycle Management</a>, try it out in the <a href="https://console.aws.amazon.com/efs">AWS Console</a>.</p>
</div>
</div>]<h1 id="Amazon_EC2_Fleet_Functionality_is_Now_Available_via_EC2_Auto_Scaling_in_the_AWS_GovCloud_(US-West)_Region"> <a name="Amazon_EC2_Fleet_Functionality_is_Now_Available_via_EC2_Auto_Scaling_in_the_AWS_GovCloud_(US-West)_Region"> Amazon EC2 Fleet Functionality is Now Available via EC2 Auto Scaling in the AWS GovCloud (US-West) Region</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon EC2 Auto Scaling now lets you provision and automatically scale instances across purchase options, Availability Zones (AZ), and instance families in a single Auto Scaling group (ASG), to optimize scale, performance, and cost. Now you can include <a href="/ec2/spot/">Spot Instances</a> with On-Demand and RIs in a single ASG, to save up to 90% on compute in the AWS GovCloud (US-West) Region.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>EC2 Fleet is an API to provision capacity across purchase options, AZs and instance types. Now this EC2 Fleet functionality is available via EC2 Auto Scaling. Powered by EC2 Fleet, you can now create an ASG by defining which EC2 instance types work for you and how much of the desired capacity should be filled using On-Demand, RI and Spot purchase options. EC2 Auto Scaling continues to optimize and maintain the mix as and when the ASG scales out or scales back, simplifying capacity provisioning and cost optimization with automatic scaling across instances and purchase options. EC2 Auto Scaling also continues to provide lifecycle hooks, instance health checks and scheduled scaling to automate capacity management.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>When setting up an ASG, now you can specify what percentage of your ASG capacity should be fulfilled by On-Demand instances or RIs, and what percentage with Spot Instances. You can also indicate instances types or instances with specific amount of RAM or vCPU in the ASG configurations. EC2 Auto Scaling then provisions the lowest price combination of instances to meet the desired capacity based on these preferences.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>This capability is now available in AWS GovCloud (US-West) Region. Visit <a href="/govcloud-us/">AWS GovCloud (US) homepage</a> to learn more about these regions. To learn more about provisioning and automatically scaling instances across purchase options, Availability Zones (AZ), and instance families with EC2 Auto Scaling, visit this <a href="/blogs/aws/new-ec2-auto-scaling-groups-with-multiple-instance-types-purchase-options/">blog</a>.  </p>
</div>
</div>]<h1 id="Amazon_FSx_for_Lustre_is_Now_Available_in_the_EU_(London)_Region"> <a name="Amazon_FSx_for_Lustre_is_Now_Available_in_the_EU_(London)_Region"> Amazon FSx for Lustre is Now Available in the EU (London) Region</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon FSx for Lustre is now available in the AWS EU (London) Region. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Amazon FSx for Lustre provides a high-performance file system optimized for fast processing of workloads such as machine learning, high performance computing (HPC), video processing, financial modeling, and electronic design automation (EDA). Amazon FSx for Lustre file systems can be configured as standalone file systems or can be linked to an Amazon S3 bucket. When linked to an S3 bucket, an FSx for Lustre file system transparently presents S3 objects as files and allows you to write results back to S3, making it easy for you to process cloud data sets on S3 using a high-performance file system. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>For more information, please visit the <a href="/fsx/lustre/" target="_blank">Amazon FSx for Lustre</a> product page, and see the <a href="/about-aws/global-infrastructure/regional-product-services/" target="_blank">AWS Region Table</a> for complete regional availability information.</p>
</div>
</div>]<h1 id="Amazon_FSx_for_Windows_File_Server_is_Now_Available_in_the_EU_(London)_Region"> <a name="Amazon_FSx_for_Windows_File_Server_is_Now_Available_in_the_EU_(London)_Region"> Amazon FSx for Windows File Server is Now Available in the EU (London) Region</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon FSx for Windows File Server is now available in the AWS EU (London) Region.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Amazon FSx for Windows File Server provides a fully managed native Microsoft Windows file system so you can easily move your Windows-based applications that require shared file storage to AWS. Built on Windows Server, Amazon FSx natively supports the SMB protocol, Windows NTFS, and Active Directory (AD). To meet a broad spectrum of needs, Amazon FSx delivers high levels of throughput and IOPs, and provides consistent sub-millisecond latencies.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>For more information, please visit the <a href="/fsx/windows/" target="_blank">Amazon FSx for Windows File Server</a> product page, and see the <a href="/about-aws/global-infrastructure/regional-product-services/" target="_blank">AWS Region Table</a> for complete regional availability information.</p>
</div>
</div>]<h1 id="AWS_Config_now_enables_you_to_provision_AWS_Config_rules_across_all_AWS_accounts_in_your_organization"> <a name="AWS_Config_now_enables_you_to_provision_AWS_Config_rules_across_all_AWS_accounts_in_your_organization"> AWS Config now enables you to provision AWS Config rules across all AWS accounts in your organization</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Config now supports a <a href="https://docs.aws.amazon.com/config/latest/developerguide/config-rule-multi-account-deployment.html">new set of APIs</a> to manage AWS Config rules across your organization in AWS Organizations. Using this capability, you can centrally create, update, and delete AWS Config rules across all accounts in your organization. This capability is particularly useful if you have a need to deploy a common set of AWS Config rules across all accounts. You can also specify accounts where AWS Config rules should not be created. In addition, you can use these APIs from the master account in AWS Organizations to enforce governance by ensuring that the underlying AWS Config rules are not modifiable by your organization’s member accounts. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>These APIs work for both managed and custom AWS Config rules. For more information, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/config-rule-multi-account-deployment.html">Enabling AWS Config Rules Across all Accounts in Your Organization</a> in the AWS Config Developer Guide.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>The new APIs are available in all commercial AWS Regions where AWS Config and AWS Organizations are supported. For the full list of supported Regions, see <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html">AWS Regions and Endpoints</a> in the AWS General Reference. To learn more about AWS Config, visit the <a href="/config/">AWS Config webpage</a>. To learn more about AWS Organizations, visit the <a href="/organizations/">AWS Organizations webpage</a>. </p>
</div>
</div>]<h1 id="Introducing_AWS_Budgets_Reports"> <a name="Introducing_AWS_Budgets_Reports"> Introducing AWS Budgets Reports</a> </h1>[<div class="aws-text-box">
<div class="">
<p> Starting today, you can create and send daily, weekly, or monthly reports to monitor the performance of your AWS Budgets. Using the new AWS Budgets Reports console, you can easily select the subset of budgets that you would like to include in your report, define the delivery frequency, and specify your email recipients. For example, you can create a report that monitors all budgets for linked accounts belonging to a particular business unit and have that report delivered each morning to that business unit’s engineering, product, and finance leaders.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS Budgets gives you the ability to set custom budgets that alert you when your costs or usage exceed (or are forecasted to exceed) your budgeted amount. You can also use AWS Budgets to set reservation utilization or coverage targets and receive alerts when your metrics drop below the threshold you define. Reservation alerts support Amazon EC2, Amazon RDS, Amazon Redshift, Amazon ElastiCache, and Elasticsearch reservations.</p>
<p>To learn more about AWS Budgets Reports, please refer to the <a href="https://aws.amazon.com/aws-cost-management/aws-budgets/" target="_blank">AWS Budgets</a> webpage or the <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html" target="_blank">Managing your Costs with Budgets</a> user guide. You can also proceed directly to the <a href="https://console.aws.amazon.com/billing/home?#/budgets/reports" target="_blank">AWS Budgets Reports dashboard</a>.</p>
</div>
</div>]<h1 id="Session_Manager_launches_tunneling_support_for_SSH_and_SCP"> <a name="Session_Manager_launches_tunneling_support_for_SSH_and_SCP"> Session Manager launches tunneling support for SSH and SCP</a> </h1>[<div class="aws-text-box">
<div class="">
<p>You can now use AWS Systems Manager Session Manager to tunnel SSH (Secure Shell) and SCP (Secure Copy) traffic between a client and a server. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>You often need to allow SSH and SCP protocol access to cloud and on-premises servers when performing maintenance tasks or troubleshooting problems. These protocols commonly require using an access server (for example, a Bastion host) and maintaining an open inbound port between a client and server, increasing your cost and security risk. With SSH protocol tunneling using Session Manager, you do not need an access server or an open inbound port for SSH-based access and SCP-based file copy. This reduces cost and improves your security posture when using SSH and SCP. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To get started, configure an SSH client that supports ProxyCommand. This will start a Session Manager session to your target instance when the SSH client is used. Subsequent SSH and SCP traffic between your client and the target instance tunnels through a Systems Manager Session Manager connection. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Session Manager is a feature in Systems Manager. Systems Manager enables visibility and control of your cloud and on-premises infrastructure. It provides an integrated experience that combines native features and other AWS services for viewing data and securely automating operational tasks across your infrastructure. This simplifies resource and application management, shortens the time to detect and resolve operational problems, and makes it easier to operate and manage your infrastructure securely at scale.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>This enhancement, and the latest AWS Systems Manager Agent, is available in all AWS Regions where Systems Manager is available. For more information, see our <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html" target="_blank">Documentation</a>. To learn more about Session Manager, visit our <a href="https://aws.amazon.com/systems-manager/" target="_blank">Product Page</a>.</p>
</div>
</div>]<h1 id="Session_Manager_launches_Run_As_to_start_interactive_sessions_with_your_own_operating_system_user_account"> <a name="Session_Manager_launches_Run_As_to_start_interactive_sessions_with_your_own_operating_system_user_account"> Session Manager launches Run As to start interactive sessions with your own operating system user account</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS Systems Manager Session Manager now lets you define the operating system user account that an interactive shell uses on an instance. You can associate an operating system user with your IAM principal (user or role) for Session Manager. You can also set the operating system user in your Session Manager preferences. This enables you to better manage shell privileges for multiple users that need interactive access to instances. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To get started, go to the AWS Identity and Access Management (IAM) console in your account to tag your users and roles with the operating system user account value that Session Manager should use. Then enable Run As in your account’s Session Manager preferences in the Systems Manager console. New sessions will use the value from this IAM tag as the operating system user when starting a session.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Session Manager is a feature in Systems Manager. Systems Manager enables visibility and control of your cloud and on-premises infrastructure. It provides an integrated experience that combines native features and other AWS services for viewing data and securely automating operational tasks across your infrastructure. This simplifies resource and application management, shortens the time to detect and resolve operational problems, and makes it easier to operate and manage your infrastructure securely at scale. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>This enhancement, and the latest AWS Systems Manager Agent, is available in all AWS Regions where Systems Manager is available. For more information, see our <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html" target="_blank">Documentation</a>. To learn more about Session Manager, visit our <a href="https://aws.amazon.com/systems-manager/" target="_blank">Product Page</a>.</p>
</div>
</div>]<h1 id="AWS_Elemental_MediaLive_Now_Supports_AWS_CloudFormation"> <a name="AWS_Elemental_MediaLive_Now_Supports_AWS_CloudFormation"> AWS Elemental MediaLive Now Supports AWS CloudFormation</a> </h1>[<div class="aws-text-box">
<div class="">
<p>You can now use <a href="https://aws.amazon.com/cloudformation/">AWS CloudFormation</a> templates to create and configure AWS Elemental MediaLive channels (both inputs and outputs). This improvement enables you to use AWS CloudFormation to deploy MediaLive resources in a secure, efficient, and repeatable way.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p><a href="https://aws.amazon.com/medialive/">AWS Elemental MediaLive</a> is a broadcast-grade live video processing service. It lets you create high-quality live video streams for delivery to broadcast televisions and internet-connected multiscreen devices, like connected TVs, tablets, smartphones, and set-top boxes.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>The service functions independently or as part of <a href="https://aws.amazon.com/media-services/">AWS Elemental Media Services</a>, a family of services that form the foundation of cloud-based workflows and offer you the capabilities you need to transport, create, package, monetize, and deliver video.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Visit the <a href="https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/">AWS region table</a> for a full list of AWS Regions where AWS Elemental MediaLive is available.</p>
</div>
</div>]<h1 id="Introducing_Amazon_CloudWatch_Anomaly_Detection_–_Now_in_Preview"> <a name="Introducing_Amazon_CloudWatch_Anomaly_Detection_–_Now_in_Preview"> Introducing Amazon CloudWatch Anomaly Detection – Now in Preview</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon CloudWatch Anomaly Detection applies machine-learning algorithms to continuously analyze system and application metrics, determine a normal baseline, and surface anomalies with minimal user intervention. You can use Anomaly Detection to isolate and troubleshoot unexpected changes in your metric behavior. <br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>You can apply CloudWatch Anomaly Detection on metrics in your account, including custom and AWS services metrics. CloudWatch Anomaly Detection will automatically determine a range of expected behavior, which you can optionally customize by specifying data exclusion periods, anomaly sensitivity, and daylight-savings time zone. You can create alarms to notify you when anomalies occur and visualize the expected behavior on a metric graph.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Get started by enabling Anomaly Detection via the AWS Management Console, AWS Command Line Interface, and AWS SDKs. Anomaly Detection is available in preview in all commercial AWS Regions except the Asia Pacific (Hong Kong) and China Regions. CloudWatch Anomaly Detection is priced per alarm. To learn more, please visit the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html">CloudWatch Anomaly Detection documentation</a> and <a href="https://aws.amazon.com/cloudwatch/pricing/">pricing</a> pages.</p>
</div>
</div>]<h1 id="AWS_IoT_Expands_Globally"> <a name="AWS_IoT_Expands_Globally"> AWS IoT Expands Globally</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS IoT Core, AWS IoT Device Management, and AWS IoT Device Defender are now available in multiple additional regions. <br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p><a href="/iot-core/">AWS IoT Core</a> is now available in 5 additional regions - US West (N. California), Canada (Central), EU (Paris), EU (Stockholm), and South America (Sao Paulo), extending the footprint to 18 AWS regions. AWS IoT Core is a managed cloud platform that lets billions of connected devices easily and securely interact with cloud applications and other devices. <br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p><a href="/iot-device-management/">AWS IoT Device Management</a> is now available in 5 additional regions - US West (N. California), Canada (Central), EU (Paris), EU (Stockholm), and South America (Sao Paulo), extending the footprint to 18 AWS regions. AWS IoT Device Management is a managed service that lets you securely onboard, organize, monitor, and remotely manage your IoT devices at scale throughout their lifecycle. <br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p><a href="/iot-device-defender/">AWS IoT Device Defender</a> is now available in 3 additional regions - US West (N. California), Canada (Central), and Asia Pacific (Mumbai), extending the footprint to 13 AWS regions. AWS IoT Device Defender is a fully-managed AWS IoT service that makes it easy for customers to manage the end to end security of their IoT fleet.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Please see the <a href="https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/">AWS Regions page</a> for all the regions where the services are now available. Visit our IoT website to learn more about <a href="/iot/">AWS IoT services</a>. </p>
</div>
</div>]<h1 id="Amazon_Aurora_with_PostgreSQL_Compatibility_Supports_Serverless"> <a name="Amazon_Aurora_with_PostgreSQL_Compatibility_Supports_Serverless"> Amazon Aurora with PostgreSQL Compatibility Supports Serverless</a> </h1>[<div class="aws-text-box">
<div class="">
<p><a href="https://aws.amazon.com/rds/aurora/serverless/" target="_blank">Amazon Aurora Serverless</a> is now available for Amazon Aurora with PostgreSQL compatibility. It is a new deployment option that automatically starts, scales, and shuts down an <a href="https://aws.amazon.com/rds/aurora/" target="_blank">Amazon Aurora</a> database, and it offers database capacity without the need to provision, scale, and manage any database servers.</p>
<p>Many applications have intermittent or cyclical usage patterns. For example, retail applications experience seasonal spikes, development and test workloads require database access only at certain times of the day or week, and new applications face unknown usage demands. This creates a capacity planning dilemma, since you must either over-provision database capacity upfront and pay for resources you won’t use, or under-provision resources and risk performance problems and a poor user experience.<br/> <br/> With Amazon Aurora Serverless, you no longer have to provision or manage database capacity. The database automatically and quickly starts, scales, shuts down, and starts up again in seconds, based on the needs of the workload. You simply create an endpoint through the <a href="https://console.aws.amazon.com/rds" target="_blank">Amazon RDS Management Console</a>, and Amazon Aurora Serverless handles the rest. You <a href="https://aws.amazon.com/rds/aurora/pricing/" target="_blank">pay by the second</a>, and only when the database is in use.<br/> <br/> Read about Aurora Serverless on the <a href="http://aws.amazon.com/blogs/aws/amazon-aurora-postgresql-serverless-now-generally-available" target="_blank">AWS Blog</a>, the Aurora Serverless <a href="https://aws.amazon.com/rds/aurora/" target="_blank">product page</a>, and in the <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html" target="_blank">Aurora documentation</a>.<br/> <br/> Amazon Aurora is a fully managed relational database that combines the performance and availability of high-end commercial databases with the simplicity and cost-effectiveness of open source databases. Aurora PostgreSQL Serverless is available in the US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), and Asia Pacific (Tokyo) regions, and will expand to additional regions in the coming year.</p>
</div>
</div>]<h1 id="Amazon_Elasticsearch_Service_increases_data_protection_with_automated_hourly_snapshots_at_no_extra_charge"> <a name="Amazon_Elasticsearch_Service_increases_data_protection_with_automated_hourly_snapshots_at_no_extra_charge"> Amazon Elasticsearch Service increases data protection with automated hourly snapshots at no extra charge</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon Elasticsearch Service has increased its snapshot frequency from daily to hourly, providing more granular recovery points. If you need to restore your cluster, you now have numerous, recent snapshots to choose from. These automated snapshots are retained for 14 days at no extra charge.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Hourly snapshots are automatically enabled for domains running Elasticsearch versions 5.3 and above — no action is required on your part. For more information on how to access automated snapshots and perform restore operation, please refer to the <a href="https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains-snapshots.html">documentation</a>.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Hourly snapshots are now available on Amazon Elasticsearch Service across 21 regions globally: US East (N. Virginia, Ohio), US West (Oregon, N. California), AWS GovCloud (US-Gov-East, US-Gov-West), Canada (Central), South America (Sao Paulo), EU (Ireland, London, Frankfurt, Paris, Stockholm), Asia Pacific (Singapore, Sydney, Tokyo, Seoul, Mumbai, Hong Kong), and China (Beijing – operated by Sinnet, Ningxia – operated by NWCD). Please refer to the <a href="/about-aws/global-infrastructure/regional-product-services/">AWS Region Table</a> for more information about Amazon Elasticsearch Service availability. </p>
</div>
</div>]<h1 id="Amazon_RDS_for_PostgreSQL_Supports_New_Minor_Versions_11.4,_10.9,_9.6.14,_9.5.18,_and_9.4.23_"> <a name="Amazon_RDS_for_PostgreSQL_Supports_New_Minor_Versions_11.4,_10.9,_9.6.14,_9.5.18,_and_9.4.23_"> Amazon RDS for PostgreSQL Supports New Minor Versions 11.4, 10.9, 9.6.14, 9.5.18, and 9.4.23 </a> </h1>[<div class="aws-text-box">
<div class="">
<p>Following the recent announcement of updates to the <a href="https://www.postgresql.org/about/news/1949/">PostgreSQL database</a>, we have updated <a href="https://aws.amazon.com/rds/postgresql/">Amazon RDS for PostgreSQL</a> to support PostgreSQL minor versions. This release contains an important security fix and also bug fixes and improvements done by the PostgreSQL community. </p>
<p>With this release, pg_hint_plan extension has been updated for PostgreSQL versions 11, 10, 9.6 and 9.5.</p>
<p>Amazon RDS for PostgreSQL makes it easy to set up, operate, and scale PostgreSQL deployments in the cloud. Learn more about upgrading your database instances from the <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.html">Amazon RDS User Guide</a>. See <a href="https://aws.amazon.com/rds/postgresql/pricing/">Amazon RDS for PostgreSQL Pricing</a> for pricing details and regional availability.</p>
</div>
</div>]<h1 id="Amazon_DocumentDB_(with_MongoDB_compatibility)_Now_Provides_Cluster_Deletion_Protection"> <a name="Amazon_DocumentDB_(with_MongoDB_compatibility)_Now_Provides_Cluster_Deletion_Protection"> Amazon DocumentDB (with MongoDB compatibility) Now Provides Cluster Deletion Protection</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon DocumentDB is a fast, scalable, highly available, and fully managed document database service that supports MongoDB workloads. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>You can now enable deletion protection for your Amazon DocumentDB clusters to help you prevent against accidental deletion of a cluster. When a cluster is configured with deletion protection, the cluster cannot be deleted by any user. Deletion protection is available for Amazon DocumentDB in all <a href="/about-aws/global-infrastructure/regional-product-services/">supported regions</a>.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Deletion protection is now enabled by default in the Amazon DocumentDB management console. You can also turn on or off deletion protection for an existing cluster with a few clicks in the Amazon DocumentDB management console or using the AWS Command Line Interface (CLI). Deletion protection is enforced by management console, AWS CLI, and AWS CloudFormation.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more about Amazon DocumentDB and deletion protection, please see our <a href="/documentdb/">product page</a> and <a href="https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html">documentation</a>.</p>
</div>
</div>]<h1 id="US_commercial_regions_now_accept_Chinese_Yuan_payments_from_China_based_customers."> <a name="US_commercial_regions_now_accept_Chinese_Yuan_payments_from_China_based_customers."> US commercial regions now accept Chinese Yuan payments from China based customers.</a> </h1>[<div class="aws-text-box">
<div class="">
<p>AWS now supports China based customers, who use services in US commercial regions, to pay their invoices from Amazon Web Services, Inc. (“AWS Inc.”) in Chinese Yuan through a China UnionPay credit card.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS has partnered with Lianlian Yintong Electronic Payment Co., Ltd. (“Lianlian Pay”), a licensed payment processor in China, to enable China based customers using services billed by AWS Inc. to pay their invoices in Chinese Yuan. Customers no longer need to navigate complicated and time consuming foreign exchange requirements to produce the US dollars needed to pay their monthly invoice. Starting today, customers only need to conduct a one-time registration process through the AWS Billing Console to bind their China UnionPay credit card to their AWS account. One registered, customer’s following month anniversary billings will be deducted automatically through their China UnionPay credit card in Chinese Yuan. </p>
</div>
</div>]<h1 id="AWS_WAF_and_AWS_Shield_Advanced_Now_Available_in_EU_(Paris),_Canada_(Central),_Asia_Pacific_(Mumbai),_and_South_America_(Sao_Paulo)"> <a name="AWS_WAF_and_AWS_Shield_Advanced_Now_Available_in_EU_(Paris),_Canada_(Central),_Asia_Pacific_(Mumbai),_and_South_America_(Sao_Paulo)"> AWS WAF and AWS Shield Advanced Now Available in EU (Paris), Canada (Central), Asia Pacific (Mumbai), and South America (Sao Paulo)</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Starting today, AWS WAF and AWS Shield Advanced are available in four new regions: EU (Paris), Canada (Central), Asia Pacific (Mumbai), and South America (Sao Paulo). </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS WAF is a web application firewall that helps protect your web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources. AWS WAF gives you control over which traffic to allow or block to your web applications by defining customizable web security rules. AWS WAF can be deployed on Amazon CloudFront, Application Load Balancer, and Amazon API Gateway. To learn more visit the detailed page <a href="/waf/">here</a>. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards web applications running on AWS. AWS Shield provides always-on detection and automatic inline mitigations that minimize application downtime and latency, so there is no need to engage AWS Support to benefit from DDoS protection. There are two tiers of AWS Shield - Standard and Advanced. To learn more visit the detailed page <a href="/shield/">here</a>. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>AWS WAF and AWS Shield Advanced are now available on Amazon CloudFront and 16 AWS regions: US East (N. Virginia), US East (Ohio), US West (Oregon), US West (N. California), EU (Ireland), EU (Frankfurt), EU (London), EU (Stockholm), EU (Paris), Asia Pacific (Tokyo), Asia Pacific (Sydney), Asia Pacific (Singapore), Asia Pacific (Mumbai), Asia Pacific (Seoul), South America (Sao Paulo), and Canada (Central). AWS Shield Advanced is also available on Amazon Route 53. </p>
</div>
</div>]<h1 id="AWS_Amplify_Console_Updates_Build_image_with_SAM_CLI_and_Custom_Container_Support"> <a name="AWS_Amplify_Console_Updates_Build_image_with_SAM_CLI_and_Custom_Container_Support"> AWS Amplify Console Updates Build image with SAM CLI and Custom Container Support</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Today, the Amplify Console launched several updates to the build service including SAM CLI and custom container support. The Amplify Console offers a Git-based workflow for continuously deploying and hosting fullstack serverless web apps. <br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>The default build image is now using Amazon Linux 2 with Node 10 and SAM CLI pre-installed. Custom containers allow developer to swap out the default container with their own build environment. At build time, Amplify will retrieve the Docker image from the container registry specified in the project configuration and use the environment to compile your source code, run your tests, and deploy your application. With the SAM CLI, developers can run SAM commands as part of their backend deployment without installing any other dependencies.<br/> </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Learn more by visiting our <a href="https://docs.aws.amazon.com/amplify/latest/userguide/custom-build-image.html">documentation</a>. </p>
</div>
</div>]None[<div class="aws-text-box">
<div class="">
<p>The <a href="/partners/" target="_blank">AWS Partner Network (APN)</a> launched the <a href="/manufacturing/partner-solutions/" target="_blank">AWS Industrial Software Competency</a> in 2018 that verifies, validates, and vets top <a href="https://aws.amazon.com/blogs/apn/how-aws-industrial-software-competency-partners-are-shaping-the-next-industrial-revolution/" target="_blank">APN Technology Partners</a> with solutions for an end-to-end Industrial Software value chain. These Independent Software Vendors (ISVs) provide technology offerings targeting one or more of the primary steps in discrete manufacturing or process industries: Product Design, Production Design, and Production/Operations.</p>
<p>Launching soon, a correlative track for best-in-class APN Consulting Partners designed to connect customers with highly-specialized Industrial Software System Integrators. These APN Partners can help customers achieve meaningful outcomes and support exploration and integration with top solutions designed specifically for this industry.</p>
<p>To receive the AWS Industrial Software Competency designation, APN Partners must undergo rigorous technical validation related to industry-specific technology, as well as an assessment of the security, performance, and reliability of their AWS solutions. This validation gives customers complete confidence in choosing top APN Partner solutions from the tens of thousands in the AWS Partner Network.</p>
<p>APN Consulting Partners with the AWS Industrial Software Competency will support the following categories:</p>
<ul>
<li><b>Product Design:</b> Applications and services used in the design phase, including Computer Aided Design (CAD), Computer Aided Engineering (CAE), Electronic Design Automation (EDA), Product Lifecycle Management (PLM), Product Data Management (PDM), and Civil Engineering</li>
<li><b>Production Design:</b> Applications for factory layout and Computer-Aided Manufacturing (CAM), Product Lifecycle Management (PLM), Product Data Management (PDM)</li>
<li><b>Production &amp; Operations:</b> Discrete and process industry applications like Manufacturing Execution Systems (MES), Manufacturing Operations Management (MOM), Plant Information Management System (PIMS), supply chain logistics, Industrial Internet of Things (IIoT), analytic applications for industrial use, and manufacturing specific Enterprise Resource Planning (ERP) solutions</li>
</ul>
<p>Congratulations to the Advanced and Premier tier APN Partners that are paving the way for this new AWS Competency designation:</p>
<p><b><a href="https://www.reply.com/storm-reply/en/?utm_source=AWSWebsite&amp;utm_medium=referral&amp;utm_campaign=AWSIndustrialCompetency&amp;utm_term=&amp;utm_content=" target="_blank">Storm Reply</a></b></p>
<p><i>Premier APN Consulting Partner based in Italy</i><br/> With a deep knowledge of the business processes of industrial and manufacturing companies, Storm Reply supports customers to build Industrial IoT solutions and provides digital platform to process real time data coming from factories, providing services on top like Machine Learning training and computation, big data processing, data warehousing and business logic.</p>
<p><a href="https://www2.deloitte.com/us/en/pages/about-deloitte/solutions/deloitte-aws-relationship.html" target="_blank"><b>Deloitte</b></a></p>
<p><i>Premier APN Consulting Partner based in US</i><br/> The manufacturing industry is ever changing. Rapid globalization, technological advancements, changing consumer preferences, and evolving government policies are reshaping the manufacturing industry, exponentially accelerating the pace of competition and continually raising the bar on company performance. Deloitte serves more than 95% of the Fortune 500 Industrial Manufacturing companies and can help anticipate, plan for, and manage the dramatic swings that characterize this market.</p>
<p><a href="https://www.accenture.com/us-en/industries/industrial-equipment-index" target="_blank"><b>Accenture </b></a></p>
<p><i>Premier APN Consulting Partner based in US</i><br/> Accenture is a leading global professional services company, providing a broad range of services and solutions in strategy, consulting, digital, technology and operations. Accenture helps help Industrial Equipment companies digitally transform their business through smart, connected and living technologies, to become Industry X.0 businesses.</p>
<p><a href="https://www.wipro.com/process-and-industrial-manufacturing/" target="_blank"><b>Wipro </b></a></p>
<p><i>Premier APN Consulting Partner based in India</i><br/> Wipro helps Industrial and Manufacturing businesses in their digital transformation journey of achieving operational excellence and superior customer experience across the entire value chain through continuous innovation, leveraging a combination of its own IPs and Platforms and the power of an unparalleled ecosystem of partners like AWS.</p>
<p>Contact your Partner Development Manager (PDM) to learn more about becoming an AWS Industrial Software Competency Partner! You can find the <a href="https://s3-us-west-2.amazonaws.com/competency.awspartner.com/Industrial+Software/AWS+Indistrial+Software+Competency+Consulting+Partner+Validation+Checklist.pdf" target="_blank">requirements here</a>. </p>
</div>
</div>]<h1 id="Amazon_DocumentDB_(with_MongoDB_compatibility)_Now_Supports_Stopping_and_Starting_Clusters"> <a name="Amazon_DocumentDB_(with_MongoDB_compatibility)_Now_Supports_Stopping_and_Starting_Clusters"> Amazon DocumentDB (with MongoDB compatibility) Now Supports Stopping and Starting Clusters</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon DocumentDB is a fast, scalable, highly available, and fully managed document database service that supports MongoDB workloads. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Amazon DocumentDB now allows you to stop and start clusters. Stopping and starting clusters makes it easy and affordable to use Amazon DocumentDB clusters for development and test purposes where the cluster is not required to be running all of the time. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p> Stopping and starting a cluster requires just a few clicks in the AWS Management Console or a single call using the AWS Command Line Interface and takes just a few minutes to complete. Stopping a cluster stops the primary instance and all replica instances. While your cluster is stopped, you are charged for cluster storage, manual snapshots and automated backup storage within your specified retention window, but not for instance hours. You can stop a cluster for up to seven days at a time. After seven days, the cluster will be automatically started.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>To learn more about Amazon DocumentDB and stopping and starting clusters, please see our <a href="/documentdb/">product page</a> and <a href="https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html">documentation</a>.</p>
</div>
</div>]<h1 id="AWS_CodeCommit_Now_Supports_Resource_Tagging"> <a name="AWS_CodeCommit_Now_Supports_Resource_Tagging"> AWS CodeCommit Now Supports Resource Tagging</a> </h1>[<div class="aws-text-box">
<div class="">
<p>You can now assign tags to AWS CodeCommit repositories. With tags, you can group and find repositories with a common tag as well as define AWS Identity and Access Management (IAM) permissions based on tags. You can tag existing repositories as well as add tags to new repositories when you create them. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Each tag is a simple label consisting of a customer-defined key and an optional value that can make it easier to manage, search for, and <a href="https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html" target="_blank">filter resources</a>. IAM policies also support tag-based conditions, enabling you to constrain IAM permissions based on specific tags or tag values. For example, you can tag your repositories to ensure only selected groups of users have access based on those tags.</p>
<p>These features are provided at no additional cost. To learn more about AWS CodeCommit and tagging, see <a href="https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-tag-repository.html" target="_blank">the documentation</a>. See <a href="https://aws.amazon.com/answers/account-management/aws-tagging-strategies" target="_blank">AWS Tagging Strategies</a> for general best practices for using tags with AWS resources.</p>
<p>Learn more about AWS CodeCommit by visiting our <a href="https://aws.amazon.com/codecommit" target="_blank">product page</a>. You can see a full list of AWS Regions where AWS CodeCommit is available <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html#codecommit_region" target="_blank">here</a>.<br/>  </p>
</div>
</div>]<h1 id="Amazon_DynamoDB_now_supports_deleting_a_global_secondary_index_before_it_finishes_building"> <a name="Amazon_DynamoDB_now_supports_deleting_a_global_secondary_index_before_it_finishes_building"> Amazon DynamoDB now supports deleting a global secondary index before it finishes building</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Now, you can use the <a href="https://aws.amazon.com/dynamodb/" target="_blank">Amazon DynamoDB</a> console or the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html" target="_blank">UpdateTable</a> API/CLI to delete a global secondary index even as it’s being created. Previously, you could not cancel the creation of a global secondary index—indexes could only be deleted once they finished building. This can help you save time if you no longer want a global secondary index or if you want a new global secondary index with different attribute projections. To learn more, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.OnlineOps.html#GSI.OnlineOps.Deleting" target="_blank">Deleting a Global Secondary Index From a Table</a> in the DynamoDB Developer Guide.</p>
</div>
</div>]<h1 id="Amazon_RDS_Introduces_Compatibility_Checks_for_Upgrades_from_MySQL_5.7_to_MySQL_8.0"> <a name="Amazon_RDS_Introduces_Compatibility_Checks_for_Upgrades_from_MySQL_5.7_to_MySQL_8.0"> Amazon RDS Introduces Compatibility Checks for Upgrades from MySQL 5.7 to MySQL 8.0</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon Relational Database Service (RDS) now performs checks to confirm compatibility of your MySQL 5.7 database with MySQL 8.0, and stops the upgrade if incompatibilities are found.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>RDS automatically looks for incompatibilities when you initiate an upgrade from MySQL 5.7 to 8.0. This capability helps you avoid unplanned downtimes, as the compatibility checks are performed before the instance is stopped for the upgrade. RDS sends you an <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html">RDS event notification</a> whenever an incompatible upgrade is detected. You can review the PrePatchCompatibility log file generated by RDS for detailed information on each incompatibility and take actions to correct it. </p>
<p> Read more about database upgrade prechecks in our <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.html#USER_UpgradeDBInstance.MySQL.57to80Prechecks">documentation</a>. To initiate an upgrade from MySQL 5.7 to 8.0, visit the <a href="https://console.aws.amazon.com/rds/home">RDS console</a> or download the latest <a href="https://aws.amazon.com/tools/#sdk">AWS SDK or CLI</a>.<br/> </p>
</div>
</div>]<h1 id="Amazon_Aurora_Supports_Cloning_Across_AWS_Accounts"> <a name="Amazon_Aurora_Supports_Cloning_Across_AWS_Accounts"> Amazon Aurora Supports Cloning Across AWS Accounts</a> </h1>[<div class="aws-text-box">
<div class="">
<p>You can now share your Amazon Aurora DB clusters with other AWS accounts for quick and efficient database cloning.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Database cloning is faster than restoring a snapshot and requires no additional space at the time of creation. You are only charged for additional storage if you make data changes in the cloned DB cluster. Cross-account database cloning could be useful, for example, when you have separate accounts for production and testing. You can use the clone to verify schema changes, test different parameters, and run analytic queries on production data without providing direct access to the production account or impacting the performance of the production database. </p>
<p> Both MySQL- and PostgreSQL-compatible editions of Amazon Aurora support cross-account database cloning. Read more about database cloning in the <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Clone.html#Aurora.Managing.Clone.Cross-Account">Aurora documentation</a>. To create a cross-account database clone, visit the <a href="https://console.aws.amazon.com/rds/home">AWS Management Console</a> or download the latest <a href="https://aws.amazon.com/tools/#sdk">AWS SDK or CLI</a>.</p>
<p> Aurora integrates with <a href="https://aws.amazon.com/ram/">AWS Resource Access Manager (RAM)</a>, enabling you to securely share DB clusters with other accounts for cloning. This capability is supported in all AWS regions where Aurora and RAM are available. Refer the <a href="https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/">AWS Region Table</a> for regional availability.</p>
</div>
</div>]<h1 id="Amazon_API_Gateway_Now_Supports_Tag-Based_Access_Control_and_Tags_on_WebSocket_APIs"> <a name="Amazon_API_Gateway_Now_Supports_Tag-Based_Access_Control_and_Tags_on_WebSocket_APIs"> Amazon API Gateway Now Supports Tag-Based Access Control and Tags on WebSocket APIs</a> </h1>[<div class="aws-text-box">
<div class="">
<p>Amazon API Gateway now offers tag-based access control for WebSocket APIs using AWS Identity and Access Management (IAM) policies, enabling you to easily categorize API Gateway resources for WebSocket APIs by purpose, owner, or other criteria.  </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Tags are simple key-value pairs that you can define on API Gateway resources. Previously, API Gateway supported tags on REST API related resources. With the addition of tag-based access control to WebSocket resources, you can now give permissions to WebSocket resources at various levels by creating policies based on tags. For example, you can grant full access to admins to while limiting access to developers. To see the complete list of top-level API Gateway resources and to learn more about how to use tags to control access, read our <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging-iam-policy.html">documentation</a>. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>You can tag API Gateway resources using the API Gateway console, AWS CLI, or AWS SDK. For more information about API Gateway, visit the <a href="/api-gateway/">product page</a>. Tag-based access control is available in all regions where API Gateway is available. To see all regions where API Gateway is available, see the <a href="/about-aws/global-infrastructure/regional-product-services/">AWS region table</a>.</p>
</div>
</div>]<h1 id="Amazon_DynamoDB_now_supports_up_to_25_unique_items_and_4_MB_of_data_per_transactional_request_in_the_AWS_China_(Beijing)_Region,_Operated_by_Sinnet,_and_the_AWS_China_(Ningxia)_Region,_Operated_by_NWCD"> <a name="Amazon_DynamoDB_now_supports_up_to_25_unique_items_and_4_MB_of_data_per_transactional_request_in_the_AWS_China_(Beijing)_Region,_Operated_by_Sinnet,_and_the_AWS_China_(Ningxia)_Region,_Operated_by_NWCD"> Amazon DynamoDB now supports up to 25 unique items and 4 MB of data per transactional request in the AWS China (Beijing) Region, Operated by Sinnet, and the AWS China (Ningxia) Region, Operated by NWCD</a> </h1>[<div class="aws-text-box">
<div class="">
<p><a href="https://aws.amazon.com/dynamodb/" target="_blank">Amazon DynamoDB</a> now supports up to 25 unique items and 4 MB of data per transactional request in the AWS China (Beijing) Region, Operated by Sinnet, and the AWS China (Ningxia) Region, Operated by NWCD. Transactions enable developers to simplify their code and support workflows and business logic that require adding, updating, or deleting multiple items as a single, all-or-nothing operation. </p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>DynamoDB transactions provide atomic, consistent, isolated, and durable (ACID) operations so that developers can maintain data correctness in applications more easily. With support for transactions with up to 25 unique items and 4 MB of data, developers can now use the DynamoDB transactional APIs to process larger transactions, such as large retail orders or financial transactions.</p>
</div>
</div>, <div class="aws-text-box section">
<div class="">
<p>Support for transactions is available in all AWS Regions where DynamoDB is available. Pricing for transactions is based on the sizes of the items in your transactions. To get started with DynamoDB transactions, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transactions.html" target="_blank">Amazon DynamoDB Transactions</a>. </p>
</div>
</div>]