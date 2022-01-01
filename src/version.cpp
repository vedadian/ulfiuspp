/*
ulfiuspp, A C++17 wrapper for Ulfius framework

Copyright 2022 by Behrooz Vedadian
 
NMTEngine is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License   
along with ulfiuspp. If not, see <http://www.gnu.org/licenses/>.
*/
// @author Behrooz Vedadian <vedadian@gmail.com>

#include <string_view>

constexpr std::string_view VERSION = "0.1.0.0";

extern "C" {

const char* getVersion() {
    return VERSION.data();
}

}