from engine import *
v = Video("m03", decoration="grid")
v.fix = {"corvete": "Corvette"}
BG = "linear-gradient(180deg,#0a1a3a 0%,#122c6a 60%,#1c3f9a 100%)"
v.credits = ["John Titor insignia — uso educativo/fair use", "IBM 5100 (Sandstein) — CC BY-SA 3.0 (Wikimedia Commons)", "1967 Chevrolet Corvette C2 — Wikimedia Commons (ver manifest)"]

@S(v, 0)
def s1(s):
    s.pill("novembro de 2000", 60, 230, bg="#ffd93d", t=0.1, how="left", size=56)
    s.emoji("💬", 340, 330, 300, t="fórum", how="pop", bob=8)
    s.counter(2000, 2036, 40, 760, 1000, size=300, color="#ffd93d", t="2036", dur=1.4)
    s.text("um soldado do futuro?", 40, 1090, 1000, size=64, color="#fff", t="soldado", how="up")

@S(v, "chamava", bg=BG)
def s2(s):
    s.photo("mist/Titor_insignia.jpg", fit="contain", frame=(100, 250, 880, 800), zoom=(1.0, 1.08))
    s.pill("John Titor", 60, 1080, bg="#ffd93d", t="Titor", how="left", size=60)

@S(v, "Segundo", bg=BG)
def s3(s):
    s.photo("mist/IBM_5100_-_MfK_Bern.jpg", fit="contain", frame=(60, 300, 960, 720), zoom=(1.0, 1.08))
    s.pill("IBM 5100 · 1975", 60, 1060, bg="#ffd93d", t="IBM", how="left", size=56)

@S(v, "descreveu", bg=BG)
def s4(s):
    s.photo("mist/1967_Chevrolet_Corvette_C2_BS_O24.jpg", pan=(-50, 0), zoom=(1.0, 1.15))
    s.pill("Corvette 1967", 40, 260, bg="#ffd93d", t="1967", how="left", size=60)

@S(v, "previsões", bg=BG)
def s5(s):
    s.path("M80 700 L1000 700", color="#ffffff", width=14, t=0.1, dur=0.8)
    s.ball(250, 650, 100, "#ffd93d", "#ff9a2e", t="2004", how="pop")
    s.text("2004", 160, 780, 280, size=80, color="#ffd93d", t="2004", how="up")
    s.text("guerra civil", 100, 880, 400, size=48, color="#fff", t="civil", how="up")
    s.ball(740, 650, 100, "#ff6a8a", "#c01f4a", t="2015", how="pop")
    s.text("2015", 650, 780, 280, size=80, color="#ff6a8a", t="2015", how="up")
    s.text("guerra mundial", 600, 880, 400, size=48, color="#fff", t="mundial", how="up")
    s.text("previsões", 40, 300, 1000, size=110, color="#fff", t=0.2, how="slam")

@S(v, "acompanhar", bg=BG)
def s6(s):
    for k, (x, y, w, c) in enumerate([(80, 300, 520, "#ffffff"), (440, 480, 560, "#ffd93d"), (100, 660, 500, "#b9c8ff")]):
        s.rect(x, y, w, 120, c, t=0.2 + k * 0.7, how="pop", radius=60)
    s.emoji("👀", 380, 900, 220, t="detalhe", how="pop", bob=8)
    s.text("cada mensagem", 40, 1100, 1000, size=70, color="#fff", t="mensagem", how="up")

@S(v, ("tempo", 2), bg=BG)
def s7(s):
    s.emoji("⏳", 340, 280, 380, t=0.1, how="pop", bob=10)
    s.text("o tempo é o pior<br>inimigo de quem faz previsões", 40, 760, 1000, size=70, color="#ffd93d", t="pior", how="up")
