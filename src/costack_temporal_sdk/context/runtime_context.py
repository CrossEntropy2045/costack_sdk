from typing import List
from costack_temporal_sdk.context.function_context import FunctionContext

class RuntimeContext:
    def __init__(self, debug):
        self._debug = debug

        self._steps: List[FunctionContext] = []

    @property
    def debug(self):
        return self._debug
    @property
    def steps(self):
        return self._steps
    
    def add_step(self, step):
        self._steps.append(step)
