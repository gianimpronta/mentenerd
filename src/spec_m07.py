from engine import *
v = Video("m07", decoration="grid")
v.fix = {"Hadron": "Headroom"}
BG = "linear-gradient(180deg,#0a0a14 0%,#14143a 60%,#232366 100%)"
v.credits = ["Max Headroom broadcast signal intrusion — domínio público; vídeo WGN (arquivo Fuzzy Memories) — Wikimedia Commons"]

@S(v, 0)
def s1(s):
    s.emoji("📺", 330, 300, 380, t=0.1, how="pop", bob=8)
    s.counter(1, 22, 40, 760, 1000, size=150, color="#ffd93d", t="22", dur=0.7, suffix=" nov", prefix="")
    s.text("1987 · Chicago", 40, 940, 1000, size=90, color="#fff", t="1987", how="slam")

@S(v, "telejornal", bg=BG)
def s2(s):
    s.rect(100, 360, 880, 620, "#000000", t=0.1, how="pop", radius=40, border="14px solid #3a3a7a")
    s.text("esportes", 100, 420, 880, size=64, color="#b9c8ff", t="esportes", how="fade", out="preta")
    s.counter(0, 15, 40, 1040, 1000, size=200, color="#ffd93d", t="preta", dur=1.2, suffix=" s")

@S(v, "seguida", bg=BG)
def s3(s):
    s.video("wgn_c.mp4", w=960, y=300)
    s.pill("Max Headroom", 60, 1040, bg="#ffd93d", t="Max", how="left", size=60)

@S(v, "Durou", bg=BG)
def s4(s):
    s.photo("mist/Max_Headroom_broadcast_signal_intrusion.jpg", fit="contain", frame=(60, 300, 960, 720), zoom=(1.0, 1.08))
    s.pill("cerca de meio minuto", 60, 1070, bg="#ffd93d", t="meio", how="left", size=56)

@S(v, "engenheiros", bg=BG)
def s5(s):
    k = s.emoji("🎛️", 340, 330, 380, t=0.1, how="pop")
    s.raw('', f'tl.to("{k}",{{rotation:140,duration:1.6,ease:"power2.inOut"}},{s.T("frequência") - 0.3:.2f});')
    s.text("trocaram a frequência", 40, 820, 1000, size=80, color="#fff", t="frequência", how="up")
    s.text("o invasor sumiu", 40, 980, 1000, size=70, color="#ffd93d", t="sumiu", how="up")

@S(v, "Mas", bg=BG)
def s6(s):
    s.emoji("⏰", 330, 300, 380, t=0.2, how="pop", bob=8)
    s.counter(0, 2, 40, 760, 1000, size=220, color="#ffd93d", t="duas", dur=1.0, suffix=" h")
    s.text("outra emissora", 40, 1040, 1000, size=84, color="#fff", t="outra", how="up")
