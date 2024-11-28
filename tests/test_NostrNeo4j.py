import nostr_neo4j

def test_NostrNeo4j():
    db = nostr_neo4j.NostrNeo4j(uri="bolt://localhost:7687", user="neo4j", password="password")
    assert db is not None
    db.close()