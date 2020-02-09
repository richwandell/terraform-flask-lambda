terraform {
  backend "s3" {}
}

provider "aws" {
  region = var.aws_region
}

data "aws_iam_policy_document" "policy" {
  statement {
    sid = ""
    effect = "Allow"

    principals {
      identifiers = ["lambda.amazonaws.com"]
      type = "Service"
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "iam_for_lambda" {
  name = "iam_for_lambda"
  assume_role_policy = data.aws_iam_policy_document.policy.json
}

resource "aws_lambda_function" "lambda" {
  function_name = "hello_flask"

  filename = "flask-app.zip"
  source_code_hash = filebase64sha256("flask-app.zip")

  role = aws_iam_role.iam_for_lambda.arn
  handler = "lambda.http_server"
  runtime = var.runtime

  environment {
    variables = {
      greeting = "Hello"
    }
  }
}

resource "aws_api_gateway_rest_api" "example" {
  name        = "ServerlessExample"
  description = "Terraform Serverless Application Example"
}

resource "aws_api_gateway_resource" "proxy" {
  parent_id = aws_api_gateway_rest_api.example.root_resource_id
  path_part = "{proxy+}"
  rest_api_id = aws_api_gateway_rest_api.example.id
}

resource "aws_api_gateway_method" "proxy" {
  authorization = "NONE"
  http_method = "ANY"
  resource_id = aws_api_gateway_resource.proxy.id
  rest_api_id = aws_api_gateway_rest_api.example.id
}

resource "aws_api_gateway_integration" "lambda" {
  http_method = aws_api_gateway_method.proxy.http_method
  resource_id = aws_api_gateway_method.proxy.resource_id
  rest_api_id = aws_api_gateway_rest_api.example.id
  type = "AWS_PROXY"
  uri = aws_lambda_function.lambda.invoke_arn
  integration_http_method = "POST"
}

resource "aws_api_gateway_deployment" "example" {
  depends_on = [
    aws_api_gateway_integration.lambda
  ]

  rest_api_id = aws_api_gateway_rest_api.example.id
  stage_name = "test"
}

resource "aws_lambda_permission" "apigw" {
  statement_id = "AllowAPIGatewayInvoke"
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda.function_name
  principal = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.example.execution_arn}/*/*"
}

output "base_url" {
  value = aws_api_gateway_deployment.example.invoke_url
}


