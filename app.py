#!/usr/bin/env python3
import aws_cdk as cdk
from caresense.caresense_stack import CareSenseStack

app = cdk.App()
CareSenseStack(app, "CareSenseStack", env=cdk.Environment(
    account="462498958925",
    region="us-east-1"
))

app.synth()
