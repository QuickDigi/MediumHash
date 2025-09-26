# MediumHash

**MediumHash** is a lightweight and fast hashing tool with optional basic security testing features.

---

## Features

- Hash any text easily.
- Optional security tests:
  - **Avalanche Test**
  - **Collision Test**
  - **Distribution Test**
- No heavy external dependencies.

---

## Installation

Simply copy the `src` folder into your project, or install as a Python package if packaged later.

---

## Usage

```python
from MediumHash import MediumHash

    hasher = MediumHash()

    result = hasher.hash("Hello World")
    print(f"Hashed: {result}")
```

---

## Sample Test Results

=== Avalanche Test === 
Avalanche avg = 50.00% Std dev = 2.11%

=== Distribution Test === 
Mean freq = 500.00, Std dev = 24.19

=== Collision Test === 
Progress: 500/5000 
Progress: 1000/5000 
Progress: 1500/5000 
Progress: 2000/5000 
Progress: 2500/5000 
Progress: 3000/5000 
Progress: 3500/5000 
Progress: 4000/5000 
Progress: 4500/5000 
Progress: 5000/5000 
Total tested = 5000 
Collisions = 0 ✅ No collisions found (good sign).

## Security Notes

* `MediumHash` is designed for educational and research purposes.
* Tests indicate strong performance in Avalanche, Collision, and Distribution.
* Not recommended for password hashing or sensitive production data without additional security measures.

---

## License
`GLP` (GNU ``GENERAL PUBLIC LICENSE``) License
