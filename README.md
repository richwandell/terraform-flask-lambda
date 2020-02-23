# Terraform Flask Lambda

This project uses terraform to create a AWS Lambda environment which will run a 
Flask app. 

The flask app is built using Docker and a Aws AMI image to match the lambda 
execution environment. 

## Building the Archive
`docker-compose up build_service`

This command will use docker-compose to mount the source code using a volume.
The entrypoint file for the build container will handle creating an archive 
from the Flask application including all python requirements. The out file generated 
from the build is `flask-app.zip`. 

## Testing Archive 
`docker-compose up test_build`

This command will start a docker container which will mount the current working dir
into /app_build folder. It will then extract the flask-app.zip file into /app and 
run `python3 run.py`. The zip file contains all requirements for the app so there
should be no need to install python requirements. If everything works you should be
able to open `http://localhost:5000/hello_lambda` and you will get a response.

## Terraform
Inside of the `aws` folder, create a file `.backend.tf` with reference to a AWS S3 bucket for use 
with the Terraform s3 backend. And a `terraform.tfvars` file containing credentials you would like to 
use for postgres.

*.backend.tf*
```hcl-terraform
bucket = "some-s3-bucket"
key = "path/to/terraform.tfstate"
region = "some region"
```
*terraform.tfvars*
```hcl-terraform
postgres_pass = "somepgpass"
postgres_user = "somepguser"
```
Now initialize terraform using `terraform init --backend-config .backend.tf`. This should create a file
storing the terraform state in the s3 bucket. 

After terraform is initialized run `terraform plan` and then `terraform apply`.

If everything works correctly you should have a running flask app deployed to AWS
Lambda.

### Dotenv
When using windows you can load environment variables in the cmd.exe terminal using the 
provided .bat script `dotenv.bat`. This file will read through a `.env` file with 
settings in the format `SETTING=VALUE` and it will add these to the terminal environment.
OSX and Linux can set environment variables using `dotenv.sh`.