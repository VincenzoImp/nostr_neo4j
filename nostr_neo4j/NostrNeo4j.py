# nostr_neo4j/NostrNeo4j.py

from neo4j import GraphDatabase
from .User import User
from .Event import Event

class NostrNeo4j:
    """
    Class to interact with the Neo4j database.

    Attributes:
    - driver: GraphDatabase, Neo4j database driver

    Methods:
    - __init__(uri: str, user: str, password: str) -> None: initialize the NostrNeo4j object
    - close() -> None: close the connection to the Neo4j database
    - __set_user(user: User) -> None: set the user in the Neo4j database
    - get_user(pubkey: str) -> User: get the user from the Neo4j database
    - __add_event_kind_0(event: Event) -> None: add an event of kind 0 to the Neo4j database
    - add_event(event: Event) -> None: add an event to the Neo4j database
    """
    
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
        - None

        Raises:
        - TypeError: if uri is not a str
        - TypeError: if user is not a str
        - TypeError: if password is not a str
        """
        if not isinstance(uri, str):
            raise TypeError(f"uri must be a str, not {type(uri)}")
        if not isinstance(user, str):
            raise TypeError(f"user must be a str, not {type(user)}")
        if not isinstance(password, str):
            raise TypeError(f"password must be a str, not {type(password)}")
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        return

    def close(self) -> None:
        """
        Close the connection to the Neo4j database.

        Example:
        >>> db.close()

        Returns:
        - None

        Raises:
        - None
        """
        self.driver.close()
        return
    
    def __set_user(self, user: User) -> None:
        """
        Set the user in the Neo4j database.

        Parameters:
        - user: User, user object

        Example:
        >>> user = User("0x123")
        >>> db.__set_user(user)

        Returns:
        - None

        Raises:
        - TypeError: if user is not a User object
        """
        if not isinstance(user, User):
            raise TypeError(f"user must be a User object, not {type(user)}")
        with self.driver.session() as session:
            query = """
            MERGE (u:User {pubkey: $pubkey})
            SET u.pubkey = $pubkey
            """
            session.run(query, pubkey=user.pubkey)
        return

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
            query = """
            MATCH (u:User {pubkey: $pubkey})
            RETURN u.pubkey AS pubkey
            """
            result = session.run(query, pubkey=pubkey)
            record = result.single()
            if record:
                return User(record["pubkey"])
            return None
    
    def __add_event_kind_0(self, event: Event) -> None:
        """
        Add an event of kind 0 to the Neo4j database.

        Parameters:
        - event: Event, event object

        Example:
        >>> event = Event("0x123", 1612137600, 0, "0x123", "0x123", "content", [["tag1", "tag2"]])
        >>> db.__add_event_kind_0(event)
        """
        assert isinstance(event, Event), f"event must be an Event object, not {type(event)}"
        assert event.kind == 0, f"event kind must be 0, not {event.kind}"
        with self.driver.session() as session:
            user = self.get_user(event.pubkey)
            if not user:
                user = User(event.pubkey)
                self.__set_user(user)
            # TODO: Implement

    def add_event(self, event: Event) -> None:
        """
        Add an event to the Neo4j database.

        Parameters:
        - event: Event, event object

        Example:
        >>> event = Event("0x123", 1612137600, 0, "0x123", "0x123", "content", [["tag1", "tag2"]])
        >>> db.add_event(event)
        """
        assert isinstance(event, Event), f"event must be a Event object, not {type(event)}"
        if event.kind == 0:
            self.__add_event_kind_0(event)
        else:
            raise NotImplementedError(f"Event kind {event.kind} not implemented")