# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xtlsapi.xray_api.common.serial import typed_message_pb2 as common_dot_serial_dot_typed__message__pb2
import importlib
transport_dot_global_dot_config__pb2 = importlib.import_module('transport.global.config_pb2')


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63ore/config.proto\x12\txray.core\x1a!common/serial/typed_message.proto\x1a\x1dtransport/global/config.proto\"\x87\x02\n\x06\x43onfig\x12\x30\n\x07inbound\x18\x01 \x03(\x0b\x32\x1f.xray.core.InboundHandlerConfig\x12\x32\n\x08outbound\x18\x02 \x03(\x0b\x32 .xray.core.OutboundHandlerConfig\x12-\n\x03\x61pp\x18\x04 \x03(\x0b\x32 .xray.common.serial.TypedMessage\x12-\n\ttransport\x18\x05 \x01(\x0b\x32\x16.xray.transport.ConfigB\x02\x18\x01\x12\x33\n\textension\x18\x06 \x03(\x0b\x32 .xray.common.serial.TypedMessageJ\x04\x08\x03\x10\x04\"\x9a\x01\n\x14InboundHandlerConfig\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12;\n\x11receiver_settings\x18\x02 \x01(\x0b\x32 .xray.common.serial.TypedMessage\x12\x38\n\x0eproxy_settings\x18\x03 \x01(\x0b\x32 .xray.common.serial.TypedMessage\"\xba\x01\n\x15OutboundHandlerConfig\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x39\n\x0fsender_settings\x18\x02 \x01(\x0b\x32 .xray.common.serial.TypedMessage\x12\x38\n\x0eproxy_settings\x18\x03 \x01(\x0b\x32 .xray.common.serial.TypedMessage\x12\x0e\n\x06\x65xpire\x18\x04 \x01(\x03\x12\x0f\n\x07\x63omment\x18\x05 \x01(\tB=\n\rcom.xray.coreP\x01Z\x1egithub.com/xtls/xray-core/core\xaa\x02\tXray.Coreb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'core.config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.xray.coreP\001Z\036github.com/xtls/xray-core/core\252\002\tXray.Core'
  _CONFIG.fields_by_name['transport']._options = None
  _CONFIG.fields_by_name['transport']._serialized_options = b'\030\001'
  _CONFIG._serialized_start=99
  _CONFIG._serialized_end=362
  _INBOUNDHANDLERCONFIG._serialized_start=365
  _INBOUNDHANDLERCONFIG._serialized_end=519
  _OUTBOUNDHANDLERCONFIG._serialized_start=522
  _OUTBOUNDHANDLERCONFIG._serialized_end=708
# @@protoc_insertion_point(module_scope)
