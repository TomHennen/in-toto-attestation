# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: in_toto_attestation/predicates/scai/v0/scai.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2

from in_toto_attestation.v1 import (
    resource_descriptor_pb2 as in__toto__attestation_dot_v1_dot_resource__descriptor__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n1in_toto_attestation/predicates/scai/v0/scai.proto\x12&in_toto_attestation.predicates.scai.v0\x1a\x1cgoogle/protobuf/struct.proto\x1a\x30in_toto_attestation/v1/resource_descriptor.proto"\xce\x01\n\x12\x41ttributeAssertion\x12\x11\n\tattribute\x18\x01 \x01(\t\x12:\n\x06target\x18\x02 \x01(\x0b\x32*.in_toto_attestation.v1.ResourceDescriptor\x12+\n\nconditions\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12<\n\x08\x65vidence\x18\x04 \x01(\x0b\x32*.in_toto_attestation.v1.ResourceDescriptor"\x9f\x01\n\x0f\x41ttributeReport\x12N\n\nattributes\x18\x01 \x03(\x0b\x32:.in_toto_attestation.predicates.scai.v0.AttributeAssertion\x12<\n\x08producer\x18\x02 \x01(\x0b\x32*.in_toto_attestation.v1.ResourceDescriptorBg\n/io.github.intoto.attestation.predicates.scai.v0Z4github.com/in-toto/attestation/go/predicates/scai/v0b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "in_toto_attestation.predicates.scai.v0.scai_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n/io.github.intoto.attestation.predicates.scai.v0Z4github.com/in-toto/attestation/go/predicates/scai/v0"
    _globals["_ATTRIBUTEASSERTION"]._serialized_start = 174
    _globals["_ATTRIBUTEASSERTION"]._serialized_end = 380
    _globals["_ATTRIBUTEREPORT"]._serialized_start = 383
    _globals["_ATTRIBUTEREPORT"]._serialized_end = 542
# @@protoc_insertion_point(module_scope)
