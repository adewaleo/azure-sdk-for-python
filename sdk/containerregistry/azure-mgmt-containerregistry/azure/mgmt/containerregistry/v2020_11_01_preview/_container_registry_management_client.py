# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import ContainerRegistryManagementClientConfiguration
from .operations import ConnectedRegistriesOperations
from .operations import ExportPipelinesOperations
from .operations import RegistriesOperations
from .operations import ImportPipelinesOperations
from .operations import Operations
from .operations import PipelineRunsOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import ReplicationsOperations
from .operations import ScopeMapsOperations
from .operations import TokensOperations
from .operations import WebhooksOperations
from .operations import AgentPoolsOperations
from .operations import RunsOperations
from .operations import TaskRunsOperations
from .operations import TasksOperations
from . import models


class ContainerRegistryManagementClient(SDKClient):
    """ContainerRegistryManagementClient

    :ivar config: Configuration for client.
    :vartype config: ContainerRegistryManagementClientConfiguration

    :ivar connected_registries: ConnectedRegistries operations
    :vartype connected_registries: azure.mgmt.containerregistry.v2020_11_01_preview.operations.ConnectedRegistriesOperations
    :ivar export_pipelines: ExportPipelines operations
    :vartype export_pipelines: azure.mgmt.containerregistry.v2020_11_01_preview.operations.ExportPipelinesOperations
    :ivar registries: Registries operations
    :vartype registries: azure.mgmt.containerregistry.v2020_11_01_preview.operations.RegistriesOperations
    :ivar import_pipelines: ImportPipelines operations
    :vartype import_pipelines: azure.mgmt.containerregistry.v2020_11_01_preview.operations.ImportPipelinesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.containerregistry.v2020_11_01_preview.operations.Operations
    :ivar pipeline_runs: PipelineRuns operations
    :vartype pipeline_runs: azure.mgmt.containerregistry.v2020_11_01_preview.operations.PipelineRunsOperations
    :ivar private_endpoint_connections: PrivateEndpointConnections operations
    :vartype private_endpoint_connections: azure.mgmt.containerregistry.v2020_11_01_preview.operations.PrivateEndpointConnectionsOperations
    :ivar replications: Replications operations
    :vartype replications: azure.mgmt.containerregistry.v2020_11_01_preview.operations.ReplicationsOperations
    :ivar scope_maps: ScopeMaps operations
    :vartype scope_maps: azure.mgmt.containerregistry.v2020_11_01_preview.operations.ScopeMapsOperations
    :ivar tokens: Tokens operations
    :vartype tokens: azure.mgmt.containerregistry.v2020_11_01_preview.operations.TokensOperations
    :ivar webhooks: Webhooks operations
    :vartype webhooks: azure.mgmt.containerregistry.v2020_11_01_preview.operations.WebhooksOperations
    :ivar agent_pools: AgentPools operations
    :vartype agent_pools: azure.mgmt.containerregistry.v2020_11_01_preview.operations.AgentPoolsOperations
    :ivar runs: Runs operations
    :vartype runs: azure.mgmt.containerregistry.v2020_11_01_preview.operations.RunsOperations
    :ivar task_runs: TaskRuns operations
    :vartype task_runs: azure.mgmt.containerregistry.v2020_11_01_preview.operations.TaskRunsOperations
    :ivar tasks: Tasks operations
    :vartype tasks: azure.mgmt.containerregistry.v2020_11_01_preview.operations.TasksOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param filter: An OData filter expression that describes a subset of
     connectedRegistries to return. The parameters that can be filtered are
     parent.id (the resource id of the connectedRegistry parent), mode, and
     connectionState. The supported operator is eq.
    :type filter: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, filter=None, base_url=None):

        self.config = ContainerRegistryManagementClientConfiguration(credentials, subscription_id, filter, base_url)
        super(ContainerRegistryManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.connected_registries = ConnectedRegistriesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.export_pipelines = ExportPipelinesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.registries = RegistriesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.import_pipelines = ImportPipelinesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.pipeline_runs = PipelineRunsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.replications = ReplicationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.scope_maps = ScopeMapsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.tokens = TokensOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.webhooks = WebhooksOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.agent_pools = AgentPoolsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.runs = RunsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.task_runs = TaskRunsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.tasks = TasksOperations(
            self._client, self.config, self._serialize, self._deserialize)
