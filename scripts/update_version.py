# ulfiuspp, A C++17 wrapper for Ulfius framework
#
# Copyright 2022 by Behrooz Vedadian
# 
# NMTEngine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License   
# along with ulfiuspp. If not, see <http://www.gnu.org/licenses/>.

import os
import re
import sys
import argparse
import json

arg_parser = argparse.ArgumentParser(os.path.basename(__file__))
arg_parser.add_argument('--major', '-m', action='store_true', default=False)
arg_parser.add_argument('--minor', '-n', action='store_true', default=False)
arg_parser.add_argument('--patch', '-p', action='store_true', default=False)
arg_parser.add_argument('--tweak', '-t', action='store_true', default=False)
arg_parser.add_argument('--pre_release', '-r', type=str, required=False, default=None)

args = arg_parser.parse_args()

src_path = os.path.join(os.path.dirname(__file__), '../src')

with open(os.path.join(src_path, 'version.cpp')) as f:
    version_cpp_contents = f.read()
    version_string_match = re.search('constexpr std::string_view VERSION = "([^-]*?)(-.*?)?";', version_cpp_contents)
if not version_string_match:
    sys.exit(1)
if not version_string_match.group(1):
    sys.exit(1)
major, minor, patch, tweak, *_ = [int(e) for e in version_string_match.group(1).split('.')] + [0, 0, 0, 0, 0]
pre_release = version_string_match.group(2) or ''

if not (args.major or args.minor or args.patch or args.tweak) and args.pre_release is None:
    print('Current version information:')
    print('major:', major)
    print('minor:', minor)
    print('patch:', patch)
    print('tweak:', tweak)
    print('pre_release:', json.dumps(pre_release))
else:
    if args.major:
        major += 1
    if args.minor:
        minor += 1
    if args.patch:
        patch += 1
    if args.tweak:
        tweak += 1
    if args.pre_release is not None:
        if args.pre_release != '':
            pre_release = '-' + args.pre_release
        else:
            pre_release = ''
    version_cpp_contents = re.sub(
        'constexpr std::string_view VERSION = ".*?";',
        f'constexpr std::string_view VERSION = "{major}.{minor}.{patch}.{tweak}{pre_release}";',
        version_cpp_contents
    )
    print(f'Updating version to "{major}.{minor}.{patch}.{tweak}{pre_release}"')
    with open(os.path.join(src_path, 'version.cpp'), 'w') as f:
        f.write(version_cpp_contents)
