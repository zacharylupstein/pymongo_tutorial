schema = {
    "type": "object",
    "required": ["firstName", "phoneNumber", "email"],
    "additionalProperties": False,
    "properties": {
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "phoneNumber": {"type": "string"},
        "email":{"type": "string"},
        "password": {"type": "string"},
    },
}

updateSchema = {
    "type": "object",
    "required": [],
    "additionalProperties": False,
    "properties": {
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "phoneNumber": {"type": "string"},
        "email":{"type": "string"},
        "password": {"type": "string"},
    },
}