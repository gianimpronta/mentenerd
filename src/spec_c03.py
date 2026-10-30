from engine import *
v = Video("c03", decoration="stars")
BG = "linear-gradient(180deg,#070b2a 0%,#10206b 60%,#1e3a9a 100%)"
v.credits = ["Moon nearside LRO — NASA/GSFC/ASU, domínio público", "Earthrise over Compton crater — NASA/LRO, domínio público"]

MOON = ("#e6e6ee", "#8e90a6")

@S(v, 0)
def s1(s):
    s.photo("small/Moon_nearside_LRO_5000.jpg", pan=(0, -30), zoom=(1.0, 1.15))
    s.text("sempre o mesmo lado", 40, 300, 1000, size=100, color="#ffd93d", t="mesmo", how="slam")

@S(v, "porque", bg=BG)
def s2(s):
    s.ball(400, 520, 280, "#7fd3ff", "#1f5fb0", face=True, t=0.1, how="pop")
    s.raw('<div id="orb" style="position:absolute;left:540px;top:660px;width:0;height:0"><div class="ball" id="moonO" style="left:300px;top:-90px;width:180px;height:180px;background:radial-gradient(circle at 36% 30%,#f2f2f8,#8e90a6)"><div style="position:absolute;left:0;top:30%;width:60%;height:50%"><i class="e l" style="left:6%;width:42%;height:60%"><b></b></i><i class="e r" style="right:6%;width:42%;height:60%"><b></b></i></div></div></div>',
          f'tl.fromTo("#orb",{{rotation:0}},{{rotation:360,duration:{s.dur_est()+0.5:.2f},ease:"none"}},{s.t0:.2f});')
    s.pill("1 volta em torno de si = 27 dias", 40, 250, bg="#b9d0ff", t="eixo", how="left", size=44)
    s.pill("1 volta em torno da Terra = 27 dias", 40, 340, bg="#ffd93d", t="mesmo", how="left", size=44)
    s.text("acoplamento de maré", 40, 1000, 1000, size=84, color="#fff", t="acoplamento", how="slam")

@S(v, "passado", bg=BG)
def s3(s):
    m = s.ball(380, 620, 300, "#f2f2f8", "#8e90a6", face=True, t=0.1)
    s.raw('', f'tl.to("{m}",{{rotation:1080,duration:{(s.T("gravidade")-s.t0):.2f},ease:"power2.out"}},{s.t0:.2f});')
    s.pill("antes: girava mais rápido", 60, 330, bg="#ffd93d", t=0.2, how="left", size=48)
    s.ball(-380, 1160, 520, "#7fd3ff", "#1f5fb0", face=True, t="gravidade", how="pop")
    s.text("a gravidade da Terra freou a Lua", 40, 960, 1000, size=64, color="#fff", t="freando", how="up")

@S(v, "resultado", bg=BG)
def s4(s):
    s.photo("science/Earthrise_over_Compton_crater_-LRO_full_res.jpg", pan=(-60, 0), zoom=(1.0, 1.15))
    s.text("o mesmo rosto<br>sempre para nós", 40, 300, 1000, size=88, color="#ffd93d", t="mesmo", how="slam")

@S(v, "oculto", bg=BG)
def s5(s):
    s.ball(260, 420, 560, "#9a9cb0", "#202238", face=False, t=0.1)
    s.text("lado oculto", 40, 1010, 1000, size=104, color="#ffd93d", t="oculto", how="slam")
    s.text("nunca aparece daqui", 40, 1140, 1000, size=62, color="#fff", t="nunca", how="up")

@S(v, "Ele", bg=BG)
def s6(s):
    s.ball(300, 620, 480, "#d8d8e4", "#6e7088", face=False, t=0.1)
    pr = s.emoji("🛰️", 40, 300, 240, t=0.3, how="pop", bob=10)
    s.move(pr, "sonda", x=300, y=260, dur=1.4)
    s.emoji("📸", 700, 420, 180, t="foto", how="pop")
    s.pill("1959 · sonda soviética Luna 3", 40, 1060, bg="#ffd93d", t="1959", how="left", size=50)

@S(v, "finalmente", bg=BG)
def s7(s):
    s.ball(100, 420, 400, "#d8d8e4", "#6e7088", face=False, t=0.1)
    for k, (x, y, r) in enumerate([(180, 520, 90), (330, 640, 70), (220, 720, 60), (300, 480, 50)]):
        s.ball(x, y, r, "#4a4c63", "#3a3c52", t=0.2 + k * 0.1)
    s.text("lado visível", 60, 860, 460, size=48, color="#fff", t=0.3, how="up")
    s.ball(580, 420, 400, "#d8d8e4", "#8a8ca0", face=False, t="crateras")
    for k in range(9):
        s.ball(620 + (k * 83) % 300, 460 + (k * 61) % 300, 26 + (k % 3) * 14, "#9a9cb0", "#6a6c84", t=("crateras", 1), how="pop")
    s.text("lado oculto", 560, 860, 460, size=48, color="#fff", t="crateras", how="up")
    s.text("muito mais crateras", 40, 1000, 1000, size=72, color="#ffd93d", t="crateras", how="up")
