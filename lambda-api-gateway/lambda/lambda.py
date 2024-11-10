import json

def lambda_handler(event, context):
    data = event.get("body")
    processed_data = data.upper()
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Data processed successfully!',
            'processed_data': processed_data
        })
    }
