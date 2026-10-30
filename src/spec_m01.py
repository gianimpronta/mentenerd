from engine import *
v = Video("m01", decoration="stars")
v.fix = {"WebDriverTorso": "Webdriver Torso"}
BG = "linear-gradient(180deg,#12062e 0%,#2a1160 60%,#4a1f9a 100%)"
v.credits = ["Aqua by Webdriver Torso (vídeo) — domínio público (Wikimedia Commons)", "Webdriver Torso slide — domínio público (Wikimedia Commons)"]

@S(v, 0)
def s1(s):
    s.photo("mist/Webdriver_Torso_Slide.tiff", fit="contain", frame=(60, 330, 960, 640), zoom=(1.0, 1.06))
    s.counter(2000, 2013, 40, 120, 1000, size=200, color="#ffd93d", t=0.2, dur=1.0)
    s.text("um canal no YouTube", 40, 1060, 1000, size=70, color="#fff", t="canal", how="up")

@S(v, "Ele", bg=BG)
def s2(s):
    s.pill("Webdriver Torso", 60, 250, bg="#ffd93d", t=0.1, how="left", size=60)
    s.counter(0, 11, 40, 480, 1000, size=300, color="#fff", t="onze" if False else "11", dur=1.0, suffix=" s")
    s.text("vídeos de 11 segundos", 40, 850, 1000, size=70, color="#b9c8ff", t="segundos", how="up")
    r = s.rect(160, 1000, 150, 90, "#ff3b3b", t="postava", how="pop")
    b = s.rect(700, 1000, 120, 70, "#3b6bff", t="postava", how="pop")
    s.move(r, "segundos", x=300, dur=1.4, ease="sine.inOut"); s.move(b, "segundos", x=-300, dur=1.4, ease="sine.inOut")

@S(v, "Neles", bg=BG)
def s3(s):
    s.video("aqua_c.mp4", w=960, y=300)
    s.pill("retângulos + bipes 🔊", 60, 1000, bg="#ffd93d", t="bipes", how="left", size=52)

@S(v, "Sem", bg=BG)
def s4(s):
    s.text("SEM DESCRIÇÃO", 40, 260, 1000, size=100, color="#ffd93d", t="descrição", how="slam")
    s.text("SEM ROSTO", 40, 460, 1000, size=100, color="#fff", t="rosto", how="slam")
    s.text("SEM EXPLICAÇÃO", 40, 660, 1000, size=100, color="#ff6a8a", t="explicação", how="slam")
    s.pill("nome de máquina: f2v - slide 0000", 60, 940, bg="#b9c8ff", t="máquina", how="left", size=44)

@S(v, "muitos", bg=BG)
def s5(s):
    s.counter(0, 70, 40, 250, 1000, size=320, color="#ffd93d", t="70", dur=1.8, suffix=" mil")
    s.text("vídeos", 40, 640, 1000, size=110, color="#fff", t="vídeos", how="up")
    s.pill("um a cada 2 minutos", 130, 880, bg="#ff6a8a", t="minutos", how="up", size=56)

@S(v, ("Ninguém", 2), bg=BG)
def s6(s):
    s.text("?", 240, 260, 600, size=620, color="#ffd93d", t=0.1, how="slam")
    s.text("quem estava por trás?", 40, 1000, 1000, size=76, color="#fff", t="trás", how="up")

@S(v, "Seria", bg=BG)
def s7(s):
    s.emoji("🕵️", 100, 280, 240, t="código", how="pop", bob=8)
    s.pill("código de espiões?", 60, 560, bg="#ffd93d", t="código", how="left", size=48)
    s.emoji("📣", 640, 640, 240, t="propaganda", how="pop", bob=8)
    s.pill("propaganda viral?", 60, 820, bg="#5ee08a", t="propaganda", how="left", size=48)
    s.emoji("🔊", 120, 880, 200, t="mensagem", how="pop", bob=8)
    s.pill("mensagem nos bipes?", 380, 1020, bg="#ff9a2e", t="mensagem", how="left", size=48)

@S(v, ("Só", 3), bg=BG)
def s8(s):
    for k in range(24):
        col = "#ff3b3b" if k % 2 == 0 else "#3b6bff"
        s.rect(80 + (k % 6) * 150, 280 + (k // 6) * 130, 110, 80, col, t=0.1 + k * 0.03, how="pop", radius=8)
    for k, (x, y) in enumerate([(230, 410), (680, 540), (380, 670)]):
        s.rect(x - 14, y - 14, 138, 108, "rgba(255,217,61,0)", t="três", how="pop", radius=12, border="8px solid #ffd93d")
    s.text("três fugiam do padrão", 40, 900, 1000, size=84, color="#ffd93d", t="fugiam", how="slam")
