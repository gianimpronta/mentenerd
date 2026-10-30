# Mente Nerd

Canal de Shorts narrados e sem rosto (https://www.youtube.com/channel/UC9C44mfEUFqv-T34nUid0OQ).

- `PROGRESS.md`, `cronograma.csv`, `meta.json`: status, agenda e metadados de publicação.
- `roteiros.md`: roteiros com marcações de entonação (ElevenLabs).
- `audio/originais`: narrações geradas; `audio/rapido`: versão 10% mais rápida (atempo 1.1) com tempos por palavra (`*.words.json`, Whisper).
- `src/`: gerador dos vídeos (HyperFrames). `engine.py` + um `spec_<id>.py` por vídeo; `run.sh` renderiza, `comp.sh` comprime para upload (<10 MB), `tr.py` acelera e transcreve, `meta.py` gera `meta.json`.
- `assets/lib`: fotos reais usadas entre as cenas (créditos nas descrições, em `meta.json`); `assets/clips`: trechos de vídeo recortados.
- `hfpilot/`: arquivos de projeto copiados para cada vídeo.

Nota: `engine.py` ainda usa o caminho absoluto `LIB` da sessão onde foi criado; ajuste a variável para `assets/lib` ao rodar em outra máquina. Os vídeos renderizados não estão aqui.
