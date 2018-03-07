# Copyright (c) 2018 Yellow Pages Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
config

Permit to manage global configurations
"""

import os

class Config:
    default_env = "local"
    os_env = "BRANCH_ENV"
    
    env = {
        "local" : {
            "mongo" : {
                "uri": "mongodb://localhost:27017",
                "db": "cloud-drone-counter-local",
                "timeoutms": 5000
                }
            }
        }
    
    def __init__(self):
        config_env = os.environ.get(self.os_env, self.default_env)
        print("Config: environment: %s" % config_env)
        if config_env not in self.env.keys():
            raise Exception("Environment %s=%s not set in config.py" % (self.os_env, config_env))
        
        self.active_env = config_env
    
    def getconfig(self):
        return self.env[self.active_env]
    
    def getgeneric(self, section, key, default):
        if key is not None:
            return self.getconfig()[section].get(key, default)
        
        return self.getconfig()[section]
    
    def getmongo(self, key=None, default=None):
        return self.getgeneric("mongo", key, default)

