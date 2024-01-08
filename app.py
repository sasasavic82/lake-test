# Copyright 2024 Telstra.com, Pty. Ltd. or its affiliates. All Rights Reserved.

import aws_cdk as cdk
from constructs import Construct

class EmptyStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        pass


print("Hello from StarkLake... Bootstrapping an EmptyStack")
app = cdk.App()

EmptyStack(app, 'StackStub')

app.synth()



