from costack_temporal_sdk.context.runtime_context import RuntimeContext
import config
from costack_temporal_sdk.step import step
from costack_temporal_sdk.lambda_runtime import lambda_runtime
import os

def func(a, b): 
    return a+b

@lambda_runtime
def handler(event, context): 
    print(context)
    step(func, 3, 4)
    return event

if __name__ == "__main__":
    os.environ["DEBUG"] = "True"
    print(handler("event", "context"))
    print(config.runtime)