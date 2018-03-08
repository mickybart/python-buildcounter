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

"""Settings module

This is a special module that permit to share some common variables between all other modules
that need it. Specially those for flask-restplus
"""

from .storage import Storage

config = None
storage = None

def init(_config):
    """Settings Init
    
    Args:
        _config (Config): Configuration ot the build counter
    """
    global config
    global storage
    config = _config
    storage = Storage(config.mongo["uri"],
                      config.mongo["timeoutms"],
                      config.mongo["db"],
                      config.mongo["collection"])
