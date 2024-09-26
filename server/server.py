import grpc
from concurrent import futures
import subprocess
import digtool_pb2
import digtool_pb2_grpc

class DigToolService(digtool_pb2_grpc.DigToolServiceServicer):
    def QueryDNS(self, request, context):
        hostname = request.hostname
        command = ['dig', hostname]

        if request.flags:
            command.append(request.flags)

        try:
            result = subprocess.check_output(command, universal_newlines=True)
            return digtool_pb2.DNSResponse(results=[result], error="")
        except subprocess.CalledProcessError as e:
            return digtool_pb2.DNSResponse(results=[], error=str(e))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    digtool_pb2_grpc.add_DigToolServiceServicer_to_server(DigToolService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()