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
config module

Permit to manage global configurations
"""

import json

class Config:
    """Configuration for buildcounter and sub-modules
    
    This class can be overriden and so adapted by every compagnies.
        
    Constructor
    
    Args:
        mongo_credentials (dict): Mongo credentials eg: {"uri": "", "db": "", "timeoutms": 5000, "collection": ""}
    """
    
    def __init__(self, mongo_credentials):
        self.mongo = mongo_credentials
        
    def load_json(json_file):
        """Load JSON file
        
        Args:
            json_file (str): filename of a json file
            
        Returns:
            dict: content of the file
        """
        try:
            with open(json_file) as f:
                return json.load(f)
        except FileNotFoundError:
            return None
