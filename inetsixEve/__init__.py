#!/usr/bin/python
# coding: utf-8 -*-
#
# Copyright 2021 Arista Networks Thomas Grimonet
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: //www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import absolute_import, division, print_function

import json
import requests
import urllib
from datetime import datetime
from loguru import logger

__version__ = '0.0.2'
__author__ = 'titom73'

@logger.catch
class EveApi():

    EVE_ENDPOINTS = dict()
    EVE_ENDPOINTS['login'] = 'api/auth/login'

    def __init__(self, server, username='admin', password='password', proto='https', ssl_check=False):
        self._user = username
        self._password = password
        self._server = server
        self._proto = proto
        self._ssl_check = ssl_check
        logger.debug('EVE-NG API server set to {} with username {}'.format(self._server, self._user))
        self._cookies = self._login()

    def _login(self):
        data = {"username": self._user, "password": self._password, "html5": "-1"}
        url = self._proto + '://' + self._server + \
            '/' + self.EVE_ENDPOINTS['login']
        login = requests.post(url=url, data=json.dumps(data), verify=self._ssl_check)
        if login.status_code == 200:
            return login.cookies
        else:
            logger.error('Login error to {} with status-code: {}'.format(self._server, login.status_code))
            return None

    def _get(self, uri):
        headers = {'Accept': 'application/json'}
        now = datetime.now()
        time_stamp = int(datetime.timestamp(now) * 1000)
        # full_url = self._proto + '://' + self._server + \
        #     '/api/' + uri + '?_={}'.format(time_stamp)
        full_url = self._proto + '://' + self._server + '/api/' + uri + '?_=' + str(time_stamp)
        logger.debug('GET url: {}'.format(full_url))
        try:
            response = requests.get(url=full_url, headers=headers, cookies=self._cookies, verify=self._ssl_check)
            response_json = response.json()
            return response_json
        except:
            logger.error('Error requesting API data')
            return None

    def _put(self, uri):
        headers = {'Accept': 'application/json'}
        now = datetime.now()
        time_stamp = int(datetime.timestamp(now) * 1000)
        full_url = self._proto + '://' + self._server + \
            '/api/' + uri + '?_=' + str(time_stamp)
        logger.debug('PUT url: {}'.format(full_url))
        try:
            response = requests.put(
                url=full_url, headers=headers, cookies=self._cookies, verify=self._ssl_check)
            response_json = response.json()
            return response_json
        except:
            logger.error('Error requesting API data')
            return None

    def get_project_nodes(self, project_path):
        eve_lab = f'labs/{project_path}.unl/nodes'
        return self._get(uri=eve_lab)

    def get_api_data(self, uri):
        return self._get(uri=uri)

    def lab_action(self, project_path, action, api_type='get'):
        logger.debug('Run {} command for {}'.format(action, project_path))
        project_path = urllib.parse.quote(project_path)
        nodes = self.get_project_nodes(project_path=project_path)
        if action == 'stop':
            action = 'stop/stopmode=1'
        results = dict()
        for node in nodes['data'].keys():
            nodeId = str(nodes['data'][node]['id'])
            eve_lab = f'labs/{project_path}.unl/nodes/{nodeId}/{action}'
            result = None
            if api_type == 'get':
                result = self._get(uri=eve_lab)
            elif api_type == 'put':
                result = self._put(uri=eve_lab)
            results[nodes['data'][node]['name']] = result
        return results

    def lab_topology(self, project_path):
        logger.debug('Run topology command for {}'.format(project_path))
        eve_lab = f'labs/{project_path}.unl/topology'
        return self._query(uri=eve_lab)
