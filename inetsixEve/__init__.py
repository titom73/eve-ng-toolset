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
from datetime import datetime
from loguru import logger


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

    def _query(self, uri):
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'DNT': '1',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'Referer': '{}://{}/legacy/'.format(self._proto, self._server),
            'Accept-Language': 'en-US,en;q=0.9',
        }
        now = datetime.now()
        time_stamp = int(datetime.timestamp(now) * 1000)
        full_url = self._proto + '://' + self._server + \
            '/api/' + uri + '?_={}'.format(time_stamp)
        logger.debug('Request url: {}'.format(full_url))
        try:
            response = requests.get(url=full_url, headers=headers, cookies=self._cookies, verify=self._ssl_check)
            response_json = response.json()
            return response_json
        except:
            logger.error('Error requesting API data')
            return None

    def get_project_nodes(self, project_path):
        eve_lab = 'labs/{}.unl/nodes'.format(project_path)
        return self._query(uri=eve_lab)

    def get_api_data(self, uri):
        return self._query(uri=uri)
