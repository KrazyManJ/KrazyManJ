import pyvscode
from scripts.pinned_generator import *

open("README.md","w").write(f"""
<p align=center><img width=600 src="svgs/title.svg" alt="KrazyManJ" title="KrazyManJ"></p>

<p align=center >
  Backend developer mainly making code to make his life easier, and also make easier life for other devs. Love to use Python, JS or TS.
</p>

***

<a href="https://github.com/KrazyManJ">
    <img width=1500 src="https://github-readme-stats.vercel.app/api/top-langs/?username=krazymanj&layout=compact&bg_color=0d1117&border_radius=10&hide_border=true&card_width=600&hide_title=true&title_color=70D7FF&text_color=ffffff&langs_count=10">
</a>

***

<p align=center><img width=200 src="svgs/pinned.svg" alt="Pinned" title="Pinned"></p>

{gen_strict_pinned(["obsidian-keyshots","pyvscode"])}

***
""".strip())

pyvscode.open("README.md")