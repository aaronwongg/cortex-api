# predictor.py

import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

from transformers import BartTokenizer, BartForConditionalGeneration


class PythonPredictor:
    def __init__(self, config):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"using device: {self.device}")
        self.tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
        self.model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn").to(self.device)

    def predict(self, payload):
        input_length = len(payload["text"].split())
        tokens = self.tokenizer.encode(payload["text"], return_tensors="pt").to(self.device)
        prediction = self.model.generate(tokens, max_length=input_length + 20, do_sample=True)
        return self.tokenizer.decode(prediction[0])