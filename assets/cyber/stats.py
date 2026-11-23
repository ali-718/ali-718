"""Builds the self-hosted GitHub stats widgets (no third-party stats servers).

Run by .github/workflows/snake.yml:
    GITHUB_TOKEN=... GH_USER=ali-718 python assets/cyber/stats.py dist
Local layout preview with made-up numbers:
    python assets/cyber/stats.py preview-dir --sample
"""
import datetime as dt
import json
import os
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate import BG, C, DIM, R, TXT, Y, esc, panel  # noqa: E402

LANG_COLORS = [Y, C, R, "#B967FF", "#05FFA1", "#FF8A00"]

USER_Q = """query($login:String!){ user(login:$login){
  followers{totalCount} pullRequests{totalCount} issues{totalCount}
  contributionsCollection{ totalCommitContributions restrictedContributionsCount
    contributionCalendar{ totalContributions weeks{ contributionDays{ date contributionCount } } } } } }"""
REPOS_Q = """query($login:String!,$after:String){ user(login:$login){
  repositories(first:100, after:$after, ownerAffiliations:OWNER, isFork:false, privacy:PUBLIC){
    totalCount pageInfo{hasNextPage endCursor}
    nodes{ stargazerCount languages(first:10, orderBy:{field:SIZE,direction:DESC}){ edges{ size node{name} } } } } } }"""


def gql(token, query, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json",
                 "User-Agent": "cyber-readme-stats"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    if data.get("errors"):
        raise SystemExit(f"GraphQL error: {data['errors']}")
    return data["data"]["user"]


def fetch(token, login):
    u = gql(token, USER_Q, {"login": login})
    repos, stars, langs, after = 0, 0, {}, None
    while True:
        page = gql(token, REPOS_Q, {"login": login, "after": after})["repositories"]
        repos = page["totalCount"]
        for n in page["nodes"]:
            stars += n["stargazerCount"]
            for e in n["languages"]["edges"]:
                langs[e["node"]["name"]] = langs.get(e["node"]["name"], 0) + e["size"]
        if not page["pageInfo"]["hasNextPage"]:
            break
        after = page["pageInfo"]["endCursor"]
    cc = u["contributionsCollection"]
    days = [(d["date"], d["contributionCount"]) for w in cc["contributionCalendar"]["weeks"] for d in w["contributionDays"]]
    return dict(repos=repos, stars=stars, langs=langs, followers=u["followers"]["totalCount"],
                prs=u["pullRequests"]["totalCount"], issues=u["issues"]["totalCount"],
                commits=cc["totalCommitContributions"] + cc["restrictedContributionsCount"],
                total=cc["contributionCalendar"]["totalContributions"], days=days)


def sample():
    import random
    random.seed(718)
    today = dt.date.today()
    days = [((today - dt.timedelta(days=i)).isoformat(), random.choice([0, 0, 1, 2, 3, 5, 8])) for i in range(364, -1, -1)]
    return dict(repos=42, stars=5, followers=37, prs=15, issues=1, commits=312, total=sum(c for _, c in days), days=days,
                langs={"JavaScript": 900, "TypeScript": 700, "C#": 400, "HTML": 150, "CSS": 120, "Java": 60, "Shell": 10})


def streaks(days):
    counts = [c for _, c in days]
    longest = run = 0
    for c in counts:
        run = run + 1 if c else 0
        longest = max(longest, run)
    i = len(counts) - 1
    if i >= 0 and counts[i] == 0:  # today not counted yet -> streak still alive from yesterday
        i -= 1
    cur = 0
    while i >= 0 and counts[i]:
        cur += 1
        i -= 1
    return cur, longest


def fmt(n):
    return f"{n / 1000:.1f}k" if n >= 10000 else f"{n:,}"


def diagnostics(s):
    synced = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    rows = [("PUBLIC REPOS", s["repos"]), ("STARS EARNED", s["stars"]), ("COMMITS // 12 MO", s["commits"]),
            ("PULL REQUESTS", s["prs"]), ("ISSUES OPENED", s["issues"]), ("FOLLOWERS", s["followers"])]
    b = [f'<text x="40" y="70" class="mono" font-size="12" fill="{DIM}" letter-spacing="3">CORE METRICS</text>']
    for i, (label, val) in enumerate(rows):
        y = 106 + i * 40
        b.append(f'<text x="40" y="{y}" class="mono" font-size="15" fill="{TXT}" letter-spacing="2">'
                 f'<tspan fill="{C}">▸</tspan> {label}</text>'
                 f'<text x="560" y="{y + 2}" text-anchor="end" class="disp" font-size="24" fill="{Y}">{fmt(val)}</text>'
                 f'<line x1="40" y1="{y + 14}" x2="560" y2="{y + 14}" stroke="{Y}" stroke-opacity=".12" stroke-dasharray="4 6"/>')

    # languages
    total = sum(s["langs"].values()) or 1
    top = sorted(s["langs"].items(), key=lambda kv: -kv[1])[:6]
    b.append(f'<text x="640" y="70" class="mono" font-size="12" fill="{DIM}" letter-spacing="3">CODE IMPLANTS // TOP LANGUAGES</text>')
    x = 640.0
    for i, (name, size) in enumerate(top):
        w = 520 * size / total
        b.append(f'<rect x="{x:.1f}" y="88" width="{max(w - 2, 1):.1f}" height="16" fill="{LANG_COLORS[i]}"/>')
        x += w
    if x < 1160:
        b.append(f'<rect x="{x:.1f}" y="88" width="{1160 - x:.1f}" height="16" fill="#2C303B"/>')
    for i, (name, size) in enumerate(top):
        cx, cy = 640 + (i % 2) * 270, 142 + (i // 2) * 40
        b.append(f'<rect x="{cx}" y="{cy - 12}" width="12" height="12" fill="{LANG_COLORS[i]}"/>'
                 f'<text x="{cx + 22}" y="{cy}" class="mono" font-size="15" fill="{TXT}">{esc(name)}</text>'
                 f'<text x="{cx + 250}" y="{cy}" text-anchor="end" class="mono" font-size="15" fill="{DIM}">{100 * size / total:.1f}%</text>')
    if not top:
        b.append(f'<text x="640" y="142" class="mono" font-size="15" fill="{DIM}">NO PUBLIC CODE DETECTED</text>')

    # streak strip
    cur, longest = streaks(s["days"])
    b.append(f'<line x1="0" y1="352" x2="1200" y2="352" stroke="{Y}" stroke-opacity=".3"/>')
    for i, (label, val, col, live) in enumerate([("CURRENT STREAK", f"{cur} DAYS", R, True),
                                                 ("LONGEST STREAK // 12 MO", f"{longest} DAYS", Y, False),
                                                 ("CONTRIBUTIONS // 12 MO", fmt(s["total"]), C, False)]):
        cx = 200 + i * 400
        anim = ('<animate attributeName="fill-opacity" values="1;.35;1" dur="1.6s" repeatCount="indefinite"/>' if live else "")
        b.append(f'<text x="{cx}" y="400" text-anchor="middle" class="disp" font-size="34" fill="{col}">{val}{anim}</text>'
                 f'<text x="{cx}" y="426" text-anchor="middle" class="mono" font-size="12" fill="{DIM}" letter-spacing="3">{label}</text>')
        if i:
            b.append(f'<line x1="{cx - 200}" y1="370" x2="{cx - 200}" y2="430" stroke="{Y}" stroke-opacity=".25"/>')
    aria = (f"GitHub stats: {s['repos']} public repos, {s['stars']} stars, {s['commits']} commits in 12 months, "
            f"{s['prs']} PRs, {s['issues']} issues, {s['followers']} followers. Current streak {cur} days, longest {longest} days.")
    return panel(460, "NETRUNNER DIAGNOSTICS", f'SYNCED: <tspan fill="{C}">{synced}</tspan>', "\n".join(b), aria)


def activity(s):
    days = s["days"][-30:]
    x0, x1, y0, y1 = 70, 1160, 80, 250
    mx = max([c for _, c in days] + [1])
    step = (x1 - x0) / max(len(days) - 1, 1)
    pts = [(x0 + i * step, y1 - (y1 - y0) * c / mx) for i, (_, c) in enumerate(days)]
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    area = f"{x0},{y1} {line} {x1},{y1}"
    b = [f'<defs><linearGradient id="area" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{Y}" stop-opacity=".35"/>'
         f'<stop offset="1" stop-color="{Y}" stop-opacity="0"/></linearGradient></defs>']
    for k in range(5):  # horizontal guides + y labels
        gy = y1 - (y1 - y0) * k / 4
        b.append(f'<line x1="{x0}" y1="{gy:.1f}" x2="{x1}" y2="{gy:.1f}" stroke="{C}" stroke-opacity=".12"/>'
                 f'<text x="{x0 - 12}" y="{gy + 4:.1f}" text-anchor="end" class="mono" font-size="11" fill="{DIM}">{round(mx * k / 4)}</text>')
    for i in range(0, len(days), 5):
        b.append(f'<text x="{pts[i][0]:.1f}" y="{y1 + 24}" text-anchor="middle" class="mono" font-size="11" fill="{DIM}">{days[i][0][5:]}</text>')
    b.append(f'<polygon points="{area}" fill="url(#area)"/>')
    b.append(f'<polyline points="{line}" fill="none" stroke="{Y}" stroke-width="3" stroke-linejoin="round" pathLength="1" stroke-dasharray="1">'
             f'<animate attributeName="stroke-dashoffset" values="1;0" dur="2.2s" fill="freeze"/></polyline>')
    for (x, y), (_, c) in zip(pts, days):
        if c:
            b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="{R}"/>')
    lx, ly = pts[-1]
    b.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="6" fill="none" stroke="{C}" stroke-width="2">'
             f'<animate attributeName="r" values="4;12;4" dur="1.6s" repeatCount="indefinite"/>'
             f'<animate attributeName="stroke-opacity" values="1;0;1" dur="1.6s" repeatCount="indefinite"/></circle>')
    total30 = sum(c for _, c in days)
    return panel(300, "NEURAL ACTIVITY LOG", f'LAST 30 DAYS: <tspan fill="{C}">{total30}</tspan> CONTRIBUTIONS',
                 "\n".join(b), f"Contribution activity graph, {total30} contributions in the last 30 days")


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "dist"
    if "--sample" in sys.argv:
        s = sample()
    else:
        token, login = os.environ.get("GITHUB_TOKEN"), os.environ.get("GH_USER", "ali-718")
        if not token:
            raise SystemExit("GITHUB_TOKEN is not set")
        s = fetch(token, login)
    os.makedirs(out, exist_ok=True)
    for name, svg in [("diagnostics.svg", diagnostics(s)), ("activity.svg", activity(s))]:
        with open(os.path.join(out, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(svg)
    print("wrote", out, {k: v for k, v in s.items() if k not in ("days", "langs")})


if __name__ == "__main__":
    main()
