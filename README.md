# AWS Lambda and Step Functions Serverless Data Processing Workflow

Studies based in day 53-54 of 100 Days System Design for DevOps and Cloud Engineers.

https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f

Days 71–80: High-Performance Computing (HPC) and Data Processing

Day 77–78: Implement a serverless data processing workflow using AWS Lambda and AWS Step Functions.

## Project Overview

This project consists of two components focused on implementing serverless data processing workflows using AWS Lambda, API Gateway, and AWS Step Functions:

* Lambda API Gateway Project: This project demonstrates how to expose AWS Lambda functions via API Gateway, enabling external HTTP requests to trigger serverless functions.

* Lambda Step Functions Project: This project demonstrates how to use AWS Step Functions to orchestrate workflows involving multiple AWS Lambda functions for data processing, logging, and other tasks.

Both projects are intended for practical learning and hands-on experience with serverless architecture, providing a foundational understanding of building and deploying serverless workflows using AWS services.

## How to Use

### Lambda API Gateway

This project demonstrates the use of AWS Lambda in conjunction with API Gateway to process HTTP requests from a FastAPI application.

1. Setup:

* Ensure you have AWS CLI configured and access to create Lambda functions and API Gateway endpoints.

* Deploy the resources using Terraform as described in the project files.

2. Functionality:

* The FastAPI application serves as an HTTP client that sends POST requests to the API Gateway endpoint.

* The API Gateway triggers an AWS Lambda function that processes the data and returns a response.

3. Usage:

* Build and run the FastAPI application in a Docker container:
```
docker build -t fastapi-app .
docker run -d -p 8000:8000 fastapi-app
```

* Send a POST request to the FastAPI endpoint, which triggers the AWS Lambda function:
```
curl -X 'POST' 'http://localhost:8000/process-data/' -H 'Content-Type: application/json' -d '{"message": "Hello, Lambda!"}'
```

* The Lambda function processes the input data and returns a response.

### Lambda Step Functions

This project demonstrates using AWS Step Functions to orchestrate multiple Lambda functions in a serverless workflow.

1. Setup:

* Ensure you have AWS CLI configured and access to create Step Functions and Lambda functions.

* Deploy the resources using Terraform, which will create a state machine and Lambda functions for data processing and logging.

2. Functionality:

* The workflow is defined in a Step Functions state machine, where each state represents a step in the process (e.g., data processing, logging).

* The state machine orchestrates the Lambda functions based on input data.

3. Usage:

* Trigger the Step Functions state machine using the AWS CLI:
```
aws stepfunctions start-execution \
  --state-machine-arn "arn:aws:states:<region>:<account-id>:stateMachine:<YourStateMachineName>" \
  --name "TestExecution-$(date +%s)" \
  --input '{"message": "Hello, Step Functions!"}'
```

* Check the status of the execution using:
```
aws stepfunctions list-executions --state-machine-arn "arn:aws:states:<region>:<account-id>:stateMachine:<YourStateMachineName>"
```
* View detailed execution history:
```
aws stepfunctions get-execution-history --execution-arn "<ExecutionArn>"
```

## Author
This project was implemented by [Lucas de Queiroz dos Reis][2]. It is based on the [100 Days System Design for DevOps and Cloud Engineers][1].

[1]: https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f "Medium - Deo Shankar 100 Days"
[2]: https://www.linkedin.com/in/lucas-de-queiroz/ "LinkedIn - Lucas de Queiroz"