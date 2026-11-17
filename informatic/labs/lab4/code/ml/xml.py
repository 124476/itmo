def xml_escape(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def rec_xml(obj, tag="", indent=0):
    spacing = "  " * indent

    if not isinstance(obj, (dict, list)):
        val = str(obj).lower() if isinstance(obj, bool) else str(obj)
        return f"{spacing}<{tag}>{xml_escape(val)}</{tag}>\n"

    if not obj:
        return f"{spacing}<{tag}/>\n" if tag else ""

    xml = f"{spacing}<{tag}>\n" if tag else ""
    indent = indent + 1 if tag else indent

    if isinstance(obj, dict):
        for k, v in obj.items():
            xml += rec_xml(v, k, indent)
    elif isinstance(obj, list):
        for item in obj:
            xml += rec_xml(item, "item", indent)

    xml += f"{spacing}</{tag}>\n" if tag else ""
    return xml


def to_xml(obj):
    body = rec_xml(obj)
    return f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n{body}"
