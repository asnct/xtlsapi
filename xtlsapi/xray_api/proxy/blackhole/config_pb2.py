# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/blackhole/config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from xtlsapi.xray_api.common.serial import typed_message_pb2 as common_dot_serial_dot_typed__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proxy/blackhole/config.proto',
  package='xray.proxy.blackhole',
  syntax='proto3',
  serialized_options=b'\n\030com.xray.proxy.blackholeP\001Z)github.com/xtls/xray-core/proxy/blackhole\252\002\024Xray.Proxy.Blackhole',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cproxy/blackhole/config.proto\x12\x14xray.proxy.blackhole\x1a!common/serial/typed_message.proto\"\x0e\n\x0cNoneResponse\"\x0e\n\x0cHTTPResponse\"<\n\x06\x43onfig\x12\x32\n\x08response\x18\x01 \x01(\x0b\x32 .xray.common.serial.TypedMessageB^\n\x18\x63om.xray.proxy.blackholeP\x01Z)github.com/xtls/xray-core/proxy/blackhole\xaa\x02\x14Xray.Proxy.Blackholeb\x06proto3'
  ,
  dependencies=[common_dot_serial_dot_typed__message__pb2.DESCRIPTOR,])




_NONERESPONSE = _descriptor.Descriptor(
  name='NoneResponse',
  full_name='xray.proxy.blackhole.NoneResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=103,
)


_HTTPRESPONSE = _descriptor.Descriptor(
  name='HTTPResponse',
  full_name='xray.proxy.blackhole.HTTPResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=119,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='xray.proxy.blackhole.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='xray.proxy.blackhole.Config.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=181,
)

_CONFIG.fields_by_name['response'].message_type = common_dot_serial_dot_typed__message__pb2._TYPEDMESSAGE
DESCRIPTOR.message_types_by_name['NoneResponse'] = _NONERESPONSE
DESCRIPTOR.message_types_by_name['HTTPResponse'] = _HTTPRESPONSE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NoneResponse = _reflection.GeneratedProtocolMessageType('NoneResponse', (_message.Message,), {
  'DESCRIPTOR' : _NONERESPONSE,
  '__module__' : 'proxy.blackhole.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.blackhole.NoneResponse)
  })
_sym_db.RegisterMessage(NoneResponse)

HTTPResponse = _reflection.GeneratedProtocolMessageType('HTTPResponse', (_message.Message,), {
  'DESCRIPTOR' : _HTTPRESPONSE,
  '__module__' : 'proxy.blackhole.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.blackhole.HTTPResponse)
  })
_sym_db.RegisterMessage(HTTPResponse)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'proxy.blackhole.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.blackhole.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
