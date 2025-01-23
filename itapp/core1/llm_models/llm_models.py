from itapp.core1.llm_models.models.call_gpt2 import CallGPT2


class LLM(object):
    def __init__(self, model_name: str, **kwargs):
        self.model_name = model_name.lower()
        self.parameters = kwargs

    def chat(self, question: str) -> str:
        if self.model_name == "gpt2":
            return self.__load_gpt2(question=question)

    def __load_gpt2(self, question: str) -> str:
        cgp = CallGPT2(self.parameters)

        return cgp.call_model(question)
