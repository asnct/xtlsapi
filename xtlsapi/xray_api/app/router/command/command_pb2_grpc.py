# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from xtlsapi.xray_api.app.router.command import command_pb2 as app_dot_router_dot_command_dot_command__pb2


class RoutingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeRoutingStats = channel.unary_stream(
                '/xray.app.router.command.RoutingService/SubscribeRoutingStats',
                request_serializer=app_dot_router_dot_command_dot_command__pb2.SubscribeRoutingStatsRequest.SerializeToString,
                response_deserializer=app_dot_router_dot_command_dot_command__pb2.RoutingContext.FromString,
                )
        self.TestRoute = channel.unary_unary(
                '/xray.app.router.command.RoutingService/TestRoute',
                request_serializer=app_dot_router_dot_command_dot_command__pb2.TestRouteRequest.SerializeToString,
                response_deserializer=app_dot_router_dot_command_dot_command__pb2.RoutingContext.FromString,
                )


class RoutingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SubscribeRoutingStats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestRoute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RoutingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeRoutingStats': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeRoutingStats,
                    request_deserializer=app_dot_router_dot_command_dot_command__pb2.SubscribeRoutingStatsRequest.FromString,
                    response_serializer=app_dot_router_dot_command_dot_command__pb2.RoutingContext.SerializeToString,
            ),
            'TestRoute': grpc.unary_unary_rpc_method_handler(
                    servicer.TestRoute,
                    request_deserializer=app_dot_router_dot_command_dot_command__pb2.TestRouteRequest.FromString,
                    response_serializer=app_dot_router_dot_command_dot_command__pb2.RoutingContext.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'xray.app.router.command.RoutingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RoutingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SubscribeRoutingStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/xray.app.router.command.RoutingService/SubscribeRoutingStats',
            app_dot_router_dot_command_dot_command__pb2.SubscribeRoutingStatsRequest.SerializeToString,
            app_dot_router_dot_command_dot_command__pb2.RoutingContext.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestRoute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/xray.app.router.command.RoutingService/TestRoute',
            app_dot_router_dot_command_dot_command__pb2.TestRouteRequest.SerializeToString,
            app_dot_router_dot_command_dot_command__pb2.RoutingContext.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
