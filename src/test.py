from costack_temporal_sdk.context.runtime_context import RuntimeContext
import config
from costack_temporal_sdk.step import step

def func(a, b): 
    return a + b

if __name__ == "__main__":
    config.runtime =  (RuntimeContext(False))
    
    print(step(func, 3, 4))
    print(config.runtime)