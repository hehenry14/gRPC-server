import logging
import meter_pb2_grpc
import grpc
import asyncio
import meter_resources


class ShowMeterServicer(meter_pb2_grpc.ShowMeterServicer):

    def __init__(self):
        self.db = meter_resources.read_route_guide_database()

    def ListMeters(self, request, context):
        for meter_usage in self.db:
            yield meter_usage


async def serve():
    server = grpc.aio.server()
    meter_pb2_grpc.add_ShowMeterServicer_to_server(
        ShowMeterServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(serve())
