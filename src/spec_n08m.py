from engine import *
v = Video("n08m", decoration="grid")
v.fix = {"Seriam": "Seria um", "burzorg": "Berzerk", "Playstation": "PlayStation"}
v.phr = [("E esse", "Esse"), ("conhecia, Polybius.", "conhecia: Polybius."), ("fliperamas. Com", "fliperamas, com")]
BG = "linear-gradient(180deg,#12021f 0%,#2a0845 60%,#4a0e6b 100%)"
A, B, Y = "#ff3df2", "#3dfcff", "#ffd93d"
L = "nov08/"
v.credits = ["Polybius Arcade 1 cropped — DocAtRS, CC BY-SA 3.0, Wikimedia Commons"]

@S(v, 0, bg="#08010f")
def s1(s):
    s.emoji("🌀", 340, 230, 400, t=0.05, how="pop", spin=360)
    s.text("ESSE JOGO<br>ADOECIA QUEM JOGAVA", 40, 760, 1000, size=104, color=A, t=0.1, how="slam")
    s.text("…pelo menos, diz a lenda", 40, 1110, 1000, size=66, color="#fff", t="lenda", how="up")

@S(v, ("1981", 1), bg=BG)
def s2(s):
    s.counter(1960, 1981, 40, 230, 1000, size=230, color=B, t=0.0, dur=0.8)
    s.pill("📍 Portland, EUA", 250, 520, bg=Y, t="Portland", how="up", size=60)
    s.emoji("🕹️", 400, 680, 260, t="fliperamas", how="pop", bob=6)
    s.text("POLYBIUS", 40, 1020, 1000, size=170, color=A, t="Polybius", how="slam")

@S(v, "gabinete", bg=BG)
def s3(s):
    s.photo(L + "Polybius_Arcade_1_cropped.jpg", fit="contain", frame=(300, 200, 480, 1000))
    s.pill("abstrato", 60, 1280, bg=B, t="abstrato", how="left", size=56)
    s.pill("geométrico", 380, 1280, bg=Y, t="geométricas", how="left", size=56)
    s.pill("viciante", 740, 1280, bg=A, color="#fff", t="viciante", how="left", size=56)
    s.text("fila de jogadores 👥👥👥", 40, 1420, 1000, size=64, color="#fff", t="fila", how="up")

@S(v, ("Quem", 2), bg="#14001f")
def s4(s):
    s.emoji("😵‍💫", 380, 200, 300, t=0.05, how="pop", bob=10)
    for i, (w, lab) in enumerate([("convulsões", "convulsões"), ("amnésia", "amnésia"), ("insônia", "insônia"), ("pesadelos", "pesadelos"), ("alucinações", "alucinações")]):
        s.pill(lab, 90 + (i % 2) * 380, 620 + i * 130, bg=[A, B, Y, A, B][i], color="#14123a", t=w, how="left", size=58)

@S(v, "homens", bg=BG)
def s5(s):
    for i in range(3):
        s.emoji("🕴️", 150 + i * 280, 300, 240, t="terno", how="up", bob=4)
    s.text("HOMENS DE TERNO PRETO", 40, 680, 1000, size=86, color="#fff", t="preto", how="slam")
    s.pill("💾 recolhiam dados das máquinas", 90, 900, bg=Y, t="dados", how="up", size=54)

@S(v, "poucas", bg="#0b0114")
def s6(s):
    s.text("EM POUCAS SEMANAS…", 40, 260, 1000, size=90, color=B, t=0.05, how="up")
    for i in range(3):
        s.emoji("🕹️", 150 + i * 290, 600, 220, t=0.2, how="pop", out="sumiram")
    s.text("os gabinetes sumiram", 40, 1000, 1000, size=80, color="#fff", t="sumiram", how="slam")

@S(v, "Seria um", bg=BG)
def s7(s):
    s.emoji("🧪", 380, 260, 300, t=0.1, how="pop", bob=8)
    s.text("EXPERIMENTO SECRETO<br>DO GOVERNO?", 40, 700, 1000, size=96, color=A, t="secreto", how="slam")

@S(v, "Só", bg="#08010f")
def s8(s):
    s.text("NÃO HÁ PROVA", 40, 280, 1000, size=140, color="#ff4d4d", t="prova", how="slam")
    s.pill("📰 nenhum jornal dos anos 80", 80, 620, bg="#fff", t="jornal", how="left", size=54)
    s.pill("🕹️ nenhum gabinete achado", 80, 750, bg="#fff", t="gabinete", how="left", size=54)
    s.pill("💾 nenhum código do jogo", 80, 880, bg="#fff", t="código", how="left", size=54)

@S(v, "história", bg=BG)
def s9(s):
    s.counter(1990, 2000, 40, 240, 1000, size=220, color=B, t="2000", dur=0.6, prefix="~")
    s.rect(80, 560, 920, 420, "#c0c0c0", t="site", how="pop", radius=14)
    s.text("🌐 site de fliperamas", 110, 590, 860, size=52, color="#14123a", t="site", how="fade")
    s.text("“alguém já ouviu falar<br>desse jogo?”", 110, 720, 860, size=62, color="#14123a", t="pergunta", how="up")

@S(v, "primeira", bg=BG)
def s10(s):
    s.counter(2000, 2003, 40, 260, 1000, size=220, color=Y, t="2003", dur=0.5)
    s.pill("primeira menção impressa", 170, 540, bg=B, t="impressa", how="up", size=56)
    s.text("“INCONCLUSIVA”", 40, 800, 1000, size=110, color=A, t="inconclusiva", how="slam")

@S(v, "Mas", bg="#0b0114")
def s11(s):
    s.text("MAS A LENDA TEM<br>PEDAÇOS REAIS 🧩", 40, 600, 1000, size=96, color=B, t=0.05, how="slam")

@S(v, ("1981", 2), bg=BG)
def s12(s):
    s.counter(1975, 1981, 40, 220, 1000, size=200, color="#fff", t=0.0, dur=0.5)
    s.pill("🤢 um jogador passou mal", 80, 480, bg=Y, t="mal", how="left", size=56)
    s.pill("+10 dias", 80, 610, bg="#fff", t="dez", how="left", size=56)
    s.emoji("🚨", 400, 760, 230, t="FBI", how="slam", bob=6)
    s.text("FBI: apostas ilegais", 40, 1060, 1000, size=74, color="#ff4d4d", t="apostas", how="up")

@S(v, ("1982", 1), bg=BG)
def s13(s):
    s.counter(1981, 1982, 40, 260, 1000, size=200, color="#fff", t=0.0, dur=0.4)
    s.text("BERZERK", 40, 560, 1000, size=150, color=A, t="Berzerk", how="slam")
    s.emoji("💔", 400, 800, 230, t="cardíaca", how="pop")

@S(v, ("Anos", 2), bg=BG)
def s14(s):
    s.text("O MITO VIROU<br>JOGO DE VERDADE", 40, 280, 1000, size=96, color=B, t="mito", how="slam")
    s.counter(2010, 2016, 40, 640, 1000, size=200, color=Y, t="2016", dur=0.5)
    s.emoji("🎮", 400, 920, 230, t="PlayStation", how="pop", bob=6)

@S(v, "talvez", bg="#08010f")
def s15(s):
    s.emoji("🌀", 340, 250, 400, t=0.0, how="pop", spin=360)
    s.text("UM JOGO QUE TALVEZ<br>NUNCA TENHA EXISTIDO", 40, 720, 1000, size=80, color=A, t=0.05, how="slam")
    s.text("feito de pedaços reais", 40, 1120, 1000, size=70, color="#fff", t="pedaços", how="up")
