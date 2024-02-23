import time

def generateUniqueName() -> str:
    uniq_suffix = int(time.time())
    generated_name = f"user_{uniq_suffix}"
    print(f"Generated name: {generated_name}")
    return generated_name
