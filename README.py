import re
import urllib.parse

from bs4 import BeautifulSoup


def LinkBuilder(url: str, params: dict[str, str]):
    return url + "?" + urllib.parse.urlencode(params)


LANG_DISPLAY = LinkBuilder("https://github-readme-stats.vercel.app/api/top-langs/", {
    "username": "krazymanj",
    "layout": "compact",
    "bg_color": "0d1117",
    "border_radius": 10,
    "hide_border": "true",
    "card_width": 600,
    "hide_title": "true",
    "title_color": "70D7FF",
    "text_color": "ffffff",
    "langs_count": 20
})
#
STREAK_DISPLAY = LinkBuilder("https://streak-stats.demolab.com", {
    "user": "KrazyManJ",
    "hide_border": "true",
    "border_radius": 10,
    "card_width": 800,
    "background": "EBEBEB00",
    "ring": "2397EB",
    "fire": "06B9EB",
    "dates": "C0C0C0",
    "currStreakNum": "00DCEB",
    "sideNums": "B8B8B8",
    "currStreakLabel": "EBEBEB",
    "sideLabels": "8D8D8D"
})

TROPHIES = LinkBuilder("https://github-profile-trophy.vercel.app/", {
    "username": "krazymanj",
    "no-frame": "true",
    "no-bg": "true",
    "theme": "onestar"
})

FRAMEWORKS_ICONS = LinkBuilder("https://skillicons.dev/icons", {
    "theme": "dark",
    "i": ",".join([
        "react",
        "tailwind",
        "dotnet",
        "qt",
        "fastapi"
    ])
})

TOOLS_ICONS = LinkBuilder("https://skillicons.dev/icons", {
    "theme": "dark",
    "perline": 6,
    "i": ",".join([
        "idea",
        "vscode",
        "figma",
        "git",
        "github",
        "regex",
        "gradle",
        "maven",
        "nodejs",
        "wordpress",
        "discord",
        "linkedin",
    ])
})

def RepoLink(reponame: str):
    return LinkBuilder("https://github-readme-stats.vercel.app/api/pin/", {
        "username": "krazymanj",
        "repo": reponame,
        "bg_color": "07090D",
        "hide_border": True,
        "border_radius": 10,
        "title_color": "70D7FF",
        "text_color": "8B949E",
        "cache_seconds": 7200
    })


def RepoPinList(repos: list[str]):
    def prettify_indent(val, encoding=None, formatter="minimal", indent_width=4):
        return re.compile(r'^(\s*)', re.MULTILINE).sub(r'\1' * indent_width, val)

    content = "<p width=100% align=center>"
    for repo in repos:
        content += f"<a href=https://github.com/KrazyManJ/{repo}><img src={RepoLink(repo)} alt={repo}></a>"
    return prettify_indent(BeautifulSoup(content + "</p>", "html.parser").prettify())


open("README.md", "w", encoding="UTF-8").write(
    f"""
<p align=center>
    <img width=600 src="svgs/title.svg" alt="KrazyManJ" title="KrazyManJ">
</p>

<p align=center>
  Hi, my name is Jaroslav Korčák, known as KrazyManJ on the Internet, I am fullstack developer mainly making code to make his, and others devs lifes easier.
</p>

<h3 align=center>🧱 Frameworks 🧱</h3>

<p align=center>
    <img src="{FRAMEWORKS_ICONS}">
</p>

<h3 align=center>🔨 Tools 🔨</h3>

<p align=center>
    <img src="{TOOLS_ICONS}">
</p>

***

<a href="https://github.com/KrazyManJ">
    <img width="100%" src="{LANG_DISPLAY}" alt="top-languages">
</a>

***

<a href="https://github.com/KrazyManJ">
    <img width="100%" src="{STREAK_DISPLAY}" alt="github-stats">
</a>

***

<p align=center>
    <a href="https://github.com/KrazyManJ">
        <img width="100%" src="{TROPHIES}" alt="trophies">
    </a>
</p>

***

<h2 align=center>👉🏼📌 Main Projects 👉🏼📌</h2>

{RepoPinList(["templatoron", "obsidian-keyshots", "rainmeter-dynamic-island"])}

<h2 align=center>📦 Python Packages 📦</h2>

{RepoPinList(["pyvscode", "pyjetbrains", "uniter", "XMLTK"])}

<h2 align=center>🎓 School Projects 🎓</h2>

{RepoPinList(["final-programming-project", "Curriculum-Challenges", "eshop-sneakeran"])}

<h2 align=center>⏭ Other Projects ⏭</h2>

{RepoPinList(["KrazyEngine" ,"krazymanj.github.io", "fablab-spring-2022"])}

***
""".strip())
