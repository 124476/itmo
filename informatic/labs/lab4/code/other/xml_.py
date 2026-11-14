import xmltodict

data = {
    "GameConfig": {
        "window_title": "PAC-MAN",
        "fullscreen": "false",
        "mouse_sensitivity": "1.4",
        "key_bindings": {
            "up": "Up",
            "down": "Down",
            "left": "Left",
            "right": "Right"
        },
        "skills": {
            "item": ["Python", "Go", "Rust"]
        },
        "user": {
            "@id": "123",
            "@role": "admin",
            "name": "Alice"
        }
    }
}

xml_text = xmltodict.unparse(data, pretty=True)

print(xml_text)
