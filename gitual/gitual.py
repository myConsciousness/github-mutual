"""
Copyright 2021 Kato Shinya.
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
in compliance with the License. You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License
is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied. See the License for the specific language governing permissions and limitations under
the License.
"""

from os import getenv
import re
import subprocess
import requests


class Gitual:

    def __init__(self, user_name: str, per_page=100):
        """The constructor.

        Args:
            user_name (str): The user name of GitHub
            per_page (int, optional): Number of cases to be retrieved. Defaults to 100.
        """

        self.user_name = user_name
        self.per_page = per_page

    def getFollowers():
        return requests.get('https://api.github.com/users/{}/followers?per_page={}'.format(self.user_name, self.per_page)).json()

    def getFollowing():
        return requests.get('https://api.github.com/users/{}/following?per_page={}'.format(self.user_name, self.per_page)).json()


if __name__ == '__main__':
    pass
