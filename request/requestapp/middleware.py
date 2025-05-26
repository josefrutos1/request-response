class middlewarePersonalizado:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Aquí seteamos un atributo al request
        request.custom_attribute = "valor agregado por el middleware"
        response = self.get_response(request)
        return response