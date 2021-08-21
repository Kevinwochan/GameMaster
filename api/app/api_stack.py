from aws_cdk import core as cdk
from aws_cdk import aws_lambda as _lambda, aws_apigateway as apigw, aws_dynamodb as ddb


class ApiStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        table = ddb.Table(
            self, 'Characters',
            partition_key={'name': 'path', 'type': ddb.AttributeType.STRING}
        )

        my_lambda = _lambda.Function(
            self, 'LambdaAPI',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('assets'),
            handler='lambda.handler',
            environment={
                'CHARACTER_TABLE': table.table_name
            }
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=my_lambda,
        )

        table.grant_read_write_data(my_lambda)

