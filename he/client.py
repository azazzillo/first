class Client:
    """Clients for github"""

    def __init__(
        self,
        name: str,
        login: str,
        password: str,
        balance: int
    ):
        self.name = name
        self.login = login
        self.password = password
        self.balance = balance