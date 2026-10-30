def xml_escape(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def rec_xml(obj, tag_name="", indent=0):
    spacing = " " * 2 * indent
    xml = ""

    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, list) and len(v) == 0: # пустой массив закрываем тегом <../>
                xml += f"{spacing}<{k}/>\n"
                continue

            if isinstance(v, (dict, list)):
                xml += f"{spacing}<{k}>\n"
                xml += rec_xml(v, "", indent + 1)
                xml += f"{spacing}</{k}>\n"
                continue

            val = str(v).lower() if isinstance(v, bool) else str(v)
            xml += f"{spacing}<{k}>{xml_escape(val)}</{k}>\n"

        return xml

    if isinstance(obj, list):
        if not obj: # пустой массив закрываем тегом <../>
            xml += f"{spacing}<{tag_name}/>\n"
            return xml

        if tag_name:
            xml += f"{spacing}<{tag_name}>\n"
            current_indent = indent + 1
        else:
            current_indent = indent

        for item in obj:
            xml += rec_xml(item, "item", current_indent)

        if tag_name:
            xml += f"{spacing}</{tag_name}>\n"

        return xml

    val = str(obj).lower() if isinstance(obj, bool) else str(obj)
    xml += f"{spacing}<{tag_name}>{xml_escape(val)}</{tag_name}>\n"
    return xml

def to_xml(obj):
    body = rec_xml(obj)
    return f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n{body}"
