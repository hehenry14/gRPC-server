import logging
import meter_pb2
import meter_pb2_grpc
import grpc
from concurrent import futures
import meter_resources



class ShowMeterServicer(meter_pb2_grpc.ShowMeterServicer):

    def __init__(self):
        self.db = meter_resources.read_route_guide_database()

    def ListMeters(self, request, context):
        for meter_usage in self.db:
            yield meter_usage


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meter_pb2_grpc.add_ShowMeterServicer_to_server(
        ShowMeterServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
