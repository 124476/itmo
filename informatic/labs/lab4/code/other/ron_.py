import pyron

data = {"GameConfig": {"window_title": "PAC-MAN", "fullscreen": False, "skills": ["Python", "Go"]}}

ron_text = pyron.to_string(data)
print(ron_text)

data = pyron.loads(ron_text)
print(data)
