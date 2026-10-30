from engine import *
v = Video("m08", decoration="grid")
v.fix = {"Hadron": "Headroom"}
v.phr = [("micro ondas", "micro-ondas"), ("mata moscas", "mata-moscas")]
BG = "linear-gradient(180deg,#0a0a14 0%,#14143a 60%,#232366 100%)"
v.credits = ["Vídeo WTTW (arquivo) — Wikimedia Commons", "WCIA television tower antennas — CC BY 2.5 (Wikimedia Commons)"]

@S(v, 0)
def s1(s):
    s.emoji("📺", 330, 300, 380, t=0.1, how="pop", bob=8)
    s.text("23:20", 40, 760, 1000, size=240, color="#ffd93d", t="11", how="slam")
    s.pill("Doctor Who na TV pública", 60, 1060, bg="#b9c8ff", t="Doctor", how="left", size=52)

@S(v, "invadida", bg=BG)
def s2(s):
    s.video("wttw_a.mp4", w=960, y=300)
    s.pill("agora com áudio · quase 1 min e meio", 40, 1040, bg="#ffd93d", t="áudio", how="left", size=44)

@S(v, "apanhando", bg=BG)
def s3(s):
    s.video("wttw_b.mp4", w=960, y=300)
    s.pill("mata-moscas", 60, 1040, bg="#ffd93d", t=0.3, how="left", size=56)

@S(v, "plantão", bg=BG)
def s4(s):
    s.emoji("🔇", 340, 340, 340, t=0.1, how="pop", bob=8)
    s.text("sem engenheiros<br>de plantão", 40, 780, 1000, size=90, color="#ffd93d", t="plantão", how="slam")

@S(v, "Como", bg=BG)
def s5(s):
    s.text("?", 240, 260, 600, size=620, color="#ffd93d", t=0.1, how="slam")
    s.text("como foi possível?", 40, 1000, 1000, size=84, color="#fff", t="possível", how="up")

@S(v, "invasores", bg=BG)
def s6(s):
    s.photo("mist/WCIA_television_tower_antennas.jpg", pan=(-30, -30), zoom=(1.0, 1.15), tag="torre de transmissão (ilustrativa)")
    s.text("sinal mais forte<br>que o da emissora", 40, 300, 1000, size=84, color="#ffd93d", t="forte", how="slam")

@S(v, "FCC", bg=BG)
def s7(s):
    s.emoji("🔎", 340, 300, 380, t=0.1, how="pop", bob=8)
    s.text("FCC: investigação", 40, 760, 1000, size=92, color="#fff", t="investigação", how="up")
    s.text("ninguém encontrado", 40, 920, 1000, size=70, color="#ffd93d", t="ninguém", how="up")

@S(v, "1992", bg=BG)
def s8(s):
    s.counter(1980, 1992, 40, 380, 1000, size=300, color="#ffd93d", t=0.1, dur=1.0)
    s.text("o prazo para processar acabou", 40, 760, 1000, size=76, color="#fff", t="prazo", how="up")

@S(v, "Até", bg="linear-gradient(180deg,#000 0%,#14143a 100%)")
def s9(s):
    s.text("NUNCA<br>IDENTIFICADOS", 40, 560, 1000, size=130, color="#ff6a8a", t="ninguém", how="slam", rot=-3, extra="border:10px solid #ff6a8a;padding:20px 0;border-radius:30px")
