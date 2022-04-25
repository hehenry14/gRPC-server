import asyncio
import logging

import json

import grpc
import meter_pb2
import meter_pb2_grpc

from flask import Flask

app = Flask(__name__)


async def show_meter(stub: meter_pb2_grpc.ShowMeterStub):
    logging.info('Looking for the meter usage record.')
    meter_usages = stub.ListMeters(meter_pb2.ShowMeterRequest())
    result = {}
    async for meter_usage in meter_usages:
        result[meter_usage.time] = meter_usage.meterusage
    return result


async def main():
    async with grpc.aio.insecure_channel('server:50051') as channel:
        stub = meter_pb2_grpc.ShowMeterStub(channel)
        result = await show_meter(stub)
    return json.dumps(result)


@app.route("/")
def list_meter():
    loop = asyncio.get_event_loop()
    app.logger.info('getting all the meter usages.')
    return loop.run_until_complete(main())


if __name__ == '__main__':
    app.run()
