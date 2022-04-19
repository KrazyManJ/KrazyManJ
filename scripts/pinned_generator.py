import requests
import json

class RepoLink:
    def __init__(self):
        self.__params = [] 
    
    def add_attr(self, name:str, value:str) -> "RepoLink":
        self.__params.append(f"{name}={value}")
        return self
    
    def build(self,reponame) -> str:
        args = self.__params.copy()
        args.insert(0,f"repo={reponame}")
        args.insert(0,f"username=krazymanj")
        return f'https://github-readme-stats.vercel.app/api/pin/?{"&".join(args)}'
        

link = RepoLink()\
    .add_attr("bg_color","07090D")\
    .add_attr("hide_border","true")\
    .add_attr("border_radius","10")\
    .add_attr("title_color","70D7FF")\
    .add_attr("text_color","8B949E")

response = requests.get("https://api.github.com/users/krazymanj/repos")
data = json.loads(response.text)

html = "<p width=100% align=center>"
for node in data:
    if node["name"] != "KrazyManJ":
        html += f"""
  <a href={node["html_url"]}><img src="{link.build(node["name"])}"></a>"""
html += "\n</p>"
print(html)
