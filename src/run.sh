#!/bin/bash
# uso: run.sh c02 -> gera, checa erros e renderiza
cd /tmp/claude-0/-home-claude/c387085d-c19c-553c-941a-b1d2af4f4e78/scratchpad/v
for k in "$@"; do
  python3 -I -c "
import sys; sys.path.insert(0,'.')
exec(open('spec_$k.py').read()); print(v.build())" || { echo "BUILD FAIL $k"; continue; }
  (cd $k && npx -y hyperframes@0.8.208 render -o ../$k.mp4 > ../r_$k.log 2>&1; echo "done $k $?" >> ../render_all.log)
done
