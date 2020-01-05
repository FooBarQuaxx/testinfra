# coding: utf-8
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

from __future__ import unicode_literals

import sys
from testinfra.host import get_host
from testinfra.host import get_hosts

__all__ = ['get_host', 'get_hosts']

if sys.version_info[0] == 2:
    import warnings

    class TestinfraDeprecationWarning(Warning):
        pass

    warnings.simplefilter("default", TestinfraDeprecationWarning)
    warnings.warn(
        'DEPRECATION: testinfra python2 support is unmaintained, please '
        'upgrade to python3', category=TestinfraDeprecationWarning,
        stacklevel=1)
