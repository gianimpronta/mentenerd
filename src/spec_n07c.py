from engine import *
v = Video("n07c", decoration="stars")
v.fix = {"Leon": "Léon"}
v.phr = [("0 ,3 %", "0,3%")]
BG = "linear-gradient(180deg,#071a3a 0%,#0e2f66 60%,#1d4f9a 100%)"
L = "nov07/"
v.credits = ["The Earth seen from Apollo 17 — NASA/tripulação da Apollo 17, domínio público", "Foucault pendulum animated — DemonDeLuxe (Dominique Toussaint), CC BY-SA 3.0, Wikimedia Commons"]

@S(v, 0)
def s1(s):
    s.photo(L + "The_Earth_seen_from_Apollo_17.jpg", zoom=(1.0, 1.15))
    s.counter(0, 1000, 40, 260, 1000, size=200, color="#ffd93d", t=0.2, dur=1.6, prefix="+", suffix="")
    s.text("km/h, agora mesmo", 40, 520, 1000, size=76, color="#fff", t="quilômetros", how="up")

@S(v, "linha", bg=BG)
def s2(s):
    s.emoji("🌍", 340, 220, 330, t=0.1, how="pop", spin=360)
    s.counter(0, 1600, 40, 640, 1000, size=170, color="#ffd93d", t="seiscentos", dur=1.0, prefix="+", suffix=" km/h")
    s.pill("na linha do Equador", 260, 870, bg="#fff", t="Equador", how="up", size=54)
    s.text("e ninguém sente nada 🤷", 40, 990, 1000, size=66, color="#9fd0ff", t="nada", how="up")

@S(v, "Primeiro", bg=BG)
def s3(s):
    s.pill("1. o movimento é constante", 60, 250, bg="#ffd93d", t=0.1, how="left", size=56)
    car = s.emoji("🚗", 120, 470, 230, t=0.3, how="left")
    s.move(car, "freia", x=300, dur=0.5, ease="power4.out")
    s.text("o corpo sente a MUDANÇA<br>de velocidade", 40, 780, 1000, size=66, color="#fff", t="muda", how="up")
    s.pill("1 volta por dia, sem solavancos", 120, 1010, bg="#9fd0ff", t="volta", how="up", size=50)

@S(v, "Segundo", bg=BG)
def s4(s):
    s.pill("2. a gravidade vence", 60, 250, bg="#ffd93d", t=0.1, how="left", size=56)
    s.bar(100, 470, 880, 90, 1.0, color="#5ee08a", t="gravidade", label="gravidade")
    s.bar(100, 600, 880, 90, 0.04, color="#ff6a6a", t="rotação", label="")
    s.text("giro", 120, 700, 300, size=50, color="#ff9a9a", t="rotação", how="up")
    s.counter(0, 0.3, 40, 800, 1000, size=150, color="#ff6a6a", t="0,3%", dur=0.8, dec=1, suffix="%")
    s.text("você sente o peso, não o giro", 40, 1000, 1000, size=62, color="#fff", t="peso", how="up")

@S(v, "provar", bg=BG)
def s5(s):
    s.text("DÁ PARA PROVAR", 40, 320, 1000, size=120, color="#ffd93d", t=0.1, how="slam")
    s.emoji("🙈", 390, 600, 240, t="olhar", how="pop")
    s.text("sem olhar para o céu", 40, 920, 1000, size=70, color="#fff", t="céu", how="up")

@S(v, "1851", bg=BG)
def s6(s):
    s.photo(L + "Foucault_pendulum_animated.gif", fit="contain", frame=(240, 230, 600, 760))
    s.counter(1800, 1851, 40, 120, 1000, size=110, color="#ffd93d", t=0.1, dur=0.6)
    s.pill("Léon Foucault", 60, 1010, bg="#fff", t="Foucault", how="left", size=54)
    s.pill("67 m · Panteão, Paris", 520, 1010, bg="#ffd93d", t="Panteão", how="right", size=50, right=True)

@S(v, "plano", bg=BG)
def s7(s):
    s.raw('<div class="abs" id="pdl" style="left:535px;top:200px;width:10px;height:560px;background:#d8e6ff;transform-origin:50% 0"><div style="position:absolute;left:-45px;bottom:-45px;width:100px;height:100px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#ffe9a0,#c89a20)"></div></div>',
          f'tl.fromTo("#pdl",{{rotation:-22}},{{rotation:22,duration:1.1,repeat:5,yoyo:true,ease:"sine.inOut"}},{s.t0:.2f});')
    dial = s.rect(240, 760, 600, 600, "rgba(255,255,255,0)", t=0.1, how="pop", radius=300, border="10px dashed rgba(255,217,61,.8)")
    s.raw('', f'tl.to("{dial}",{{rotation:40,duration:{s.dur_est():.2f},ease:"none"}},{s.t0:.2f});')
    s.text("≈ 11° por hora", 40, 980, 1000, size=96, color="#ffd93d", t="onze", how="slam")

@S(v, "girou")
def s8(s):
    s.photo(L + "The_Earth_seen_from_Apollo_17.jpg", zoom=(1.15, 1.0))
    s.text("A TERRA GIROU<br>POR BAIXO DO PÊNDULO", 40, 300, 1000, size=92, color="#ffd93d", t=0.1, how="slam")
