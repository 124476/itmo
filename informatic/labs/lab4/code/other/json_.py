import json

data = {
    "GameConfig": {
        "window_title": "PAC-MAN",
        "fullscreen": False,
        "mouse_sensitivity": 1.4,
        "key_bindings": {
            "up": "Up",
            "down": "Down",
            "left": "Left",
            "right": "Right"
        },
        "skills": ["Python", "Go", "Rust"],
        "user": {
            "id": 123,
            "role": "admin",
            "name": "Alice"
        }
    }
}

json_text = json.dumps(data, indent=2)
print(json_text)

data = json.loads(json_text)
print(data)
