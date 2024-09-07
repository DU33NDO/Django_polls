def atr_middleware(get_response):

    def middleware(request):
        request.my_custom_attr = "wow, a new attr"
        response = get_response(request)

        return response

    return middleware


class CustomMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        request.my_custom_attr_2 = "wow, a new attr"

        response = self.get_response(request)

        return response
