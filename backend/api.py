from livekit.agents import llm

class AssistantAgent(llm.FunctionContext):
    def __init__(self):
        super().__init__()