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

"""Counter

API for counter statistics
"""

from flask import request
from flask_restplus import Namespace, Resource, fields
import buildcounter.settings as settings

api = Namespace('', description='Deployment counter to provide some statistics')

model_history = api.model('History', {
    'owner': fields.String(required=True, description='The project', example='CLOUD'),
    'name': fields.String(required=True, description='The repo name', example='build-counter'),
    'branch': fields.String(required=True, description='The branch', example='master'),
    'author_email': fields.String(required=True, description='The author email', example='cloud@yp.ca'),
    'build_created': fields.String(required=True, description='The build created date', example='1514562027'),
    'commit': fields.String(required=True, description='The commit', example='1503ea828528d691526e7bd5b36cf30bcf8f3c3f'),
    'build_number': fields.String(required=True, description='The build number', example='10'),
    'build_image': fields.String(required=False, description='The build image', example='build system used'),
})

@api.route('/history')
class BuildHistory(Resource):
    
    @api.doc('history')
    @api.response(200, 'Deployment successfully added to history.')
    @api.expect(model_history, validate=True)
    def post(self):
        """Store the new deployment in history"""

        data = request.json

        # Mandatory
        owner = data["owner"]
        name = data["name"]
        branch = data["branch"]
        author_email = data["author_email"]
        build_created = data["build_created"]
        commit = data["commit"]
        build_number = data["build_number"]

        # Optional
        build_image = data.get("build_image", None)
        
        # Add to history
        result = settings.storage.add_history(owner, name, branch, author_email, build_created, commit, build_number, build_image)
        
        if not result:
            api.abort(400, "Failed to add the deployment into history.")
        
        return {"result" : True}, 200

@api.route('/counters/total')
class BuildCounterTotal(Resource):
    
    @api.doc('count_all')
    def get(self):
        """Count all deployments"""
        
        result = settings.storage.count_all_deployments()
        
        if result == -1:
            api.abort(400, 'Failed to count all deployments.')
        
        return {"counter" : result}, 200
    
@api.route('/counters/for/<owner>/<name>/<path:branch>')
@api.param('owner', 'The project')
@api.param('name', 'The repo name')
@api.param('branch', 'The branch')
class BuildCounterFor(Resource):
    
    @api.doc('count_for')
    def get(self, owner, name, branch):
        """Count deployments given its repo and branch"""

        result = settings.storage.count_deployments_for(owner, name, branch)
        
        if result == -1:
            api.abort(400, 'Failed to count deployments for %s/%s.' % (owner, name))
        
        return {"counter" : result}, 200
