# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse

class PipelinesBuildDefinitionTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    def test_build_definition_listShow(self):
        self.cmd('az dev configure --defaults instance=https://AzureDevOpsCliTest.visualstudio.com project=buildtests')
        self.cmd('az dev login --token vj3ep2pg3fo6vxsklkwvkiy23dkbyynmfpg4vb66xniwr23zylla')
        build_definition_name = 'BuildTests Definition1'

        #list build definition
        list_build_definition_command = 'az pipelines build definition list --detect off --output json'
        list_build_definition_output = self.cmd(list_build_definition_command).get_output_in_json()
        assert len(list_build_definition_output) > 0
        for build_definition in list_build_definition_output:
            if(build_definition["name"] == build_definition_name):
                build_definition_id = build_definition["id"]
            assert build_definition["id"] > 0


        #show build definition
        show_build_definition_command = 'az pipelines build definition show --definition-id ' + str(build_definition_id) + ' --detect off --output json'
        show_build_definition_output = self.cmd(show_build_definition_command).get_output_in_json()
        assert len(show_build_definition_output) > 0
        assert show_build_definition_output["name"] == build_definition_name
   