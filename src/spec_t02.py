from engine import *
v = Video("t02", decoration="bubbles")
v.fix = {"%": ""}
BG = "linear-gradient(180deg,#07302a 0%,#0d5f6a 60%,#127a9a 100%)"
v.credits = ["Li-ion Battery BL-59JH — CC BY-SA 4.0 (Wikimedia Commons)"]

@S(v, 0)
def s1(s):
    s.photo("tech/LG_P710_Optimus_L7_II_-_Li-ion_Battery_BL-59JH-0003.jpg", fit="contain", frame=(60, 250, 960, 700), zoom=(1.0, 1.08))
    s.text("bateria perde<br>capacidade", 40, 90, 1000, size=96, color="#ffd93d", t=0.2, how="slam")
    s.pill("ciclos de carga", 60, 1010, bg="#b9f5ff", t="ciclos", how="left", size=52)
    s.pill("calor 🔥", 60, 1110, bg="#ff9a2e", t=("calor", 1), how="left", size=52)

@S(v, "ciclo", bg=BG)
def s2(s):
    b = s.battery(130, 400, 820, 340, frac=1.0, t=0.1)
    s.raw('', f'tl.to("{b}f",{{scaleX:0.02,duration:2.0,ease:"power1.inOut"}},{s.T("equivalente") + 0.2:.2f});')
    s.counter(100, 0, 40, 780, 1000, size=160, color="#ffd93d", t="equivalente", dur=2.0, suffix="%")
    s.text("1 ciclo", 40, 220, 1000, size=120, color="#fff", t=0.2, how="slam")

@S(v, "Gastar", bg=BG)
def s3(s):
    b1 = s.battery(130, 300, 820, 220, frac=0.5, t=0.1)
    s.text("50%", 40, 560, 1000, size=100, color="#ffd93d", t="50", how="slam")
    b2 = s.battery(130, 760, 820, 220, frac=0.5, t="outro", color="#5ee0c8")
    s.text("+ 50%", 40, 1000, 1000, size=100, color="#5ee0c8", t=("50", 2), how="slam")
    s.text("= 1 ciclo", 40, 1130, 1000, size=90, color="#fff", t="ciclo", how="up")

@S(v, "muitos", bg=BG)
def s4(s):
    s.counter(0, 500, 40, 220, 1000, size=240, color="#ffd93d", t="500", dur=1.6, suffix=" ciclos")
    b = s.battery(130, 700, 820, 340, frac=1.0, t=0.2, label="")
    s.raw('', f'tl.to("{b}f",{{scaleX:0.8,duration:1.2,ease:"power2.out"}},{s.T("segura") - 0.2:.2f});')
    s.pill("80% da carga original", 60, 1090, bg="#ffd93d", t="80", how="left", size=52)

@S(v, ("calor", 2), bg="linear-gradient(180deg,#3a1005 0%,#a33a0a 60%,#e8741a 100%)")
def s5(s):
    s.emoji("🌡️", 380, 320, 360, t=0.1, how="pop", bob=8)
    s.emoji("☀️", 100, 300, 240, t="sol", how="pop", bob=10)
    s.emoji("🚗", 640, 560, 260, t="carro", how="pop")
    s.text("calor acelera o desgaste", 40, 900, 1000, size=84, color="#fff", t="acelera", how="up")

@S(v, "Evitar", bg=BG)
def s6(s):
    s.rect(80, 520, 920, 120, "rgba(255,255,255,.15)", t=0.1, how="fade", radius=60)
    s.rect(80, 520, 160, 120, "#ff4d4d", t="zero", how="pop", radius=60)
    s.rect(840, 520, 160, 120, "#ff4d4d", t="100", how="pop", radius=60)
    s.rect(260, 520, 560, 120, "#5ee08a", t="ajuda", how="pop", radius=40)
    s.text("0%", 80, 660, 200, size=64, color="#ff8a8a", t="zero", how="up")
    s.text("100%", 800, 660, 200, size=64, color="#ff8a8a", t="100", how="up")
    s.text("viver no meio", 40, 900, 1000, size=84, color="#ffd93d", t="ajuda", how="up")

@S(v, "Hoje", bg=BG)
def s7(s):
    s.emoji("📱", 360, 280, 340, t=0.1, how="pop", bob=10)
    s.pill("limite de carga: 80%", 130, 760, bg="#ffd93d", t="limitar", how="up", size=62)
    s.text("usar com cuidado<br>faz diferença", 40, 1000, 1000, size=76, color="#fff", t="diferença", how="up")
