from log import Log
import enum


class RiskLevels(enum.Enum):
    low = 0
    medium = 1
    high = 2


# A class to verify users by risk-based authentication
class Risk:
    def __init__(self, username: str, password: str, client: str):
        self.username = username
        self.password = password
        self.user_ip = client
        self.isValid: bool
        self.users_risk_level: RiskLevels
        self.internal_ip = '10.97.2.0/24'

    # Verify a incoming users risk level, and returns a risk level.
    def verify_risk_level(self):

        if self.ip_is_known() and self.user_is_known():
            return RiskLevels.low
        elif self.user_is_known() and not self.ip_is_known():
            return RiskLevels.medium

        elif self.user_is_known(self.username, self.password) is not True and not self.:
            return True
        else:
            return RiskLevels.high

    def user_is_known(self):
        return True

    def ip_is_known(self):
        return True

    def ip_is_internal(self):
        if self.user_ip is self.internal_ip:
            return True
        else:
            return False