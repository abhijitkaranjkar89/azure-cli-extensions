# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from azure.cli.core.commands import AzCommandGroup
from azext_communication.generated._help import helps  # pylint: disable=unused-import
try:
    from azext_communication.manual._help import helps  # pylint: disable=reimported
except ImportError:
    pass


class CommunicationServiceManagementClientCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azext_communication.generated._client_factory import cf_communication_cl
        communication_custom = CliCommandType(
            operations_tmpl='azext_communication.custom#{}',
            client_factory=cf_communication_cl)
        parent = super()
        parent.__init__(cli_ctx=cli_ctx, custom_command_type=communication_custom,
                        command_group_cls=CommunicationCommandGroup)

    def load_command_table(self, args):
        from azext_communication.generated.commands import load_command_table
        load_command_table(self, args)
        try:
            from azext_communication.manual.commands import load_command_table as load_command_table_manual
            load_command_table_manual(self, args)
        except ImportError:
            pass
        return self.command_table

    def load_arguments(self, command):
        from azext_communication.generated._params import load_arguments
        load_arguments(self, command)
        try:
            from azext_communication.manual._params import load_arguments as load_arguments_manual
            load_arguments_manual(self, command)
        except ImportError:
            pass


class CommunicationCommandGroup(AzCommandGroup):

    def communication_custom_command(self, name, method_name, **kwargs):
        command_name = self.custom_command(name, method_name, **kwargs)
        self._register_data_plane_account_arguments(command_name)

    def _register_data_plane_account_arguments(self, command_name):
        """ Add parameters required to create a communication client """
        from .manual._validators import validate_client_parameters

        command = self.command_loader.command_table.get(command_name, None)

        if not command:
            return

        group_name = 'communication'
        command.add_argument('connection_string', '--connection-string', required=False, default=None,
                             validator=validate_client_parameters, arg_group=group_name,
                             help='Communication connection string. Environment variable: '
                                  'AZURE_COMMUNICATION_CONNECTION_STRING')


COMMAND_LOADER_CLS = CommunicationServiceManagementClientCommandsLoader
