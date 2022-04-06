import requests
import json

response = requests.get("https://api.github.com/users/krazymanj/repos")
data = json.loads(response.text)

html = "<p width=100% align=center>"
for node in data:
    if node["name"] != "KrazyManJ":
        html += f"""
  <a href={node["html_url"]}><img src="https://github-readme-stats.vercel.app/api/pin/?username=krazymanj&repo={node["name"]}&bg_color=07090d&hide_border=true&border_radius=10&title_color=70D7FF&text_color=8b949e"></a>"""
html += "\n</p>"
print(html)
