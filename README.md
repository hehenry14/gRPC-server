# Meter Usage gRPC application

## Introduction

This is an application that reads the time based data from a csv file and returns it in an JSON format.

The application includes a gRPC server that streams data from a csv file to a flask server running the gRPC client, the flask server will get the data stream from the gRPC server and return it as json.


## Manual
To run the sever and the flask client please run:

```shell
docker-compose up
```

Send the get request to `127.0.0.1:5000/meter_usages` to get the JSON format data.

## Nice to have for the future

1. Front end app, loading the json nicely.