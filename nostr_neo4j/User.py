# nostr_neo4j/User.py

class User:
    """
    Class to represent a user in the Neo4j database.

    Attributes:
    - pubkey: str, public key of the user

    Methods:
    - __init__(pubkey: str) -> User: initialize the User object
    - __repr__() -> str: return the representation of the User object
    - from_dict(data: dict) -> User: create a User object from a dictionary
    - to_dict() -> dict: return the User object as a dictionary
    """

    def __init__(self, pubkey: str) -> "User":
        """
        Initialize the User object.

        Parameters:
        - pubkey: str, public key of the user

        Example:
        >>> user = User("0x123")
        >>> user
        User(pubkey="0x123")

        Returns:
        - User, user object

        Raises:
        - TypeError: if pubkey is not a str
        """
        if not isinstance(pubkey, str):
            raise TypeError(f"pubkey must be a str, not {type(pubkey)}")
        self.pubkey = pubkey
        return

    def __repr__(self) -> str:
        """
        Return the representation of the User object.

        Parameters:
        - None

        Example:
        >>> user = User("0x123")
        >>> user
        User(pubkey="0x123")

        Returns:
        - str, representation of the User object

        Raises:
        - None
        """
        return f"User(pubkey={self.pubkey})"
    
    @staticmethod
    def from_dict(data: dict) -> "User":
        """
        Create a User object from a dictionary.

        Parameters:
        - data: dict, dictionary containing the user data

        Example:
        >>> data = {"pubkey": "0x123"}
        >>> user = User.from_dict(data)
        >>> user
        User(pubkey="0x123")

        Returns:
        - User, user object

        Raises:
        - TypeError: if data is not a dict
        - ValueError: if data does not have the keys: pubkey
        """
        if not isinstance(data, dict):
            raise TypeError(f"data must be a dict, not {type(data)}")
        if set(data.keys()) != {"pubkey"}:
            raise ValueError(f"data must have the keys: pubkey")
        return User(data["pubkey"])
    
    def to_dict(self) -> dict:
        """
        Return the User object as a dictionary.

        Parameters:
        - None

        Example:
        >>> user = User("0x123")
        >>> user.to_dict()
        {"pubkey": "0x123"}

        Returns:
        - dict, dictionary representation of the User object

        Raises:
        - None
        """
        return {"pubkey": self.pubkey}