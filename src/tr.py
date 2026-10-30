import sys,json,subprocess,numpy as np
from faster_whisper import WhisperModel
m=WhisperModel("small",device="cpu",compute_type="int8")
for k in sys.argv[1:]:
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"../n/{k}.mp3","-filter:a","atempo=1.1","-c:a","libmp3lame","-q:a","2",f"{k}.mp3"],check=True)
    raw=subprocess.check_output(["ffmpeg","-loglevel","error","-i",f"{k}.mp3","-f","s16le","-ac","1","-ar","16000","-"])
    pcm=np.frombuffer(raw,np.int16).astype(np.float32)/32768
    segs,_=m.transcribe(pcm,language="pt",word_timestamps=True,beam_size=5)
    w=[[round(x.start,2),round(x.end,2),x.word.strip()] for s in segs for x in s.words]
    json.dump(w,open(f"{k}.words.json","w"),ensure_ascii=False)
    print(k,len(w),flush=True)
