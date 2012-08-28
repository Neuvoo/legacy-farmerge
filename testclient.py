from txprotobuf import txprotobuf
from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ClientEndpoint
from scheduler_status_pb2 import StatusService, StatusService_Stub, StatusRequest, StatusResponse

statusService = StatusService()
factory = txprotobuf.Factory(statusService)

def gotProtocol(p):
	service = StatusService_Stub(p)
	request = StatusRequest()
	request.verbosity = 0

	def callback(response):
		print "Job Count:", response.jobCount
	service.Status(txprotobuf.Controller(), request, callback)

point = TCP4ClientEndpoint(reactor, "localhost", 6388)
d = point.connect(factory)
d.addCallback(gotProtocol)
reactor.run()