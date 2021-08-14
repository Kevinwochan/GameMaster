from chalice import Chalice, Response
import boto3
import json

app = Chalice(app_name='GameMasterAPI')


@app.route('/test')
def index():
    return Response(status_code=200,
                    body=json.dumps({'Message': 'Hello World'}))


@app.route('/')
def characters():
    '''
    Fetches all characters in the DB
    TODO: set max possible returned chars to 100
    '''
    try:
        table = boto3.resource('dynamodb').Table('GameMasterCharacters')
    except Exception as e:
        print(e)
        return Response(status_code=500,
                        body=json.dumps({'Error': 'Server Error'}))
    try:
        response = table.scan(Select='ALL_ATTRIBUTES')
        print('here we are')
        print(response)
        return Response(status_code=200, body=json.dumps(reponse['Items']))
    except Exception as e:
        print(e)
        return Response(status_code=500,
                        body=json.dumps({'Error': 'Server Error'}))


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
