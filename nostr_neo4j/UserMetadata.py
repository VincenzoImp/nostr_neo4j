# nostr_neo4j/UserMetadata.py

class UserMetadata:
    """
    Class to represent the metadata of a user in the Neo4j database.

    Attributes:
    - timestamp: int, timestamp of the metadata
    - data: dict, metadata of the user

    Methods:
    - __init__: initialize the UserMetadata object
    - to_dict: return a dictionary representation of the metadata
    - from_dict: return a UserMetadata object from a dictionary representation
    - __repr__: return the representation of the UserMetadata object
    """

    def __init__(self, timestamp: int = None, data: dict = None) -> None:
        """
        Initialize the UserMetadata object.

        Parameters:
        - timestamp: int, timestamp of the metadata
        - data: dict, metadata of the user

        Example:
        >>> metadata = UserMetadata(1612137600, {"name": "Alice"})
        """
        if timestamp is not None:
            assert isinstance(timestamp, int), f"timestamp must be an integer, not {type(timestamp)}"
        if data is not None:
            assert isinstance(data, dict), f"data must be a dictionary, not {type(data)}"
            for key in data.keys():
                assert isinstance(key, str), "Keys in data must be strings"
        self.timestamp = timestamp
        self.data = data

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the metadata.

        Example:
        >>> metadata = UserMetadata(1612137600, {"name": "Alice"})
        >>> metadata.to_dict()
        {"timestamp": 1612137600, "data": {"name": "Alice"}}

        Returns:
        - metadata: dict, dictionary representation of the metadata
        """
        return {"timestamp": self.timestamp, "data": self.data}

    @staticmethod
    def from_dict(metadata: dict) -> "UserMetadata":
        """
        Return a UserMetadata object from a dictionary representation.

        Parameters:
        - metadata: dict, dictionary representation of the metadata

        Example:
        >>> metadata = UserMetadata.from_dict({"timestamp": 1612137600, "data": {"name": "Alice"}})
        >>> metadata.timestamp
        1612137600
        >>> metadata.data
        {"name": "Alice"}

        Returns:
        - metadata: UserMetadata, UserMetadata object from a dictionary representation
        """
        assert "timestamp" in metadata, "Timestamp must be in the metadata"
        assert "data" in metadata, "Data must be in the metadata"
        return UserMetadata(metadata["timestamp"], metadata["data"])

    def __repr__(self) -> str:
        """
        Return the representation of the UserMetadata object.

        Example:
        >>> metadata = UserMetadata(1612137600, {"name": "Alice"})
        >>> metadata
        UserMetadata(timestamp=1612137600, data={"name": "Alice"})

        Returns:
        - representation: str, representation of the UserMetadata object
        """
        return f"UserMetadata(timestamp={self.timestamp}, data={self.data})"