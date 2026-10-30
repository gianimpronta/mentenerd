#!/bin/bash
cd /tmp/claude-0/-home-claude/c387085d-c19c-553c-941a-b1d2af4f4e78/scratchpad/v
for k in "$@"; do nice -n 10 ffmpeg -loglevel error -y -i $k.mp4 -c:v libx264 -preset veryfast -b:v 1050k -maxrate 1400k -bufsize 2800k -pix_fmt yuv420p -c:a aac -b:a 112k -movflags +faststart up/$k.mp4; done
