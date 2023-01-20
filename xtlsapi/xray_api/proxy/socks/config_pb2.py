# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/socks/config.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xtlsapi.xray_api.common.net import address_pb2 as common_dot_net_dot_address__pb2
from xtlsapi.xray_api.common.protocol import server_spec_pb2 as common_dot_protocol_dot_server__spec__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proxy/socks/config.proto',
  package='xray.proxy.socks',
  syntax='proto3',
  serialized_options=b'\n\024com.xray.proxy.socksP\001Z%github.com/xtls/xray-core/proxy/socks\252\002\020Xray.Proxy.Socks',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18proxy/socks/config.proto\x12\x10xray.proxy.socks\x1a\x18\x63ommon/net/address.proto\x1a!common/protocol/server_spec.proto\"-\n\x07\x41\x63\x63ount\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x9a\x02\n\x0cServerConfig\x12-\n\tauth_type\x18\x01 \x01(\x0e\x32\x1a.xray.proxy.socks.AuthType\x12>\n\x08\x61\x63\x63ounts\x18\x02 \x03(\x0b\x32,.xray.proxy.socks.ServerConfig.AccountsEntry\x12,\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x1b.xray.common.net.IPOrDomain\x12\x13\n\x0budp_enabled\x18\x04 \x01(\x08\x12\x13\n\x07timeout\x18\x05 \x01(\rB\x02\x18\x01\x12\x12\n\nuser_level\x18\x06 \x01(\r\x1a/\n\rAccountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"p\n\x0c\x43lientConfig\x12\x34\n\x06server\x18\x01 \x03(\x0b\x32$.xray.common.protocol.ServerEndpoint\x12*\n\x07version\x18\x02 \x01(\x0e\x32\x19.xray.proxy.socks.Version*%\n\x08\x41uthType\x12\x0b\n\x07NO_AUTH\x10\x00\x12\x0c\n\x08PASSWORD\x10\x01*.\n\x07Version\x12\n\n\x06SOCKS5\x10\x00\x12\n\n\x06SOCKS4\x10\x01\x12\x0b\n\x07SOCKS4A\x10\x02\x42R\n\x14\x63om.xray.proxy.socksP\x01Z%github.com/xtls/xray-core/proxy/socks\xaa\x02\x10Xray.Proxy.Socksb\x06proto3'
  ,
  dependencies=[common_dot_net_dot_address__pb2.DESCRIPTOR,common_dot_protocol_dot_server__spec__pb2.DESCRIPTOR,])

_AUTHTYPE = _descriptor.EnumDescriptor(
  name='AuthType',
  full_name='xray.proxy.socks.AuthType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_AUTH', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PASSWORD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=553,
  serialized_end=590,
)
_sym_db.RegisterEnumDescriptor(_AUTHTYPE)

AuthType = enum_type_wrapper.EnumTypeWrapper(_AUTHTYPE)
_VERSION = _descriptor.EnumDescriptor(
  name='Version',
  full_name='xray.proxy.socks.Version',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SOCKS5', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SOCKS4', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SOCKS4A', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=592,
  serialized_end=638,
)
_sym_db.RegisterEnumDescriptor(_VERSION)

Version = enum_type_wrapper.EnumTypeWrapper(_VERSION)
NO_AUTH = 0
PASSWORD = 1
SOCKS5 = 0
SOCKS4 = 1
SOCKS4A = 2



_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='xray.proxy.socks.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='xray.proxy.socks.Account.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='xray.proxy.socks.Account.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=107,
  serialized_end=152,
)


_SERVERCONFIG_ACCOUNTSENTRY = _descriptor.Descriptor(
  name='AccountsEntry',
  full_name='xray.proxy.socks.ServerConfig.AccountsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='xray.proxy.socks.ServerConfig.AccountsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='xray.proxy.socks.ServerConfig.AccountsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=390,
  serialized_end=437,
)

_SERVERCONFIG = _descriptor.Descriptor(
  name='ServerConfig',
  full_name='xray.proxy.socks.ServerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_type', full_name='xray.proxy.socks.ServerConfig.auth_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accounts', full_name='xray.proxy.socks.ServerConfig.accounts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='xray.proxy.socks.ServerConfig.address', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='udp_enabled', full_name='xray.proxy.socks.ServerConfig.udp_enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='xray.proxy.socks.ServerConfig.timeout', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_level', full_name='xray.proxy.socks.ServerConfig.user_level', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SERVERCONFIG_ACCOUNTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=437,
)


_CLIENTCONFIG = _descriptor.Descriptor(
  name='ClientConfig',
  full_name='xray.proxy.socks.ClientConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server', full_name='xray.proxy.socks.ClientConfig.server', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='xray.proxy.socks.ClientConfig.version', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=439,
  serialized_end=551,
)

_SERVERCONFIG_ACCOUNTSENTRY.containing_type = _SERVERCONFIG
_SERVERCONFIG.fields_by_name['auth_type'].enum_type = _AUTHTYPE
_SERVERCONFIG.fields_by_name['accounts'].message_type = _SERVERCONFIG_ACCOUNTSENTRY
_SERVERCONFIG.fields_by_name['address'].message_type = common_dot_net_dot_address__pb2._IPORDOMAIN
_CLIENTCONFIG.fields_by_name['server'].message_type = common_dot_protocol_dot_server__spec__pb2._SERVERENDPOINT
_CLIENTCONFIG.fields_by_name['version'].enum_type = _VERSION
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['ServerConfig'] = _SERVERCONFIG
DESCRIPTOR.message_types_by_name['ClientConfig'] = _CLIENTCONFIG
DESCRIPTOR.enum_types_by_name['AuthType'] = _AUTHTYPE
DESCRIPTOR.enum_types_by_name['Version'] = _VERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'proxy.socks.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.socks.Account)
  })
_sym_db.RegisterMessage(Account)

ServerConfig = _reflection.GeneratedProtocolMessageType('ServerConfig', (_message.Message,), {

  'AccountsEntry' : _reflection.GeneratedProtocolMessageType('AccountsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SERVERCONFIG_ACCOUNTSENTRY,
    '__module__' : 'proxy.socks.config_pb2'
    # @@protoc_insertion_point(class_scope:xray.proxy.socks.ServerConfig.AccountsEntry)
    })
  ,
  'DESCRIPTOR' : _SERVERCONFIG,
  '__module__' : 'proxy.socks.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.socks.ServerConfig)
  })
_sym_db.RegisterMessage(ServerConfig)
_sym_db.RegisterMessage(ServerConfig.AccountsEntry)

ClientConfig = _reflection.GeneratedProtocolMessageType('ClientConfig', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTCONFIG,
  '__module__' : 'proxy.socks.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.socks.ClientConfig)
  })
_sym_db.RegisterMessage(ClientConfig)


DESCRIPTOR._options = None
_SERVERCONFIG_ACCOUNTSENTRY._options = None
_SERVERCONFIG.fields_by_name['timeout']._options = None
# @@protoc_insertion_point(module_scope)
