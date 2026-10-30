from engine import *
v = Video("c04", decoration="stars")
BG = "linear-gradient(180deg,#1a0630 0%,#4a0f6b 60%,#8a1f8a 100%)"
v.credits = ["Messier 87 — Event Horizon Telescope, CC BY 4.0", "Black Hole with Accretion Disk Visualization — NASA SVS, domínio público"]

def bh(s, x, y, r, t=0.1):
    s.ball(x - 40, y - 40, r + 80, "rgba(255,160,50,.0)", "rgba(255,120,30,.55)", t=t)
    s.ball(x, y, r, "#000", "#0a0010", t=t, glow="#ff8a2e")

@S(v, 0)
def s1(s):
    s.photo("science/Black_hole_-_Messier_87_crop_max_res.jpg", pan=(0, -30), zoom=(1.0, 1.15))
    s.text("cair num<br>buraco negro?", 40, 300, 1000, size=110, color="#ffd93d", t="acontece", how="slam")

@S(v, "Antes", bg=BG)
def s2(s):
    bh(s, 340, 1000, 400)
    a = s.emoji("🧑‍🚀", 400, 280, 300, t=0.3, how="pop")
    s.move(a, "gravidade", y=380, dur=2.0, ease="power1.in")
    s.pill("gravidade muda de ponto a ponto", 40, 190, bg="#ffd93d", t="gravidade", how="left", size=44)
    s.pill("pés: puxão MUITO maior", 40, 1420, bg="#ff6a4d", t="pés", how="left", size=44)
    s.pill("cabeça: puxão menor", 40, 1510, bg="#b36bff", color="#fff", t="cabeça", how="left", size=44)

@S(v, ("Você", 3), bg=BG)
def s3(s):
    a = s.emoji("🧑‍🚀", 380, 520, 300, t=0.1, how="pop")
    s.raw('', f'tl.to("{a}",{{scaleY:2.4,scaleX:.55,duration:1.6,ease:"power2.inOut"}},{s.t0 + 0.4:.2f});')
    s.emoji("🍝", 330, 1040, 260, t="espaguete", how="pop", bob=10)
    s.text("ESPAGUETIFICAÇÃO", 20, 220, 1040, size=88, color="#ffd93d", t="espaguetificação", how="slam")

@S(v, "pequenos", bg=BG)
def s4(s):
    s.photo("science/Black_Hole_with_Accretion_Disk_Visualization__SVS14619_-_1-Approaching.jpg", pan=(-40, 0), zoom=(1.0, 1.16))
    s.pill("horizonte de eventos = ponto sem volta", 40, 240, bg="#ffd93d", t="horizonte", how="left", size=44)

@S(v, "gigantes", bg=BG)
def s5(s):
    bh(s, 140, 900, 800)
    a = s.emoji("🧑‍🚀", 420, 330, 260, t=0.2, how="pop")
    s.move(a, "atravessar", y=430, dur=1.6, ease="power1.in")
    s.text("nada de especial", 40, 220, 1000, size=84, color="#fff", t="especial", how="up")

@S(v, "problema", bg=BG)
def s6(s):
    s.photo("science/Black_Hole_with_Accretion_Disk_Visualization__SVS14619_-_2-Orbiting_a_.jpg", pan=(40, 0), zoom=(1.0, 1.16))
    s.text("nem a luz volta", 40, 300, 1000, size=96, color="#ffd93d", t="luz", how="slam")

@S(v, "dentro", bg=BG)
def s7(s):
    s.text("?", 240, 360, 600, size=640, color="#ffd93d", t=0.1, how="slam")
    s.text("a física deixa de funcionar direito", 40, 1000, 1000, size=70, color="#fff", t="física", how="up")
