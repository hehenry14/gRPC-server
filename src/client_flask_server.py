import asyncio
import logging

import json
import time

import grpc
import meter_pb2_grpc

from flask import Flask

app = Flask(__name__)


async def show_meter(stub: meter_pb2_grpc.ShowMeterStub):
    logging.info('Looking for the meter usage record.')
    meter_usages = stub.ListMeters(request=None)
    result = {}
    async for meter_usage in meter_usages:
        # @TODO: do the protocol buffer properly so it does not cause error.
        result[meter_usage.time] = meter_usage.meterusage
    return result


async def main():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = meter_pb2_grpc.ShowMeterStub(channel)
        result = await show_meter(stub)
        return json.dumps(result)


@app.route("/")
async def list_meter():
    app.logger.info('getting all the meter usages.')
    return await main()

if __name__ == '__main__':
    # wait for the server to start first
    time.sleep(5)
    asyncio.run(main())
    app.run()
