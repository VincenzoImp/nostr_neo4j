# tests/test_NostrNeo4j.py

import nostr_neo4j
import unittest

class TestNostrNeo4j(unittest.TestCase):
    def test_NostrNeo4j(self):
        db = nostr_neo4j.NostrNeo4j(uri="bolt://localhost:7687", user="neo4j", password="password")
        self.assertIsInstance(db, nostr_neo4j.NostrNeo4j, "Object is not an instance of NostrNeo4j")
        db.close()

if __name__ == "__main__":
    unittest.main()