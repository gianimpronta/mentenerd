from engine import *
import math
v = Video("c06", decoration="bubbles")
BG = "linear-gradient(180deg,#0b2a52 0%,#1a5a9a 60%,#3aa0d8 100%)"
v.credits = ["Iceberg in North Star Bay — NASA, domínio público", "Ice Ih crystal lattice — CC BY-SA 4.0 (Wikimedia Commons)", "Lake Baikal in winter — CC BY-SA 4.0 (Wikimedia Commons)"]

@S(v, 0)
def s1(s):
    s.photo("small/Iceberg_in_North_Star_Bay__Greenland.jpg", pan=(-50, 0), zoom=(1.0, 1.16))
    s.text("o gelo<br>boia", 40, 300, 1000, size=170, color="#ffd93d", t="contrário", how="slam")

@S(v, "líquida", bg=BG)
def s2(s):
    cx, cy, R = 540, 560, 230
    items = []
    for k in range(6):
        ang = math.radians(60 * k - 90)
        gx, gy = cx + R * math.cos(ang) - 55, cy + R * math.sin(ang) - 55
        lx, ly = cx + (R * 0.45) * math.cos(ang + k) - 55, cy + (R * 0.45) * math.sin(ang * 1.7) - 55
        i = s.ball(lx, ly, 110, "#e8ffff", "#6fd3f0", face=True, t=0.1 + k * 0.05)
        s.raw('', f'tl.to("{i}",{{x:{(gx-lx):.0f},y:{(gy-ly):.0f},duration:1.0,ease:"power2.inOut"}},{s.T("congela"):.2f});')
        s.raw('', f'tl.to("{i}",{{y:"+=18",duration:.35,repeat:7,yoyo:true,ease:"sine.inOut"}},{s.t0 + 0.4 + k*0.05:.2f});')
    s.pill("líquida: juntinhas, em movimento", 40, 200, bg="#b9f5ff", t="movimento", how="left", size=44)
    s.text("congela → hexágono<br>com espaços vazios", 40, 940, 1000, size=76, color="#ffd93d", t="hexágonos", how="up")

@S(v, "ocupa", bg=BG)
def s3(s):
    s.photo("small/Ice_Ih_Crystal_Lattice.jpg", fit="contain", frame=(60, 230, 960, 800), zoom=(1.0, 1.08))
    s.counter(0, 9, 40, 1060, 1000, size=104, color="#ffd93d", t="9", dur=1.2, suffix="% menos denso")

@S(v, "lago", bg=BG)
def s4(s):
    s.photo("small/Lake_Baikal_in_winter.jpg", pan=(-50, 0), zoom=(1.0, 1.15))
    s.pill("gelo só em cima", 40, 240, bg="#ffd93d", t="cima", how="left", size=56)

@S(v, "Embaixo", bg=BG)
def s5(s):
    s.raw('<div class="abs" style="left:60px;top:300px;width:960px;height:140px;border-radius:30px;background:linear-gradient(#e9fbff,#9bdcf5)"></div><div class="abs" style="left:60px;top:440px;width:960px;height:560px;border-radius:0 0 60px 60px;background:linear-gradient(#1f7ac0,#0f3f7a)"></div>')
    s.text("gelo", 60, 330, 960, size=70, color="#14123a", t=0.1, how="fade")
    f = s.emoji("🐟", 140, 700, 200, t="peixes", how="pop")
    s.move(f, "sobrevivem", x=520, dur=1.8, ease="sine.inOut")
    s.text("água líquida", 60, 520, 960, size=64, color="#fff", t="líquida", how="up")

@S(v, "afundasse", bg=BG)
def s6(s):
    s.raw('<div class="abs" style="left:60px;top:300px;width:960px;height:700px;border-radius:40px;background:linear-gradient(#1f7ac0,#0f3f7a)"></div>')
    s.raw('<div class="abs" id="cong" style="left:60px;top:860px;width:960px;height:140px;border-radius:0 0 40px 40px;background:linear-gradient(#e9fbff,#9bdcf5);opacity:0"></div>', f'tl.fromTo("#cong",{{opacity:0,scaleY:0.2,transformOrigin:"50% 100%"}},{{opacity:1,scaleY:1,duration:1.4}},{s.T("congelar"):.2f});')
    s.text("congelaria de baixo<br>para cima", 40, 1030, 1000, size=70, color="#ffd93d", t="baixo", how="up")

@S(v, "detalhe", bg=BG)
def s7(s):
    s.ball(430, 420, 220, "#e8ffff", "#6fd3f0", face=True, t=0.1, how="pop", bob=12)
    s.text("um detalhe<br>pequeno muda<br>o planeta", 40, 760, 1000, size=92, color="#ffd93d", t="planeta", how="slam")
