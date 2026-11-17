import yaml

data = {
    "GameConfig": {
        "window_title": "PAC-MAN",
        "fullscreen": False,
        "mouse_sensitivity": 1.4,
        "key_bindings": {"up": "Up", "down": "Down"},
        "skills": ["Python", "Go", "Rust"],
        "user": {"id": 123, "role": "admin", "name": "Alice"}
    }
}

yaml_text = yaml.safe_dump(data)
print(yaml_text)

data = yaml.safe_load(yaml_text)
print(data)
