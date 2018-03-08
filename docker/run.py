from buildcounter.config import Config
from buildcounter.app import App

# secret.json file example :
#
# {
#     "mongo" : {
#         "uri": "",
#         "db": "",
#         "timeoutms": 5000,
#         "collection" : ""
#     }
# }
#
secrets = Config.load_json("secret.json")

config = Config(secrets["mongo"])

# OR
#
# Custom config ?
#
# class CustomConfig(Config):
#         pass
# 
# config = CustomConfig(secrets["mongo"])

App(config).run()
