# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: c2s.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='c2s.proto',
  package='de.velcommuta.denul.network.c2s',
  serialized_pb=_b('\n\tc2s.proto\x12\x1f\x64\x65.velcommuta.denul.network.c2s\"#\n\x05Store\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\x0c\"\xcf\x01\n\nStoreReply\x12J\n\x06opcode\x18\x01 \x02(\x0e\x32:.de.velcommuta.denul.network.c2s.StoreReply.StoreReplyCode\x12\x0b\n\x03key\x18\x02 \x02(\t\"h\n\x0eStoreReplyCode\x12\x0c\n\x08STORE_OK\x10\x00\x12\x18\n\x14STORE_FAIL_KEY_TAKEN\x10\x01\x12\x16\n\x12STORE_FAIL_KEY_FMT\x10\x02\x12\x16\n\x12STORE_FAIL_UNKNOWN\x10\x03\"\x12\n\x03Get\x12\x0b\n\x03key\x18\x01 \x02(\t\"\xba\x01\n\x08GetReply\x12\x46\n\x06opcode\x18\x01 \x02(\x0e\x32\x36.de.velcommuta.denul.network.c2s.GetReply.GetReplyCode\x12\x0b\n\x03key\x18\x02 \x02(\t\x12\r\n\x05value\x18\x03 \x01(\x0c\"J\n\x0cGetReplyCode\x12\n\n\x06GET_OK\x10\x00\x12\x18\n\x14GET_FAIL_UNKNOWN_KEY\x10\x01\x12\x14\n\x10GET_FAIL_UNKNOWN\x10\x02\"#\n\x06\x44\x65lete\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\x0c\n\x04\x61uth\x18\x02 \x02(\t\"\xd4\x01\n\x0b\x44\x65leteReply\x12L\n\x06opcode\x18\x01 \x02(\x0e\x32<.de.velcommuta.denul.network.c2s.DeleteReply.DeleteReplyCode\x12\x0b\n\x03key\x18\x02 \x02(\t\"j\n\x0f\x44\x65leteReplyCode\x12\r\n\tDELETE_OK\x10\x00\x12\x14\n\x10\x44\x45LETE_FAIL_AUTH\x10\x01\x12\x19\n\x15\x44\x45LETE_FAIL_NOT_FOUND\x10\x02\x12\x17\n\x13\x44\x45LETE_FAIL_UNKNOWN\x10\x03\"0\n\x0b\x43lientHello\x12\x13\n\x0b\x63lientProto\x18\x01 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\xd6\x01\n\x0bServerHello\x12Q\n\x06opcode\x18\x01 \x02(\x0e\x32\x41.de.velcommuta.denul.network.c2s.ServerHello.ClientHelloReplyCode\x12\x13\n\x0bserverProto\x18\x02 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x02(\x0c\"Q\n\x14\x43lientHelloReplyCode\x12\x13\n\x0f\x43LIENT_HELLO_OK\x10\x00\x12$\n CLIENT_HELLO_PROTO_NOT_SUPPORTED\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_STOREREPLY_STOREREPLYCODE = _descriptor.EnumDescriptor(
  name='StoreReplyCode',
  full_name='de.velcommuta.denul.network.c2s.StoreReply.StoreReplyCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STORE_OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORE_FAIL_KEY_TAKEN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORE_FAIL_KEY_FMT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORE_FAIL_UNKNOWN', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=187,
  serialized_end=291,
)
_sym_db.RegisterEnumDescriptor(_STOREREPLY_STOREREPLYCODE)

_GETREPLY_GETREPLYCODE = _descriptor.EnumDescriptor(
  name='GetReplyCode',
  full_name='de.velcommuta.denul.network.c2s.GetReply.GetReplyCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GET_OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_FAIL_UNKNOWN_KEY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_FAIL_UNKNOWN', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=426,
  serialized_end=500,
)
_sym_db.RegisterEnumDescriptor(_GETREPLY_GETREPLYCODE)

_DELETEREPLY_DELETEREPLYCODE = _descriptor.EnumDescriptor(
  name='DeleteReplyCode',
  full_name='de.velcommuta.denul.network.c2s.DeleteReply.DeleteReplyCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DELETE_OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE_FAIL_AUTH', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE_FAIL_NOT_FOUND', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE_FAIL_UNKNOWN', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=646,
  serialized_end=752,
)
_sym_db.RegisterEnumDescriptor(_DELETEREPLY_DELETEREPLYCODE)

_SERVERHELLO_CLIENTHELLOREPLYCODE = _descriptor.EnumDescriptor(
  name='ClientHelloReplyCode',
  full_name='de.velcommuta.denul.network.c2s.ServerHello.ClientHelloReplyCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CLIENT_HELLO_OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_HELLO_PROTO_NOT_SUPPORTED', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=938,
  serialized_end=1019,
)
_sym_db.RegisterEnumDescriptor(_SERVERHELLO_CLIENTHELLOREPLYCODE)


_STORE = _descriptor.Descriptor(
  name='Store',
  full_name='de.velcommuta.denul.network.c2s.Store',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='de.velcommuta.denul.network.c2s.Store.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='de.velcommuta.denul.network.c2s.Store.value', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=81,
)


_STOREREPLY = _descriptor.Descriptor(
  name='StoreReply',
  full_name='de.velcommuta.denul.network.c2s.StoreReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opcode', full_name='de.velcommuta.denul.network.c2s.StoreReply.opcode', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='de.velcommuta.denul.network.c2s.StoreReply.key', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STOREREPLY_STOREREPLYCODE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=291,
)


_GET = _descriptor.Descriptor(
  name='Get',
  full_name='de.velcommuta.denul.network.c2s.Get',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='de.velcommuta.denul.network.c2s.Get.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=293,
  serialized_end=311,
)


_GETREPLY = _descriptor.Descriptor(
  name='GetReply',
  full_name='de.velcommuta.denul.network.c2s.GetReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opcode', full_name='de.velcommuta.denul.network.c2s.GetReply.opcode', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='de.velcommuta.denul.network.c2s.GetReply.key', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='de.velcommuta.denul.network.c2s.GetReply.value', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETREPLY_GETREPLYCODE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=314,
  serialized_end=500,
)


_DELETE = _descriptor.Descriptor(
  name='Delete',
  full_name='de.velcommuta.denul.network.c2s.Delete',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='de.velcommuta.denul.network.c2s.Delete.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth', full_name='de.velcommuta.denul.network.c2s.Delete.auth', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=502,
  serialized_end=537,
)


_DELETEREPLY = _descriptor.Descriptor(
  name='DeleteReply',
  full_name='de.velcommuta.denul.network.c2s.DeleteReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opcode', full_name='de.velcommuta.denul.network.c2s.DeleteReply.opcode', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='de.velcommuta.denul.network.c2s.DeleteReply.key', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DELETEREPLY_DELETEREPLYCODE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=540,
  serialized_end=752,
)


_CLIENTHELLO = _descriptor.Descriptor(
  name='ClientHello',
  full_name='de.velcommuta.denul.network.c2s.ClientHello',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientProto', full_name='de.velcommuta.denul.network.c2s.ClientHello.clientProto', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='de.velcommuta.denul.network.c2s.ClientHello.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=754,
  serialized_end=802,
)


_SERVERHELLO = _descriptor.Descriptor(
  name='ServerHello',
  full_name='de.velcommuta.denul.network.c2s.ServerHello',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opcode', full_name='de.velcommuta.denul.network.c2s.ServerHello.opcode', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serverProto', full_name='de.velcommuta.denul.network.c2s.ServerHello.serverProto', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='de.velcommuta.denul.network.c2s.ServerHello.data', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVERHELLO_CLIENTHELLOREPLYCODE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=805,
  serialized_end=1019,
)

_STOREREPLY.fields_by_name['opcode'].enum_type = _STOREREPLY_STOREREPLYCODE
_STOREREPLY_STOREREPLYCODE.containing_type = _STOREREPLY
_GETREPLY.fields_by_name['opcode'].enum_type = _GETREPLY_GETREPLYCODE
_GETREPLY_GETREPLYCODE.containing_type = _GETREPLY
_DELETEREPLY.fields_by_name['opcode'].enum_type = _DELETEREPLY_DELETEREPLYCODE
_DELETEREPLY_DELETEREPLYCODE.containing_type = _DELETEREPLY
_SERVERHELLO.fields_by_name['opcode'].enum_type = _SERVERHELLO_CLIENTHELLOREPLYCODE
_SERVERHELLO_CLIENTHELLOREPLYCODE.containing_type = _SERVERHELLO
DESCRIPTOR.message_types_by_name['Store'] = _STORE
DESCRIPTOR.message_types_by_name['StoreReply'] = _STOREREPLY
DESCRIPTOR.message_types_by_name['Get'] = _GET
DESCRIPTOR.message_types_by_name['GetReply'] = _GETREPLY
DESCRIPTOR.message_types_by_name['Delete'] = _DELETE
DESCRIPTOR.message_types_by_name['DeleteReply'] = _DELETEREPLY
DESCRIPTOR.message_types_by_name['ClientHello'] = _CLIENTHELLO
DESCRIPTOR.message_types_by_name['ServerHello'] = _SERVERHELLO

Store = _reflection.GeneratedProtocolMessageType('Store', (_message.Message,), dict(
  DESCRIPTOR = _STORE,
  __module__ = 'c2s_pb2'
  # @@protoc_insertion_point(class_scope:de.velcommuta.denul.network.c2s.Store)
  ))
_sym_db.RegisterMessage(Store)

StoreReply = _reflection.GeneratedProtocolMessageType('StoreReply', (_message.Message,), dict(
  DESCRIPTOR = _STOREREPLY,
  __module__ = 'c2s_pb2'
  # @@protoc_insertion_point(class_scope:de.velcommuta.denul.network.c2s.StoreReply)
  ))
_sym_db.RegisterMessage(StoreReply)

Get = _reflection.GeneratedProtocolMessageType('Get', (_message.Message,), dict(
  DESCRIPTOR = _GET,
  __module__ = 'c2s_pb2'
  # @@protoc_insertion_point(class_scope:de.velcommuta.denul.network.c2s.Get)
  ))
_sym_db.RegisterMessage(Get)

GetReply = _reflection.GeneratedProtocolMessageType('GetReply', (_message.Message,), dict(
  DESCRIPTOR = _GETREPLY,
  __module__ = 'c2s_pb2'
  # @@protoc_insertion_point(class_scope:de.velcommuta.denul.network.c2s.GetReply)
  ))
_sym_db.RegisterMessage(GetReply)

Delete = _reflection.GeneratedProtocolMessageType('Delete', (_message.Message,), dict(
  DESCRIPTOR = _DELETE,
  __module__ = 'c2s_pb2'
  # @@protoc_insertion_point(class_scope:de.velcommuta.denul.network.c2s.Delete)
  ))
_sym_db.RegisterMessage(Delete)

DeleteReply = _reflection.GeneratedProtocolMessageType('DeleteReply', (_message.Message,), dict(
  DESCRIPTOR = _DELETEREPLY,
  __module__ = 'c2s_pb2'
  # @@protoc_insertion_point(class_scope:de.velcommuta.denul.network.c2s.DeleteReply)
  ))
_sym_db.RegisterMessage(DeleteReply)

ClientHello = _reflection.GeneratedProtocolMessageType('ClientHello', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTHELLO,
  __module__ = 'c2s_pb2'
  # @@protoc_insertion_point(class_scope:de.velcommuta.denul.network.c2s.ClientHello)
  ))
_sym_db.RegisterMessage(ClientHello)

ServerHello = _reflection.GeneratedProtocolMessageType('ServerHello', (_message.Message,), dict(
  DESCRIPTOR = _SERVERHELLO,
  __module__ = 'c2s_pb2'
  # @@protoc_insertion_point(class_scope:de.velcommuta.denul.network.c2s.ServerHello)
  ))
_sym_db.RegisterMessage(ServerHello)


# @@protoc_insertion_point(module_scope)
