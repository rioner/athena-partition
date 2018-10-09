import boto3
import datetime

def lambda_handler(event, context):
    # タイムゾーンの生成
    JST = timezone(timedelta(hours=+9), 'JST')    
    
    now = datetime.now(JST)
    print(now.strftime("%Y/%m/%d")) #2018/10/02

    client = boto3.client('athena')
    response = client.start_query_execution(
        QueryString="ALTER TABLE ap_northeast_1\nADD PARTITION (dt='" + now.strftime("%Y%m%d") + "')\nlocation 's3://bucket名/AWSLogs/アカウント番号/vpcflowlogs/ap-northeast-1/" + now.strftime("%Y/%m/%d") + "';",
        QueryExecutionContext={
            'Database': 'vpc_flow_logs'
        },
        ResultConfiguration={
            'OutputLocation': 's3://aws-athena-query-results-アカウント番号-ap-northeast-1/'
        }
    )
