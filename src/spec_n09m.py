from engine import *
v = Video("n09m", decoration="grid")
v.fix = {"parelhos": "paredes", "florescentes.": "fluorescentes.", "florescentes": "fluorescentes", "backrooms,": "Backrooms,", "Cain": "Kane"}
v.phr = [("alguém apostou", "alguém a postou"), ("história. Se", "história: se")]
BG = "linear-gradient(180deg,#2a2208 0%,#4a3c0c 60%,#6b5a12 100%)"
Y, W2, R = "#ffe066", "#fff6c9", "#ff5a4d"
L = "nov09/"
v.credits = ["HobbyTown USA Oshkosh interior under construction (2002) — uso livre com crédito, Wikimedia Commons", "Imagem de referência da lenda The Backrooms (fair use)"]

@S(v, 0)
def s1(s):
    s.photo(L + "Backrooms_HobbyTown_2002.jpg", zoom=(1.05, 1.25))
    s.text("ESSA FOTO NÃO DEVERIA<br>ASSUSTAR NINGUÉM", 40, 260, 1000, size=96, color=Y, t=0.1, how="slam")

@S(v, "sala", bg=BG)
def s2(s):
    s.photo(L + "Backrooms_HobbyTown_2002.jpg", fit="contain", frame=(60, 180, 960, 620))
    s.pill("carpete velho", 70, 860, bg=W2, t="carpete", how="left", size=58)
    s.pill("paredes amareladas", 70, 970, bg=Y, t="paredes", how="left", size=58)
    s.pill("💡 lâmpadas fluorescentes", 70, 1080, bg="#fff", t="lâmpadas", how="left", size=58)

@S(v, ("Mas", 1), bg=BG)
def s3(s):
    s.counter(2015, 2019, 40, 230, 1000, size=220, color=Y, t="2019", dur=0.6)
    s.pill("💬 4chan · fórum anônimo", 150, 520, bg="#fff", t="4chan", how="up", size=58)
    s.text("imagens que parecessem", 40, 760, 1000, size=66, color="#fff", t="imagens", how="up")
    s.text("“ERRADAS”", 40, 860, 1000, size=150, color=R, t="erradas", how="slam")

@S(v, "Outro", bg="#1a1504")
def s4(s):
    s.emoji("🚪", 420, 80, 160, t=0.0, how="pop")
    s.text("se você sair da realidade<br>no lugar errado…", 40, 260, 1000, size=70, color="#fff", t="realidade", how="up")
    s.text("BACKROOMS", 40, 620, 1000, size=150, color=Y, t="Backrooms", how="slam")
    s.pill("labirinto amarelo e infinito", 160, 900, bg=W2, t="labirinto", how="up", size=56)

@S(v, "ideia", bg=BG)
def s5(s):
    for i, lab in enumerate(["NÍVEL 0", "NÍVEL 1", "NÍVEL 2"]):
        s.rect(90 + i * 310, 300, 280, 280, "transparent", t="níveis", how="pop", radius=12, border=f"8px solid {Y}")
        s.text(lab, 90 + i * 310, 410, 280, size=52, color="#fff", t="níveis", how="fade")
    s.emoji("👁️", 400, 720, 240, t="criaturas", how="pop", bob=8)
    s.text("e criaturas", 40, 1030, 1000, size=74, color=R, t="criaturas", how="up")

@S(v, "janeiro", bg=BG)
def s6(s):
    s.counter(2019, 2022, 40, 200, 1000, size=200, color=Y, t="2022", dur=0.5)
    s.pill("Kane Parsons, 16 anos", 200, 460, bg="#fff", t="Kane", how="up", size=58)
    s.emoji("📼", 410, 600, 220, t="filmagem", how="pop", bob=6)
    s.counter(0, 90, 40, 880, 1000, size=200, color=R, t="90", dur=1.0, prefix="+", suffix=" mi")
    s.text("visualizações", 40, 1120, 1000, size=66, color="#fff", t="visualizações", how="up")

@S(v, "2023", bg=BG)
def s7(s):
    s.counter(2022, 2023, 40, 220, 1000, size=200, color=Y, t=0.0, dur=0.4)
    s.text("A24", 40, 470, 1000, size=200, color="#fff", t="A24", how="slam")
    s.emoji("🎬", 410, 760, 220, t="filme", how="pop")
    s.pill("estreia nos EUA: maio de 2026", 120, 1060, bg=Y, t="estreou", how="up", size=56)

@S(v, ("Mas", 2), bg="#1a1504")
def s8(s):
    s.text("DE ONDE VINHA<br>A FOTO?", 40, 240, 1000, size=110, color=Y, t="foto", how="slam")
    s.emoji("🔍", 410, 620, 220, t="resposta", how="pop", bob=6)
    s.counter(2019, 2024, 40, 880, 1000, size=180, color="#fff", t="2024", dur=0.6)
    s.pill("📄 página antiga arquivada", 170, 1110, bg=W2, t="arquivada", how="up", size=56)

@S(v, "Ela", bg=BG)
def s9(s):
    s.counter(1990, 2002, 40, 180, 1000, size=180, color=Y, t="2002", dur=0.6)
    s.photo(L + "Backrooms_HobbyTown_2002.jpg", fit="contain", frame=(120, 330, 840, 540))
    s.pill("🛠️ loja de móveis em reforma", 90, 900, bg="#fff", t="reforma", how="left", size=48)
    s.pill("📍 Oshkosh, Wisconsin (EUA)", 90, 990, bg=Y, t="Oshkosh", how="left", size=48)
    s.pill("blog de uma loja de hobbies", 90, 1080, bg=W2, t="blog", how="left", size=48)

@S(v, "Hoje", bg=BG)
def s10(s):
    s.text("A SALA NEM EXISTE MAIS", 40, 280, 1000, size=86, color="#fff", t=0.05, how="up")
    s.emoji("🏎️", 390, 560, 260, t="pista", how="right", bob=4)
    s.text("virou pista de<br>carrinho de controle remoto", 40, 920, 1000, size=66, color=Y, t="pista", how="up")

@S(v, ("lugar", 2))
def s11(s):
    s.photo(L + "Backrooms_HobbyTown_2002.jpg", zoom=(1.25, 1.05))
    s.text("O LUGAR MAIS ASSUSTADOR<br>DA INTERNET ERA<br>UMA LOJA EM REFORMA", 40, 260, 1000, size=84, color=Y, t=0.05, how="slam")
