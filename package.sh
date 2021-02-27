#!/bin/sh

if [[! -d ./vev ]]; then
  virtualenv venv
fi

source ./venv/Scripts/activate || echo "failed to activate pip env"
pip install dateutils boto3 twilio requests || echo "failed to install libraries"
cd venv/lib/python3.9/site-packages
zip -r ../../../package.zip *
zip -r package.zip index.py