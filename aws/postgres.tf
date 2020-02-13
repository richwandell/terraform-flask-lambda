resource "aws_db_instance" "postgres" {
  identifier = "flaskappdb"
  name = "flaskappdb"
  instance_class = "db.t3.micro"
  storage_type = "standard"
  storage_encrypted = false
  engine = "postgres"
  engine_version = "11"
  allocated_storage = 20
  vpc_security_group_ids = [data.aws_security_group.default.id]
  backup_retention_period = 0
  deletion_protection = false
  username = var.postgres_user
  password = var.postgres_pass
  apply_immediately = true
  skip_final_snapshot = true
}