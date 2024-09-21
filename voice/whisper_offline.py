from openai import OpenAI
f = open("../examples/kk.kt")
key = "sk-"+f.read()
client = OpenAI(api_key=key)

audio_file= open("../examples/output.wav", "rb")
translation = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print("recognized text: "translation.text)