# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: digtool.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rdigtool.proto\x12\x07\x64igtool\"-\n\nDNSRequest\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\r\n\x05\x66lags\x18\x02 \x01(\t\"-\n\x0b\x44NSResponse\x12\x0f\n\x07results\x18\x01 \x03(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t2I\n\x0e\x44igToolService\x12\x37\n\x08QueryDNS\x12\x13.digtool.DNSRequest\x1a\x14.digtool.DNSResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'digtool_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_DNSREQUEST']._serialized_start=26
  _globals['_DNSREQUEST']._serialized_end=71
  _globals['_DNSRESPONSE']._serialized_start=73
  _globals['_DNSRESPONSE']._serialized_end=118
  _globals['_DIGTOOLSERVICE']._serialized_start=120
  _globals['_DIGTOOLSERVICE']._serialized_end=193
# @@protoc_insertion_point(module_scope)
