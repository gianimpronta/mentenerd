from engine import *
v = Video("n09t", decoration="grid")
v.fix = {}
v.phr = [("e -mail", "e-mail"), ("e -mail", "e-mail"), ("mensagem não", "mensagem? Não"), ("BBN nos", "BBN, nos")]
BG = "linear-gradient(180deg,#0a0820 0%,#1a1446 60%,#2e1f66 100%)"
G, P, Y = "#5ef0a0", "#b48cff", "#ffd93d"
L = "nov09/"
v.credits = ["DEC PDP-10 no Living Computer Museum — Joe Mabel, CC BY-SA 3.0, Wikimedia Commons"]

@S(v, 0, bg="#06051a")
def s1(s):
    s.emoji("🖥️", 160, 300, 260, t=0.0, how="left")
    s.emoji("🖥️", 660, 300, 260, t=0.15, how="right")
    s.rect(420, 430, 240, 14, G, t=0.3, how="left", radius=7)
    s.text("O PRIMEIRO E-MAIL<br>FOI PARA A MÁQUINA<br>AO LADO", 40, 720, 1000, size=96, color=G, t=0.1, how="slam")

@S(v, "1971", bg=BG)
def s2(s):
    s.counter(1960, 1971, 40, 200, 1000, size=220, color=G, t=0.0, dur=0.6)
    s.pill("Ray Tomlinson · BBN", 220, 480, bg="#fff", t="Ray", how="up", size=60)
    s.text("ARPANET", 40, 680, 1000, size=150, color=P, t="ARPANET", how="slam")
    s.text("a rede que deu origem à internet 🌐", 40, 900, 1000, size=58, color="#fff", t="origem", how="up")

@S(v, ("duas", 1), bg=BG)
def s3(s):
    s.photo(L + "PDP-10.jpg", fit="contain", frame=(40, 240, 1000, 660))
    s.pill("as duas máquinas: lado a lado", 120, 1000, bg=G, t="lado", how="up", size=58)

@S(v, "Ele", bg=BG)
def s4(s):
    s.text("pessoa", 40, 300, 440, size=80, color="#fff", t="pessoa", how="left")
    s.text("computador", 600, 300, 440, size=80, color="#fff", t="computador", how="right")
    s.text("@", 40, 420, 1000, size=480, color=Y, t="arroba", how="slam")
    s.text("ray@maquina", 40, 1060, 1000, size=90, color=G, t="arroba", how="up")

@S(v, "símbolo", bg=BG)
def s5(s):
    s.text("@", 40, 200, 1000, size=360, color=Y, t=0.0, how="pop")
    s.text("PADRÃO EM TODO<br>E-MAIL DO MUNDO 🌍", 40, 760, 1000, size=90, color="#fff", t="padrão", how="slam")

@S(v, "Antes", bg=BG)
def s6(s):
    s.text("ANTES DISSO…", 40, 200, 1000, size=80, color=P, t=0.0, how="up")
    s.counter(1960, 1965, 40, 340, 1000, size=200, color=G, t="1965", dur=0.5)
    s.pill("MIT", 450, 600, bg="#fff", t="MIT", how="pop", size=70)
    s.text("só dentro do<br>mesmo computador", 40, 760, 1000, size=80, color="#fff", t="dentro", how="up")
    s.emoji("📬", 410, 1020, 200, t="recados", how="pop", bob=6)

@S(v, "conteúdo", bg="#06051a")
def s7(s):
    s.emoji("✉️", 380, 280, 300, t=0.0, how="pop", bob=8)
    s.text("?", 40, 560, 1000, size=300, color=Y, t="mensagem? Não", how="slam")
    s.text("não ficou registrado", 40, 960, 1000, size=80, color="#fff", t="registrado", how="up")

@S(v, ("teste", 2), bg=BG)
def s8(s):
    s.emoji("🖥️", 160, 300, 240, t=0.0, how="pop")
    s.emoji("🖥️", 660, 300, 240, t=0.0, how="pop")
    s.text("@", 440, 280, 200, size=220, color=Y, t=0.1, how="slam")
    s.text("UM TESTE ENTRE VIZINHAS<br>MUDOU O MUNDO", 40, 760, 1000, size=84, color=G, t="mudou", how="slam")
