# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: embeddings.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x10\x65mbeddings.proto"K\n\x10\x45mbeddingRequest\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x12\n\nbatch_size\x18\x02 \x01(\x05\x12\x0f\n\x07strings\x18\x03 \x03(\t"%\n\x0b\x42\x61tchEmbeds\x12\x16\n\x06\x65mbeds\x18\x01 \x03(\x0b\x32\x06.Embed"\x16\n\x05\x45mbed\x12\r\n\x05\x65mbed\x18\x01 \x03(\x02\x32\x37\n\tEmbedding\x12*\n\x05\x45mbed\x12\x11.EmbeddingRequest\x1a\x0c.BatchEmbeds"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "embeddings_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_EMBEDDINGREQUEST"]._serialized_start = 20
    _globals["_EMBEDDINGREQUEST"]._serialized_end = 95
    _globals["_BATCHEMBEDS"]._serialized_start = 97
    _globals["_BATCHEMBEDS"]._serialized_end = 134
    _globals["_EMBED"]._serialized_start = 136
    _globals["_EMBED"]._serialized_end = 158
    _globals["_EMBEDDING"]._serialized_start = 160
    _globals["_EMBEDDING"]._serialized_end = 215
# @@protoc_insertion_point(module_scope)
