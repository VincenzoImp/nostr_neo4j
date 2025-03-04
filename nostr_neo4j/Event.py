# nostr_neo4j/Event.py

from typing import List

class Event:

    def __init__(self, id: str, created_at: int, kind: int, pubkey: str, sig: str, content: str, tags: List[List]) -> None:
        """
        Initialize an Event object.

        Parameters:
        - id: str, id of the event
        - created_at: int, timestamp of the event
        - kind: int, kind of the event
        - pubkey: str, public key of the event
        - sig: str, signature of the event
        - content: str, content of the event
        - tags: List[List], tags of the event

        Example:
        >>> id = "0x123"
        >>> created_at = 1612137600
        >>> kind = 0
        >>> pubkey = "0x123"
        >>> sig = "0x123"
        >>> content = "content"
        >>> tags = [["tag1", "tag2"]]
        >>> event = Event(id, created_at, kind, pubkey, sig, content, tags)

        Returns:
        - event: Event, Event object
        """
        assert isinstance(id, str), f"id must be a str, not {type(id)}"
        assert isinstance(created_at, int), f"created_at must be a int, not {type(created_at)}"
        assert isinstance(kind, int), f"kind must be a int, not {type(kind)}"
        assert isinstance(pubkey, str), f"pubkey must be a str, not {type(pubkey)}"
        assert isinstance(sig, str), f"sig must be a str, not {type(sig)}"
        assert isinstance(content, str), f"content must be a str, not {type(content)}"
        assert isinstance(tags, list), f"tags must be a list, not {type(tags)}"
        for tag in tags:
            assert isinstance(tag, list), f"tags must be a list of lists, not {type(tag)}"
        self.id = id
        self.created_at = created_at
        self.kind = kind
        self.pubkey = pubkey
        self.sig = sig
        self.content = content
        self.tags = tags

    def __repr__(self) -> str:
        """
        Return a string representation of the Event object.

        Example:
        >>> id = "0x123"
        >>> created_at = 1612137600
        >>> kind = 0
        >>> pubkey = "0x123"
        >>> sig = "0x123"
        >>> content = "content"
        >>> tags = [["tag1", "tag2"]]
        >>> event = Event(id, created_at, kind, pubkey, sig, content, tags)
        >>> event
        Event(id=0x123, created_at=1612137600, kind=0, pubkey=0x123, sig=0x123, content=content, tags=[["tag1", "tag2"]])

        Returns:
        - str, string representation of the Event object
        """
        return f"Event(id={self.id}, created_at={self.created_at}, kind={self.kind}, pubkey={self.pubkey}, sig={self.sig}, content={self.content}, tags={self.tags})"

    @staticmethod
    def from_dict(data: dict) -> "Event":
        """
        Create an Event object from a dictionary.
        
        Parameters:
        - data: dict, dictionary with the keys "id", "created_at", "kind", "pubkey", "sig", "content", "tags"

        Example:
        >>> data = {"id": "0x123", "created_at": 1612137600, "kind": 0, "pubkey": "0x123", "sig": "0x123", "content": "content", "tags": [["tag1", "tag2"]]}
        >>> event = Event.from_dict(data)
        >>> event
        Event(id=0x123, created_at=1612137600, kind=0, pubkey=0x123, sig=0x123, content=content, tags=[["tag1", "tag2"]])

        Returns:
        - event: Event, Event object
        """
        return Event(data["id"], data["created_at"], data["kind"], data["pubkey"], data["sig"], data["content"], data["tags"])
    
    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the Event object.

        Example:
        >>> id = "0x123"
        >>> created_at = 1612137600
        >>> kind = 0
        >>> pubkey = "0x123"
        >>> sig = "0x123"
        >>> content = "content"
        >>> tags = [["tag1", "tag2"]]
        >>> event = Event(id, created_at, kind, pubkey, sig, content, tags)
        >>> event.to_dict()
        {"id": "0x123", "created_at": 1612137600, "kind": 0, "pubkey": "0x123", "sig": "0x123", "content": "content", "tags": [["tag1", "tag2"]]}

        Returns:
        - dict, dictionary representation of the Event object
        """
        return {
            "id": self.id,
            "created_at": self.created_at,
            "kind": self.kind,
            "pubkey": self.pubkey,
            "sig": self.sig,
            "content": self.content,
            "tags": self.tags
        }