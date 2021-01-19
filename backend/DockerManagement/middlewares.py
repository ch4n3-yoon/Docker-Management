import json


class JsonParseFromBody:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        print('[ DEBUG ] request.body :', request.body)
        response = self.get_response(request)
        return response
