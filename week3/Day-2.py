import torch
from transformers import pipeline
from diffusers import DiffusionPipeline
from datasets import load_dataset
import soundfile as sf
from IPython.display import Audio

#Sentiment Analysis
classifier = pipeline("sentiment-analysis")
result = classifier("I am super nervous and excited to begin LLM mastery!")
print(result)

# No model was supplied, defaulted to distilbert/distilbert-base-uncased-finetuned-sst-2-english and revision 714eb0f (https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english).
# Using a pipeline without specifying a model name and revision in production is not recommended.
# Device set to use cpu
# [{'label': 'POSITIVE', 'score': 0.9990718364715576}]

