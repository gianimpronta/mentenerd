from engine import *
v = Video("n08c", decoration="stars")
v.fix = {"9": "nove", "3": "três"}
v.phr = [("três. O resultado", "três: o resultado"), ("essa a onda", "essa onda")]
BG = "linear-gradient(180deg,#0a1020 0%,#1b2740 60%,#2c3d5c 100%)"
Y, C = "#ffe14d", "#7fd3ff"
L = "nov08/"
v.credits = ["Port and lighthouse overnight storm with lightning in Port-la-Nouvelle — Maxime Raynal, CC BY 2.0, Wikimedia Commons"]

@S(v, 0)
def s1(s):
    s.photo(L + "Port_lightning.jpg", zoom=(1.05, 1.2))
    s.text("TODO TROVÃO<br>CHEGA ATRASADO", 40, 300, 1000, size=120, color=Y, t=0.1, how="slam")

@S(v, "raio", bg=BG)
def s2(s):
    s.emoji("⚡", 200, 300, 260, t=0.0, how="slam")
    s.emoji("🔊", 620, 300, 260, t="trovão", how="slam")
    s.text("AO MESMO TEMPO", 40, 680, 1000, size=96, color="#fff", t="mesmo", how="up")
    s.pill("👀 você vê primeiro", 120, 880, bg=Y, t="vê", how="left", size=58)
    s.pill("👂 e ouve depois", 120, 1010, bg=C, t="ouve", how="left", size=58)

@S(v, "luz", bg=BG)
def s3(s):
    s.text("LUZ", 60, 300, 400, size=120, color=Y, t=0.0, how="left")
    s.rect(60, 470, 960, 20, Y, t=0.1, how="left", radius=10)
    s.emoji("🏹", 820, 400, 160, t=0.1, how="pop")
    s.text("SOM", 60, 700, 400, size=120, color=C, t="som", how="left")
    s.rect(60, 870, 200, 20, C, t="som", how="left", radius=10)
    s.emoji("🐌", 260, 800, 160, t="som", how="pop")

@S(v, "Em", bg=BG)
def s4(s):
    s.pill("☀️ dia seco · 20 °C", 230, 260, bg="#fff", t="seco", how="up", size=58)
    s.counter(0, 343, 40, 460, 1000, size=240, color=C, t="343", dur=1.0)
    s.text("metros por segundo", 40, 760, 1000, size=70, color="#fff", t="metros", how="up")
    s.text("luz: quase na hora ⚡", 40, 980, 1000, size=70, color=Y, t="luz", how="up")

@S(v, ("Por", 2), bg=BG)
def s5(s):
    s.emoji("📏", 400, 300, 260, t=0.0, how="pop")
    s.text("DÁ PARA ESTIMAR<br>A DISTÂNCIA", 40, 700, 1000, size=100, color=Y, t="estimar", how="slam")

@S(v, "Conte", bg=BG)
def s6(s):
    s.emoji("⏱️", 410, 120, 200, t=0.0, how="pop", bob=6)
    s.text("segundos ÷ 3", 40, 380, 1000, size=150, color="#fff", t="divida", how="slam")
    s.text("= quilômetros", 40, 640, 1000, size=110, color=Y, t="quilômetros", how="up")
    s.pill("aproximadamente", 290, 820, bg=C, t="aproximadamente", how="up", size=56)

@S(v, "Se", bg=BG)
def s7(s):
    s.counter(0, 9, 40, 260, 1000, size=240, color="#fff", t="nove", dur=0.8, suffix=" s")
    s.text("÷ 3", 40, 560, 1000, size=140, color=C, t="tempestade", how="up")
    s.counter(0, 3, 40, 780, 1000, size=220, color=Y, t="três", dur=0.5, suffix=" km")

@S(v, "onde", bg="#070b16")
def s8(s):
    s.text("E DE ONDE VEM<br>O TROVÃO?", 40, 650, 1000, size=110, color=Y, t=0.0, how="slam")

@S(v, ("raio", 2), bg=BG)
def s9(s):
    s.emoji("🌡️", 400, 250, 260, t="aquece", how="pop")
    s.text("~30.000 °C", 40, 640, 1000, size=190, color="#ff6a3d", t="30", how="slam")
    s.text("instantâneo", 40, 920, 1000, size=74, color="#fff", t="instantânea", how="up")

@S(v, ("ar", 2), bg=BG)
def s10(s):
    for i, d in enumerate([200, 420, 640]):
        s.rect(540 - d // 2, 700 - d // 2, d, d, "transparent", t=0.15 * i, how="pop", radius=d, border=f"10px solid {C}")
    s.emoji("⚡", 470, 630, 140, t=0.0, how="pop")
    s.text("ONDA DE CHOQUE", 40, 1150, 1000, size=110, color=Y, t="choque", how="slam")

@S(v, "essa onda", bg=BG)
def s11(s):
    s.emoji("👂", 400, 320, 260, t="ouvidos", how="pop")
    s.text("BUUUM!", 40, 700, 1000, size=200, color=Y, t="estrondo", how="slam")

@S(v, ("trovão", 5))
def s12(s):
    s.photo(L + "Port_lightning.jpg", zoom=(1.2, 1.05))
    s.text("O TROVÃO É O AR<br>EMPURRADO PELO RAIO", 40, 320, 1000, size=92, color=Y, t=0.05, how="slam")
