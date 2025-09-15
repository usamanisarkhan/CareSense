from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_stepfunctions as sfn,
    aws_apigateway as apigateway,
)
from constructs import Construct


class CareSenseStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Import existing Lambda functions
        self.email_lambda = _lambda.Function.from_function_arn(
            self, "EmailReminderLambda",
            "arn:aws:lambda:us-east-1:462498958925:function:email_reminder_lambda"
        )

        self.api_lambda = _lambda.Function.from_function_arn(
            self, "ApiLambda",
            "arn:aws:lambda:us-east-1:462498958925:function:api_lambda"
        )

        # Import existing Step Function
        self.state_machine = sfn.StateMachine.from_state_machine_arn(
            self, "CareSenseStateMachine",
            "arn:aws:states:us-east-1:462498958925:stateMachine:caresense1"
        )

        # Import existing API Gateway
        self.api_gateway = apigateway.RestApi.from_rest_api_attributes(
            self, "CareSenseApi",
            rest_api_id="pywsfe11yg",   # API ID extracted from your URL
            root_resource_id="0vdoc76q2f"     # placeholder, see note below
        )
