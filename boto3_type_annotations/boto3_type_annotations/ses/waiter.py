from typing import List
from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class IdentityExists(Waiter):
    def wait(self, Identities: List, WaiterConfig: Dict = None) -> NoReturn:
        pass
