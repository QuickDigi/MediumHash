from src.MediumHash import MediumHash
from security import hash_security_tests as sec

if __name__ == "__main__":
    hasher = MediumHash()

    msg = input("Enter the message: ")
    if msg == "":
        msg = "hello world"
        print("no input :( ")

    print(f"your message: {msg}")

    secTest = input("try security tests? (true/false): ")
    if secTest.lower() == "true":
        print("⚠️ Warning: Security test has been activated")
        sec.avalanche_test(hasher)
        sec.collision_test(hasher)
        sec.distribution_test(hasher)

    result = hasher.hash(msg)
    print(f"Hashed: {result}")
