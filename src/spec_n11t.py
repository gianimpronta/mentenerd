from engine import *
v = Video("n11t", decoration="grid")
v.fix = {"Vasamentos": "Vazamentos", "Poned": "Pwned"}
v.phr = [("Fui Raqueado?", "“fui hackeado?”")] + [("e -mail", "e-mail")] * 4
BG = "linear-gradient(180deg,#071018 0%,#0c2230 60%,#123a4a 100%)"
G, R, Y = "#4dffb0", "#ff5a5a", "#ffd93d"

@S(v, 0, bg="#050b10")
def s1(s):
    s.emoji("🔑", 400, 260, 260, t=0.0, how="pop", bob=8)
    s.text("SUA SENHA PODE JÁ<br>ESTAR NA INTERNET", 40, 680, 1000, size=100, color=R, t=0.1, how="slam")

@S(v, "Vazamentos", bg=BG)
def s2(s):
    s.emoji("💧", 410, 220, 220, t=0.0, how="pop", bob=6)
    s.text("vazamentos acontecem<br>o tempo todo", 40, 520, 1000, size=80, color="#fff", t=0.1, how="up")
    s.pill("📧 seu e-mail pode estar em algum", 90, 820, bg=Y, t="algum", how="left", size=54)
    s.pill("✅ dá para conferir de graça", 90, 940, bg=G, t="graça", how="left", size=54)

@S(v, ("site", 1), bg=BG)
def s3(s):
    s.text("haveibeenpwned.com", 40, 260, 1000, size=92, color=G, t="Have", how="slam")
    s.pill("“fui hackeado?”", 300, 440, bg="#fff", t="fui hackeado?", how="up", size=60)
    s.counter(2000, 2013, 40, 620, 1000, size=180, color=Y, t="2013", dur=0.6)
    s.pill("criado por Troy Hunt", 260, 870, bg=Y, t="Troy", how="up", size=58)

@S(v, "Você", bg=BG)
def s4(s):
    s.rect(80, 300, 920, 130, "#fff", t=0.0, how="pop", radius=24)
    s.text("seu@email.com 🔍", 110, 335, 860, size=60, color="#14123a", t="digita", how="fade")
    s.pill("⚠️ vazamento A · 2019", 110, 560, bg=R, color="#fff", t="vazamentos", how="left", size=54)
    s.pill("⚠️ vazamento B · 2021", 110, 680, bg=R, color="#fff", t="conhecidos", how="left", size=54)
    s.pill("⚠️ vazamento C · 2024", 110, 800, bg=R, color="#fff", t="endereço", how="left", size=54)
    s.text("exemplo ilustrativo", 40, 960, 1000, size=40, color="#9fb3c2", t="vazamentos", how="fade")

@S(v, ("site", 2), bg=BG)
def s5(s):
    s.pill("🔒 busca de senhas vazadas", 110, 300, bg="#fff", t="senhas", how="left", size=58)
    s.text("sem enviar a senha completa", 40, 480, 1000, size=70, color=G, t="completa", how="up")
    s.emoji("🔔", 410, 680, 220, t="aviso", how="pop", bob=6)
    s.pill("aviso de vazamento novo", 230, 960, bg=Y, t="aviso", how="up", size=58)

@S(v, ("Se", 4), bg=BG)
def s6(s):
    s.text("SE APARECER:", 40, 220, 1000, size=100, color=R, t=0.0, how="slam")
    s.pill("1 · troque a senha do serviço", 70, 460, bg="#fff", t="troque", how="left", size=56)
    s.pill("2 · e onde usar a mesma senha", 70, 590, bg="#fff", t="mesma", how="left", size=56)
    s.pill("3 · ative a verificação em 2 etapas", 70, 720, bg=G, t="verificação", how="left", size=56)

@S(v, ("Uma", 2), bg="#050b10")
def s7(s):
    for i in range(3):
        s.emoji("🔑", 170 + i * 280, 300, 200, t=0.1 * i, how="pop", bob=6)
    s.text("UMA SENHA DIFERENTE<br>PARA CADA SITE", 40, 680, 1000, size=96, color=G, t="diferente", how="slam")
