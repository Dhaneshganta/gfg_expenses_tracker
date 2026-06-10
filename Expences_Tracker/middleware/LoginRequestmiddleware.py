
from expenses.models import RequestLogs

class MiddlewareLoginrequest():

    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        request_info = request
        # print(vars(request_info))
        print(request_info.path,request.method)

        logs = RequestLogs.objects.create(
            request_info = vars(request_info),
            request_type = request_info.path,
            request_method = request.path
        )
        print(self.get_response(request))
        print(f"Hello, my name is {self.get_response(request)} and I am years old.")

        return self.get_response(request)



