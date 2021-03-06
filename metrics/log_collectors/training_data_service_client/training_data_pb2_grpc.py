# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import training_data_pb2 as training__data__pb2


class TrainingDataStub(object):
  """import "google/api/annotations.proto";

  // See https://developers.google.com/protocol-buffers/docs/proto3#any
  // and https://github.com/google/protobuf/blob/master/src/google/protobuf/any.proto
  import "google/protobuf/any.proto";

  Service to store evaluation metrics
  ===== GET ENDPOINTS, for external fetch =============
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetLogs = channel.unary_stream(
        '/grpc.training.data.v1.TrainingData/GetLogs',
        request_serializer=training__data__pb2.Query.SerializeToString,
        response_deserializer=training__data__pb2.LogLine.FromString,
        )
    self.GetEMetrics = channel.unary_stream(
        '/grpc.training.data.v1.TrainingData/GetEMetrics',
        request_serializer=training__data__pb2.Query.SerializeToString,
        response_deserializer=training__data__pb2.EMetrics.FromString,
        )
    self.AddEMetrics = channel.unary_unary(
        '/grpc.training.data.v1.TrainingData/AddEMetrics',
        request_serializer=training__data__pb2.EMetrics.SerializeToString,
        response_deserializer=training__data__pb2.AddResponse.FromString,
        )
    self.AddLogLine = channel.unary_unary(
        '/grpc.training.data.v1.TrainingData/AddLogLine',
        request_serializer=training__data__pb2.LogLine.SerializeToString,
        response_deserializer=training__data__pb2.AddResponse.FromString,
        )
    self.AddEMetricsBatch = channel.unary_unary(
        '/grpc.training.data.v1.TrainingData/AddEMetricsBatch',
        request_serializer=training__data__pb2.EMetricsBatch.SerializeToString,
        response_deserializer=training__data__pb2.AddResponse.FromString,
        )
    self.AddLogLineBatch = channel.unary_unary(
        '/grpc.training.data.v1.TrainingData/AddLogLineBatch',
        request_serializer=training__data__pb2.LogLineBatch.SerializeToString,
        response_deserializer=training__data__pb2.AddResponse.FromString,
        )
    self.DeleteEMetrics = channel.unary_unary(
        '/grpc.training.data.v1.TrainingData/DeleteEMetrics',
        request_serializer=training__data__pb2.Query.SerializeToString,
        response_deserializer=training__data__pb2.DeleteResponse.FromString,
        )
    self.DeleteLogLines = channel.unary_unary(
        '/grpc.training.data.v1.TrainingData/DeleteLogLines',
        request_serializer=training__data__pb2.Query.SerializeToString,
        response_deserializer=training__data__pb2.DeleteResponse.FromString,
        )
    self.DeleteJob = channel.unary_unary(
        '/grpc.training.data.v1.TrainingData/DeleteJob',
        request_serializer=training__data__pb2.Query.SerializeToString,
        response_deserializer=training__data__pb2.DeleteResponse.FromString,
        )
    self.Hello = channel.unary_unary(
        '/grpc.training.data.v1.TrainingData/Hello',
        request_serializer=training__data__pb2.Empty.SerializeToString,
        response_deserializer=training__data__pb2.HelloResponse.FromString,
        )


class TrainingDataServicer(object):
  """import "google/api/annotations.proto";

  // See https://developers.google.com/protocol-buffers/docs/proto3#any
  // and https://github.com/google/protobuf/blob/master/src/google/protobuf/any.proto
  import "google/protobuf/any.proto";

  Service to store evaluation metrics
  ===== GET ENDPOINTS, for external fetch =============
  """

  def GetLogs(self, request, context):
    """Get loglines, based on query
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEMetrics(self, request, context):
    """Get evaluation metrics records, based on query
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddEMetrics(self, request, context):
    """===== UPDATE ENDPOINTS, for internal use only =========
    (Strip these from the proto for external client generation!)

    Add evaluation metrics record
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddLogLine(self, request, context):
    """Add log line record
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddEMetricsBatch(self, request, context):
    """Add evaluation metrics record
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddLogLineBatch(self, request, context):
    """Add log line record
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteEMetrics(self, request, context):
    """Delete all evaluation metrics belonging to a training job or user id
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteLogLines(self, request, context):
    """Delete all log lines belonging to a training job or user id
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteJob(self, request, context):
    """Delete all log lines belonging to a training job or user id
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Hello(self, request, context):
    """===== In case you want it to say "Hello" =========
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TrainingDataServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetLogs': grpc.unary_stream_rpc_method_handler(
          servicer.GetLogs,
          request_deserializer=training__data__pb2.Query.FromString,
          response_serializer=training__data__pb2.LogLine.SerializeToString,
      ),
      'GetEMetrics': grpc.unary_stream_rpc_method_handler(
          servicer.GetEMetrics,
          request_deserializer=training__data__pb2.Query.FromString,
          response_serializer=training__data__pb2.EMetrics.SerializeToString,
      ),
      'AddEMetrics': grpc.unary_unary_rpc_method_handler(
          servicer.AddEMetrics,
          request_deserializer=training__data__pb2.EMetrics.FromString,
          response_serializer=training__data__pb2.AddResponse.SerializeToString,
      ),
      'AddLogLine': grpc.unary_unary_rpc_method_handler(
          servicer.AddLogLine,
          request_deserializer=training__data__pb2.LogLine.FromString,
          response_serializer=training__data__pb2.AddResponse.SerializeToString,
      ),
      'AddEMetricsBatch': grpc.unary_unary_rpc_method_handler(
          servicer.AddEMetricsBatch,
          request_deserializer=training__data__pb2.EMetricsBatch.FromString,
          response_serializer=training__data__pb2.AddResponse.SerializeToString,
      ),
      'AddLogLineBatch': grpc.unary_unary_rpc_method_handler(
          servicer.AddLogLineBatch,
          request_deserializer=training__data__pb2.LogLineBatch.FromString,
          response_serializer=training__data__pb2.AddResponse.SerializeToString,
      ),
      'DeleteEMetrics': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteEMetrics,
          request_deserializer=training__data__pb2.Query.FromString,
          response_serializer=training__data__pb2.DeleteResponse.SerializeToString,
      ),
      'DeleteLogLines': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteLogLines,
          request_deserializer=training__data__pb2.Query.FromString,
          response_serializer=training__data__pb2.DeleteResponse.SerializeToString,
      ),
      'DeleteJob': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteJob,
          request_deserializer=training__data__pb2.Query.FromString,
          response_serializer=training__data__pb2.DeleteResponse.SerializeToString,
      ),
      'Hello': grpc.unary_unary_rpc_method_handler(
          servicer.Hello,
          request_deserializer=training__data__pb2.Empty.FromString,
          response_serializer=training__data__pb2.HelloResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.training.data.v1.TrainingData', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
