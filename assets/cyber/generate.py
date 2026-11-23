"""Regenerates the cyberpunk README SVGs. Edit ATTRS/TERM/SECTIONS below, then run:
    python assets/cyber/generate.py
"""
import os, sys
from xml.sax.saxutils import escape as esc

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

Y, C, R, BG, DIM, TXT = "#FCEE0A", "#00F0FF", "#FF003C", "#0A0B10", "#8A8F98", "#E6E6E6"
STYLE = """<style>
.disp{font-family:'Arial Black','Arial Bold',Impact,'Helvetica Neue',Arial,sans-serif;font-weight:900}
.mono{font-family:Consolas,'Courier New',Menlo,monospace}
@keyframes flicker{0%,18%,22%,25%,53%,57%,100%{opacity:1}20%,24%,55%{opacity:.25}}
.flicker{animation:flicker 4s infinite}
</style>"""
COMMON_DEFS = f"""<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="{Y}" stroke-opacity=".07"/></pattern>
<pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1.5" fill="#000" opacity=".35"/></pattern>
<pattern id="stripes" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="12" fill="{Y}"/></pattern>"""


def blink_cursor(ch="_", color=C):
    return (f'<tspan fill="{color}">{ch}<animate attributeName="fill-opacity" values="1;0" '
            f'dur="1s" calcMode="discrete" repeatCount="indefinite"/></tspan>')


def write(name, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(body)


# ---------------------------------------------------------------- HEADER
def header():
    name = "ALI HAIDER"
    nameattrs = 'class="disp" font-size="100" textLength="760" lengthAdjust="spacingAndGlyphs"'
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="340" viewBox="0 0 1200 340" role="img" aria-label="Ali Haider - Fullstack Engineer">
<title>Ali Haider - Fullstack Engineer</title>
{STYLE}
<defs>
{COMMON_DEFS}
<linearGradient id="beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{C}" stop-opacity="0"/><stop offset="1" stop-color="{C}" stop-opacity=".22"/></linearGradient>
<clipPath id="frame"><path d="M0 0H1160L1200 40V340H40L0 300Z"/></clipPath>
<clipPath id="g1"><rect x="0" y="0" width="1200" height="0">
<animate attributeName="y" values="0;95;140;112;0" keyTimes="0;.88;.9;.93;.96" dur="3.2s" calcMode="discrete" repeatCount="indefinite"/>
<animate attributeName="height" values="0;18;12;26;0" keyTimes="0;.88;.9;.93;.96" dur="3.2s" calcMode="discrete" repeatCount="indefinite"/></rect></clipPath>
<clipPath id="g2"><rect x="0" y="0" width="1200" height="0">
<animate attributeName="y" values="0;150;102;128;0" keyTimes="0;.6;.62;.9;.94" dur="3.2s" calcMode="discrete" repeatCount="indefinite"/>
<animate attributeName="height" values="0;14;30;10;0" keyTimes="0;.6;.62;.9;.94" dur="3.2s" calcMode="discrete" repeatCount="indefinite"/></rect></clipPath>
<filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="8"/></filter>
</defs>
<g clip-path="url(#frame)">
<rect width="1200" height="340" fill="{BG}"/>
<rect width="1200" height="340" fill="url(#grid)"/>
<rect x="0" y="-90" width="1200" height="90" fill="url(#beam)"><animate attributeName="y" from="-90" to="340" dur="4s" repeatCount="indefinite"/></rect>

<path d="M0 0H360L336 32H0Z" fill="{Y}"/>
<text x="22" y="22" class="mono" font-size="15" font-weight="700" fill="{BG}" letter-spacing="2">NC_ID // AH-718 // NETRUNNER</text>
<text x="1130" y="24" text-anchor="end" class="mono" font-size="13" fill="{DIM}" letter-spacing="2">BUILD 20.77 :: SECTOR SYD-AU</text>
<rect x="1140" y="14" width="6" height="12" fill="{R}"/>

<text x="70" y="182" {nameattrs} fill="{Y}" opacity=".45" filter="url(#glow)">{name}</text>
<g>
<animateTransform attributeName="transform" type="translate" values="0 0;-5 0;4 0;0 0" keyTimes="0;.88;.92;.96" dur="3.2s" calcMode="discrete" repeatCount="indefinite"/>
<text x="70" y="182" {nameattrs} fill="{Y}">{name}</text>
<text x="62" y="182" {nameattrs} fill="{C}" clip-path="url(#g1)">{name}</text>
<text x="79" y="182" {nameattrs} fill="{R}" clip-path="url(#g2)">{name}</text>
</g>
<path d="M70 202H800L812 210H70Z" fill="{Y}"/>
<rect x="818" y="202" width="12" height="8" fill="{R}"><animate attributeName="opacity" values="1;0" dur="0.8s" calcMode="discrete" repeatCount="indefinite"/></rect>

<text x="70" y="244" class="mono" font-size="25" font-weight="700" fill="{C}" letter-spacing="3">FULLSTACK ENGINEER // REACT × .NET × CLOUD</text>
<text x="70" y="274" class="mono" font-size="15" fill="{DIM}" letter-spacing="2">LOC: SYDNEY_AU   EXP: 6+ YRS   CLASS: NETRUNNER   STATUS: <tspan fill="{R}">● ONLINE<animate attributeName="fill-opacity" values="1;.2" dur="1.2s" calcMode="discrete" repeatCount="indefinite"/></tspan></text>

<rect x="70" y="292" width="760" height="14" fill="none" stroke="{Y}" stroke-opacity=".5"/>
<rect x="72" y="294" width="756" height="10" fill="url(#stripes)"><animate attributeName="width" values="0;756;756" keyTimes="0;.8;1" dur="4s" repeatCount="indefinite"/></rect>
<text x="70" y="326" class="mono" font-size="12" fill="{DIM}" letter-spacing="3">SYNCING NEURAL LINK<tspan fill="{Y}">...<animate attributeName="fill-opacity" values="1;0" dur=".6s" calcMode="discrete" repeatCount="indefinite"/></tspan></text>

<g transform="translate(1020 172)">
<circle r="104" fill="none" stroke="{Y}" stroke-opacity=".25"/>
<g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="18s" repeatCount="indefinite"/>
<circle r="90" fill="none" stroke="{C}" stroke-width="2" stroke-dasharray="3 9"/>
<circle cx="0" cy="-104" r="5" fill="{R}"/></g>
<g><animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="9s" repeatCount="indefinite"/>
<circle r="74" fill="none" stroke="{Y}" stroke-width="5" stroke-dasharray="70 46"/></g>
<g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="5s" repeatCount="indefinite"/>
<path d="M0 0L0 -60A60 60 0 0 1 42 -43Z" fill="{C}" fill-opacity=".18"/></g>
<path d="M-120 0H-58M58 0H120M0 -120V-58M0 58V120" stroke="{Y}" stroke-opacity=".6"/>
<circle r="56" fill="none" stroke="{C}" stroke-opacity=".4"/>
<text y="10" text-anchor="middle" class="disp flicker" font-size="34" fill="{Y}">718</text>
<text y="34" text-anchor="middle" class="mono" font-size="11" fill="{C}" letter-spacing="2">LVL MAX</text>
</g>

<rect x="0" y="120" width="1200" height="3" fill="{C}" opacity="0"><animate attributeName="opacity" values="0;.7;0" keyTimes="0;.9;.92" dur="3.2s" calcMode="discrete" repeatCount="indefinite"/></rect>
<rect x="300" y="160" width="520" height="6" fill="{R}" opacity="0"><animate attributeName="opacity" values="0;.6;0" keyTimes="0;.6;.62" dur="3.2s" calcMode="discrete" repeatCount="indefinite"/></rect>
<rect width="1200" height="340" fill="url(#scan)"/>
</g>
<path d="M1 1H1159.5L1199 40.5V339H40.5L1 299.5Z" fill="none" stroke="{Y}" stroke-width="2" stroke-opacity=".8"/>
<path d="M1160 0H1200V40Z" fill="{Y}"/><path d="M0 300V340H40Z" fill="{Y}"/>
</svg>
"""


# ---------------------------------------------------------------- SECTION HEADERS
def section(num, title, tag):
    hexid = f"0x{(num * 0x2077 + 0x718):06X}"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="80" viewBox="0 0 1200 80" role="img" aria-label="{esc(title)}">
<title>{esc(title)}</title>
{STYLE}
<defs>
{COMMON_DEFS}
<clipPath id="frame"><path d="M0 0H1170L1200 30V80H30L0 50Z"/></clipPath>
</defs>
<g clip-path="url(#frame)">
<rect width="1200" height="80" fill="{BG}"/>
<rect width="1200" height="80" fill="url(#grid)"/>
<path d="M0 0H96L72 80H0Z" fill="{Y}"/>
<path d="M100 0H112L88 80H76Z" fill="{R}"/>
<text x="14" y="54" class="disp" font-size="34" fill="{BG}">{num:02d}</text>
<text x="124" y="48" class="disp flicker" font-size="30" fill="{Y}" letter-spacing="2">{esc(title)}{blink_cursor()}</text>
<line x1="124" y1="64" x2="1150" y2="64" stroke="{C}" stroke-opacity=".25" stroke-width="2"/>
<line x1="124" y1="64" x2="1150" y2="64" stroke="{C}" stroke-width="2" stroke-dasharray="140 1200"><animate attributeName="stroke-dashoffset" values="140;-1200" dur="3s" repeatCount="indefinite"/></line>
<text x="1160" y="26" text-anchor="end" class="mono" font-size="13" fill="{DIM}" letter-spacing="2">SYS://{esc(tag)}</text>
<text x="1160" y="50" text-anchor="end" class="mono" font-size="12" fill="{R}" letter-spacing="2">{hexid}</text>
<rect width="1200" height="80" fill="url(#scan)"/>
</g>
<path d="M1 1H1169.5L1199 30.5V79H30.5L1 49.5Z" fill="none" stroke="{Y}" stroke-opacity=".6" stroke-width="2"/>
</svg>
"""


SECTIONS = [
    (1, "IDENTITY", "WHOAMI.EXE"),
    (2, "NEURAL STACK", "CYBERWARE.DB"),
    (3, "CORPO HISTORY", "EMPLOYERS.LOG"),
    (4, "GIGS COMPLETED", "DEPLOYMENTS.DAT"),
    (5, "SYSTEM DIAGNOSTICS", "GH_TELEMETRY"),
    (6, "TRAINING PROTOCOLS", "MENTOR.SYS"),
    (7, "OFF-DUTY", "LEISURE.CFG"),
    (8, "COMMS LINK", "OPEN_CHANNELS"),
]


# ---------------------------------------------------------------- ATTRIBUTES
ATTRS = [
    ("REFLEXES", "FRONTEND :: React · React Native · Next.js", 19),
    ("TECHNICAL", "BACKEND :: .NET Core · REST · CQRS · Mediator", 18),
    ("INTELLIGENCE", "ARCHITECTURE :: Microservices · OAuth 2.0", 17),
    ("BODY", "CLOUD OPS :: Azure · AWS · GitHub Actions", 17),
    ("COOL", "UI CRAFT :: Tailwind · Material UI · Redux · Zustand", 18),
    ("EMPATHY", "TRAINING :: Mentoring devs in JS / TS / C#", 19),
]


def attributes():
    rows_h = 62
    h = 86 + len(ATTRS) * rows_h + 10
    parts = []
    for i, (label, sub, lvl) in enumerate(ATTRS):
        y0 = 86 + i * rows_h
        parts.append(f'<text x="40" y="{y0 + 22}" class="disp" font-size="21" fill="{Y}" letter-spacing="2">{label}</text>')
        parts.append(f'<text x="40" y="{y0 + 44}" class="mono" font-size="13" fill="{DIM}">{esc(sub)}</text>')
        for j in range(20):
            x = 520 + j * 28
            d = f"M{x + 7} {y0 + 6}H{x + 24}L{x + 17} {y0 + 36}H{x}Z"
            if j < lvl:
                col = C if j == lvl - 1 else Y
                # begin at 0 with the delay encoded in keyTimes, so the base (static) state is fully lit
                T = 2.0
                begin = 0.3 + i * 0.12 + j * 0.03
                k1, k2 = begin / T, (begin + 0.1) / T
                anim = (f'<animate attributeName="opacity" values="0;0;1;1" keyTimes="0;{k1:.3f};{k2:.3f};1" '
                        f'dur="{T}s" fill="freeze"/>')
                if j == lvl - 1:
                    anim += f'<animate attributeName="fill-opacity" values="1;.25;1" begin="{T}s" dur="1.4s" repeatCount="indefinite"/>'
                parts.append(f'<path d="{d}" fill="{col}">{anim}</path>')
            else:
                parts.append(f'<path d="{d}" fill="#14161D" stroke="#2C303B"/>')
        parts.append(f'<text x="1160" y="{y0 + 31}" text-anchor="end" class="disp" font-size="24" fill="{C}">{lvl}<tspan class="mono" font-size="14" fill="{DIM}" font-weight="400">/20</tspan></text>')
        if i < len(ATTRS) - 1:
            parts.append(f'<line x1="40" y1="{y0 + 54}" x2="1160" y2="{y0 + 54}" stroke="{Y}" stroke-opacity=".12" stroke-dasharray="4 6"/>')
    total = sum(a[2] for a in ATTRS)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}" role="img" aria-label="Netrunner attributes: skill levels">
<title>Netrunner attributes</title>
{STYLE}
<defs>
{COMMON_DEFS}
<clipPath id="frame"><path d="M0 0H1170L1200 30V{h}H30L0 {h - 30}Z"/></clipPath>
</defs>
<g clip-path="url(#frame)">
<rect width="1200" height="{h}" fill="{BG}"/>
<rect width="1200" height="{h}" fill="url(#grid)"/>
<path d="M0 0H440L416 34H0Z" fill="{Y}"/>
<text x="24" y="24" class="disp" font-size="19" fill="{BG}" letter-spacing="3">NETRUNNER ATTRIBUTES</text>
<text x="1160" y="26" text-anchor="end" class="mono" font-size="13" fill="{DIM}" letter-spacing="2">PTS ALLOCATED: <tspan fill="{C}">{total}/{len(ATTRS) * 20}</tspan></text>
<line x1="0" y1="62" x2="1200" y2="62" stroke="{Y}" stroke-opacity=".3"/>
{chr(10).join(parts)}
<rect width="1200" height="{h}" fill="url(#scan)"/>
</g>
<path d="M1 1H1169.5L1199 30.5V{h - 1}H30.5L1 {h - 30.5}Z" fill="none" stroke="{Y}" stroke-opacity=".6" stroke-width="2"/>
</svg>
"""


# ---------------------------------------------------------------- TERMINAL
PROMPT = "ali@night-city:~$ "
TERM = [
    ("cmd", "whoami"),
    ("out", [(Y, "ALI HAIDER"), (DIM, "  ::  "), (TXT, "Fullstack Engineer @ Westpac, Sydney AU")]),
    ("cmd", "cat ./runtime.log"),
    ("out", [(C, "[OK] "), (TXT, " 6+ years shipping production-grade software")]),
    ("out", [(C, "[OK] "), (Y, " FRONTEND  "), (DIM, ">> "), (TXT, "React · React Native · Next.js · Tailwind · MUI")]),
    ("out", [(C, "[OK] "), (Y, " STATE     "), (DIM, ">> "), (TXT, "Redux for heavy loads · Zustand for light ones")]),
    ("out", [(C, "[OK] "), (Y, " BACKEND   "), (DIM, ">> "), (TXT, ".NET Core · REST APIs · Microservices · CQRS · Mediator")]),
    ("out", [(C, "[OK] "), (Y, " SECURITY  "), (DIM, ">> "), (TXT, "OAuth 2.0 authentication")]),
    ("out", [(C, "[OK] "), (Y, " CLOUD     "), (DIM, ">> "), (TXT, "Azure (App Service, Service Bus, DevOps) · AWS (EC2, S3, Lambda)")]),
    ("out", [(C, "[OK] "), (Y, " PIPELINE  "), (DIM, ">> "), (TXT, "CI/CD with GitHub Actions")]),
    ("cmd", "./mission --print"),
    ("final", [(R, "> "), (TXT, "Localized, best-practice software that hits hard for clients & users ")]),
]


def terminal():
    lh, top = 29, 66
    h = top + len(TERM) * lh + 30
    defs, lines, timing = [], [], []
    t = 0.6
    for i, (kind, content) in enumerate(TERM):
        ybase = top + i * lh + 18
        if kind == "cmd":
            nchars = len(PROMPT) + len(content)
            dur = 0.25 + len(content) * 0.07
            body = f'<tspan fill="{C}">{PROMPT}</tspan><tspan fill="#FFFFFF">{esc(content)}</tspan>'
        else:
            nchars = sum(len(s) for _, s in content)
            dur = 0.25 if kind == "out" else 1.6
            body = "".join(f'<tspan fill="{col}">{esc(s)}</tspan>' for col, s in content)
            if kind == "final":
                body += blink_cursor("█", Y)
        w = 40 + nchars * 11 + 40
        timing.append((i, ybase, t, t + dur, w))
        lines.append(f'<text x="40" y="{ybase}" class="mono" font-size="17" clip-path="url(#l{i})" xml:space="preserve">{body}</text>')
        t += dur + (0.45 if kind == "cmd" else 0.12)
    # all animations begin at 0 with delays in keyTimes; the static base state shows every line
    T = t + 0.5
    for i, ybase, s, e, w in timing:
        defs.append(f'<clipPath id="l{i}"><rect x="0" y="{ybase - 22}" width="1200" height="{lh}">'
                    f'<animate attributeName="width" values="0;0;{w};1200" keyTimes="0;{s / T:.4f};{e / T:.4f};1" '
                    f'dur="{T:.2f}s" fill="freeze"/></rect></clipPath>')
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}" role="img" aria-label="Terminal: Ali Haider, Fullstack Engineer. 6+ years. React, React Native, Next.js, .NET Core, Azure, AWS, CI/CD.">
<title>whoami</title>
{STYLE}
<defs>
{COMMON_DEFS}
<clipPath id="frame"><path d="M0 0H1200V{h - 30}L1170 {h}H0Z"/></clipPath>
{chr(10).join(defs)}
</defs>
<g clip-path="url(#frame)">
<rect width="1200" height="{h}" fill="{BG}"/>
<rect width="1200" height="{h}" fill="url(#grid)" opacity=".5"/>
<rect width="1200" height="38" fill="{Y}"/>
<text x="20" y="25" class="mono" font-size="15" font-weight="700" fill="{BG}" letter-spacing="2">NET_TERMINAL v20.77 — ali@night-city</text>
<rect x="1110" y="13" width="12" height="12" fill="{BG}"/><rect x="1132" y="13" width="12" height="12" fill="{BG}"/><rect x="1154" y="13" width="12" height="12" fill="{R}"/>
{chr(10).join(lines)}
<rect width="1200" height="{h}" fill="url(#scan)"/>
</g>
<path d="M1 1H1199V{h - 30.5}L1169.5 {h - 1}H1V1Z" fill="none" stroke="{Y}" stroke-opacity=".6" stroke-width="2"/>
</svg>
"""


# ---------------------------------------------------------------- FOOTER
def footer():
    tick = ("/// THANKS FOR JACKING IN /// STAY CHROME, CHOOM /// OPEN TO COLLABS & GIGS "
            "/// REACT · REACT NATIVE · .NET · AZURE · AWS /// SYDNEY_AU ")
    tattrs = f'class="mono" font-size="15" font-weight="700" fill="{BG}" letter-spacing="2" textLength="1400" lengthAdjust="spacingAndGlyphs"'
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="140" viewBox="0 0 1200 140" role="img" aria-label="End of transmission">
<title>End of transmission</title>
{STYLE}
<defs>
{COMMON_DEFS}
<clipPath id="frame"><path d="M30 0H1200V110L1170 140H0V30Z"/></clipPath>
<clipPath id="gl"><rect x="0" y="0" width="1200" height="0">
<animate attributeName="y" values="0;38;56;0" keyTimes="0;.85;.89;.93" dur="3s" calcMode="discrete" repeatCount="indefinite"/>
<animate attributeName="height" values="0;10;14;0" keyTimes="0;.85;.89;.93" dur="3s" calcMode="discrete" repeatCount="indefinite"/></rect></clipPath>
</defs>
<g clip-path="url(#frame)">
<rect width="1200" height="140" fill="{BG}"/>
<rect width="1200" height="140" fill="url(#grid)"/>
<text x="600" y="66" text-anchor="middle" class="disp flicker" font-size="36" fill="{Y}" letter-spacing="6">END OF TRANSMISSION</text>
<text x="594" y="66" text-anchor="middle" class="disp" font-size="36" fill="{C}" letter-spacing="6" clip-path="url(#gl)">END OF TRANSMISSION</text>
<rect x="0" y="96" width="1200" height="30" fill="{Y}"/>
<g><animateTransform attributeName="transform" type="translate" from="0 0" to="-1400 0" dur="22s" repeatCount="indefinite"/>
<text x="0" y="117" {tattrs}>{esc(tick)}</text>
<text x="1400" y="117" {tattrs}>{esc(tick)}</text></g>
<rect width="1200" height="140" fill="url(#scan)"/>
</g>
<path d="M30.5 1H1199V109.5L1169.5 139H1V30.5Z" fill="none" stroke="{Y}" stroke-opacity=".6" stroke-width="2"/>
</svg>
"""


# ---------------------------------------------------------------- TILES (clickable dark cards)
def tile(label, value, status="", accent=Y, w=600, link=False, mono=False, live=False, idx=0):
    h = 76
    vclass, vsize = ("mono", 21) if mono else ("disp", 22)
    status_svg = ""
    if status:
        dot_anim = ('<animate attributeName="fill-opacity" values="1;.15" dur="1s" calcMode="discrete" repeatCount="indefinite"/>'
                    if live else "")
        status_svg = (f'<text x="{w - 26}" y="28" text-anchor="end" class="mono" font-size="12" fill="{DIM}" letter-spacing="2">'
                      f'<tspan fill="{accent}">●{dot_anim}</tspan> {esc(status)}</text>')
    arrow = (f'<text x="{w - 26}" y="58" text-anchor="end" class="mono" font-size="18" font-weight="700" fill="{accent}">&gt;&gt;</text>'
             if link else "")
    begin = (idx * 0.43) % 3
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}: {esc(value)}">
<title>{esc(value)}</title>
{STYLE}
<defs>
{COMMON_DEFS}
<clipPath id="frame"><path d="M0 0H{w - 20}L{w} 20V{h}H20L0 {h - 20}Z"/></clipPath>
</defs>
<g clip-path="url(#frame)">
<rect width="{w}" height="{h}" fill="{BG}"/>
<rect width="{w}" height="{h}" fill="url(#grid)"/>
<rect width="8" height="{h}" fill="{accent}"/>
<text x="26" y="28" class="mono" font-size="12" fill="{DIM}" letter-spacing="3">{esc(label)}</text>
<text x="26" y="58" class="{vclass}" font-size="{vsize}" fill="{Y}" letter-spacing="1">{esc(value)}</text>
{status_svg}
{arrow}
<line x1="26" y1="{h - 6}" x2="{w - 26}" y2="{h - 6}" stroke="{accent}" stroke-width="2" stroke-dasharray="90 {w * 2}" stroke-opacity=".8"><animate attributeName="stroke-dashoffset" values="90;-{w}" begin="{begin:.2f}s" dur="3s" repeatCount="indefinite"/></line>
<rect width="{w}" height="{h}" fill="url(#scan)"/>
</g>
<path d="M1 1H{w - 20.5}L{w - 1} 20.5V{h - 1}H20.5L1 {h - 20.5}Z" fill="none" stroke="{accent}" stroke-opacity=".55" stroke-width="2"/>
</svg>
"""


TILES = {
    # identity
    "id-role": dict(label="ROLE // CURRENT GIG", value="Fullstack Engineer @ Westpac", status="ACTIVE", accent=R, live=True, link=True),
    "id-location": dict(label="LOCATION", value="Sydney, AU", status="NC-SYD", accent=C),
    "id-class": dict(label="SIDE CLASS", value="Trainer & Mentor", accent=Y),
    "id-chipset": dict(label="CHIPSET // EDUCATION", value="Master of IT @ KOI", accent=C, link=True),
    "id-network": dict(label="NETWORK", value="LinkedIn Profile", accent=Y, link=True),
    "id-line": dict(label="DIRECT LINE", value="alimurtuza718@gmail.com", accent=R, link=True, mono=True),
    # corpo history
    "corp-westpac": dict(label="CORP 01 // CURRENT EMPLOYER", value="Westpac", status="ACTIVE CONTRACT", accent=R, live=True, link=True, w=1200),
    "corp-mae": dict(label="CORP 02", value="MAE Logistics", status="COMPLETED", accent=Y, link=True),
    "corp-raena": dict(label="CORP 03", value="RAENA", status="COMPLETED", accent=C, link=True),
    "corp-somee": dict(label="CORP 04", value="Somee Social", status="COMPLETED", accent=C, link=True),
    "corp-bizintel": dict(label="CORP 05", value="BizIntel", status="COMPLETED", accent=Y, link=True),
}
for slug, name in [("ma3", "MA3 Logistics"), ("ayms", "AYMS International"), ("somee", "Somee Social"),
                   ("rdash", "Rdash 360"), ("linkstore", "Linkstore (testing build)"), ("dresez", "Dresez")]:
    TILES[f"web-{slug}"] = dict(label="NET DEPLOYMENT // WEB", value=name, status="WEB", accent=C, link=True)
for slug, name in [("raena", "RAENA Reseller & Dropship"), ("somee", "Somee Social"), ("beeplink", "Beeplink"),
                   ("kumbayah", "KumBaYah"), ("bakier", "Bakier"), ("glow", "Glow Calculator"), ("macca", "Macca Motors")]:
    TILES[f"app-{slug}"] = dict(label="MOBILE IMPLANT // ANDROID", value=name, status="PLAY STORE", accent=Y, link=True)
TILES["app-macca"]["w"] = 1200


# ---------------------------------------------------------------- GENERIC PANEL FRAME
def panel(h, tab, right, body, aria):
    tabw = 40 + len(tab) * 15
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}" role="img" aria-label="{esc(aria)}">
<title>{esc(tab)}</title>
{STYLE}
<defs>
{COMMON_DEFS}
<clipPath id="frame"><path d="M0 0H1170L1200 30V{h}H30L0 {h - 30}Z"/></clipPath>
</defs>
<g clip-path="url(#frame)">
<rect width="1200" height="{h}" fill="{BG}"/>
<rect width="1200" height="{h}" fill="url(#grid)"/>
<path d="M0 0H{tabw}L{tabw - 24} 34H0Z" fill="{Y}"/>
<text x="24" y="24" class="disp" font-size="17" fill="{BG}" letter-spacing="3">{esc(tab)}</text>
<text x="1160" y="26" text-anchor="end" class="mono" font-size="13" fill="{DIM}" letter-spacing="2">{right}</text>
{body}
<rect width="1200" height="{h}" fill="url(#scan)"/>
</g>
<path d="M1 1H1169.5L1199 30.5V{h - 1}H30.5L1 {h - 30.5}Z" fill="none" stroke="{Y}" stroke-opacity=".6" stroke-width="2"/>
</svg>
"""


def stack():
    raw = open(os.path.join(OUT, "src", "skillicons.svg"), encoding="utf-8").read()
    inner = raw[raw.index(">", raw.index("<svg")) + 1: raw.rindex("</svg>")]
    row_w, size = 2056, 110  # 7 icons of 256 + 6 gaps of 44 (source units)
    pw = row_w * size / 256
    x = (1200 - pw) / 2
    body = f"""<defs><g id="strip">{inner}</g></defs>
<svg x="{x:.1f}" y="70" width="{pw:.1f}" height="{size}" viewBox="0 0 {row_w} 256"><use href="#strip"/></svg>
<svg x="{x:.1f}" y="200" width="{pw:.1f}" height="{size}" viewBox="2100 0 {row_w} 256"><use href="#strip"/></svg>
<rect x="0" y="60" width="60" height="260" fill="{C}" fill-opacity=".10"><animate attributeName="x" values="-60;1200" dur="3.5s" repeatCount="indefinite"/></rect>"""
    return panel(340, "CYBERWARE INSTALLED", f'MODULES: <tspan fill="{C}">14</tspan>', body,
                 "React, Next.js, TypeScript, JavaScript, Node.js, .NET, C#, Tailwind, Material UI, Redux, Azure, AWS, GitHub Actions, Git")


BIO = [
    "With over 6+ years of experience, I specialize in building responsive, user-focused front-end applications using modern frameworks like React and React Native. My expertise in Tailwind CSS and Material UI enables me to create clean, cohesive designs that enhance user engagement. For state management, I leverage Redux for complex applications and Zustand for lightweight solutions.",
    "On the backend, I excel in .NET Core, designing RESTful APIs, implementing microservices, and using patterns like CQRS and Mediator for maintainable and scalable systems. I also configure OAuth 2.0 for secure authentication.",
    "I have strong DevOps expertise, working with Azure (App Service, Service Bus, Azure DevOps) and AWS (EC2, S3, Lambda) to streamline development and deployment. I implement CI/CD pipelines with tools like GitHub Actions for fast, reliable deployments.",
    "Committed to localization and following industry best practices, I deliver impactful, high-quality software solutions tailored to client and user needs.",
]


def bio():
    import textwrap
    y, out = 80, []
    for p in BIO:
        for ln in textwrap.wrap(p, 104):
            out.append(f'<text x="40" y="{y}" class="mono" font-size="16" fill="{TXT}">{esc(ln)}</text>')
            y += 25
        y += 16
    return panel(y + 10, "DECRYPTED BIO", f'CLEARANCE: <tspan fill="{R}">GRANTED</tspan>', "\n".join(out), " ".join(BIO))


TRAINING = ["Fullstack web development (React.js / React Native / .NET Core)", "JavaScript / TypeScript / C#",
            "Git", "Programming fundamentals"]


def training():
    rows = []
    for i, t in enumerate(TRAINING):
        y = 84 + i * 48
        rows.append(f'<text x="40" y="{y}" class="disp" font-size="18" fill="{C}">P-{i + 1:02d}</text>'
                    f'<text x="120" y="{y}" class="mono" font-size="18" fill="{TXT}">{esc(t)}</text>'
                    f'<text x="1160" y="{y}" text-anchor="end" class="mono" font-size="13" fill="{Y}" letter-spacing="2">[ LOADED ]</text>'
                    f'<line x1="40" y1="{y + 16}" x2="1160" y2="{y + 16}" stroke="{Y}" stroke-opacity=".12" stroke-dasharray="4 6"/>')
    h = 84 + len(TRAINING) * 48
    return panel(h, "MENTOR.SYS LOADED", "JACKING NEW RUNNERS IN", "\n".join(rows), "Training: " + ", ".join(TRAINING))


HOBBIES = [("01", "GAMING", "Play videogames", Y), ("02", "TRAVEL", "Travelling", C), ("03", "COOKING", "Cooking", R)]


def offduty():
    cells = []
    for i, (n, title, sub, col) in enumerate(HOBBIES):
        x = 40 + i * 380
        cells.append(f'<path d="M{x} 60H{x + 350}L{x + 360} 70V150H{x + 10}L{x} 140Z" fill="#11131A" stroke="{col}" stroke-opacity=".6"/>'
                     f'<rect x="{x}" y="60" width="6" height="80" fill="{col}"/>'
                     f'<text x="{x + 24}" y="94" class="disp" font-size="26" fill="{col}">{title}</text>'
                     f'<text x="{x + 24}" y="124" class="mono" font-size="15" fill="{DIM}">{n} // {esc(sub)}</text>')
    return panel(176, "LEISURE.CFG", "STATUS: OFF-DUTY", "\n".join(cells), "Hobbies: videogames, travelling, cooking")


write("header.svg", header())
for n, title, tag in SECTIONS:
    write(f"section-{n:02d}.svg", section(n, title, tag))
write("attributes.svg", attributes())
write("terminal.svg", terminal())
write("footer.svg", footer())
write("stack.svg", stack())
write("bio.svg", bio())
write("training.svg", training())
write("offduty.svg", offduty())
os.makedirs(os.path.join(OUT, "tiles"), exist_ok=True)
for i, (slug, spec) in enumerate(TILES.items()):
    write(os.path.join("tiles", f"{slug}.svg"), tile(idx=i, **spec))
print("ok", sorted(os.listdir(OUT)))
