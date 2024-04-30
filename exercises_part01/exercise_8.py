def check_string(text):
    text = text.lower()
    if text.endswith("a") or text.startswith("a"):
        return True
    return False


print(check_string("asd"))
print(check_string("wasd"))
