"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.struct_pb2
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class DoActionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...

    def __init__(self, *, name: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___DoActionRequest = DoActionRequest

class DoActionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self) -> None:
        ...
global___DoActionResponse = DoActionResponse

class ResourceRunCommandRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    COMMAND_NAME_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    'Note(erd): okay in v1 because names are unique. v2 should be a VRN'
    command_name: typing.Text = ...

    @property
    def args(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, resource_name: typing.Text=..., command_name: typing.Text=..., args: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['args', b'args']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['args', b'args', 'command_name', b'command_name', 'resource_name', b'resource_name']) -> None:
        ...
global___ResourceRunCommandRequest = ResourceRunCommandRequest

class ResourceRunCommandResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULT_FIELD_NUMBER: builtins.int

    @property
    def result(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, result: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['result', b'result']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['result', b'result']) -> None:
        ...
global___ResourceRunCommandResponse = ResourceRunCommandResponse