import json
import boto3
import os
import re

def lambda_handler(event, context):
    
      rds = boto3.client('rds', region_name='ap-northeast-3')

      message_unicode = event['Records'][0]['Sns']['Message']
      message_dist = json.loads(message_unicode)
      SourceDBClusterSnapshotId = message_dist['Source ARN']
      SourceSnapshotName = message_dist['Source ID']
      SourceSnapshotName = re.sub('rds\:', '', SourceSnapshotName)
      EventId = message_dist['Event ID']
      EventId = EventId.split("#")
      EventId_dist = EventId[1]

      if EventId_dist == "RDS-EVENT-0169":
          response = rds.copy_db_cluster_snapshot(
            SourceDBClusterSnapshotIdentifier = SourceDBClusterSnapshotId,
            TargetDBClusterSnapshotIdentifier = SourceSnapshotName,
            CopyTags=True,
            SourceRegion='ap-northeast-1'
          )
          print(response)
      elif EventId_dist == "RDS-EVENT-0075":
          response = rds.copy_db_cluster_snapshot(
            SourceDBClusterSnapshotIdentifier = SourceDBClusterSnapshotId,
            TargetDBClusterSnapshotIdentifier = SourceSnapshotName,
            CopyTags=True,
            SourceRegion='ap-northeast-1'
          )
          print(response)
      else:
          print('Event ID other than completion.')
