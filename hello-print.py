from zyjkit.print import zprint

data = {
    "name": "Alice",
    "scores": [92, 87, 95],
    "details": {
        "age": 28,
        "hobbies": ["reading", "hiking", {"sports": ["tennis", "swimming"]}],
        "contact": {"email": "alice@example.com"}
    }
}

zprint(data)
