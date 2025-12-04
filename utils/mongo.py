from bson import ObjectId

def convert_object_id(data):
    """Recursively convert all ObjectId fields inside a dict/list."""
    if isinstance(data, list):
        return [convert_object_id(i) for i in data]

    if isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            if isinstance(v, ObjectId):
                new_data[k] = str(v)
            else:
                new_data[k] = convert_object_id(v)
        return new_data

    return data
