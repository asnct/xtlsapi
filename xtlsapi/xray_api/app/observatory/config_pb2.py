# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/observatory/config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/observatory/config.proto',
  package='xray.core.app.observatory',
  syntax='proto3',
  serialized_options=b'\n\030com.xray.app.observatoryP\001Z)github.com/xtls/xray-core/app/observatory\252\002\024Xray.App.Observatory',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x61pp/observatory/config.proto\x12\x19xray.core.app.observatory\"N\n\x11ObservationResult\x12\x39\n\x06status\x18\x01 \x03(\x0b\x32).xray.core.app.observatory.OutboundStatus\"\x8e\x01\n\x0eOutboundStatus\x12\r\n\x05\x61live\x18\x01 \x01(\x08\x12\r\n\x05\x64\x65lay\x18\x02 \x01(\x03\x12\x19\n\x11last_error_reason\x18\x03 \x01(\t\x12\x14\n\x0coutbound_tag\x18\x04 \x01(\t\x12\x16\n\x0elast_seen_time\x18\x05 \x01(\x03\x12\x15\n\rlast_try_time\x18\x06 \x01(\x03\"F\n\x0bProbeResult\x12\r\n\x05\x61live\x18\x01 \x01(\x08\x12\r\n\x05\x64\x65lay\x18\x02 \x01(\x03\x12\x19\n\x11last_error_reason\x18\x03 \x01(\t\"#\n\tIntensity\x12\x16\n\x0eprobe_interval\x18\x01 \x01(\r\"i\n\x06\x43onfig\x12\x18\n\x10subject_selector\x18\x02 \x03(\t\x12\x11\n\tprobe_url\x18\x03 \x01(\t\x12\x16\n\x0eprobe_interval\x18\x04 \x01(\x03\x12\x1a\n\x12\x65nable_concurrency\x18\x05 \x01(\x08\x42^\n\x18\x63om.xray.app.observatoryP\x01Z)github.com/xtls/xray-core/app/observatory\xaa\x02\x14Xray.App.Observatoryb\x06proto3'
)




_OBSERVATIONRESULT = _descriptor.Descriptor(
  name='ObservationResult',
  full_name='xray.core.app.observatory.ObservationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='xray.core.app.observatory.ObservationResult.status', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=59,
  serialized_end=137,
)


_OUTBOUNDSTATUS = _descriptor.Descriptor(
  name='OutboundStatus',
  full_name='xray.core.app.observatory.OutboundStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='alive', full_name='xray.core.app.observatory.OutboundStatus.alive', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delay', full_name='xray.core.app.observatory.OutboundStatus.delay', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_error_reason', full_name='xray.core.app.observatory.OutboundStatus.last_error_reason', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outbound_tag', full_name='xray.core.app.observatory.OutboundStatus.outbound_tag', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_seen_time', full_name='xray.core.app.observatory.OutboundStatus.last_seen_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_try_time', full_name='xray.core.app.observatory.OutboundStatus.last_try_time', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=140,
  serialized_end=282,
)


_PROBERESULT = _descriptor.Descriptor(
  name='ProbeResult',
  full_name='xray.core.app.observatory.ProbeResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='alive', full_name='xray.core.app.observatory.ProbeResult.alive', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delay', full_name='xray.core.app.observatory.ProbeResult.delay', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_error_reason', full_name='xray.core.app.observatory.ProbeResult.last_error_reason', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=284,
  serialized_end=354,
)


_INTENSITY = _descriptor.Descriptor(
  name='Intensity',
  full_name='xray.core.app.observatory.Intensity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='probe_interval', full_name='xray.core.app.observatory.Intensity.probe_interval', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=356,
  serialized_end=391,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='xray.core.app.observatory.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subject_selector', full_name='xray.core.app.observatory.Config.subject_selector', index=0,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='probe_url', full_name='xray.core.app.observatory.Config.probe_url', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='probe_interval', full_name='xray.core.app.observatory.Config.probe_interval', index=2,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_concurrency', full_name='xray.core.app.observatory.Config.enable_concurrency', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=393,
  serialized_end=498,
)

_OBSERVATIONRESULT.fields_by_name['status'].message_type = _OUTBOUNDSTATUS
DESCRIPTOR.message_types_by_name['ObservationResult'] = _OBSERVATIONRESULT
DESCRIPTOR.message_types_by_name['OutboundStatus'] = _OUTBOUNDSTATUS
DESCRIPTOR.message_types_by_name['ProbeResult'] = _PROBERESULT
DESCRIPTOR.message_types_by_name['Intensity'] = _INTENSITY
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObservationResult = _reflection.GeneratedProtocolMessageType('ObservationResult', (_message.Message,), {
  'DESCRIPTOR' : _OBSERVATIONRESULT,
  '__module__' : 'app.observatory.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.core.app.observatory.ObservationResult)
  })
_sym_db.RegisterMessage(ObservationResult)

OutboundStatus = _reflection.GeneratedProtocolMessageType('OutboundStatus', (_message.Message,), {
  'DESCRIPTOR' : _OUTBOUNDSTATUS,
  '__module__' : 'app.observatory.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.core.app.observatory.OutboundStatus)
  })
_sym_db.RegisterMessage(OutboundStatus)

ProbeResult = _reflection.GeneratedProtocolMessageType('ProbeResult', (_message.Message,), {
  'DESCRIPTOR' : _PROBERESULT,
  '__module__' : 'app.observatory.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.core.app.observatory.ProbeResult)
  })
_sym_db.RegisterMessage(ProbeResult)

Intensity = _reflection.GeneratedProtocolMessageType('Intensity', (_message.Message,), {
  'DESCRIPTOR' : _INTENSITY,
  '__module__' : 'app.observatory.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.core.app.observatory.Intensity)
  })
_sym_db.RegisterMessage(Intensity)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'app.observatory.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.core.app.observatory.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
