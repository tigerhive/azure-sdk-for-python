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

from .resource_py3 import Resource


class ExportExecution(Resource):
    """A export execution.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :param execution_type: The type of the export execution. Possible values
     include: 'OnDemand', 'Scheduled'
    :type execution_type: str or
     ~azure.mgmt.costmanagement.models.ExecutionType
    :param status: The status of the export execution. Possible values
     include: 'Queued', 'InProgress', 'Completed', 'Failed', 'Timeout',
     'NewDataNotAvailable', 'DataNotAvailable'
    :type status: str or ~azure.mgmt.costmanagement.models.ExecutionStatus
    :param submitted_by: The identifier for the entity that executed the
     export. For OnDemand executions, it is the email id. For Scheduled
     executions, it is the constant value - System.
    :type submitted_by: str
    :param submitted_time: The time when export was queued to be executed.
    :type submitted_time: datetime
    :param processing_start_time: The time when export was picked up to be
     executed.
    :type processing_start_time: datetime
    :param processing_end_time: The time when export execution finished.
    :type processing_end_time: datetime
    :param file_name: The name of the file export got written to.
    :type file_name: str
    :param run_settings:
    :type run_settings:
     ~azure.mgmt.costmanagement.models.CommonExportProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tags': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'execution_type': {'key': 'properties.executionType', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'submitted_by': {'key': 'properties.submittedBy', 'type': 'str'},
        'submitted_time': {'key': 'properties.submittedTime', 'type': 'iso-8601'},
        'processing_start_time': {'key': 'properties.processingStartTime', 'type': 'iso-8601'},
        'processing_end_time': {'key': 'properties.processingEndTime', 'type': 'iso-8601'},
        'file_name': {'key': 'properties.fileName', 'type': 'str'},
        'run_settings': {'key': 'properties.runSettings', 'type': 'CommonExportProperties'},
    }

    def __init__(self, *, execution_type=None, status=None, submitted_by: str=None, submitted_time=None, processing_start_time=None, processing_end_time=None, file_name: str=None, run_settings=None, **kwargs) -> None:
        super(ExportExecution, self).__init__(**kwargs)
        self.execution_type = execution_type
        self.status = status
        self.submitted_by = submitted_by
        self.submitted_time = submitted_time
        self.processing_start_time = processing_start_time
        self.processing_end_time = processing_end_time
        self.file_name = file_name
        self.run_settings = run_settings
