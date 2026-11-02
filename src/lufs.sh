#!/bin/bash
# uso: lufs.sh entrada.mp4 saida.mp4  -> voz tratada + -14 LUFS / -1 dBTP (2 passadas), vídeo copiado
in="$1"; out="$2"
PRE="highpass=f=80,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120:makeup=2"
J=$(ffmpeg -hide_banner -nostats -i "$in" -af "$PRE,loudnorm=I=-14:TP=-1.5:LRA=9:print_format=json" -f null - 2>&1 | python3 -c "import sys,json;s=sys.stdin.read();print(s[s.rindex('{'):])")
g(){ echo "$J" | python3 -c "import sys,json;print(json.load(sys.stdin)['$1'])"; }
ffmpeg -loglevel error -y -i "$in" -c:v copy -af "$PRE,loudnorm=I=-14:TP=-1.5:LRA=9:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true,aresample=48000" -c:a aac -b:a 128k -movflags +faststart "$out"
