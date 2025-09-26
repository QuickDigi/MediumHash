import hashlib

def compare_with_sha3(data):
    """Compare with SHA3-256 for reference"""
    sha3_hash = hashlib.sha3_256(data.encode() if isinstance(data, str) else data).hexdigest()
    return sha3_hash