import pandas as pd

import meter_pb2


def read_route_guide_database():
    """Reads the route guide database.
  Returns:
    The full contents of the route guide database as a sequence of
      route_guide_pb2.Features.
  """
    meter_usage_list = []
    data_dict = pd.read_csv('/app/src/data/meterusage.1649407467.csv', header=None, index_col=0, squeeze=True).to_dict()

    for time in data_dict:
        if time != 'time':
            meter_usage = meter_pb2.MeterUsage(
                time=time,
                meterusage=float(data_dict[time])
               )
            meter_usage_list.append(meter_usage)
    return meter_usage_list