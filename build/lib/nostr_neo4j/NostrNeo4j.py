from neo4j import GraphDatabase
import json
import UserMetadata
import User
import Event

class NostrNeo4j:
    
    def __init__(self, uri: str, user: str, password: str) -> None:
        """
        Initialize the NostrNeo4j object.

        Parameters:
        - uri: str, URI of the Neo4j database
        - user: str, user of the Neo4j database
        - password: str, password of the Neo4j database

        Example:
        >>> uri = "bolt://localhost:7687"
        >>> user = "neo4j"
        >>> password = "password"
        >>> db = NostrNeo4j(uri, user, password)

        Returns:
        - db: NostrNeo4j, NostrNeo4j object
        """
        assert isinstance(uri, str), f"uri must be a string, not {type(uri)}"
        assert isinstance(user, str), f"user must be a string, not {type(user)}"
        assert isinstance(password, str), f"password must be a string, not {type(password)}"
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self) -> None:
        """
        Close the connection to the Neo4j database.

        Example:
        >>> db.close()
        """
        self.driver.close()    
    
    def set_user(self, user: User) -> None:
        """
        Set the user in the Neo4j database.

        Parameters:
        - user: User, user object

        Example:
        >>> user = User("0x123")
        >>> db.set_user(user)
        """
        assert isinstance(user, User), f"user must be a User object, not {type(user)}"
        with self.driver.session() as session:
            session.run(
                "MERGE (u:User {pubkey: $pubkey}) "
                "SET u += $props",
                pubkey=user.pubkey,
                props=user.to_dict()
            )

    def get_user(self, pubkey: str) -> User:
        """
        Get the user from the Neo4j database.

        Parameters:
        - pubkey: str, public key of the user

        Returns:
        - user: User, user object

        Example:
        >>> pubkey = "0x123"
        >>> db.get_user(pubkey)
        >>> User(
        """
        assert isinstance(pubkey, str), f"pubkey must be a string, not {type(pubkey)}"
        with self.driver.session() as session:
            result = session.run(
                "MATCH (u:User {pubkey: $pubkey}) "
                "RETURN u",
                pubkey=pubkey
            )
            record = result.single()
        if record is None:
            return None
        return User.from_dict(record["u"])
    
    def add_event_kind_0(self, event: Event) -> None:
        assert isinstance(event, Event), f"event must be an Event object, not {type(event)}"
        assert event.kind == 0, f"event kind must be 0, not {event.kind}"
        user = self.get_user(event.pubkey)
        new_metadata = UserMetadata(event.created_at, json.loads(event.content))
        if user is None:
            user = User(event.pubkey)
        if user.first_event_timestamp is None or user.first_event_timestamp > new_metadata.timestamp:
            user.first_event_timestamp = new_metadata.timestamp
        if user.metadata is None or user.metadata.timestamp < new_metadata.timestamp:
            user.metadata = new_metadata
        self.set_user(user)

        