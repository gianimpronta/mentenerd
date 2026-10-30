from engine import *
v = Video("m02", decoration="stars")
v.fix = {"WebDriver": "Webdriver", "1": "1,99€", ",99€": ""}
BG = "linear-gradient(180deg,#12062e 0%,#2a1160 60%,#4a1f9a 100%)"
v.credits = ["Eiffel Tower and Pont Alexandre III at night — CC BY 2.0 (Wikimedia Commons)", "Google Webdriver Torso logo — Wikimedia Commons"]

@S(v, 0)
def s1(s):
    for k, (x, lab) in enumerate([(60, "1"), (400, "2"), (740, "3")]):
        s.rect(x, 360, 280, 380, "#ffffff", t=("três" if k == 0 else 0.4 + k * 0.5) if k == 0 else 0.5 + k * 0.5, how="pop", radius=30)
        s.text(lab, x, 400, 280, size=240, color="#14123a", t=0.5 + k * 0.5 if k else 0.5, how="slam")
    s.text("os três vídeos estranhos", 40, 880, 1000, size=80, color="#ffd93d", t="estranhos", how="up")

@S(v, "primeiro", bg=BG)
def s2(s):
    # silhueta dançando (sem foto)
    s.rect(380, 280, 120, 120, "#14123a", t=0.2, how="pop", radius=60)
    body = s.rect(350, 400, 180, 320, "#14123a", t=0.2, how="pop", radius=60)
    s.rect(300, 440, 70, 260, "#14123a", t=0.3, how="pop", radius=35, extra="transform:rotate(25deg)")
    s.rect(510, 440, 70, 260, "#14123a", t=0.3, how="pop", radius=35, extra="transform:rotate(-25deg)")
    s.raw('', f'tl.to("{body}",{{rotation:6,duration:0.35,repeat:11,yoyo:true,ease:"sine.inOut"}},{s.t0 + 0.6:.2f});')
    s.rect(120, 880, 200, 120, "#ff3b3b", t=0.2, how="pop", radius=10)
    s.text("→", 330, 860, 160, size=120, color="#ffd93d", t="silhueta", how="pop")
    s.text("silhueta", 420, 890, 520, size=70, color="#fff", t="silhueta", how="up")
    s.pill("o famoso meme", 60, 1060, bg="#ffd93d", t="meme", how="left", size=52)

@S(v, "segundo", bg=BG)
def s3(s):
    s.photo("mist/Eiffel_Tower_and_Pont_Alexandre_III_at_night.jpg", pan=(-40, 0), zoom=(1.0, 1.15))
    s.pill("Torre Eiffel à noite", 40, 260, bg="#ffd93d", t="Eiffel", how="left", size=56)

@S(v, "terceiro", bg=BG)
def s4(s):
    s.pill("só na França 🇫🇷", 60, 260, bg="#ffffff", t="França", how="left", size=60)
    s.pill("1,99 €", 60, 460, bg="#ffd93d", t="199", how="left", size=80)
    s.pill("dublado em espanhol 🇪🇸", 60, 700, bg="#ff6a8a", t="espanhol", how="left", size=56)
    s.emoji("📺", 380, 900, 240, t="episódio", how="pop", bob=8)

@S(v, ("Eram", 2), bg=BG)
def s5(s):
    s.text("algo mais<br>organizado", 40, 300, 1000, size=110, color="#ffd93d", t="organizado", how="slam")
    s.emoji("🕸️", 380, 720, 300, t="parecia", how="pop", bob=8)

@S(v, "blogueiro", bg=BG)
def s6(s):
    pts = [(200, 420), (500, 320), (820, 450), (320, 760), (700, 780), (540, 560)]
    for k, (x, y) in enumerate(pts):
        s.rect(x, y, 130, 90, "#ff3b3b" if k % 2 == 0 else "#3b6bff", t=("rede" if k > 1 else 0.3 + k * 0.2), how="pop", radius=10)
    s.path("M265 465 L565 365 M565 365 L885 495 M265 465 L385 805 M885 495 L765 825 M385 805 L765 825 M265 465 L605 605 M605 605 L885 495", color="#ffd93d", width=8, t="rede", dur=1.4)
    s.emoji("🔍", 120, 900, 220, t="blogueiro", how="pop", bob=8)
    s.text("uma rede de contas", 40, 1010, 1000, size=70, color="#fff", t="rede", how="up")

@S(v, "junho", bg=BG)
def s7(s):
    s.photo("mist/Google_webdriver_torso_logo.gif", fit="contain", frame=(160, 300, 760, 760), zoom=(1.0, 1.08))
    s.pill("junho de 2014: o YouTube responde", 40, 1100, bg="#ffd93d", t="respondeu", how="left", size=46)

@S(v, "Aquilo", bg=BG)
def s8(s):
    s.emoji("⚙️", 340, 300, 380, t=0.1, how="pop", spin=120)
    s.text("TESTE DE ENVIO", 40, 780, 1000, size=100, color="#fff", t="teste", how="slam")
    s.text("só material de teste", 40, 960, 1000, size=64, color="#ffd93d", t="material", how="up", rot=-3, extra="border:8px solid #ffd93d;padding:12px 0;border-radius:24px")

@S(v, "maior", bg=BG)
def s9(s):
    s.text("à vista de<br>todo mundo", 40, 360, 1000, size=120, color="#ffd93d", t="vista", how="slam")
