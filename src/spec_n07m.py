from engine import *
v = Video("n07m", decoration="stars")
v.fix = {"zumbia": "zumbe", "porquê": "por quê", "4625": "4.625"}
v.phr = [("Rádio Amadores", "Radioamadores"), ("UVB 76", "UVB-76"), ("UZB 76", "UZB-76"), ("UVB 76", "UVB-76"), ("comunicação esperto", "comunicações perto")]
BG = "linear-gradient(180deg,#04140c 0%,#0b2a1a 60%,#13432a 100%)"
L = "nov07/"
v.credits = ["Shortwave Radio — Junglecat, domínio público, Wikimedia Commons", "Frequencysounds of UVB-76 — The.doctor.vale, CC BY-SA 4.0, Wikimedia Commons", "UVB-76 detail — Janm67, CC BY-SA 3.0, Wikimedia Commons"]

@S(v, 0)
def s1(s):
    s.photo(L + "Shortwave_Radio.jpg", zoom=(1.05, 1.2))
    s.text("ZUMBE HÁ<br>QUASE 50 ANOS", 40, 260, 1000, size=118, color="#7dff9a", t=0.15, how="slam")
    s.text("ninguém sabe por quê", 40, 640, 1000, size=74, color="#fff", t="ninguém", how="up")

@S(v, "Ela", bg=BG)
def s2(s):
    s.counter(0, 4625, 40, 230, 1000, size=230, color="#7dff9a", t="4.625", dur=1.2, suffix="")
    s.text("kHz · ondas curtas", 40, 500, 1000, size=70, color="#fff", t="ondas", how="up")
    for k in range(9):
        s.rect(110 + k * 96, 760, 60, 60 + (k % 3) * 70, "#7dff9a", t=("zumbido") , how="pop", radius=10, opacity=0.85)
    s.counter(0, 20, 40, 1000, 1000, size=120, color="#ffd93d", t="20", dur=0.8, prefix="+", suffix=" por minuto")

@S(v, "Radioamadores", bg=BG)
def s3(s):
    s.photo(L + "Frequencysounds_of_UVB-76.png", fit="contain", frame=(60, 260, 960, 620))
    s.pill("“o Zumbidor”", 60, 940, bg="#ffd93d", t="Zumbidor", how="left", size=64)
    s.text("UVB-76", 40, 1040, 1000, size=130, color="#7dff9a", t="UVB-76", how="slam")

@S(v, "primeira", bg=BG)
def s4(s):
    s.counter(1950, 1976, 40, 230, 1000, size=220, color="#fff", t="1976", dur=0.9)
    s.pill("primeira transmissão conhecida", 70, 500, bg="#7dff9a", t="1976", how="left", size=50)
    s.pill("União Soviética ☭", 70, 600, bg="#ff6a6a", color="#fff", t="Soviética", how="left", size=50)
    s.counter(1976, 1982, 40, 760, 1000, size=200, color="#ffd93d", t="1982", dur=0.6)
    s.text("gravação mais antiga", 40, 1000, 1000, size=64, color="#fff", t="1982", how="up")

@S(v, "sinais", bg=BG)
def s5(s):
    s.text("RÚSSIA", 40, 280, 1000, size=170, color="#fff", t="Rússia", how="slam")
    s.emoji("📡", 390, 560, 230, t="transmissor", how="pop", bob=8)
    s.pill("📍 perto de Moscou", 260, 900, bg="#ffd93d", t="Moscou", how="up", size=60)

@S(v, "nome", bg=BG)
def s6(s):
    s.text("UMA CURIOSIDADE<br>NO NOME", 40, 200, 1000, size=64, color="#fff", t=0.1, how="up")
    a = s.text("UZB-76", 40, 300, 1000, size=170, color="#ffd93d", t="UZB-76", how="slam")
    s.rect(200, 400, 680, 16, "#ff4d4d", t="UVB-76", how="left", radius=8)
    s.text("UVB-76", 40, 600, 1000, size=170, color="#7dff9a", t="UVB-76", how="slam")
    s.pill("erro de transcrição ✍️", 210, 900, bg="#fff", t="transcrição", how="up", size=56)

@S(v, "Nenhuma", bg=BG)
def s7(s):
    s.text("?", 240, 180, 600, size=620, color="#7dff9a", t=0.1, how="slam")
    s.text("nenhuma confirmação oficial", 40, 900, 1000, size=70, color="#fff", t="confirmou", how="up")

@S(v, "Mas", bg="#020805")
def s8(s):
    s.text("o zumbido para…", 40, 380, 1000, size=100, color="#7dff9a", t=0.2, how="fade")
    s.emoji("🎙️", 390, 600, 240, t="voz", how="pop", bob=6)
    s.text("e uma voz aparece", 40, 950, 1000, size=74, color="#fff", t="aparece", how="up")

@S(v, "São", bg=BG)
def s9(s):
    s.photo(L + "UVB-76-detail.png", fit="contain", frame=(40, 230, 1000, 380))
    s.pill("🇷🇺 mensagens em russo, ao vivo", 50, 680, bg="#fff", t="russo", how="left", size=48)
    s.pill("indicativos", 50, 790, bg="#7dff9a", t="indicativos", how="left", size=52)
    s.pill("grupos de 5 dígitos: 74 581", 50, 900, bg="#ffd93d", t="grupos", how="left", size=52)
    s.pill("palavras-código", 50, 1010, bg="#ff9a2e", t="palavras", how="left", size=52)

@S(v, "setembro", bg=BG)
def s10(s):
    s.counter(2000, 2010, 40, 240, 1000, size=200, color="#fff", t="2010", dur=0.6)
    s.emoji("🦢", 380, 500, 260, t="Lago", how="pop", bob=8)
    s.pill("“O Lago dos Cisnes”, Tchaikovsky 🎻", 70, 880, bg="#ffd93d", t="Tchaikovsky", how="up", size=48)
    s.text("no lugar do zumbido", 40, 1010, 1000, size=60, color="#7dff9a", t="substituir", how="up")

@S(v, ("Com", 2), bg=BG)
def s11(s):
    s.pill("novo indicativo", 70, 300, bg="#7dff9a", t="indicativo", how="left", size=60)
    s.pill("novo endereço", 70, 430, bg="#ffd93d", t="endereço", how="left", size=60)
    s.emoji("🏢", 400, 600, 240, t="base", how="pop")
    s.text("base de comunicações perto de Moscou", 40, 900, 1000, size=60, color="#fff", t="base", how="up")

@S(v, "explicação", bg=BG)
def s12(s):
    s.text("A EXPLICAÇÃO MAIS CITADA", 40, 230, 1000, size=66, color="#7dff9a", t=0.1, how="up")
    s.emoji("🚧", 380, 420, 260, t="ocupada", how="slam")
    s.text("manter a frequência ocupada", 40, 780, 1000, size=70, color="#fff", t="ocupada", how="up")
    s.pill("um marcador de canal", 230, 930, bg="#ffd93d", t="marcador", how="up", size=56)

@S(v, "Teorias", bg=BG)
def s13(s):
    s.pill("🕵️ estação de espiões?", 60, 300, bg="#fff", t="espiões", how="left", size=56)
    s.pill("☢️ resposta nuclear automática?", 60, 440, bg="#fff", t="nuclear", how="left", size=56)
    s.text("❌ ❌", 40, 600, 1000, size=150, color="#ff4d4d", t="pouco", how="slam")
    s.text("horários imprevisíveis · sinal fraco", 40, 900, 1000, size=56, color="#7dff9a", t="imprevisíveis", how="up")

@S(v, ("Quase", 2))
def s14(s):
    s.photo(L + "Shortwave_Radio.jpg", zoom=(1.2, 1.05))
    s.text("QUASE MEIO SÉCULO NO AR", 40, 300, 1000, size=96, color="#7dff9a", t=0.1, how="slam")
    s.text("e nenhum governo diz para quê", 40, 620, 1000, size=70, color="#fff", t="governo", how="up")
