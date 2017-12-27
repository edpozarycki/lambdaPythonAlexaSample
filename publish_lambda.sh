rm lambda.zip
zip lambda.zip lambdaPythonAlexaCode.py
aws lambda update-function-code --function-name pozpython --zip-file fileb://lambda.zip
