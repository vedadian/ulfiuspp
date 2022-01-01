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

cmake_minimum_required(VERSION 3.12.4)
project(ulfiuspp)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_definitions(-Wfatal-errors)

add_custom_target(update_version python3 ${PROJECT_SOURCE_DIR}/scripts/update_version.py -t)
add_library(${PROJECT_NAME}
    src/version.cpp
)
add_dependencies(${PROJECT_NAME} update_version)