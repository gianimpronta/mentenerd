from engine import *
v = Video("n09c", decoration="stars")
v.fix = {"Gigante": "gigante", "Horizonte": "horizonte"}
v.phr = [("olho. Ela", "olho: ela")]
BG = "linear-gradient(180deg,#050a24 0%,#0e1a44 60%,#1c2c66 100%)"
M, C = "#ffe9a8", "#8fd0ff"
L = "nov09/"
v.credits = ["Harvest moon — Roadcrusher (Wikipedia em inglês), CC BY-SA 3.0, Wikimedia Commons"]

@S(v, 0)
def s1(s):
    s.photo(L + "Harvest_moon.jpg", zoom=(1.05, 1.25))
    s.text("A LUA GIGANTE<br>É UMA ILUSÃO", 40, 280, 1000, size=120, color=M, t=0.1, how="slam")

@S(v, "Ela", bg=BG)
def s2(s):
    s.ball(640, 260, 200, "#fff7d6", M, t=0.0, how="pop", glow="#ffe9a8")
    s.ball(240, 600, 200, "#fff7d6", M, t="embaixo", how="pop", glow="#ffe9a8")
    s.text("🏠🌳🏠🌳🏠", 40, 700, 1000, size=110, color="#fff", t="embaixo", how="up")
    s.text("MESMO TAMANHO", 40, 960, 1000, size=110, color=M, t="mesmo", how="slam")

@S(v, "Medidas", bg=BG)
def s3(s):
    s.emoji("📐", 410, 220, 220, t=0.0, how="pop")
    s.text("o diâmetro aparente<br>não muda", 40, 520, 1000, size=84, color="#fff", t="diâmetro", how="up")
    s.pill("≈ 0,5° no céu", 330, 780, bg=C, t="aparente", how="up", size=60)
    s.emoji("📷", 410, 940, 200, t="Fotos", how="pop", bob=6)
    s.text("fotos confirmam", 40, 1170, 1000, size=66, color=M, t="mesmo", how="up")

@S(v, "Dá", bg=BG)
def s4(s):
    s.text("FAÇA O TESTE", 40, 220, 1000, size=110, color=M, t=0.0, how="slam")
    s.ball(420, 520, 240, "#fff7d6", M, t="pedrinha", how="pop", glow="#ffe9a8")
    s.ball(470, 570, 140, "#7d7a80", "#4a474e", t="pedrinha", how="slam")
    s.pill("✋ braço esticado", 100, 830, bg="#fff", t="braço", how="left", size=58)
    s.pill("😉 um olho fechado", 100, 940, bg=C, t="feche", how="left", size=58)
    s.text("cobre do mesmo jeito", 40, 1060, 1000, size=70, color=M, t="cobre", how="up")

@S(v, "Então", bg="#030616")
def s5(s):
    s.text("ENTÃO POR QUE<br>A ILUSÃO?", 40, 640, 1000, size=120, color=M, t=0.0, how="slam")

@S(v, "explicação", bg=BG)
def s6(s):
    s.emoji("🧠", 410, 200, 220, t=0.0, how="pop", bob=6)
    s.text("“parece mais longe”", 40, 500, 1000, size=74, color="#fff", t="distante", how="up")
    s.pill("🌳 árvores", 330, 620, bg="#fff", t="árvores", how="left", size=58)
    s.pill("🏠 casas", 330, 730, bg="#fff", t="casas", how="left", size=58)
    s.pill("⛰️ montanhas", 330, 840, bg="#fff", t="montanhas", how="left", size=58)
    s.text("→ parece MAIOR", 40, 980, 1000, size=100, color=M, t="maior", how="slam")

@S(v, "pesquisadores", bg=BG)
def s7(s):
    s.text("isso DESCREVE…", 40, 420, 1000, size=110, color="#fff", t=0.0, how="up")
    s.text("…mas não explica", 40, 700, 1000, size=100, color=C, t="explica", how="up")

@S(v, "Ainda")
def s8(s):
    s.photo(L + "Harvest_moon.jpg", zoom=(1.2, 1.05))
    s.text("?", 240, 160, 600, size=480, color=M, t=0.05, how="slam")
    s.text("NENHUMA TEORIA ÚNICA", 40, 760, 1000, size=80, color="#fff", t="teoria", how="up")
    s.text("conhecida há séculos", 40, 1000, 1000, size=70, color=M, t="séculos", how="up")
