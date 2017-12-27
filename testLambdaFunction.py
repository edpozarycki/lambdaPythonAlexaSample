import lambdaPythonAlexaCode

event = {
  'session': {
    'sessionId': "SessionId.21dffc00-602b-4a3c-91b5-f29a3d6fadf8",
    'application': {
      'applicationId': "amzn1.ask.skill.f95d6302-e53d-4e98-8f84-3c206701ef29"
    },
    'attributes': {},
    'user': {
      'userId': "amzn1.ask.account.AHDOPLZ6O5SVQ52SJ2NFNN75TIJGOEEQ4LPSOCDVIMK2BIEM7SG3RET32WV2OB5E7CGOR6BY2PE6T6N7I4AESFGLBLKAK5RT3GF42ND7F22RPIFBJF7JKODCCMIJDVT4HJU6XW4PJCYURPPIWLFMUR4LJJ6IUNDV3SUKX55EKNAT5AQQVJIBVTJYBPOPP4EQCZKYOC765MQOM2Y"
    },
    'new': "true"
  },
  'request': {
    'type': "IntentRequest",
    'requestId': "EdwRequestId.81a005dd-1d61-48c3-95fa-dd141accb2cf",
    'locale': "en-US",
    'timestamp': "2017-05-29T21:41:30Z",
    'intent': {
      'name': "PozIndividualFact",
      'slots': {
        'family_member': {
          'name': "family_member",
          'value': "Tyler"
        }
      }
    }
  },
  'version': "1.0"
}

event = {
  "session": {
    "sessionId": "SessionId.197d1a74-21cc-4e74-983f-e755662b8872",
    "application": {
      "applicationId": "amzn1.ask.skill.f95d6302-e53d-4e98-8f84-3c206701ef29"
    },
    "attributes": {
      "testfield": "testvalue"
    },
    "user": {
      "userId": "amzn1.ask.account.AHDOPLZ6O5SVQ52SJ2NFNN75TIJGOEEQ4LPSOCDVIMK2BIEM7SG3RET32WV2OB5E7CGOR6BY2PE6T6N7I4AESFGLBLKAK5RT3GF42ND7F22RPIFBJF7JKODCCMIJDVT4HJU6XW4PJCYURPPIWLFMUR4LJJ6IUNDV3SUKX55EKNAT5AQQVJIBVTJYBPOPP4EQCZKYOC765MQOM2Y"
    },
    "new": "false"
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "EdwRequestId.6efb3300-6c73-4cef-9d5a-8d36dae2e55e",
    "locale": "en-US",
    "timestamp": "2017-06-04T18:28:35Z",
    "intent": {
      "name": "PutIntent",
      "slots": {
        "fact": {
          "name": "fact"
        },
        "family_member": {
          "name": "family_member"
        }
      }
    }
  },
  "version": "1.0"
  }
  


print event
context = ""

lambdaPythonAlexaCode.lambda_handler(event, context)
