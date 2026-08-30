from client import AutonomousSoftwareEngineeringLifecycleAgentClient

def main():
    client = AutonomousSoftwareEngineeringLifecycleAgentClient()
    res = client.execute_engineering_task('https://github.com/enterprise/core/issues/102')
    print('Autonomous SWE Lifecycle Agent: ' + res['devin_execution_id'])
    print('Sandbox Ready: ' + str(res['environment_sandboxed']) + ' | Commands Executed: ' + str(res['terminal_commands_executed']))
    print('Browser Checks: ' + str(res['browser_visual_verifications_count']) + ' | CI Status: ' + res['ci_build_status'])
    print('PR Created: ' + res['pull_request_created_url'])

if __name__ == '__main__':
    main()
