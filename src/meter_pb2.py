# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmeter.proto\x12\x08getmeter\"*\n\x10ShowMeterRequest\x12\x16\n\x0erequest_method\x18\x01 \x01(\t\".\n\nMeterUsage\x12\x0c\n\x04time\x18\x01 \x01(\t\x12\x12\n\nmeterusage\x18\x02 \x01(\x02\x32M\n\tShowMeter\x12@\n\nListMeters\x12\x1a.getmeter.ShowMeterRequest\x1a\x14.getmeter.MeterUsage0\x01\x62\x06proto3')



_SHOWMETERREQUEST = DESCRIPTOR.message_types_by_name['ShowMeterRequest']
_METERUSAGE = DESCRIPTOR.message_types_by_name['MeterUsage']
ShowMeterRequest = _reflection.GeneratedProtocolMessageType('ShowMeterRequest', (_message.Message,), {
  'DESCRIPTOR' : _SHOWMETERREQUEST,
  '__module__' : 'meter_pb2'
  # @@protoc_insertion_point(class_scope:getmeter.ShowMeterRequest)
  })
_sym_db.RegisterMessage(ShowMeterRequest)

MeterUsage = _reflection.GeneratedProtocolMessageType('MeterUsage', (_message.Message,), {
  'DESCRIPTOR' : _METERUSAGE,
  '__module__' : 'meter_pb2'
  # @@protoc_insertion_point(class_scope:getmeter.MeterUsage)
  })
_sym_db.RegisterMessage(MeterUsage)

_SHOWMETER = DESCRIPTOR.services_by_name['ShowMeter']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SHOWMETERREQUEST._serialized_start=25
  _SHOWMETERREQUEST._serialized_end=67
  _METERUSAGE._serialized_start=69
  _METERUSAGE._serialized_end=115
  _SHOWMETER._serialized_start=117
  _SHOWMETER._serialized_end=194
# @@protoc_insertion_point(module_scope)