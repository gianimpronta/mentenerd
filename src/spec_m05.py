from engine import *
v = Video("m05", decoration="stars")
v.phr = []
BG = "linear-gradient(180deg,#050a2a 0%,#0a1f5a 60%,#12358a 100%)"
v.credits = ["Cicada 3301 first message — domínio público", "Runic letters (Elder Futhark) — domínio público", "Cicada 3301 poster locations — CC BY-SA 4.0 (Wikimedia Commons)", "Cicada 3301 logo — uso educativo/fair use"]

@S(v, 0)
def s1(s):
    s.photo("mist/Cicada3301_s_First_Message.jpg", fit="contain", frame=(60, 280, 960, 760), zoom=(1.0, 1.06))
    s.pill("4 de janeiro de 2012", 60, 160, bg="#ffd93d", t=0.2, how="left", size=56)
    s.text("procurando pessoas<br>muito inteligentes", 40, 1060, 1000, size=60, color="#b9d0ff", t="procurando", how="up")

@S(v, "escondia", bg=BG)
def s2(s):
    for k, (lab, c) in enumerate([("texto", "#ffffff"), ("código", "#ffd93d"), ("código", "#5ee08a")]):
        s.rect(100 + k * 300, 300, 260, 160, c, t=("texto", "código", "outro")[k], how="pop", radius=30)
        s.text(lab, 100 + k * 300, 350, 260, size=56, color="#14123a", t=("texto", "código", "outro")[k], how="fade")
    s.path("M360 380 L400 380 M660 380 L700 380", color="#fff", width=14, t="código", dur=0.5)
    s.pill("criptografia", 60, 640, bg="#b9d0ff", t="criptografia", how="left", size=60)
    s.pill("esteganografia", 60, 780, bg="#ff9a2e", t="esteganografia", how="left", size=60)
    s.text("e muita pesquisa", 40, 960, 1000, size=70, color="#fff", t="pesquisa", how="up")

@S(v, "trilha", bg=BG)
def s3(s):
    s.photo("mist/Runic_letters_elder_futhark.jpg", fit="contain", frame=(60, 280, 960, 760), zoom=(1.0, 1.06))
    s.pill("páginas cheias de runas", 60, 160, bg="#ffd93d", t="runas", how="left", size=52)

@S(v, "cartazes", bg=BG)
def s4(s):
    s.photo("mist/Cicada_3301_poster_locations.png", fit="contain", frame=(60, 250, 960, 780), zoom=(1.0, 1.06))
    s.pill("cartazes em lugares físicos do mundo", 40, 1070, bg="#ffd93d", t="físicos", how="left", size=44)

@S(v, "assinadas", bg=BG)
def s5(s):
    s.emoji("🔑", 340, 300, 380, t=0.1, how="pop", bob=10)
    s.text("mesma chave digital", 40, 800, 1000, size=84, color="#ffd93d", t="chave", how="up")
    s.text("poucos chegaram ao fim", 40, 980, 1000, size=60, color="#fff", t="Poucos", how="up")

@S(v, "grupo", bg=BG)
def s6(s):
    s.photo("mist/Cicada_3301_logo.jpg", fit="contain", frame=(160, 280, 760, 760), zoom=(1.0, 1.06))
    s.pill("Cicada 3301", 60, 1080, bg="#ffd93d", t="Cicada", how="left", size=62)

@S(v, "estranho", bg=BG)
def s7(s):
    s.text("só o primeiro<br>ano", 40, 360, 1000, size=130, color="#ffd93d", t="primeiro", how="slam")
    s.counter(2012, 2017, 40, 800, 1000, size=200, color="#fff", t="durar", dur=1.5)
