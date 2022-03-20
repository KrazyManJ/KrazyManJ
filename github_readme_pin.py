import pyperclip
from urllib import parse

copied = False
link = ""
while not copied:

    projectname = input("Name of github project: ")
    link = f"[![{projectname}](https://github-readme-stats.vercel.app/api/pin/?" \
           f"username=krazymanj" \
           f"&repo={parse.quote(projectname, safe='')}" \
           f"&bg_color=07090d" \
           f"&hide_border=true" \
           f"&border_radius=10" \
           f"&title_color=35def1" \
           f"&text_color=8b949e" \
           f")](https://github.com/KrazyManJ/{parse.quote(projectname, safe='')})"

    if len(projectname) > 0: copied = True
    else: print("You cannot leave input empty!")

print("Link was successfully copied into your clipboard!")
pyperclip.copy(link)
