from engine import *
v = Video("n07t", decoration="grid")
v.fix = {"Wi": "Wi-Fi", "-Fi": "", "-Fi,": "", "Mac": "MAC"}
BG = "linear-gradient(180deg,#10153a 0%,#2a1d6a 60%,#4a2a9a 100%)"
L = "nov07/"
v.credits = ["TP-Link Archer A6 Router (v4) — Paowee, CC BY-SA 4.0, Wikimedia Commons", "Netgear Nighthawk AC1900 WiFi Router — Evan-Amos, domínio público, Wikimedia Commons"]

def dev(s, y, ico, name, t, color="#ffffff", tc="#14123a"):
    return s.pill(f"{ico}&nbsp; {name}", 90, y, bg=color, color=tc, t=t, how="left", size=54)

@S(v, 0)
def s1(s):
    s.photo(L + "TP-link_Archer_A6_Router_(v4)_-_Front_Side.jpg", zoom=(1.05, 1.2), focus=(0.5, 0.5))
    s.text("TEM ALGUÉM<br>NO SEU WI-FI?", 40, 250, 1000, size=124, color="#ffd93d", t=0.15, how="slam")
    s.emoji("👀", 400, 640, 220, t="agora", how="pop")

@S(v, "dá", bg=BG)
def s2(s):
    s.emoji("⏱️", 390, 380, 260, t=0.1, how="pop", spin=360)
    s.text("dá para conferir<br>em poucos minutos", 40, 760, 1000, size=80, color="#fff", t="minutos", how="up")

@S(v, "Abra", bg=BG)
def s3(s):
    s.pill("painel / app do roteador", 60, 230, bg="#ffd93d", t="painel", how="left", size=54)
    s.text("DISPOSITIVOS CONECTADOS", 40, 370, 1000, size=60, color="#9fd0ff", t="dispositivos", how="up")
    dev(s, 480, "📱", "Celular", "lista")
    dev(s, 600, "💻", "Notebook", "lista")
    dev(s, 720, "📺", "TV da sala", "conectados")
    dev(s, 840, "👤", "???", "conectados", color="#ff4d4d", tc="#fff")

@S(v, ("Em", 2), bg=BG)
def s4(s):
    s.photo(L + "Netgear-Nighthawk-AC1900-WiFi-Router.jpg", fit="contain", frame=(90, 220, 900, 620))
    s.emoji("🏷️", 420, 860, 180, t="etiqueta", how="pop")
    s.pill("endereço + senha na etiqueta", 150, 1060, bg="#ffd93d", t="etiqueta", how="up", size=52)

@S(v, "identifique", bg=BG)
def s5(s):
    s.text("IDENTIFIQUE CADA UM", 40, 230, 1000, size=70, color="#ffd93d", t=0.1, how="up")
    dev(s, 400, "📱", "Celular da Ana", "Celulares")
    dev(s, 520, "💻", "Notebook do Pedro", "computadores")
    dev(s, 640, "📺", "TV (nome da marca)", "marca")
    dev(s, 760, "👤", "desconhecido", "marca", color="#ff4d4d", tc="#fff")

@S(v, "tirar", bg=BG)
def s6(s):
    s.pill("📴 desligue o Wi-Fi dos seus aparelhos", 40, 230, bg="#fff", t="desligue", how="left", size=46)
    a = dev(s, 400, "📱", "Celular da Ana", 0.1); b = dev(s, 520, "💻", "Notebook do Pedro", 0.1); c = dev(s, 640, "📺", "TV", 0.1)
    for x in (a, b, c): s.out(x, "aparelhos", 0.4)
    dev(s, 760, "👤", "desconhecido ainda aqui", "continuam", color="#ff4d4d", tc="#fff")
    s.pill("compare o endereço MAC", 180, 920, bg="#ffd93d", t="compare", how="up", size=56)

@S(v, "solução", bg=BG)
def s7(s):
    s.emoji("🔑", 390, 250, 240, t="trocar", how="slam")
    s.text("troque a senha do Wi-Fi", 40, 560, 1000, size=74, color="#ffd93d", t="trocar", how="up")
    s.text("todo mundo cai…", 40, 720, 1000, size=64, color="#fff", t="derruba", how="up")
    s.text("✅ e só os seus voltam", 40, 860, 1000, size=64, color="#5ee08a", t="entrar", how="up")

@S(v, ("Muitos", 2), bg=BG)
def s8(s):
    s.pill("dica extra", 60, 230, bg="#ffd93d", t=0.1, how="left", size=56)
    s.emoji("🚫", 390, 300, 260, t="bloquear", how="slam")
    s.pill("bloquear pelo endereço MAC", 150, 720, bg="#fff", t="MAC", how="up", size=58)

@S(v, "conferência")
def s9(s):
    s.photo(L + "TP-link_Archer_A6_Router_(v4)_-_Front_Side.jpg", zoom=(1.2, 1.05))
    s.text("QUEM ESTÁ DE CARONA<br>NO SEU SINAL?", 40, 300, 1000, size=96, color="#ffd93d", t=0.1, how="slam")
