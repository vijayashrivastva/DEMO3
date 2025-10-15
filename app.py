import aws_cdk as cdk
from stacks.analytics_stack import AnalyticsStack

app = cdk.App()
AnalyticsStack(app, "S3AthenaAnalyticsStack")
app.synth()