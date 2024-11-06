from urllib import request
from project import Project
import toml
#import json # debug


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed = toml.loads(content)
        root = parsed["tool"]["poetry"]
        #print(json.dumps(root, indent=2)) # debug
        return Project(
            root["name"],
            root["description"],
            root["license"],
            root["authors"],
            [name for name in root["dependencies"]],
            [name for name in root["group"]["dev"]["dependencies"]]
        )
