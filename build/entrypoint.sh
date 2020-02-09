#!/bin/bash

rm -r /app
cp -r /app_build /app
rm -r /app/.venv
cd /app && pipenv install

pipenv lock --requirements > requirements.txt
pip3 install -r requirements.txt
/build_archive.sh
