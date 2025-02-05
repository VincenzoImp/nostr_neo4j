class User:
    """
    Class to represent a user in the Neo4j database.

    Attributes:
    - pubkey: str, public key of the user
    - metadata: User.Metadata, metadata of the user
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

    def __init__(self, pubkey: str, metadata: "User.Metadata", timestamp_firstEvent: int) -> None:
        """
        Initialize the User object.

        Parameters:
        - pubkey: str, public key of the user
        - metadata: User.Metadata, metadata of the user
        - timestamp_firstEvent: int, timestamp of the first event of the user

        Example:
        >>> user = User("0x123", User.Metadata(1612137600, {"name": "Alice"}), 1612137600)
        >>> user
        User(pubkey="0x123", metadata=User.Metadata(timestamp=1612137600, data={"name": "Alice"}), timestamp_firstEvent=1612137600)

        Returns:
        - user: User, user object
        """
        assert isinstance(pubkey, str), f"pubkey must be a string, not {type(pubkey)}"
        assert isinstance(metadata, User.Metadata), f"metadata must be a User.Metadata object, not {type(metadata)}"
        assert isinstance(timestamp_firstEvent, int), f"timestamp_firstEvent must be an integer, not {type(timestamp_firstEvent)}"
        self.pubkey = pubkey
        self.metadata = metadata
        self.timestamp_firstEvent = timestamp_firstEvent

    def __repr__(self) -> str:
        """
        Return the representation of the User object.

        Example:
        >>> user = User("0x123", User.Metadata(1612137600, {"name": "Alice"}), 1612137600)
        >>> user
        User(pubkey="0x123", metadata=User.Metadata(timestamp=1612137600, data={"name": "Alice"}), timestamp_firstEvent=1612137600)

        Returns:
        - str, representation of the User object
        """
        return f"User(pubkey={self.pubkey!r}, metadata={self.metadata!r}, timestamp_firstEvent={self.timestamp_firstEvent!r})"
    
    class Metadata:
        """
        Class to represent the metadata of a user in the Neo4j database.

        Attributes:
        - timestamp: int, timestamp of the metadata
        - data: dict, metadata of the user

        Methods:
        - __init__: initialize the User.Metadata object
        - to_dict: return a dictionary representation of the metadata
        - from_dict: return a User.Metadata object from a dictionary representation
        - __repr__: return the representation of the User.Metadata object
        """

        def __init__(self) -> None:
            """
            Initialize the User.Metadata object.

            Parameters:
            - timestamp: int, timestamp of the metadata
            - data: dict, metadata of the user

            Example:
            >>> metadata = User.Metadata()
            >>> metadata
            User.Metadata(timestamp=None, data=None)
            """
            self.timestamp = None
            self.data = None
            
        def __init__(self, timestamp: int, data: dict) -> None:
            """
            Initialize the User.Metadata object.

            Parameters:
            - timestamp: int, timestamp of the metadata
            - data: dict, metadata of the user

            Example:
            >>> metadata = User.Metadata(1612137600, {"name": "Alice"})
            """
            assert isinstance(timestamp, int), f"timestamp must be an integer, not {type(timestamp)}"
            assert isinstance(data, dict), f"data must be a dictionary, not {type(data)}"
            for key in data:
                assert isinstance(key, str), "Keys in data must be strings"
            self.timestamp = timestamp
            self.data = data

        def to_dict(self) -> dict:
            """
            Return a dictionary representation of the metadata.

            Example:
            >>> metadata = User.Metadata(1612137600, {"name": "Alice"})
            >>> metadata.to_dict()
            {"timestamp": 1612137600, "data": {"name": "Alice"}}

            Returns:
            - metadata: dict, dictionary representation of the metadata
            """
            return {"timestamp": self.timestamp, "data": self.data}

        @staticmethod
        def from_dict(metadata: dict) -> "User.Metadata":
            """
            Return a User.Metadata object from a dictionary representation.

            Parameters:
            - metadata: dict, dictionary representation of the metadata

            Example:
            >>> metadata = User.Metadata.from_dict({"timestamp": 1612137600, "data": {"name": "Alice"}})
            >>> metadata.timestamp
            1612137600
            >>> metadata.data
            {"name": "Alice"}

            Returns:
            - metadata: User.Metadata, User.Metadata object from a dictionary representation
            """
            assert "timestamp" in metadata, "Timestamp must be in the metadata"
            assert "data" in metadata, "Data must be in the metadata"
            return User.Metadata(metadata["timestamp"], metadata["data"])

        def __repr__(self) -> str:
            """
            Return the representation of the User.Metadata object.

            Example:
            >>> metadata = User.Metadata(1612137600, {"name": "Alice"})
            >>> metadata
            User.Metadata(timestamp=1612137600, data={"name": "Alice"})

            Returns:
            - representation: str, representation of the User.Metadata object
            """
            return f"User.Metadata(timestamp={self.timestamp}, data={self.data})"