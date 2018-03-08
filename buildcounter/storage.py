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

"""Storage module

Permit to store and query build statistics.
"""

import pymongo

class Storage:
    """Storage MongoDB
    
    Constructor
    
    Args:
        config (config object): Configuration of mongo and mysql
    
    """
    def __init__(self, config):
        self.mongo_client = None
        
        self.config = config

        self.mongo_connect()
            
    def mongo_connect(self):
        """Connect to Mongo"""
        
        # Mongo client will auto-reconnect so there is no needs to call twice this function
        
        # Already connected ?
        if self.mongo_client is not None:
            return
        
        # Connect to Mongo
        try:
            print("connection to mongo...")
            # Init Mongo and create DB and collections objects
            self.mongo_client = pymongo.MongoClient(self.config.getmongo("uri"), serverSelectionTimeoutMS=self.config.getmongo("timeoutms"))
            self.db = self.mongo_client[self.config.getmongo("db")]
            self.history = self.db.get_collection("history")
            
            if len(self.history.index_information()) == 0:
                # collection does not exist
                # create it and create indexes
                self.db.create_collection("history")
                self.history.create_index( [("branch", pymongo.HASHED)] )
                self.history.create_index( [("owner", pymongo.HASHED)] )
                self.history.create_index( [("name", pymongo.HASHED)] )
                self.history.create_index( "timestamp" )

            print("mongo: connected")
        except Exception as e:
            print("mongo: " + str(e))
            self.mongo_client = None
    
    def __del__(self):
        if self.mongo_client is not None:
            self.mongo_client.close()
    
    def add_history(self, owner, name, branch, author_email, build_created, commit, build_number, drone_image):
        """Store into the history the new deployment
        
        Args:
            owner (string): project (eg: CLOUD)
            name (string): repo (eg: curator)
            branch (string): master/develop/release
            author_email (string): author email of the commit
            build_created (int): date
            commit (string): sha of the commit
            build_number (int): build number in cicd
            drone_image (string): drone used to build the deployment

        Returns:
            bool: inserted in the history collection (True) or not inserted in the history collection (False)
        
        """
        try:
            result = self.history.insert_one({"owner": owner,
                                              "name": name,
                                              "branch": branch,
                                              "author_email": author_email,
                                              "build_created": int(build_created),
                                              "commit": commit,
                                              "build_number" : int(build_number),
                                              "drone_image": drone_image})
        except:
            return False
        
        return (result is not None)
    
    def count_all_deployments(self):
        """Get the total number of deployments
        
        Returns:
            int: Number of deployments ([0..INF]) or Error (-1)
        
        """
        
        try:
            result = self.history.count()
        except:
            return -1
        
        return result
    
    def count_deployments_for(self, owner, name, branch):
        """Get the total number of deployments for the repo and branch
        
        Args:
            owner (string): project (eg: CLOUD)
            name (string): repo (eg: curator)
            branch (string): master/develop/release
        
        Returns:
            int: Number of deployments ([0..INF]) or Error (-1)
        
        """
        
        if branch == "all":
            query = {"owner": owner, "name": name}
        elif branch == "release":
            query = {"owner": owner, "name": name, "branch": {"$regex" : branch}}
        else:
            query = {"owner": owner, "name": name, "branch": branch}
        
        try:
            result = self.history.count(query)
        except:
            return -1
        
        return result
    
