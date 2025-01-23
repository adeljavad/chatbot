from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch


class CallGPT2(object):
    def __init__(self, kwargs: dict):
        
        self.len = kwargs.get("len", 99)
        self.sample = kwargs.get("len", True)
        self.top_k = kwargs.get("len", 70)
        self.top_p = kwargs.get("len", 0.85)
        self.temp = kwargs.get("len", 0.3)

    def call_model(self, question: str) -> str:
        generative_model = GPT2LMHeadModel.from_pretrained("./llm_model/gpt2")
        generative_tokenizer = GPT2Tokenizer.from_pretrained("./llm_model/gpt2")

        prompt = f"{question + ' answer in one sentence'}\nAnswer:"
        inputs = generative_tokenizer.encode(prompt, return_tensors="pt")
        outputs = generative_model.generate(
            inputs, max_length=self.len, do_sample=self.sample,
            top_k=self.top_k, top_p=self.top_p, temperature=self.temp
        )

        ans = generative_tokenizer.decode(outputs[0], skip_special_tokens=True)
        ans = ans.split("Answer:")[1].strip()
        ans = ans.split("\n")[0].strip()

        return ans

