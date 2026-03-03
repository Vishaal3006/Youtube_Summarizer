import torch
import gradio as gr
from PIL import Image
import scipy.io.wavfile as wav

from transformers import pipeline

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# model=

pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large",device = device)
