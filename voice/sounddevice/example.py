from funasr import AutoModel
# paraformer-zh is a multi-functional asr model
# use vad, punc, spk or not as you need
model_dir = "./paraformer-zh-streaming"
model = AutoModel(model=model_dir, model_revision="v2.0.4"
                  # spk_model="cam++", spk_model_revision="v2.0.2",
                  )
res = model.generate(input=f"{model.model_path}/example/asr_example.wav", 
                     batch_size_s=300, 
                     hotword='魔搭')
print(res)