import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_java_installed(Command):
    java_version_cmd = Command(
        "java -version 2>&1 | grep version | awk '{print $3}' | sed 's/\"//g'"
    )
    assert java_version_cmd.stdout >= '1.8'
