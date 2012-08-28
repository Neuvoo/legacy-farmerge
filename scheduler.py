from txprotobuf import txprotobuf
from twisted.application import service, internet
from scheduler_status_pb2 import StatusService, StatusRequest, StatusResponse

class SchedulerStatusService(StatusService):
    def Status(self, controller, request, callback):
        response = StatusResponse()
        response.jobCount = 9000
        print "StatusResponse", response.jobCount
        callback(response)
        
statusService = SchedulerStatusService()
factory = txprotobuf.Factory(statusService)
application = service.Application("StatusService")
internet.TCPServer(6388, factory).setServiceParent(application)