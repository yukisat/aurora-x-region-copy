## aurora-x-region-copy
Using RDS Event Notification. Lambda cross-region copy

### Sequence of events
Amazon RDS event notification → SNS → Lambda

### Amazon RDS event notification
RDS resources eligible for event subscription
- DB snapshot
category
- backup

### Supported Event ID
> backup
> RDS-EVENT-0169
> Automated cluster snapshot created.

> backup
> RDS-EVENT-0075
> A manual DB cluster snapshot has been created.

### Lambda
Python3.7
