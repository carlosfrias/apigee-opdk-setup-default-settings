from subprocess import Popen
from ansible.module_utils.basic import *

def getenforce():
    results = Popen('getenforce', stdout=subprocess.PIPE)
    return results.stdout.readline().strip()


def main():
    module = AnsibleModule(argument_spec=dict())
    module.exit_json(changed = True,
                     ansible_facts = dict(
                             selinux_status=getenforce()
                     ))



if __name__ == '__main__':
    main()