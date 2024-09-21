from openai import OpenAI
f = open("../examples/kk.kt")
key = "sk-"+f.read()
client = OpenAI(api_key=key)

audio_file= open("output.wav", "rb")
translation = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file
)
print(translation.text)