# Meter Usage gRPC application

This is an application that reads the time based data from a csv file and returns it in an JSON format.

The application includes a gRPC server that streams data from a csv file, to run the sever please run:

```shell
python meter_server.py
```

The gRPC client is set up on a FLASK server, to run the flask server, please run `src/app.py`.