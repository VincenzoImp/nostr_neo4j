# nostr_neo4j/UserMetadata.py

class UserMetadata:
    """
    Class to represent the metadata of a user in the Neo4j database.

    Attributes:
    - timestamp: int, timestamp of the metadata
    - data: dict, metadata of the user

    Methods:
    - __init__(timestamp: int = None, data: dict = None) -> None: initialize the UserMetadata object
    - __repr__() -> str: return the representation of the UserMetadata object
    - from_dict(metadata: dict) -> UserMetadata: create a UserMetadata object from a dictionary
    - to_dict() -> dict: return the UserMetadata object as a dictionary
    """

    def __init__(self, timestamp: int, data: dict) -> "UserMetadata":
        """
        Initialize the UserMetadata object.

        Parameters:
        - timestamp: int, timestamp of the metadata
        - data: dict, metadata of the user

        Example:
        >>> metadata = UserMetadata(1612137600, {"name": "Alice"})

        Returns:
        - UserMetadata, UserMetadata object

        Raises:
        -
        """
        if not isinstance(timestamp, int):
            raise TypeError(f"timestamp must be an integer, not {type(timestamp)}")
        if not isinstance(data, dict):
            raise TypeError(f"data must be a dictionary, not {type(data)}")
        for key in data.keys():
            if not isinstance(key, str):
                raise TypeError("Keys in data must be strings")
        self.timestamp = timestamp
        self.data = data
        return

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