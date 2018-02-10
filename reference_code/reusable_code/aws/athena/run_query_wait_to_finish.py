import boto3
import time
from datetime import datetime


def run_query_and_wait_to_complete():
    aws_kwargs = dict(
        region_name="X",
        aws_access_key_id="X",
        aws_secret_access_key="X"
    )
    client = boto3.client('athena', **aws_kwargs)
    athena_query = 'MSCK REPAIR TABLE org'
    athena_db = 'org_backup_db'
    # the bucket is automatically created if it doesn't exist  
    # and the name is not taken
    d = datetime.utcnow()
    athena_output_location = ('s3://test-org-backup/%s/%s/%s/' % 
                              (d.year, d.month, d.day)) 
    response = client.start_query_execution(
        QueryString=athena_query,
        QueryExecutionContext={
            'Database': athena_db
        },
        ResultConfiguration={
            'OutputLocation': athena_output_location
        }
    )

    print(response)

    query_execution_id = response['QueryExecutionId']
    states_to_wait = ['SUBMITTED', 'QUEUED', 'RUNNING']
    # the rest states are ['SUCCEEDED', 'FAILED', 'CANCELLED']
    while True:
        execution_result = client.get_query_execution(
            QueryExecutionId=query_execution_id)
        execution_state = execution_result['QueryExecution']['Status']['State']
        print('Query execution state: %s' % execution_state)
        if execution_state in states_to_wait:
            time.sleep(0.5)
        else:
            break

    print('Finished execution')


if __name__ == '__main__':
    run_query_and_wait_to_complete()
