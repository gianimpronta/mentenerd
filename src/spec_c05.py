from engine import *
v = Video("c05", decoration="grid")
BG = "linear-gradient(180deg,#06302e 0%,#0a5a50 60%,#0f8a70 100%)"
v.credits = ["GPS Block I exploded view e Navstar-2F — NASA/USAF, domínio público"]

@S(v, 0)
def s1(s):
    s.photo("tech/Navstar-2F.jpg", pan=(-40, 0), zoom=(1.0, 1.16))
    s.text("GPS", 40, 300, 1000, size=240, color="#ffd93d", t=0.2, how="slam")
    s.text("+ Einstein", 40, 600, 1000, size=110, color="#fff", t="Einstein", how="slam")

@S(v, "satélites", bg=BG)
def s2(s):
    s.photo("tech/GPS_Block1_ExplodedView.png", fit="contain", frame=(60, 200, 960, 700), zoom=(1.0, 1.06))
    s.pill("relógios atômicos", 60, 940, bg="#ffd93d", t="atômicos", how="left", size=50)
    s.counter(0, 14, 40, 1020, 1000, size=130, color="#fff", t="mil", dur=1.2, suffix=" mil km/h")

@S(v, "relatividade", bg=BG)
def s3(s):
    s.ball(-300, 1300, 700, "#7fd3ff", "#1f5fb0", face=True, t=0.1)
    s.emoji("🛰️", 620, 260, 220, t=0.2, how="pop", bob=12)
    s.pill("velocidade → relógio mais lento 🐢", 40, 560, bg="#ff6a4d", t="velocidade", how="left", size=40)
    s.pill("gravidade fraca → relógio mais rápido 🐇", 40, 680, bg="#5ee08a", t="fraca", how="left", size=40)
    s.text("não se cancelam", 40, 900, 1000, size=90, color="#ffd93d", t="cancelam", how="slam")

@S(v, "total", bg=BG)
def s4(s):
    s.emoji("⏱️", 380, 330, 300, t=0.2, how="pop", bob=10)
    s.counter(0, 38, 40, 700, 1000, size=280, color="#ffd93d", t="adianta", dur=1.4, suffix=" µs")
    s.text("a mais, por dia", 40, 1020, 1000, size=76, color="#fff", t="dia", how="up")

@S(v, "Parece", bg=BG)
def s5(s):
    s.emoji("💡", 80, 300, 200, t=0.2, how="pop")
    s.path("M300 380 L960 380", color="#ffd93d", width=18, t="luz", dur=1.0)
    s.counter(0, 300, 40, 560, 1000, size=240, color="#ffd93d", t="percorre", dur=1.4, suffix=" m")
    s.text("a luz percorre isso<br>em 1 microssegundo", 40, 860, 1000, size=64, color="#fff", t="microsegundo", how="up")

@S(v, "Sem", bg=BG)
def s6(s):
    s.raw('<div class="abs" style="left:100px;top:760px;width:880px;height:380px;border-radius:40px;background:rgba(255,255,255,.1)"></div>')
    p = s.emoji("📍", 160, 780, 180, t=0.2, how="pop")
    s.move(p, "dia", x=640, dur=1.6, ease="power2.in")
    s.counter(0, 10, 40, 300, 1000, size=280, color="#ff6a4d", t="erro", dur=1.4, suffix=" km")
    s.text("de erro por dia", 40, 590, 1000, size=76, color="#fff", t="quilômetros", how="up")

@S(v, "celular", bg=BG)
def s7(s):
    s.emoji("📱", 360, 360, 340, t=0.1, how="pop", bob=10)
    s.text("a relatividade<br>entra na conta", 40, 860, 1000, size=96, color="#ffd93d", t="relatividade", how="slam")
