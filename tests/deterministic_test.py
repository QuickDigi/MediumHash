# deterministic_test.py
from hash import MediumHash

seed = b"fixed-seed-demo"
h1 = MediumHash() 
print(h1.hash("hello world") == h1.hash("hello world"))  # *True
