from engine import *
v = Video("m06", decoration="stars")
v.fix = {"Primos": "Primus"}
v.phr = [("chama o gente", "chamou gente")]
BG = "linear-gradient(180deg,#050a2a 0%,#0a1f5a 60%,#12358a 100%)"
v.credits = ["Runic letters (Elder Futhark) — domínio público", "Cicada 3301 logo — uso educativo/fair use"]

def mark(s, x, label, color, t, sub):
    s.ball(x, 600, 90, color[0], color[1], t=t, how="pop")
    s.text(label, x - 100, 710, 290, size=64, color="#fff", t=t, how="up")
    s.text(sub, x - 130, 790, 350, size=40, color="#b9d0ff", t=t, how="fade")

@S(v, 0)
def s1(s):
    s.path("M60 640 L1020 640", color="#ffffff", width=12, t=0.1, dur=0.8)
    mark(s, 130, "2013", ("#ffd93d", "#ff9a2e"), "2013", "enigma")
    mark(s, 460, "2014", ("#5ee08a", "#1f9a5a"), "2014", "enigma")
    s.text("o grupo voltou", 40, 280, 1000, size=100, color="#ffd93d", t=0.2, how="slam")

@S(v, "Liber", bg=BG)
def s2(s):
    s.photo("mist/Runic_letters_elder_futhark.jpg", fit="contain", frame=(60, 280, 960, 760), zoom=(1.0, 1.06))
    s.pill("Liber Primus: livro de runas", 60, 160, bg="#ffd93d", t=0.2, how="left", size=52)
    s.text("em grande parte nunca decifrado", 40, 1060, 1000, size=56, color="#fff", t="decifrado", how="up")

@S(v, "2015", bg=BG)
def s3(s):
    s.path("M60 640 L1020 640", color="#ffffff", width=12, t=0.1, dur=0.6)
    s.ball(100, 590, 100, "#ff4d4d", "#a01f1f", t="2015", how="pop")
    s.text("2015", 30, 720, 260, size=64, color="#fff", t="2015", how="up")
    s.text("sem enigma", 0, 800, 320, size=44, color="#ff8a8a", t="enigma", how="fade")
    s.emoji("🐦", 430, 500, 150, t="Twitter", how="pop")
    s.text("2016", 400, 720, 260, size=64, color="#fff", t="2016", how="up")
    s.emoji("✉️", 760, 500, 150, t="abril", how="pop")
    s.text("abril de 2017", 700, 720, 340, size=56, color="#ffd93d", t="abril", how="up")
    s.text("última mensagem verificada", 40, 960, 1000, size=60, color="#fff", t="verificada", how="up")

@S(v, "Depois", bg="linear-gradient(180deg,#000 0%,#050a2a 100%)")
def s4(s):
    s.text("silêncio", 40, 700, 1000, size=150, color="#b9d0ff", t="silêncio", how="fade")

@S(v, "Quem", bg=BG)
def s5(s):
    s.text("?", 340, 160, 400, size=420, color="#ffd93d", t=0.1, how="slam")
    s.emoji("🕵️", 100, 700, 200, t="espionagem", how="pop", bob=8)
    s.pill("agências", 340, 760, bg="#ffd93d", t="espionagem", how="left", size=54)
    s.emoji("🗝️", 100, 940, 200, t="sociedades", how="pop", bob=8)
    s.pill("sociedades secretas", 340, 1000, bg="#b9d0ff", t="secretas", how="left", size=54)
    s.text("SEM PROVA", 40, 1110, 1000, size=80, color="#ff6a8a", t="provou", how="slam", rot=-3)

@S(v, "Hoje", bg=BG)
def s6(s):
    s.photo("mist/Runic_letters_elder_futhark.jpg", pan=(-40, 0), zoom=(1.05, 1.18))
    s.text("páginas inteiras<br>por decifrar", 40, 300, 1000, size=100, color="#ffd93d", t="inteiras", how="slam")

@S(v, "Cicada", bg=BG)
def s7(s):
    s.photo("mist/Cicada_3301_logo.jpg", fit="contain", frame=(160, 280, 760, 760), zoom=(1.0, 1.06))
    s.pill("nunca disse para quê", 60, 1080, bg="#ffd93d", t="nunca", how="left", size=56)
