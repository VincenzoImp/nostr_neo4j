# nostr_neo4j/utils.py

import json
import hashlib
import bech32
import secp256k1

def npub_to_hex(npub: str) -> str:
    if not npub.startswith('npub'): None
    hrp, data = bech32.bech32_decode(npub)
    decoded_bytes = bech32.convertbits(data, 5, 8, False)
    return bytes(decoded_bytes).hex()

def hex_to_npub(hex_str: str) -> str:
    byte_data = bytes.fromhex(hex_str)
    data = bech32.convertbits(byte_data, 8, 5, True)
    npub = bech32.bech32_encode('npub', data)
    return npub

def sign_event_id(event_id: str, private_key_hex: str) -> str:
    private_key = secp256k1.PrivateKey(bytes.fromhex(private_key_hex))
    sig = private_key.schnorr_sign(bytes.fromhex(event_id), bip340tag=None, raw=True)
    return sig.hex()

def calc_event_id(public_key: str, created_at: int, kind_number: int, tags: list, content: str) -> str:
    def escape_content(content):
        # The following characters in the content field must be escaped as shown, and all other characters must be included verbatim:
        # A line break (0x0A), use \n
        # A double quote (0x22), use \"
        # A backslash (0x5C), use \\
        # A carriage return (0x0D), use \r
        # A tab character (0x09), use \t
        # A backspace, (0x08), use \b
        # A form feed, (0x0C), use \f
        return content
    content = escape_content(content)
    data = [0, public_key.lower(), created_at, kind_number, tags, content]
    data_str = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(data_str.encode("UTF-8")).hexdigest()

def verify_signature(event_id: str, pubkey: str, sig: str) -> bool:
    try:
        pub_key = secp256k1.PublicKey(bytes.fromhex("02" + pubkey), True)
        result = pub_key.schnorr_verify(bytes.fromhex(event_id), bytes.fromhex(sig), None, raw=True)
        if result:
            return True
        else:
            return False
    except (ValueError, TypeError) as e:
        return False