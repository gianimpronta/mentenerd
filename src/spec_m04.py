from engine import *
v = Video("m04", decoration="grid")
v.fix = {"previo": "previu", "postes": "posts"}
BG = "linear-gradient(180deg,#1a0a14 0%,#3a1030 60%,#6a1a4a 100%)"
v.credits = ["John Titor insignia — uso educativo/fair use"]

def X(s, x, y, t):
    s.path(f"M{x} {y} L{x+110} {y+110} M{x+110} {y} L{x} {y+110}", color="#ff4d4d", width=22, t=t, dur=0.35)

@S(v, 0)
def s1(s):
    s.text("guerra civil · 2004", 40, 360, 1000, size=84, color="#fff", t="civil", how="up")
    X(s, 440, 520, "civil")
    s.text("guerra mundial · 2015", 40, 760, 1000, size=84, color="#fff", t="mundial", how="up")
    X(s, 440, 920, "mundial")
    s.text("nada aconteceu", 40, 190, 1000, size=100, color="#ffd93d", t=0.1, how="slam")

@S(v, "março", bg=BG)
def s2(s):
    s.rect(80, 320, 920, 520, "#0b0b1c", t=0.1, how="pop", radius=30, border="6px solid #5ee08a")
    s.text("última mensagem<br>março de 2001_", 80, 420, 920, size=72, color="#5ee08a", t="mensagem", how="up")
    s.text("desapareceu", 40, 940, 1000, size=100, color="#ffd93d", t="desapareceu", how="slam")

@S(v, "Foram", bg=BG)
def s3(s):
    s.photo("mist/Titor_insignia.jpg", fit="contain", frame=(100, 250, 880, 800), zoom=(1.0, 1.08))
    s.pill("virou lenda da internet", 60, 1080, bg="#ffd93d", t="lenda", how="left", size=52)

@S(v, "Então", bg=BG)
def s4(s):
    s.rect(380, 300, 320, 320, "#14123a", t=0.1, how="pop", radius=160)
    s.rect(330, 640, 420, 420, "#14123a", t=0.1, how="pop", radius=120)
    s.text("?", 380, 330, 320, size=260, color="#ffd93d", t=0.3, how="slam")
    s.text("quem era?", 40, 1100, 1000, size=90, color="#fff", t="quem", how="up")

@S(v, "2009", bg=BG)
def s5(s):
    s.emoji("🌴", 100, 280, 260, t="Flórida", how="pop", bob=8)
    s.emoji("🏠", 600, 320, 260, t="família", how="pop", bob=8)
    s.counter(2000, 2009, 40, 740, 1000, size=200, color="#ffd93d", t=0.1, dur=0.8)
    s.text("NADA COMPROVADO", 40, 1000, 1000, size=84, color="#ff6a8a", t="comprovado", how="slam", rot=-3, extra="border:8px solid #ff6a8a;padding:12px 0;border-radius:24px")

@S(v, "Outro", bg=BG)
def s6(s):
    s.emoji("✍️", 100, 300, 260, t=0.2, how="pop", bob=8)
    s.emoji("📖", 640, 340, 260, t="literário", how="pop", bob=8)
    s.text("experimento literário?", 40, 760, 1000, size=84, color="#fff", t="experimento", how="up")
    s.text("há quem acredite,<br>há quem veja ficção", 40, 980, 1000, size=64, color="#ffd93d", t="acredite", how="up")

@S(v, "fato", bg=BG)
def s7(s):
    s.rect(380, 300, 320, 320, "#14123a", t=0.1, how="pop", radius=160)
    s.rect(330, 640, 420, 420, "#14123a", t=0.1, how="pop", radius=120)
    s.text("sem rosto<br>sem prova<br>sem volta", 40, 1090, 1000, size=60, color="#ffd93d", t="rosto", how="up")
