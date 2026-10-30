"""Motor de vídeos Mente Nerd (HyperFrames). Uso: ver spec_*.py"""
import json, os, re, html, shutil, unicodedata, subprocess
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
LIB = "/tmp/claude-0/-home-claude/c387085d-c19c-553c-941a-b1d2af4f4e78/scratchpad/hfpilot/assets/lib"
PILOT = os.path.join(ROOT, "..", "hfpilot")

def norm(w):
    w = unicodedata.normalize("NFKD", w.lower())
    return re.sub(r"[^a-z0-9]", "", "".join(c for c in w if not unicodedata.combining(c)))

FACE = '<i class="e l"><b></b></i><i class="e r"><b></b></i><i class="sm"></i>'

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#101028}
#root{position:absolute;inset:0;font-family:"Nunito",sans-serif;color:#fff;overflow:hidden}
.sc{position:absolute;inset:0;overflow:hidden}
.in{position:absolute;inset:0}
.abs{position:absolute}
.ball{position:absolute;border-radius:50%}
.e{position:absolute;top:34%;width:24%;height:28%;background:#fff;border-radius:50%}
.e.l{left:20%}.e.r{right:20%}
.e b{position:absolute;left:34%;top:30%;width:50%;height:56%;background:#14123a;border-radius:50%}
.sm{position:absolute;left:34%;top:66%;width:32%;height:14%;border-bottom:5px solid #14123a;border-radius:0 0 50% 50%}
.pill{position:absolute;padding:14px 34px;border-radius:44px;font-weight:900;font-size:44px;color:#14123a;background:#ffd93d;white-space:nowrap}
.txt{position:absolute;text-align:center;font-weight:900;line-height:1.05;text-shadow:0 6px 0 rgba(0,0,0,.28)}
.cap{position:absolute;left:50px;right:50px;top:1215px;text-align:center;font-weight:900;font-size:62px;line-height:1.15;color:#e8ecf5;text-shadow:0 5px 0 rgba(20,10,60,.8),0 0 24px rgba(10,5,40,.9)}
.shade{position:absolute;left:0;right:0;bottom:0;height:900px;background:linear-gradient(180deg,rgba(8,6,30,0),rgba(8,6,30,.78))}
.shadeT{position:absolute;left:0;right:0;top:0;height:420px;background:linear-gradient(0deg,rgba(8,6,30,0),rgba(8,6,30,.45))}
.photo{position:absolute;left:0;top:0;transform-origin:50% 50%}
.frame{position:absolute;overflow:hidden;border-radius:44px;box-shadow:0 20px 60px rgba(0,0,0,.5)}
.blur{position:absolute;inset:-60px;object-fit:cover;filter:blur(40px) brightness(.55)}
svg{position:absolute;overflow:visible}
"""


class Scene:
    def __init__(self, v, idx, at, bg, deco):
        self.v, self.idx, self.at, self.bg, self.deco = v, idx, at, bg, deco
        self.html, self.js, self.n = "", "", 0
        self.t0 = None  # preenchido por Video.build

    # ---- tempo
    def T(self, t):
        """t: str (palavra, a partir do início da cena) | (str,n) | float (s após o início) | None"""
        if t is None:
            return self.t0
        if isinstance(t, (int, float)):
            return self.t0 + t
        if isinstance(t, tuple):
            word, occ = t
        else:
            word, occ = t, 1
        k = norm(word)
        c = 0
        for a, b, w in self.v.words:
            if a >= self.t0 - 0.05 and norm(w) == k:
                c += 1
                if c == occ:
                    return a
        raise KeyError(f"palavra '{word}' ({occ}) não achada depois de {self.t0}")

    def _id(self, p="x"):
        self.n += 1
        return f"s{self.idx}{p}{self.n}"

    def add(self, h, js=""):
        self.html += h + "\n"
        self.js += js + "\n"

    # ---- elementos
    def anim_in(self, sel, t, how="pop", dur=0.4):
        T = self.T(t)
        a = {
            "pop": f'tl.fromTo("{sel}",{{scale:0,opacity:0}},{{scale:1,opacity:1,duration:{dur},ease:"back.out(2.2)"}},{T:.2f});',
            "fade": f'tl.fromTo("{sel}",{{opacity:0}},{{opacity:1,duration:{dur},ease:"power2.out"}},{T:.2f});',
            "up": f'tl.fromTo("{sel}",{{opacity:0,y:60}},{{opacity:1,y:0,duration:{dur},ease:"power3.out"}},{T:.2f});',
            "down": f'tl.fromTo("{sel}",{{opacity:0,y:-60}},{{opacity:1,y:0,duration:{dur},ease:"power3.out"}},{T:.2f});',
            "left": f'tl.fromTo("{sel}",{{opacity:0,x:-120}},{{opacity:1,x:0,duration:{dur},ease:"power3.out"}},{T:.2f});',
            "right": f'tl.fromTo("{sel}",{{opacity:0,x:120}},{{opacity:1,x:0,duration:{dur},ease:"power3.out"}},{T:.2f});',
            "slam": f'tl.fromTo("{sel}",{{scale:2.4,opacity:0}},{{scale:1,opacity:1,duration:{dur},ease:"power4.out"}},{T:.2f});',
        }[how]
        return a

    def out(self, sel, t, dur=0.3):
        T = self.T(t)
        self.js += f'tl.to("{sel}",{{opacity:0,duration:{dur}}},{T:.2f});\n'

    def text(self, s, x, y, w, size=80, color="#fff", t=None, how="up", out=None, rot=0, extra=""):
        i = self._id("t")
        self.add(f'<div class="txt" id="{i}" style="left:{x}px;top:{y}px;width:{w}px;font-size:{size}px;color:{color};transform:rotate({rot}deg);{extra}">{s}</div>',
                 self.anim_in("#" + i, t, how))
        if out is not None:
            self.out("#" + i, out)
        return "#" + i

    def pill(self, s, x, y, bg="#ffd93d", color="#14123a", t=None, how="left", size=44, out=None, right=False):
        i = self._id("p")
        pos = f"right:{x}px" if right else f"left:{x}px"
        self.add(f'<div class="pill" id="{i}" style="{pos};top:{y}px;background:{bg};color:{color};font-size:{size}px">{s}</div>',
                 self.anim_in("#" + i, t, how, 0.3))
        if out is not None:
            self.out("#" + i, out)
        return "#" + i

    def ball(self, x, y, size, c1, c2, face=False, t=None, how="pop", bob=0, glow=None, out=None, label=None, lsize=40):
        i = self._id("b")
        g = f"box-shadow:0 0 {size // 2}px {glow};" if glow else ""
        lab = f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:{lsize}px;color:#14123a">{label}</div>' if label else ""
        self.add(f'<div class="ball" id="{i}" style="left:{x}px;top:{y}px;width:{size}px;height:{size}px;background:radial-gradient(circle at 36% 30%,{c1},{c2});{g}">{FACE if face else ""}{lab}</div>',
                 self.anim_in("#" + i, t, how))
        if bob:
            self.js += f'tl.to("#{i}",{{y:"+={bob}",duration:0.9,repeat:{int(self.dur_est() / 1.8) + 1},yoyo:true,ease:"sine.inOut"}},{self.T(t) + 0.4:.2f});\n'
        if out is not None:
            self.out("#" + i, out)
        return "#" + i

    def emoji(self, ch, x, y, size=200, t=None, how="pop", spin=0, bob=0, out=None):
        i = self._id("m")
        self.add(f'<div class="abs" id="{i}" style="left:{x}px;top:{y}px;font-size:{size}px;line-height:1;width:{size * 1.3}px;text-align:center;font-family:\'Noto Color Emoji\'">{ch}</div>',
                 self.anim_in("#" + i, t, how))
        T = self.T(t)
        if spin:
            self.js += f'tl.to("#{i}",{{rotation:{spin},duration:{self.dur_est() - (T - self.t0):.2f},ease:"none"}},{T:.2f});\n'
        if bob:
            self.js += f'tl.to("#{i}",{{y:"+={bob}",duration:0.9,repeat:{int(self.dur_est() / 1.8) + 1},yoyo:true,ease:"sine.inOut"}},{T + 0.4:.2f});\n'
        if out is not None:
            self.out("#" + i, out)
        return "#" + i

    def move(self, sel, t, x=None, y=None, dur=0.8, ease="power2.inOut", scale=None, rot=None):
        v = []
        if x is not None: v.append(f"x:{x}")
        if y is not None: v.append(f"y:{y}")
        if scale is not None: v.append(f"scale:{scale}")
        if rot is not None: v.append(f"rotation:{rot}")
        self.js += f'tl.to("{sel}",{{{",".join(v)},duration:{dur},ease:"{ease}"}},{self.T(t):.2f});\n'

    def counter(self, a, b, x, y, w, size=170, color="#ffd93d", t=None, dur=1.5, suffix="", prefix="", dec=0, how="slam", out=None):
        i = self._id("c")
        T = self.T(t)
        self.add(f'<div class="txt" id="{i}" style="left:{x}px;top:{y}px;width:{w}px;font-size:{size}px;color:{color}">{prefix}{a}{suffix}</div>',
                 self.anim_in("#" + i, t, how, 0.3) +
                 f'\n(function(){{const o={{v:{a}}};tl.to(o,{{v:{b},duration:{dur},ease:"power2.out",onUpdate:()=>{{document.getElementById("{i}").textContent="{prefix}"+o.v.toFixed({dec}).replace(".",",")+"{suffix}"}}}},{T:.2f});}})();')
        if out is not None:
            self.out("#" + i, out)
        return "#" + i

    def bar(self, x, y, w, h, frac, color="#4aa3ff", track="rgba(255,255,255,.18)", t=None, dur=1.2, label=None, lcolor="#14123a", out=None):
        i = self._id("r")
        T = self.T(t)
        lab = f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:{int(h * 0.55)}px;color:{lcolor}">{label}</div>' if label else ""
        self.add(f'<div class="abs" id="{i}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{h}px;background:{track};overflow:hidden"><div id="{i}f" style="position:absolute;left:0;top:0;bottom:0;width:100%;transform-origin:0 50%;background:{color};border-radius:{h}px"></div>{lab}</div>',
                 self.anim_in("#" + i, t, "fade", 0.2) + f'\ntl.fromTo("#{i}f",{{scaleX:0}},{{scaleX:{frac},duration:{dur},ease:"power2.out"}},{T:.2f});')
        if out is not None:
            self.out("#" + i, out)
        return "#" + i

    def path(self, d, color="#fff", width=14, t=None, dur=1.0, w=1080, h=1920, ox=0, oy=0, ease="power1.inOut", out=None, dash=None):
        i = self._id("w")
        T = self.T(t)
        self.add(f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="left:{ox}px;top:{oy}px"><path id="{i}" d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1 1.2" stroke-dashoffset="1.1"/></svg>',
                 f'tl.to("#{i}",{{strokeDashoffset:0,duration:{dur},ease:"{ease}"}},{T:.2f});')
        if out is not None:
            self.out("#" + i, out)
        return "#" + i

    def rect(self, x, y, w, h, color="#fff", t=None, how="pop", radius=0, border=None, opacity=1, out=None, extra=""):
        i = self._id("q")
        bd = f"border:{border};" if border else ""
        self.add(f'<div class="abs" id="{i}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{color};border-radius:{radius}px;opacity:{opacity};{bd}{extra}"></div>',
                 self.anim_in("#" + i, t, how, 0.3))
        if out is not None:
            self.out("#" + i, out)
        return "#" + i

    def qr(self, x, y, size, text="https://www.youtube.com/@mentenerd", t=None, how="pop", pad=0.04):
        import qrcode
        q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=0, box_size=1)
        q.add_data(text); q.make(fit=True)
        m = q.get_matrix(); n = len(m)
        d = "".join(f"M{c} {r}h1v1h-1z" for r, row in enumerate(m) for c, b in enumerate(row) if b)
        i = self._id("qr")
        p = size * pad
        self.add(f'<div class="abs" id="{i}" style="left:{x}px;top:{y}px;width:{size}px;height:{size}px;background:#fff;border-radius:28px;box-shadow:0 20px 60px rgba(0,0,0,.45)"><svg viewBox="0 0 {n} {n}" width="{size - 2 * p}" height="{size - 2 * p}" style="left:{p}px;top:{p}px"><path d="{d}" fill="#14123a"/></svg></div>',
                 self.anim_in("#" + i, t, how, 0.4))
        self.qr_info = dict(x=x + p, y=y + p, cell=(size - 2 * p) / n, n=n, size=size)
        return "#" + i

    def battery(self, x, y, w, h, frac=1.0, color="#5ee08a", t=None, how="pop", label=None):
        i = self._id("bt")
        self.add(f'<div class="abs" id="{i}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
                 f'<div class="abs" style="left:0;top:0;width:{w - 30}px;height:{h}px;border:10px solid #fff;border-radius:34px;background:rgba(255,255,255,.08)"></div>'
                 f'<div class="abs" style="left:{w - 30}px;top:{h * 0.3}px;width:30px;height:{h * 0.4}px;background:#fff;border-radius:0 12px 12px 0"></div>'
                 f'<div class="abs" id="{i}f" style="left:22px;top:22px;width:{w - 74}px;height:{h - 44}px;border-radius:20px;background:{color};transform-origin:0 50%"></div>'
                 f'<div id="{i}l" style="position:absolute;left:0;top:0;width:{w - 30}px;height:{h}px;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:{int(h * 0.38)}px;color:#14123a">{label or ""}</div></div>',
                 self.anim_in("#" + i, t, how, 0.4) + f'\ntl.set("#{i}f",{{scaleX:{frac}}},0);')
        return "#" + i

    def video(self, file, w=960, y=260, tag=None, x=None):
        import subprocess as sp
        src = os.path.join(ROOT, "media", file)
        vw, vh = [int(z) for z in sp.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", src]).decode().strip().split(",")]
        h = int(w * vh / vw)
        os.makedirs(os.path.join(self.v.dir, "assets"), exist_ok=True)
        shutil.copy(src, os.path.join(self.v.dir, "assets", file))
        i = self._id("vd")
        x = (1080 - w) // 2 if x is None else x
        self.add(f'<div class="shade"></div><div class="frame" id="{i}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:#000"><video src="assets/{file}" muted playsinline style="width:100%;height:100%;display:block;object-fit:cover"></video></div>',
                 f'tl.fromTo("#{i}",{{scale:0.92,opacity:0}},{{scale:1,opacity:1,duration:.35,ease:"power3.out"}},{self.t0:.2f});')
        if tag:
            tg = self._id("tg")
            self.add(f'<div class="pill" id="{tg}" style="left:50px;top:{y + h + 30}px;font-size:40px;background:#ffd93d">{tag}</div>',
                     f'tl.fromTo("#{tg}",{{opacity:0,x:-60}},{{opacity:1,x:0,duration:.35,ease:"power3.out"}},{self.t0 + 0.4:.2f});')
        return "#" + i

    def raw(self, h, js=""):
        self.add(h, js)

    def dur_est(self):
        return max(1.0, (self.t1 - self.t0)) if hasattr(self, "t1") else 6.0

    # ---- fotos / vídeos de fundo
    def photo(self, src, fit="cover", pan=(0, 0), zoom=(1.0, 1.12), tag=None, focus=(0.5, 0.5), frame=None):
        """src: caminho relativo a LIB. fit cover = tela cheia; contain = quadro sobre fundo desfocado."""
        name = self.v.stage_img(src)
        i = self._id("ph")
        if fit == "cover":
            self.add(f'<img class="photo" id="{i}" src="assets/{name}" style="width:{self.v.imgw(name)}px;height:{self.v.imgh(name)}px;left:{-(self.v.imgw(name) - 1080) * focus[0]:.0f}px;top:{-(self.v.imgh(name) - 1920) * focus[1]:.0f}px"/>' +
                     '<div class="shade"></div><div class="shadeT"></div>',
                     f'tl.fromTo("#{i}",{{scale:{zoom[0]},x:0,y:0}},{{scale:{zoom[1]},x:{pan[0]},y:{pan[1]},duration:{self.dur_est() + 0.5:.2f},ease:"none"}},{self.t0:.2f});')
        else:
            fx, fy, fw, fh = frame or (60, 200, 960, 980)
            iw, ih = self.v.imgw(name, raw=True), self.v.imgh(name, raw=True)
            sc = min(fw / iw, fh / ih)
            w, h = iw * sc, ih * sc
            fx2, fy2 = fx + (fw - w) / 2, fy + (fh - h) / 2
            self.add(f'<img class="blur" src="assets/{name}"/><div class="shade"></div>'
                     f'<div class="frame" id="{i}" style="left:{fx2:.0f}px;top:{fy2:.0f}px;width:{w:.0f}px;height:{h:.0f}px"><img src="assets/{name}" style="width:100%;height:100%;display:block"/></div>',
                     f'tl.fromTo("#{i}",{{scale:{zoom[0]},y:0,opacity:0}},{{scale:{zoom[1]},y:{pan[1]},opacity:1,duration:{self.dur_est() + 0.5:.2f},ease:"none"}},{self.t0:.2f});')
        if tag:
            tg = self._id("tg")
            self.add(f'<div class="pill" id="{tg}" style="left:50px;top:1080px;font-size:36px;background:rgba(255,255,255,.92)">{tag}</div>',
                     f'tl.fromTo("#{tg}",{{opacity:0,x:-60}},{{opacity:1,x:0,duration:.35,ease:"power3.out"}},{self.t0 + 0.4:.2f});')
        return "#" + i


class Video:
    def __init__(self, name, bg_default="#1c1058", decoration="stars"):
        self.name = name
        self.dir = os.path.join(ROOT, name)
        self.words = json.load(open(os.path.join(ROOT, f"{name}.words.json")))
        self.words = [(a, b, w) for a, b, w in self.words]
        self.fix = {}
        self.phr = []
        self.TOT = round(float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", os.path.join(ROOT, f"{name}.mp3")])), 2)
        self.scenes = []
        self.deco = decoration
        self.bgd = bg_default
        self.imgs = {}
        self.media = []
        self.credits = []

    def scene(self, at, bg=None, deco=None):
        s = Scene(self, len(self.scenes) + 1, at, bg or self.bgd, deco or self.deco)
        self.scenes.append(s)
        return s

    # imagens
    def stage_img(self, rel, max_h=2200):
        src = os.path.join(LIB, rel)
        import hashlib
        base = re.sub(r"[^A-Za-z0-9_.-]", "_", os.path.splitext(os.path.basename(rel))[0])[:30] + "_" + hashlib.md5(rel.encode()).hexdigest()[:6] + ".jpg"
        os.makedirs(os.path.join(self.dir, "assets"), exist_ok=True)
        out = os.path.join(self.dir, "assets", base)
        if base not in self.imgs:
            im = Image.open(src)
            im = im.convert("RGB")
            w, h = im.size
            sc = min(2100 / h, 4.5)
            nw, nh = int(w * sc), int(h * sc)
            if nw < 1200:
                k = 1200 / nw
                nw, nh = 1200, int(nh * k)
            if nw > 4800:
                k = 4800 / nw
                nw, nh = 4800, int(nh * k)
            im2 = im.resize((nw, nh), Image.LANCZOS)
            im2.save(out, quality=88)
            self.imgs[base] = (nw, nh, w, h)
        return base

    def imgw(self, name, raw=False):
        return self.imgs[name][2 if raw else 0]

    def imgh(self, name, raw=False):
        return self.imgs[name][3 if raw else 1]

    def apply_fix(self):
        out = []
        for a, b, w in self.words:
            core = re.sub(r"[.,!?;:]+$", "", w); tail = w[len(core):]
            if core in self.fix:
                if self.fix[core] == "":
                    continue
                w = self.fix[core] + tail
            out.append((a, b, w))
        self.words = out
        for old, new in self.phr:
            ks = [norm(z) for z in old.split()]
            n = len(ks)
            for j in range(len(self.words) - n + 1):
                if [norm(self.words[j + q][2]) for q in range(n)] == ks:
                    a = self.words[j][0]; b = self.words[j + n - 1][1]
                    self.words[j:j + n] = [(a, b, new)]
                    break

    def build(self):
        self.apply_fix()
        os.makedirs(os.path.join(self.dir, "assets"), exist_ok=True)
        for f in ["package.json", "hyperframes.json", "meta.json"]:
            shutil.copy(os.path.join(PILOT, f), os.path.join(self.dir, f))
        shutil.copy(os.path.join(ROOT, f"{self.name}.mp3"), os.path.join(self.dir, "assets", "voice.mp3"))
        # tempos das cenas
        starts = []
        for s in self.scenes:
            if isinstance(s.at, (int, float)):
                starts.append(float(s.at))
            else:
                k = norm(s.at[0] if isinstance(s.at, tuple) else s.at)
                occ = s.at[1] if isinstance(s.at, tuple) else 1
                c = 0
                for a, b, w in self.words:
                    if norm(w) == k:
                        c += 1
                        if c == occ:
                            starts.append(max(0.0, a - 0.05))
                            break
                else:
                    raise KeyError(s.at)
        starts[0] = 0.0
        for i in range(1, len(starts)):
            if starts[i] <= starts[i - 1] + 0.5:
                raise ValueError(f'{self.name}: cena {i + 1} comeca em {starts[i]:.2f}, antes/colada na cena {i} ({starts[i - 1]:.2f}): {starts}')
        for i, s in enumerate(self.scenes):
            s.t0 = starts[i]
            s.t1 = starts[i + 1] if i + 1 < len(starts) else self.TOT
        # executa os construtores (callbacks) com tempos conhecidos
        body, js = "", ""
        for s in self.scenes:
            s.build_fn(s)
            ov = 0.2 if s.idx < len(self.scenes) else 0
            d = s.t1 - s.t0 + ov
            deco = deco_html(s.deco, s.idx)
            body += (f'<div class="sc clip" id="sc{s.idx}" data-start="{s.t0:.2f}" data-duration="{d:.2f}" style="z-index:{s.idx}">'
                     f'<div class="in" id="in{s.idx}" style="background:{s.bg}">{deco}{s.html}</div></div>\n')
            js += f'tl.fromTo("#in{s.idx}",{{opacity:0}},{{opacity:1,duration:.2,ease:"power1.out"}},{s.t0:.2f});\n' + s.js
        cap, capjs = self.captions()
        doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{self.TOT}" data-width="1080" data-height="1920">
<audio id="voice" src="assets/voice.mp3" data-start="0" data-duration="{self.TOT}" data-volume="1"></audio>
{body}
{cap}
</div>
<script>
window.__timelines=window.__timelines||{{}};
const tl=gsap.timeline({{paused:true}});
{js}
{capjs}
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
        open(os.path.join(self.dir, "index.html"), "w").write(doc)
        return self.dir

    def captions(self):
        words = self.words
        groups, cur = [], []
        for k, (a, b, t) in enumerate(words):
            cur.append((a, b, t))
            nxt = words[k + 1] if k + 1 < len(words) else None
            if nxt is None or nxt[0] - b >= 0.18 or len(cur) >= 4 or re.search(r"[.?!]$", t):
                groups.append(cur)
                cur = []
        cap, tl = "", ""
        for gi, g in enumerate(groups):
            s = max(0.05, g[0][0] - 0.04)
            e = g[-1][1] + 0.05
            nxt_s = groups[gi + 1][0][0] - 0.04 if gi + 1 < len(groups) else self.TOT
            e = min(e + 0.1, nxt_s)
            e = max(e, s + 0.3) if nxt_s - s > 0.3 else nxt_s
            e = min(e, self.TOT)
            spans = "".join(f'<span id="c{gi}w{wi}">{html.escape(re.sub(chr(91) + "!?.,;:" + chr(93) + "+$", "", t))}</span> ' for wi, (a, b, t) in enumerate(g))
            cap += f'<div class="cap clip" id="cg{gi}" data-start="{s:.2f}" data-duration="{e - s:.2f}" style="z-index:100">{spans}</div>\n'
            tl += f'tl.fromTo("#cg{gi}",{{opacity:0,y:16}},{{opacity:1,y:0,duration:0.14,ease:"power3.out"}},{s:.2f});\n'
            for wi, (a, b, t) in enumerate(g):
                tl += f'tl.fromTo("#c{gi}w{wi}",{{color:"#e8ecf5"}},{{color:"#ffc83d",duration:0.05}},{a:.2f});tl.to("#c{gi}w{wi}",{{color:"#e8ecf5",duration:0.04}},{b + 0.02:.2f});\n'
        return cap, tl


def deco_html(kind, idx):
    if kind == "stars":
        return "".join(f'<i class="ball" style="left:{(i * 137 + idx * 53) % 1080}px;top:{(i * 263 + idx * 91) % 1900}px;width:{3 + i % 4}px;height:{3 + i % 4}px;background:#fff;opacity:{.2 + (i % 5) * .1}"></i>' for i in range(50))
    if kind == "bubbles":
        return "".join(f'<i class="ball" style="left:{(i * 173 + idx * 41) % 1000}px;top:{(i * 311 + idx * 77) % 1800}px;width:{30 + (i % 5) * 26}px;height:{30 + (i % 5) * 26}px;background:rgba(255,255,255,.07)"></i>' for i in range(22))
    if kind == "grid":
        return '<div class="abs" style="inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.05) 2px,transparent 2px);background-size:90px 90px"></div>'
    return ""


def S(video, at, bg=None, deco=None):
    """decorator: @S(v, 'palavra', bg=...) def f(s): ..."""
    def wrap(fn):
        sc = video.scene(at, bg, deco)
        sc.build_fn = fn
        return fn
    return wrap
