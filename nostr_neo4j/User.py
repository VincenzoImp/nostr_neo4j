# nostr_neo4j/User.py

class User:
    """
    Class to represent a user in the Neo4j database.

    Attributes:
    - pubkey: str, public key of the user

    Methods:
    - __init__: initialize the User object
    - __repr__: return the representation of the User object
    """

    def __init__(self, pubkey: str) -> None:
        """
        Initialize the User object.

        Parameters:
        - pubkey: str, public key of the user

        Example:
        >>> user = User("0x123")
        >>> user
        User(pubkey="0x123")

        Returns:
        - user: User, user object
        """
        assert isinstance(pubkey, str), f"pubkey must be a string, not {type(pubkey)}"
        self.pubkey = pubkey

    def __repr__(self) -> str:
        """
        Return the representation of the User object.

        Example:
        >>> user = User("0x123")
        >>> user
        User(pubkey="0x123")

        Returns:
        - str, representation of the User object
        """
        return f"User(pubkey={self.pubkey})"
    
    # def __eq__(self, other: 'User') -> bool:
    #     """
    #     Check if two User objects are equal.

    #     Parameters:
    #     - other: User, other User object to compare

    #     Example:
    #     >>> user1 = User("0x123")
    #     >>> user2 = User("0x123")
    #     >>> user1 == user2
    #     True

    #     Returns:
    #     - bool, True if the User objects are equal, False otherwise
    #     """
    #     assert isinstance(other, User), f"other must be a User object, not {type(other)}"
    #     return self.pubkey == other.pubkey
    
    # def __ne__(self, other: 'User') -> bool:
    #     """
    #     Check if two User objects are not equal.

    #     Parameters:
    #     - other: User, other User object to compare

    #     Example:
    #     >>> user1 = User("0x123")
    #     >>> user2 = User("0x456")
    #     >>> user1 != user2
    #     True

    #     Returns:
    #     - bool, True if the User objects are not equal, False otherwise
    #     """
    #     assert isinstance(other, User), f"other must be a User object, not {type(other)}"
    #     return self.pubkey != other.pubkey
    
    @staticmethod
    def from_dict(data: dict) -> 'User':
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
        - user: User, user object
        """
        assert isinstance(data, dict), f"data must be a dict, not {type(data)}"
        return User(data["pubkey"])
    
    def to_dict(self) -> dict:
        """
        Return the User object as a dictionary.

        Example:
        >>> user = User("0x123")
        >>> user.to_dict()
        {"pubkey": "0x123"}

        Returns:
        - dict, dictionary representation of the User object
        """
        return {"pubkey": self.pubkey}