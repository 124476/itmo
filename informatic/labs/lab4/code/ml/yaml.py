def to_yaml(obj, indent=0):
    spacing = " " * indent

    if isinstance(obj, dict):
        if not obj:
            return "{}"

        lines = []
        for k, v in obj.items():
            if isinstance(v, (dict, list)) and v:
                lines.append(f"{spacing}{k}:")
                lines.append(to_yaml(v, indent + 2))
            else:
                lines.append(f"{spacing}{k}: {yaml_val(v)}")

        return "\n".join(lines)

    elif isinstance(obj, list):
        if not obj:
            return "[]"

        lines = []
        for item in obj:
            if isinstance(item, (dict, list)) and item:
                item_str = to_yaml(item, indent + 2)
                lines.append(f"{spacing}- {item_str[indent + 2:]}")
            else:
                lines.append(f"{spacing}- {yaml_val(item)}")

        return "\n".join(lines)

    return yaml_val(obj)


def yaml_val(v):
    if isinstance(v, str):
        safe_v = v.replace('"', '\\"')
        return f'"{safe_v}"'

    if isinstance(v, bool):
        return "true" if v else "false"

    return str(v)