import UserMetadata

class User:
    """
    Class to represent a user in the Neo4j database.

    Attributes:
    - pubkey: str, public key of the user
    - metadata: UserMetadata, metadata of the user
    - timestamp_firstEvent: int, timestamp of the first event of the user

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
        User(pubkey="0x123", metadata=None, timestamp_firstEvent=None)

        Returns:    
        - user: User, user object
        """
        assert isinstance(pubkey, str), f"pubkey must be a string, not {type(pubkey)}"
        self.pubkey = pubkey
        self.metadata = None
        self.timestamp_firstEvent = None

    def __init__(self, pubkey: str, metadata: "UserMetadata", timestamp_firstEvent: int) -> None:
        """
        Initialize the User object.

        Parameters:
        - pubkey: str, public key of the user
        - metadata: UserMetadata, metadata of the user
        - timestamp_firstEvent: int, timestamp of the first event of the user

        Example:
        >>> user = User("0x123", UserMetadata(1612137600, {"name": "Alice"}), 1612137600)
        >>> user
        User(pubkey="0x123", metadata=UserMetadata(timestamp=1612137600, data={"name": "Alice"}), timestamp_firstEvent=1612137600)

        Returns:
        - user: User, user object
        """
        assert isinstance(pubkey, str), f"pubkey must be a string, not {type(pubkey)}"
        assert isinstance(metadata, UserMetadata), f"metadata must be a UserMetadata object, not {type(metadata)}"
        assert isinstance(timestamp_firstEvent, int), f"timestamp_firstEvent must be an integer, not {type(timestamp_firstEvent)}"
        self.pubkey = pubkey
        self.metadata = metadata
        self.timestamp_firstEvent = timestamp_firstEvent

    def __repr__(self) -> str:
        """
        Return the representation of the User object.

        Example:
        >>> user = User("0x123", UserMetadata(1612137600, {"name": "Alice"}), 1612137600)
        >>> user
        User(pubkey="0x123", metadata=UserMetadata(timestamp=1612137600, data={"name": "Alice"}), timestamp_firstEvent=1612137600)

        Returns:
        - str, representation of the User object
        """
        return f"User(pubkey={self.pubkey!r}, metadata={self.metadata!r}, timestamp_firstEvent={self.timestamp_firstEvent!r})"