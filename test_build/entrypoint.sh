#!/bin/bash

rm -r /app
cd /app_build && unzip flask-app.zip -d /app
cd /app && python3 run.py
