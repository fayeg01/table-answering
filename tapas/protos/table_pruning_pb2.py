# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tapas/protos/table_pruning.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tapas/protos/table_pruning.proto',
  package='language.tapas',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n tapas/protos/table_pruning.proto\x12\x0elanguage.tapas\"\xf7\x03\n\x04Loss\x12:\n\x0cunsupervised\x18\xc8\x01 \x01(\x0b\x32!.language.tapas.Loss.UnsupervisedH\x00\x12\x32\n\x05train\x18\x90\x03 \x01(\x0b\x32\".language.tapas.Loss.HardSelection\x12\x31\n\x04\x65val\x18\xf4\x03 \x01(\x0b\x32\".language.tapas.Loss.HardSelection\x12\'\n\x17\x61\x64\x64_classification_loss\x18\xd8\x04 \x01(\x08:\x05\x66\x61lse\x1a\x88\x01\n\rHardSelection\x12\x44\n\x0cselection_fn\x18\x01 \x01(\x0e\x32..language.tapas.Loss.HardSelection.SelectionFn\"1\n\x0bSelectionFn\x12\x07\n\x03\x41LL\x10\x00\x12\t\n\x05TOP_K\x10\x01\x12\x0e\n\nMASK_TOP_K\x10\x02\x1a\x8f\x01\n\x0cUnsupervised\x12H\n\x0eregularization\x18\x05 \x01(\x0e\x32\x30.language.tapas.Loss.Unsupervised.Regularization\"5\n\x0eRegularization\x12\x08\n\x04NONE\x10\x00\x12\x06\n\x02L1\x10\x01\x12\x06\n\x02L2\x10\x02\x12\t\n\x05L1_L2\x10\x03\x42\x06\n\x04loss\"`\n\x10\x41vgCosSimilarity\x12(\n\x19use_positional_embeddings\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\"\n\x04loss\x18\x03 \x01(\x0b\x32\x14.language.tapas.Loss\"\xeb\x01\n\x05TAPAS\x12\x32\n\tselection\x18\x02 \x01(\x0e\x32\x1f.language.tapas.TAPAS.Selection\x12\x18\n\x10\x62\x65rt_config_file\x18\x03 \x01(\t\x12\x1c\n\x14\x62\x65rt_init_checkpoint\x18\x04 \x01(\t\x12,\n\x1dreset_position_index_per_cell\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\"\n\x04loss\x18\x05 \x01(\x0b\x32\x14.language.tapas.Loss\"$\n\tSelection\x12\x0b\n\x07\x43OLUMNS\x10\x00\x12\n\n\x06TOKENS\x10\x01\"\r\n\x0b\x46irstTokens\"\xdf\x01\n\x11TablePruningModel\x12\x16\n\x0emax_num_tokens\x18\x01 \x01(\x05\x12>\n\x12\x61vg_cos_similarity\x18\x02 \x01(\x0b\x32 .language.tapas.AvgCosSimilarityH\x00\x12&\n\x05tapas\x18\x03 \x01(\x0b\x32\x15.language.tapas.TAPASH\x00\x12\x33\n\x0c\x66irst_tokens\x18\x04 \x01(\x0b\x32\x1b.language.tapas.FirstTokensH\x00\x42\x15\n\x13table_pruning_model')
)



_LOSS_HARDSELECTION_SELECTIONFN = _descriptor.EnumDescriptor(
  name='SelectionFn',
  full_name='language.tapas.Loss.HardSelection.SelectionFn',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOP_K', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MASK_TOP_K', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=353,
  serialized_end=402,
)
_sym_db.RegisterEnumDescriptor(_LOSS_HARDSELECTION_SELECTIONFN)

_LOSS_UNSUPERVISED_REGULARIZATION = _descriptor.EnumDescriptor(
  name='Regularization',
  full_name='language.tapas.Loss.Unsupervised.Regularization',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='L1', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='L2', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='L1_L2', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=495,
  serialized_end=548,
)
_sym_db.RegisterEnumDescriptor(_LOSS_UNSUPERVISED_REGULARIZATION)

_TAPAS_SELECTION = _descriptor.EnumDescriptor(
  name='Selection',
  full_name='language.tapas.TAPAS.Selection',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COLUMNS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOKENS', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=856,
  serialized_end=892,
)
_sym_db.RegisterEnumDescriptor(_TAPAS_SELECTION)


_LOSS_HARDSELECTION = _descriptor.Descriptor(
  name='HardSelection',
  full_name='language.tapas.Loss.HardSelection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='selection_fn', full_name='language.tapas.Loss.HardSelection.selection_fn', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LOSS_HARDSELECTION_SELECTIONFN,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=402,
)

_LOSS_UNSUPERVISED = _descriptor.Descriptor(
  name='Unsupervised',
  full_name='language.tapas.Loss.Unsupervised',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='regularization', full_name='language.tapas.Loss.Unsupervised.regularization', index=0,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LOSS_UNSUPERVISED_REGULARIZATION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=405,
  serialized_end=548,
)

_LOSS = _descriptor.Descriptor(
  name='Loss',
  full_name='language.tapas.Loss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unsupervised', full_name='language.tapas.Loss.unsupervised', index=0,
      number=200, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='train', full_name='language.tapas.Loss.train', index=1,
      number=400, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eval', full_name='language.tapas.Loss.eval', index=2,
      number=500, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='add_classification_loss', full_name='language.tapas.Loss.add_classification_loss', index=3,
      number=600, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LOSS_HARDSELECTION, _LOSS_UNSUPERVISED, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='loss', full_name='language.tapas.Loss.loss',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=53,
  serialized_end=556,
)


_AVGCOSSIMILARITY = _descriptor.Descriptor(
  name='AvgCosSimilarity',
  full_name='language.tapas.AvgCosSimilarity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='use_positional_embeddings', full_name='language.tapas.AvgCosSimilarity.use_positional_embeddings', index=0,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss', full_name='language.tapas.AvgCosSimilarity.loss', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=558,
  serialized_end=654,
)


_TAPAS = _descriptor.Descriptor(
  name='TAPAS',
  full_name='language.tapas.TAPAS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='selection', full_name='language.tapas.TAPAS.selection', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bert_config_file', full_name='language.tapas.TAPAS.bert_config_file', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bert_init_checkpoint', full_name='language.tapas.TAPAS.bert_init_checkpoint', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reset_position_index_per_cell', full_name='language.tapas.TAPAS.reset_position_index_per_cell', index=3,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss', full_name='language.tapas.TAPAS.loss', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TAPAS_SELECTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=657,
  serialized_end=892,
)


_FIRSTTOKENS = _descriptor.Descriptor(
  name='FirstTokens',
  full_name='language.tapas.FirstTokens',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=894,
  serialized_end=907,
)


_TABLEPRUNINGMODEL = _descriptor.Descriptor(
  name='TablePruningModel',
  full_name='language.tapas.TablePruningModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_num_tokens', full_name='language.tapas.TablePruningModel.max_num_tokens', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avg_cos_similarity', full_name='language.tapas.TablePruningModel.avg_cos_similarity', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tapas', full_name='language.tapas.TablePruningModel.tapas', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_tokens', full_name='language.tapas.TablePruningModel.first_tokens', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='table_pruning_model', full_name='language.tapas.TablePruningModel.table_pruning_model',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=910,
  serialized_end=1133,
)

_LOSS_HARDSELECTION.fields_by_name['selection_fn'].enum_type = _LOSS_HARDSELECTION_SELECTIONFN
_LOSS_HARDSELECTION.containing_type = _LOSS
_LOSS_HARDSELECTION_SELECTIONFN.containing_type = _LOSS_HARDSELECTION
_LOSS_UNSUPERVISED.fields_by_name['regularization'].enum_type = _LOSS_UNSUPERVISED_REGULARIZATION
_LOSS_UNSUPERVISED.containing_type = _LOSS
_LOSS_UNSUPERVISED_REGULARIZATION.containing_type = _LOSS_UNSUPERVISED
_LOSS.fields_by_name['unsupervised'].message_type = _LOSS_UNSUPERVISED
_LOSS.fields_by_name['train'].message_type = _LOSS_HARDSELECTION
_LOSS.fields_by_name['eval'].message_type = _LOSS_HARDSELECTION
_LOSS.oneofs_by_name['loss'].fields.append(
  _LOSS.fields_by_name['unsupervised'])
_LOSS.fields_by_name['unsupervised'].containing_oneof = _LOSS.oneofs_by_name['loss']
_AVGCOSSIMILARITY.fields_by_name['loss'].message_type = _LOSS
_TAPAS.fields_by_name['selection'].enum_type = _TAPAS_SELECTION
_TAPAS.fields_by_name['loss'].message_type = _LOSS
_TAPAS_SELECTION.containing_type = _TAPAS
_TABLEPRUNINGMODEL.fields_by_name['avg_cos_similarity'].message_type = _AVGCOSSIMILARITY
_TABLEPRUNINGMODEL.fields_by_name['tapas'].message_type = _TAPAS
_TABLEPRUNINGMODEL.fields_by_name['first_tokens'].message_type = _FIRSTTOKENS
_TABLEPRUNINGMODEL.oneofs_by_name['table_pruning_model'].fields.append(
  _TABLEPRUNINGMODEL.fields_by_name['avg_cos_similarity'])
_TABLEPRUNINGMODEL.fields_by_name['avg_cos_similarity'].containing_oneof = _TABLEPRUNINGMODEL.oneofs_by_name['table_pruning_model']
_TABLEPRUNINGMODEL.oneofs_by_name['table_pruning_model'].fields.append(
  _TABLEPRUNINGMODEL.fields_by_name['tapas'])
_TABLEPRUNINGMODEL.fields_by_name['tapas'].containing_oneof = _TABLEPRUNINGMODEL.oneofs_by_name['table_pruning_model']
_TABLEPRUNINGMODEL.oneofs_by_name['table_pruning_model'].fields.append(
  _TABLEPRUNINGMODEL.fields_by_name['first_tokens'])
_TABLEPRUNINGMODEL.fields_by_name['first_tokens'].containing_oneof = _TABLEPRUNINGMODEL.oneofs_by_name['table_pruning_model']
DESCRIPTOR.message_types_by_name['Loss'] = _LOSS
DESCRIPTOR.message_types_by_name['AvgCosSimilarity'] = _AVGCOSSIMILARITY
DESCRIPTOR.message_types_by_name['TAPAS'] = _TAPAS
DESCRIPTOR.message_types_by_name['FirstTokens'] = _FIRSTTOKENS
DESCRIPTOR.message_types_by_name['TablePruningModel'] = _TABLEPRUNINGMODEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Loss = _reflection.GeneratedProtocolMessageType('Loss', (_message.Message,), dict(

  HardSelection = _reflection.GeneratedProtocolMessageType('HardSelection', (_message.Message,), dict(
    DESCRIPTOR = _LOSS_HARDSELECTION,
    __module__ = 'tapas.protos.table_pruning_pb2'
    # @@protoc_insertion_point(class_scope:language.tapas.Loss.HardSelection)
    ))
  ,

  Unsupervised = _reflection.GeneratedProtocolMessageType('Unsupervised', (_message.Message,), dict(
    DESCRIPTOR = _LOSS_UNSUPERVISED,
    __module__ = 'tapas.protos.table_pruning_pb2'
    # @@protoc_insertion_point(class_scope:language.tapas.Loss.Unsupervised)
    ))
  ,
  DESCRIPTOR = _LOSS,
  __module__ = 'tapas.protos.table_pruning_pb2'
  # @@protoc_insertion_point(class_scope:language.tapas.Loss)
  ))
_sym_db.RegisterMessage(Loss)
_sym_db.RegisterMessage(Loss.HardSelection)
_sym_db.RegisterMessage(Loss.Unsupervised)

AvgCosSimilarity = _reflection.GeneratedProtocolMessageType('AvgCosSimilarity', (_message.Message,), dict(
  DESCRIPTOR = _AVGCOSSIMILARITY,
  __module__ = 'tapas.protos.table_pruning_pb2'
  # @@protoc_insertion_point(class_scope:language.tapas.AvgCosSimilarity)
  ))
_sym_db.RegisterMessage(AvgCosSimilarity)

TAPAS = _reflection.GeneratedProtocolMessageType('TAPAS', (_message.Message,), dict(
  DESCRIPTOR = _TAPAS,
  __module__ = 'tapas.protos.table_pruning_pb2'
  # @@protoc_insertion_point(class_scope:language.tapas.TAPAS)
  ))
_sym_db.RegisterMessage(TAPAS)

FirstTokens = _reflection.GeneratedProtocolMessageType('FirstTokens', (_message.Message,), dict(
  DESCRIPTOR = _FIRSTTOKENS,
  __module__ = 'tapas.protos.table_pruning_pb2'
  # @@protoc_insertion_point(class_scope:language.tapas.FirstTokens)
  ))
_sym_db.RegisterMessage(FirstTokens)

TablePruningModel = _reflection.GeneratedProtocolMessageType('TablePruningModel', (_message.Message,), dict(
  DESCRIPTOR = _TABLEPRUNINGMODEL,
  __module__ = 'tapas.protos.table_pruning_pb2'
  # @@protoc_insertion_point(class_scope:language.tapas.TablePruningModel)
  ))
_sym_db.RegisterMessage(TablePruningModel)


# @@protoc_insertion_point(module_scope)
