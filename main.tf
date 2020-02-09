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



