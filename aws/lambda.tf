resource "aws_lambda_function" "lambda" {
  function_name = "hello_flask"

  filename = "../flask-app.zip"
  source_code_hash = filebase64sha256("../flask-app.zip")

  role = aws_iam_role.iam_for_lambda.arn
  handler = "lambda.http_server"
  runtime = var.runtime

  environment {
    variables = {
      greeting = "Hello"
    }
  }
}