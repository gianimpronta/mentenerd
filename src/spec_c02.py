from engine import *
v = Video("c02", decoration="stars")
BG = "linear-gradient(180deg,#2b0f0a 0%,#7a2a0a 55%,#c4550f 100%)"
v.credits = ["Sun (SDO) e imagem ultravioleta extrema — NASA, domínio público"]

@S(v, 0)
def s1(s):
    s.photo("science/Sun_-_August_1__2010.jpg", pan=(-40, 0), zoom=(1.0, 1.18))
    s.counter(0, 8, 40, 260, 1000, size=300, color="#ffd93d", t=0.4, dur=1.6, suffix=" min")
    s.text("do Sol até a Terra", 40, 620, 1000, size=76, color="#fff", t="Terra", how="up")

@S(v, "Mas", bg=BG)
def s2(s):
    s.ball(170, 350, 740, "rgba(255,150,40,.25)", "rgba(255,120,30,.10)", t=0.2)
    s.ball(240, 420, 600, "#fff6b0", "#ff9a2e", face=False, t=0.2)
    s.pill("fusão nuclear", 60, 250, bg="#ffd93d", t="fusão", how="left", size=54)
    s.path("M300 600 L420 520 L380 680 L520 620 L470 760 L610 700 L560 820 L700 740", color="#ffffff", width=12, t="denso", dur=1.6, ox=0, oy=0)
    s.text("tão denso que a luz<br>não sai em linha reta", 40, 1000, 1000, size=70, color="#fff", t="reta", how="up")

@S(v, "Ela", bg=BG)
def s3(s):
    s.photo("science/Ultiwavelength_extreme_ultraviolet_sun.jpg", pan=(50, 0), zoom=(1.0, 1.16))
    s.path("M60 760 L200 640 L170 820 L330 700 L300 880 L470 760 L430 940 L610 820 L580 1000 L760 880 L720 1040 L900 930", color="#ffd93d", width=14, t="absorvida", dur=3.2)
    s.text("bilhões de vezes", 40, 300, 1000, size=110, color="#fff", t="bilhões", how="slam")
    s.text("em zigue-zague", 40, 520, 1000, size=70, color="#ffd93d", t="zig", how="up")

@S(v, "estimativas", bg=BG)
def s4(s):
    s.emoji("⏳", 350, 300, 360, t=0.2, how="pop", spin=0, bob=12)
    s.text("de dezenas de milhares", 40, 760, 1000, size=76, color="#fff", t="dezenas", how="up")
    s.text("a mais de 100 mil anos", 40, 900, 1000, size=76, color="#ffd93d", t="mais", how="up")

@S(v, ("Só", 2), bg="linear-gradient(180deg,#0a0a2a 0%,#1a1f5a 100%)")
def s5(s):
    s.ball(-120, 560, 320, "#fff6b0", "#ff9a2e", face=True, t=0.2, glow="#ff8a2e")
    s.ball(800, 640, 200, "#7fd3ff", "#1f5fb0", face=True, t=0.3)
    s.path("M240 720 L820 740", color="#ffd93d", width=18, t="atravessa", dur=1.0, ox=0, oy=0)
    ph = s.ball(240, 695, 50, "#ffffff", "#ffd93d", t="atravessa", how="pop", glow="#ffe27a")
    s.move(ph, "atravessa", x=560, dur=1.0, ease="none")
    s.counter(0, 8, 40, 960, 1000, size=240, color="#ffd93d", t="minutos", dur=1.0, suffix=" min")

@S(v, "Ou", bg=BG)
def s6(s):
    s.photo("science/Sun_-_August_1__2010.jpg", pan=(40, 0), zoom=(1.12, 1.0))
    s.text("criada antes<br>das cidades", 40, 300, 1000, size=104, color="#ffd93d", t="cidades", how="slam")

@S(v, 40.8, bg="linear-gradient(180deg,#2b0f0a 0%,#7a2a0a 55%,#c4550f 100%)")
def s7(s):
    s.counter(0, 8, 40, 300, 1000, size=220, color="#ffd93d", t="minutos", dur=1.0, suffix=" min")
    s.text("para chegar", 40, 560, 1000, size=70, color="#fff", t="chegar", how="up")
    s.emoji("⏳", 340, 760, 300, t="milhares", how="pop", bob=10)
    s.text("milhares de anos<br>para sair", 40, 1090, 1000, size=76, color="#ffd93d", t="milhares", how="up")
