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