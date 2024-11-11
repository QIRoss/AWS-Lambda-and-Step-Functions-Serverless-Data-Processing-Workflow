import json

def lambda_handler(event, context):
    data = event.get("processed_data", "No data received")
    print(f"Logging data: {data}")
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Data logged successfully!',
            'logged_data': data
        })
    }
