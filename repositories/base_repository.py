from bson import ObjectId

class BaseRepository:

    @staticmethod
    def convert_object_id(data):
        """Recursively convert ObjectId → str in dicts/lists."""
        if isinstance(data, list):
            return [BaseRepository.convert_object_id(i) for i in data]

        if isinstance(data, dict):
            new_data = {}
            for key, value in data.items():
                if isinstance(value, ObjectId):
                    new_data[key] = str(value)
                else:
                    new_data[key] = BaseRepository.convert_object_id(value)
            return new_data

        return data
