from engine import *

v = Video("c01", decoration="bubbles")
BG = "linear-gradient(180deg,#0b2f45 0%,#0e5568 60%,#127a86 100%)"
v.credits = ["Waves at La Corniche — CC BY 4.0 (Wikimedia Commons)", "Mountain landscape / erosion — CC BY 4.0 (Wikimedia Commons)", "Salt crystals — CC0 (Wikimedia Commons)"]


@S(v, 0)
def s1(s):
    s.photo("small/Waves_at_La_Corniche.jpg", pan=(-60, 0), zoom=(1.0, 1.15))
    s.counter(0, 35, 40, 260, 1000, size=240, color="#ffd93d", t=0.3, dur=2.6, suffix=" g")
    s.text("de sal por litro", 40, 520, 1000, size=74, color="#fff", t="litro")
    s.text("De onde vem tanto sal?", 60, 760, 960, size=92, color="#8ff3ff", t="onde", how="slam")


@S(v, "Principalmente", bg=BG)
def s2(s):
    s.emoji("⛰️", 30, 700, 360, t=0.2, how="pop")
    s.emoji("🌧️", 420, 330, 300, t="chuva", how="down", bob=14)
    s.pill("chuva levemente ácida", 60, 190, bg="#b9f5ff", t="levemente", how="left", size=46)
    for k in range(4):
        s.ball(380 + k * 70, 560 + (k % 2) * 40, 34, "#e8ffff", "#6fd3f0", t=("chuva", 1), how="pop")
    # cristais soltos da rocha
    for k in range(5):
        i = s.ball(210 + k * 30, 940 + (k % 2) * 25, 40, "#ffffff", "#bfe3ff", face=False, t="soltando", how="pop")
        s.move(i, "minerais", x=300 + k * 70, y=40 + (k % 3) * 25, dur=0.9)
    s.text("rocha → minerais", 520, 780, 520, size=62, color="#ffd93d", t="minerais", how="right")
    # rio até o mar
    s.path("M330 1120 C 460 1060 560 1180 700 1130 S 940 1100 1040 1160", color="#4aa3ff", width=34, t="rios", dur=1.0)
    s.raw('<div class="ball" style="left:-200px;top:1280px;width:1480px;height:1100px;background:radial-gradient(circle at 50% 18%,#2a8fd8,#10407a)"></div>')
    s.text("OCEANO", 120, 1130, 840, size=70, color="#e6fbff", t="oceano", how="up")


@S(v, "Os", bg=BG)
def s3(s):
    s.photo("small/" + [f for f in os.listdir(LIB + "/small") if f.startswith("Mountain_landscape")][0], pan=(60, 0), zoom=(1.0, 1.14))
    s.pill("rio: quase sem sal", 60, 260, bg="#b9f5ff", t="pouco", how="left", size=52)
    s.text("a água sempre passa", 60, 420, 960, size=70, color="#fff", t="sempre", how="up")


@S(v, "Já", bg="linear-gradient(180deg,#1c3f8f 0%,#2a7fd0 55%,#10407a 100%)")
def s4(s):
    s.ball(740, 210, 230, "#fff6b0", "#ffc93d", face=True, t=0.2, glow="#ffe27a", bob=10)
    s.raw('<div class="ball" style="left:-200px;top:1180px;width:1480px;height:1100px;background:radial-gradient(circle at 50% 18%,#2a8fd8,#10407a)"></div>')
    s.text("mar", 40, 1420, 400, size=64, color="#e6fbff", t="mar", how="up")
    # gotas sobem
    for k in range(4):
        i = s.ball(140 + k * 110, 1140, 60, "#ffffff", "#8fe4ff", face=True, t="evapora", how="pop")
        s.move(i, ("evapora", 1), y=-700 - k * 60, dur=1.4, ease="power1.in")
    c = s.emoji("☁️", 120, 340, 340, t="nuvem", how="pop", bob=12)
    s.out(c, "chuva", 0.1)
    s.emoji("🌧️", 120, 340, 340, t="chuva", how="fade")
    # sal fica
    for k in range(6):
        s.ball(120 + k * 120, 1480 + (k % 2) * 70, 62, "#ffffff", "#dfe8ff", face=False, t="sal", how="pop")
    s.text("o sal fica", 300, 920, 700, size=96, color="#ffd93d", t=("fica", 1), how="slam")


@S(v, "Isso", bg=BG)
def s5(s):
    s.photo("science/Salt-crystals.jpg", pan=(0, -40), zoom=(1.0, 1.18))
    s.text("milhões de anos", 40, 300, 1000, size=104, color="#ffd93d", t="milhões", how="slam")
    s.text("sal chegando,<br>quase nenhum saindo", 40, 560, 1000, size=70, color="#fff", t="chegando", how="up")


@S(v, "Por", bg="linear-gradient(180deg,#0b2f45 0%,#0e5568 100%)")
def s6(s):
    s.text("concentração de sal", 40, 330, 1000, size=74, color="#b9f5ff", t="concentração", how="up")
    s.counter(0, 35, 40, 480, 1000, size=250, color="#ffd93d", t="subindo", dur=2.2, suffix=" g/L")
    s.bar(100, 820, 880, 70, 1.0, color="#ffd93d", t="subindo", dur=2.2)
    s.emoji("🧂", 400, 960, 230, t="chegar", how="pop", bob=10)


@S(v, 40.2, bg=BG)
def s7(s):
    s.photo("small/Waves_at_La_Corniche.jpg", pan=(60, 0), zoom=(1.1, 1.0), focus=(0.8, 0.5))
    s.text("ponto final<br>de uma viagem", 40, 300, 1000, size=96, color="#ffd93d", t="ponto", how="slam")


@S(v, 45.15, bg="linear-gradient(180deg,#1c3f8f 0%,#3b9be0 100%)")
def s8(s):
    s.emoji("🌧️", 330, 280, 380, t=0.2, how="pop", bob=12)
    s.ball(430, 760, 120, "#ffffff", "#8fe4ff", face=True, t="doce", how="pop", bob=14)
    s.text("chuva = água doce", 40, 960, 1000, size=84, color="#fff", t="doce", how="up")
    s.text("só a água volta", 40, 1080, 1000, size=70, color="#ffd93d", t="só", how="up")

if __name__ == "__main__":
    print(v.build())
