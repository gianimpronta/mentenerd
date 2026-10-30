from engine import *
v = Video("t01", decoration="grid")
v.fix = {"ReadSolomon": "Reed-Solomon", "%": ""}
BG = "linear-gradient(180deg,#10153a 0%,#2a1d6a 60%,#4a2a9a 100%)"
v.credits = ["QR Code gerado por código; ilustração própria"]

def patch(s, t, x, y, w, h, color="#ff4d4d"):
    return s.rect(x, y, w, h, color, t=t, how="pop", radius=18)

@S(v, 0)
def s1(s):
    s.qr(134, 280, 812, t=0.1)
    q = s.qr_info
    s.rect(560, 300, 380, 300, "#14123a", t="rasgado", how="slam", radius=30)
    s.ball(250, 800, 260, "#14123a", "#14123a", t="sujo", how="pop")
    s.emoji("📱", 800, 1000, 160, t="funciona", how="pop", bob=8)
    s.emoji("✅", 880, 880, 120, t="mesmo", how="pop")

@S(v, "correção", bg=BG)
def s2(s):
    s.qr(134, 260, 600, t=0.1)
    s.pill("conteúdo", 60, 940, bg="#ffffff", t="conteúdo", how="left", size=54)
    s.pill("dados extras de redundância", 60, 1060, bg="#ffd93d", t="redundância", how="left", size=50)
    s.emoji("💿", 760, 300, 200, t="CDs", how="pop", bob=8)
    s.pill("Reed-Solomon", 560, 560, bg="#5ee08a", t="Reed-Solomon", how="right", size=56)

@S(v, "nível", bg=BG)
def s3(s):
    s.qr(190, 520, 700, t=0.1)
    s.counter(0, 30, 40, 220, 1000, size=240, color="#ffd93d", t="30", dur=1.4, suffix="%")
    s.text("pode estar danificado", 40, 470, 1000, size=60, color="#fff", t="danificado", how="up")
    s.rect(500, 600, 340, 300, "#ff4d4d", t="danificado", how="pop", radius=28, opacity=0.9)

@S(v, "logo", bg=BG)
def s4(s):
    s.qr(134, 280, 812, t=0.0)
    s.rect(410, 556, 260, 260, "#ffffff", t="logo", how="pop", radius=40)
    s.emoji("🧠", 450, 590, 190, t="logo", how="pop", bob=8)
    s.text("leitura continua funcionando", 40, 1110, 1000, size=60, color="#ffd93d", t="quebrar", how="up")

@S(v, "quadrados", bg=BG)
def s5(s):
    q = s.qr(134, 280, 812, t=0.0)
    i = s.qr_info
    c, n = i["cell"], i["n"]
    for (cx, cy) in [(0, 0), (n - 7, 0), (0, n - 7)]:
        s.rect(i["x"] + cx * c - 8, i["y"] + cy * c - 8, 7 * c + 16, 7 * c + 16, "rgba(255,217,61,0)", t="quadrados", how="pop", radius=14, border="10px solid #ffd93d")
    s.raw('', f'tl.to("{q}",{{rotation:180,duration:1.4,ease:"power2.inOut"}},{s.T("cabeça") - 0.3:.2f});')
    s.pill("posição e orientação", 60, 1110, bg="#ffd93d", t="orientação", how="left", size=52)

@S(v, "matemática", bg=BG)
def s6(s):
    s.text("∑", 240, 300, 600, size=620, color="#ffd93d", t=0.1, how="slam")
    s.text("matemática escondida<br>nos quadradinhos", 40, 1000, 1000, size=76, color="#fff", t="quadradinhos", how="up")
