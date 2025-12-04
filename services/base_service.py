class BaseService:

    @staticmethod
    def format_response(data, message="Success"):
        return {
            "status": True,
            "message": message,
            "data": data
        }

    @staticmethod
    def format_error(message="Error"):
        return {
            "status": False,
            "message": message,
            "data": None
        }
