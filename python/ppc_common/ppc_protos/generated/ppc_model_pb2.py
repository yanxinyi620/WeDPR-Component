# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ppc_model.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fppc_model.proto\x12\tppc.model\"|\n\x0cModelRequest\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x10\n\x08receiver\x18\x02 \x01(\t\x12\x0f\n\x07task_id\x18\x03 \x01(\t\x12\x0b\n\x03key\x18\x04 \x01(\t\x12\x0b\n\x03seq\x18\x05 \x01(\x03\x12\x11\n\tslice_num\x18\x06 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x07 \x01(\x0c\"3\n\x0c\x42\x61seResponse\x12\x12\n\nerror_code\x18\x01 \x01(\x03\x12\x0f\n\x07message\x18\x02 \x01(\t\"M\n\rModelResponse\x12.\n\rbase_response\x18\x01 \x01(\x0b\x32\x17.ppc.model.BaseResponse\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"#\n\rPlainBoolList\x12\x12\n\nplain_list\x18\x01 \x03(\x08\"\xb1\x01\n\rBestSplitInfo\x12\x0f\n\x07tree_id\x18\x01 \x01(\x03\x12\x0f\n\x07leaf_id\x18\x02 \x01(\x03\x12\x0f\n\x07\x66\x65\x61ture\x18\x03 \x01(\x03\x12\r\n\x05value\x18\x04 \x01(\x03\x12\x12\n\nagency_idx\x18\x05 \x01(\x03\x12\x16\n\x0e\x61gency_feature\x18\x06 \x01(\x03\x12\x11\n\tbest_gain\x18\x07 \x01(\x02\x12\x0e\n\x06w_left\x18\x08 \x01(\x02\x12\x0f\n\x07w_right\x18\t \x01(\x02\"3\n\x0bModelCipher\x12\x12\n\nciphertext\x18\x01 \x01(\x0c\x12\x10\n\x08\x65xponent\x18\x02 \x01(\x0c\"M\n\nCipherList\x12\x12\n\npublic_key\x18\x01 \x01(\x0c\x12+\n\x0b\x63ipher_list\x18\x02 \x03(\x0b\x32\x16.ppc.model.ModelCipher\"=\n\x0e\x43ipher1DimList\x12+\n\x0b\x63ipher_list\x18\x01 \x03(\x0b\x32\x16.ppc.model.ModelCipher\"W\n\x0e\x43ipher2DimList\x12\x12\n\npublic_key\x18\x01 \x01(\x0c\x12\x31\n\x0e\x63ipher_1d_list\x18\x02 \x03(\x0b\x32\x19.ppc.model.Cipher1DimList\"_\n\rEncAggrLabels\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x12\n\ncount_list\x18\x02 \x03(\x03\x12+\n\x0b\x63ipher_list\x18\x03 \x03(\x0b\x32\x16.ppc.model.ModelCipher\"_\n\x11\x45ncAggrLabelsList\x12\x12\n\npublic_key\x18\x01 \x01(\x0c\x12\x36\n\x14\x65nc_aggr_labels_list\x18\x02 \x03(\x0b\x32\x18.ppc.model.EncAggrLabels\"/\n\x10IterationRequest\x12\r\n\x05\x65poch\x18\x01 \x01(\x03\x12\x0c\n\x04stop\x18\x02 \x01(\x08\x32Y\n\x0cModelService\x12I\n\x12MessageInteraction\x12\x17.ppc.model.ModelRequest\x1a\x18.ppc.model.ModelResponse\"\x00\x42\x08P\x01\xa2\x02\x03PPCb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ppc_model_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'P\001\242\002\003PPC'
    _globals['_MODELREQUEST']._serialized_start = 30
    _globals['_MODELREQUEST']._serialized_end = 154
    _globals['_BASERESPONSE']._serialized_start = 156
    _globals['_BASERESPONSE']._serialized_end = 207
    _globals['_MODELRESPONSE']._serialized_start = 209
    _globals['_MODELRESPONSE']._serialized_end = 286
    _globals['_PLAINBOOLLIST']._serialized_start = 288
    _globals['_PLAINBOOLLIST']._serialized_end = 323
    _globals['_BESTSPLITINFO']._serialized_start = 326
    _globals['_BESTSPLITINFO']._serialized_end = 503
    _globals['_MODELCIPHER']._serialized_start = 505
    _globals['_MODELCIPHER']._serialized_end = 556
    _globals['_CIPHERLIST']._serialized_start = 558
    _globals['_CIPHERLIST']._serialized_end = 635
    _globals['_CIPHER1DIMLIST']._serialized_start = 637
    _globals['_CIPHER1DIMLIST']._serialized_end = 698
    _globals['_CIPHER2DIMLIST']._serialized_start = 700
    _globals['_CIPHER2DIMLIST']._serialized_end = 787
    _globals['_ENCAGGRLABELS']._serialized_start = 789
    _globals['_ENCAGGRLABELS']._serialized_end = 884
    _globals['_ENCAGGRLABELSLIST']._serialized_start = 886
    _globals['_ENCAGGRLABELSLIST']._serialized_end = 981
    _globals['_ITERATIONREQUEST']._serialized_start = 983
    _globals['_ITERATIONREQUEST']._serialized_end = 1030
    _globals['_MODELSERVICE']._serialized_start = 1032
    _globals['_MODELSERVICE']._serialized_end = 1121
# @@protoc_insertion_point(module_scope)
