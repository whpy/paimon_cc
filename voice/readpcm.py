import pyaudio

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(2),channels=1, rate=16000,output=True)

with open("./rtasr_python3_demo/python/test_1.pcm","rb") as f:
    stream.write(f.read())

stream.stop_stream()
stream.close()
p.terminate()