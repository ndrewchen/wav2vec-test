import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

def get_transcript(filename):
    audio, rate = librosa.load(filename, sr = 16000)

    input_values = tokenizer(audio, return_tensors = "pt").input_values

    logits = model(input_values).logits
    prediction = torch.argmax(logits, dim = -1)
    transcription = tokenizer.batch_decode(prediction)[0]
    print(transcription)

get_transcript("taken_clip.wav")
get_transcript("test1.wav")
# get_transcript("test2.wav") # commented out because it takes pretty long to run
get_transcript("test3.wav")