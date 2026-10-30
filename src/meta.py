import json, re, os
M = {
 "c01": ("Por que o mar é salgado e os rios não? #shorts", "O mar tem em média 35 gramas de sal por litro. A chuva desgasta as rochas, os rios levam os minerais até o oceano e, como o sal não evapora, ele fica para trás. #ciencia #curiosidades #oceano #geologia #quimica", "2026-10-28", "15:00"),
 "c02": ("A luz do Sol que chega hoje começou a viagem há milhares de anos #shorts", "A luz leva cerca de 8 minutos do Sol até a Terra, mas passa de dezenas de milhares a mais de cem mil anos (as estimativas variam) até sair do interior do Sol. #ciencia #sol #fisica #astronomia #curiosidades", "2026-10-29", "15:00"),
 "c03": ("Por que a gente sempre vê o mesmo lado da Lua? #shorts", "A Lua gira, sim, mas leva o mesmo tempo para girar em torno de si e em torno da Terra. É o acoplamento de maré. O lado oculto só foi visto em 1959, pela sonda soviética Luna 3. #ciencia #lua #astronomia #curiosidades #espaco", "2026-10-30", "15:00"),
 "c04": ("O que acontece se você cair num buraco negro? #shorts", "A diferença de gravidade esticaria o seu corpo, a chamada espaguetificação. Em buracos negros gigantes, você poderia cruzar o horizonte de eventos sem notar nada de especial. #ciencia #buraconegro #fisica #astronomia #curiosidades", "2026-10-31", "15:00"),
 "c05": ("O GPS só funciona porque Einstein estava certo #shorts", "Por causa da relatividade, o relógio dos satélites adianta cerca de 38 microssegundos por dia. Sem a correção, o erro seria de cerca de 10 quilômetros por dia. #ciencia #gps #einstein #relatividade #tecnologia", "2026-11-01", "15:00"),
 "c06": ("Por que o gelo boia? #shorts", "O gelo é cerca de 9% menos denso que a água líquida porque suas moléculas formam hexágonos com espaços vazios. Por isso o gelo flutua e os lagos não congelam de baixo para cima. #ciencia #gelo #agua #quimica #curiosidades", "2026-11-02", "15:00"),
 "t01": ("Por que um QR code funciona mesmo rasgado? #shorts", "O QR code guarda dados extras de correção de erros, calculados pelo código Reed-Solomon. No nível mais alto, ele ainda pode ser lido com até 30% danificado. #tecnologia #qrcode #curiosidades #matematica #celular", "2026-11-01", "19:00"),
 "t02": ("Por que a bateria do celular perde capacidade? #shorts", "Dois fatores pesam mais: os ciclos de carga e o calor. Em muitos celulares, depois de cerca de 500 ciclos a bateria segura só uns 80% da carga original. #tecnologia #bateria #celular #dicas #curiosidades", "2026-11-03", "19:00"),
 "m01": ("Webdriver Torso, parte 1: o canal que ninguém entendia #shorts", "Mistérios da Internet: em 2013, um canal do YouTube passou a postar milhares de vídeos de retângulos coloridos e bipes. Ninguém sabia por quê. Parte 1 de 2. #misterios #youtube #internet #curiosidades #webdrivertorso", "2026-10-30", "12:00"),
 "m02": ("Webdriver Torso, parte 2: a resposta #shorts", "Mistérios da Internet: três vídeos fugiam do padrão, e em 2014 o YouTube explicou que o canal era um teste de envio de vídeos. Parte 2 de 2. #misterios #youtube #internet #curiosidades #webdrivertorso", "2026-10-31", "12:00"),
 "m03": ("John Titor, parte 1: o soldado de 2036 #shorts", "Mistérios da Internet: em 2000, um usuário de fórum disse ser um soldado vindo de 2036, em busca de um IBM 5100. Parte 1 de 2. #misterios #johntitor #internet #curiosidades #viagemnotempo", "2026-11-01", "12:00"),
 "m04": ("John Titor, parte 2: o que aconteceu com ele #shorts", "Mistérios da Internet: as previsões falharam, o autor sumiu em 2001 e a identidade de John Titor nunca foi provada. Parte 2 de 2. #misterios #johntitor #internet #curiosidades #viagemnotempo", "2026-11-02", "12:00"),
 "m05": ("Cicada 3301, parte 1: o enigma #shorts", "Mistérios da Internet: em 2012, uma imagem num fórum anônimo recrutava pessoas muito inteligentes por meio de criptografia, runas e cartazes pelo mundo. Parte 1 de 2. #misterios #cicada3301 #internet #curiosidades #criptografia", "2026-11-03", "12:00"),
 "m06": ("Cicada 3301, parte 2: o livro que ninguém leu #shorts", "Mistérios da Internet: o grupo voltou em 2013 e 2014, deixou o Liber Primus quase todo sem decifrar e silenciou em 2017. Parte 2 de 2. #misterios #cicada3301 #internet #curiosidades #criptografia", "2026-11-04", "12:00"),
 "m07": ("Max Headroom, parte 1: a primeira invasão #shorts", "Mistérios da Internet: em 22 de novembro de 1987, um telejornal de Chicago foi invadido por um homem com máscara do Max Headroom. Parte 1 de 2. #misterios #maxheadroom #tv #curiosidades #historia", "2026-11-05", "12:00"),
 "m08": ("Max Headroom, parte 2: a segunda invasão #shorts", "Mistérios da Internet: duas horas depois, uma TV pública de Chicago foi invadida de novo, desta vez com áudio. Ninguém foi identificado. Parte 2 de 2. #misterios #maxheadroom #tv #curiosidades #historia", "2026-11-06", "12:00"),
}
CR = {
 "Waves_at_La_Corniche": "Waves at La Corniche — Christian Ferrer, CC BY 4.0, Wikimedia Commons",
 "Mountain_landscape": "Mountain landscape, Ergaki — Vyacheslav Argenberg, CC BY 4.0, Wikimedia Commons",
 "Salt-crystals": "Salt crystals — Nate Steiner, CC0, Wikimedia Commons",
 "Sun_-_August_1": "Sun, 1 ago 2010 — NASA/SDO/AIA, domínio público",
 "Ultiwavelength": "Sol em ultravioleta extremo — NASA/Goddard/SDO AIA Team, domínio público",
 "Moon_nearside": "Lado visível da Lua — NASA/GSFC/Arizona State University, domínio público",
 "Earthrise": "Earthrise sobre a cratera Compton — NASA/GSFC/ASU, domínio público",
 "Black_hole_-_Messier": "Messier 87 — Event Horizon Telescope, CC BY 4.0, Wikimedia Commons",
 "Black_Hole_with_Accretion": "Visualização de buraco negro — NASA SVS/Caltech-IPAC/Robert Hurt, domínio público",
 "Navstar": "Navstar-2F — USAF, domínio público",
 "GPS_Block1": "GPS Block I — John T. Greenwood, domínio público",
 "LG_P710": "Bateria Li-ion BL-59JH — Raimond Spekking, CC BY-SA 4.0, Wikimedia Commons",
 "Iceberg": "Iceberg na North Star Bay — Jeremy Harbeck/NASA, domínio público",
 "Ice_Ih": "Rede cristalina do gelo Ih — Psiĥedelisto (base: Dbuckingham42), CC BY-SA 4.0, Wikimedia Commons",
 "Lake_Baikal": "Lago Baikal no inverno — Sergey Pesterev, CC BY-SA 4.0, Wikimedia Commons",
 "Webdriver_Torso_Slide": "Webdriver Torso — YouTube, domínio público",
 "Google_webdriver": "Logo do Webdriver Torso — Wikimedia Commons",
 "Eiffel": "Torre Eiffel à noite — Getfunky Paris, CC BY 2.0, Wikimedia Commons",
 "IBM_5100": "IBM 5100 — Sandstein, CC BY-SA 3.0, Wikimedia Commons",
 "1967_Chevrolet": "Chevrolet Corvette 1967 — MrWalkr, CC BY-SA 4.0, Wikimedia Commons",
 "Titor_insignia": "Insígnia de John Titor — uso educativo (fair use)",
 "Cicada3301_s_First": "Primeira mensagem do Cicada 3301 — Cicada 3301, domínio público",
 "Runic_letters": "Runas Elder Futhark — ClaesWallin, domínio público",
 "Cicada_3301_poster": "Cartazes do Cicada 3301 — Андрей Романенко e telenavdrives/OpenStreetCam, CC BY-SA 4.0, Wikimedia Commons",
 "Cicada_3301_logo": "Logo do Cicada 3301 — uso educativo (fair use)",
 "Max_Headroom_broadcast": "Invasão do Max Headroom — domínio público",
 "WCIA": "Torre de TV (WCIA) — Dual Freq, CC BY 2.5, Wikimedia Commons",
 "aqua_c": "Aqua, vídeo do Webdriver Torso — YouTube, domínio público",
 "wgn_c": "Invasão do Max Headroom na WGN-TV (1987) — domínio público, Wikimedia Commons",
 "wttw": "Invasão do Max Headroom na WTTW (1987) — domínio público, Wikimedia Commons",
}
def credits(k):
    src = open(f"spec_{k}.py").read()
    return [line for key, line in CR.items() if key in src]
out = {}
for k, (t, d, day, hm) in M.items():
    cr = credits(k)
    desc = d + ("\n\nImagens e créditos:\n" + "\n".join("• " + c for c in cr) if cr else "")
    out[k] = dict(title=t, description=desc, date=day, time=hm)
json.dump(out, open("meta.json", "w"), ensure_ascii=False, indent=1)
print(len(out), len(out["m05"]["title"]), out["c01"]["description"])
