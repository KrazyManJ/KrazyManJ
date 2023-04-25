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
    "langs_count": 10
})

TROPHIES = LinkBuilder("https://github-profile-trophy.vercel.app/", {
    "username": "krazymanj",
    "no-frame": "true",
    "no-bg": "true",
    "theme": "onestar"
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
    return prettify_indent(BeautifulSoup(content + "</p>","html.parser").prettify())


open("README.md", "w").write(
f"""
<p align=center>
    <img width=600 src="svgs/title.svg" alt="KrazyManJ" title="KrazyManJ">
</p>

<p align=center >
  Backend developer mainly making code to make his life easier, and also make easier life for other devs. Love to use Python, JS or TS.
</p>

***

<a href="https://github.com/KrazyManJ">
    <img width=1500 src="{LANG_DISPLAY}" alt="top-languages">
</a>

***

<p align=center>
    <a href="https://github.com/KrazyManJ">
        <img width=1500 src="{TROPHIES}" alt="trophies">
    </a>
</p>

***

<h2 align=center>Main Projects</h2>

{RepoPinList(["templatoron", "obsidian-keyshots"])}

<h2 align=center>Python Packages</h2>

{RepoPinList(["pyvscode", "pyjetbrains", "uniter", "XMLTK"])}

***
""".strip())
