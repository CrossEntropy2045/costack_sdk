import config
import sys 
sys.path.insert(0,'..')
from costack_sdk.costack_workflow.step import step
from costack_sdk.costack_workflow.lambda_runtime import lambda_runtime
import os

def func(a, b, keykey=""):
    print(keykey) 
    return a+b

@lambda_runtime
def handler(event, context): 
    step(print, context)
    step(func, 3, 4, keykey="keykey")
    return event

if __name__ == "__main__":
    os.environ["DEBUG"] = "True"
    print(handler("event", "context"))
    print(config.runtime)
