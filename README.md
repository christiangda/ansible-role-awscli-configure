# Ansible Role: christiangda.awscli

[![Build Status](https://travis-ci.org/christiangda/ansible-role-awscli_configure.svg?branch=master)](https://travis-ci.org/christiangda/ansible-role-awscli-configure)
[![Ansible Role](https://img.shields.io/ansible/role/44078.svg)](https://galaxy.ansible.com/christiangda/awscli_configure)

This role create the necessary files to [configure AWS Command Line Interface (awscli)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).

This roles is very basic, its only function is transform a variable defined in `yaml` format with the content of the `.aws/config` and `.aws/credentials` files to the `.ini` file format and put those in the place you want.

See the examples to understand it.

## Requirements

This role work on RedHat, CentOS, Debian and Ubuntu distributions

* RedHat
  * 6
  * 7
  * 8
* CentOS
  * 6
  * 7
  * 8
* Ubuntu
  * 14.*
  * 16.*
  * 18.*
  * 19.*
* Debian
  * jessie (8)
  * stretch (9)
  * buster (10)
  * sid (unstable)

To see the compatibility matrix of Python vs. Ansible see the project [Travis-CI build matrix](https://travis-ci.org/christiangda/ansible-role-awscli-configure)

## Role Variables

```yaml
# Define the path where AWS CLI ".aws"'s folder will be created.
# NOTE: The folder ".aws" will be created by the role, do not add it to the path
# By default this will be created in the $HOME path of the user who executes o become in ansible
# possible values:
# - https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html
# default value: "~/."
awscliconf_path: "~/."
```

```yaml
# If you use an "awscliconf_path" that doesn't exist in the target, you need to set
# this variable to "true", in another case the execution will fail
# NOTE: Unfortunately when you set this variable to "true", the role always sends "change" status.
# possible values:
# - true
# - false
# default value: false
awscliconf_recursive_path_creation: false
```

```yaml
# The owner user for the folder ".aws" that will be created inside the path defined in "awscliconf_path"
# possible values:
# - https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html
# default value: "root"
awscliconf_files_owner: "root"
```

```yaml
# The owner group for the folder ".aws" that will be created inside the path defined in "awscliconf_path"
# possible values:
# - https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html
# default value: "root"
awscliconf_files_group: "root"
```

```yaml
# This variable define the content of the two AWS CLI configuration files
# - .aws/config
# - .aws/credentials
# NOTE: If you don't set this variable, some default values will be sets
# possible values:
# - https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html
# default values:
#  config:
#    - default:
#        output: json
#
#  credentials:
#    - default:
#        aws_access_key_id: ''
#        aws_secret_access_key: ''
awscliconf_files: ""
```

## Dependencies

This role has not dependencies, but is important that you [install AWS Command Line Interface (awscli)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in order to make sense of this.

My role [christiangda.awscli](https://galaxy.ansible.com/christiangda/awscli) can help you to [install AWS Command Line Interface (awscli)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html).

## Example Playbook

### RedHat/CentOS, Ubuntu and Debian

If you have installed [AWS Command Line Interface (awscli)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) already

```yaml
- hosts: redhat-8
    gather_facts: True
    roles:
      - role: christiangda.awscli_configure
        vars:
          awscliconf_path: '/home/christian.gonzalez'
          awscliconf_files_owner: 'christian.gonzalez'
          awscliconf_files_group: 'christian.gonzalez'
          awscliconf_files:
            credentials:
              - default:
                  aws_access_key_id: '12345679'
                  aws_secret_access_key: '123456789'
            config:
              - default:
                  region: us-west-2
                  output: json
              - profile development:
                  role_arn: 'arn:aws:iam::123456789012:role/role-for-development'
                  mfa_serial: 'arn:aws:iam::11111111111:mfa/christian.gonzalez'
                  region: eu-west-1
                  source_profile: default

```

**When you have RedHat/CentOS 8 or Debian/Ubuntu target** and you don't have installed [AWS Command Line Interface (awscli)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) and wants to use my role [christiangda.awscli](https://galaxy.ansible.com/christiangda/awscli)

```yaml
- hosts: redhat-8
    gather_facts: True
    roles:
      - role: christiangda.awscli
      - role: christiangda.awscli_configure
        vars:
          awscliconf_files:
            credentials:
              - default:
                  aws_access_key_id: '12345679'
                  aws_secret_access_key: '123456789'
            config:
              - default:
                  region: us-west-2
                  output: json
              - profile development:
                  role_arn: 'arn:aws:iam::123456789012:role/role-for-development'
                  mfa_serial: 'arn:aws:iam::11111111111:mfa/christian.gonzalez'
                  region: eu-west-1
                  source_profile: default
```

**When you have RedHat/CentOS 6/7 target** and you don't have installed [AWS Command Line Interface (awscli)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) and [EPEL Repository](https://fedoraproject.org/wiki/EPEL) either, and wants to use my roles [christiangda.epel_role](https://galaxy.ansible.com/christiangda/epel_repo), [christiangda.awscli](https://galaxy.ansible.com/christiangda/awscli)

```yaml
- hosts: redhat-7
    gather_facts: True
    roles:
      - role: christiangda.epel_repo
      - role: christiangda.awscli
      - role: christiangda.awscli_configure
        vars:
          awscliconf_files:
            credentials:
              - default:
                  aws_access_key_id: '12345679'
                  aws_secret_access_key: '123456789'
            config:
              - default:
                  region: us-west-2
                  output: json
              - profile development:
                  role_arn: 'arn:aws:iam::123456789012:role/role-for-development'
                  mfa_serial: 'arn:aws:iam::11111111111:mfa/christian.gonzalez'
                  region: eu-west-1
                  source_profile: default
```

**When you have multiples OS targets and wants to install EPEL repository only in RedHat/CentOS 6/7** using my roles [christiangda.epel_role](https://galaxy.ansible.com/christiangda/epel_repo), [christiangda.awscli](https://galaxy.ansible.com/christiangda/awscli)

```yaml
- hosts: servers
    gather_facts: True
    roles:
    - role: christiangda.epel_repo
      when: >
        ansible_os_family == 'RedHat' and (
          ansible_distribution == 'CentOS' or
          ansible_distribution == 'RedHat'
        )
        and (
          ansible_distribution_major_version == '6' or
          ansible_distribution_major_version == '7'
        )
      changed_when: false
    - role: christiangda.awscli
    - role: christiangda.awscli_configure
      vars:
        awscliconf_files:
          credentials:
            - default:
                aws_access_key_id: '12345679'
                aws_secret_access_key: '123456789'

            - production-profile:
                aws_access_key_id: '12345679'
                aws_secret_access_key: '123456789'
          config:
            - default:
                region: us-west-2
                output: json
            - profile development:
                role_arn: arn:aws:iam::123456789012:role/role-name
                role_session_name: maria_garcia_role
                source_profile: production-profile
                aws_session_token: AQoEXAMPLEH4aoAH0gNCAPyJxz4BlCFFxWNE1OPTgk5TthT+FvwqnKwRcOIfrRh3c/LTo6UDdyJwOOvEVPvLXCrrrUtdnniCEXAMPLE/IvU1dYUg2RVAJBanLiHb4IgRmpRV3zrkuWJOgQs8IZZaIv2BXIa2R4Olgk
                s3:
                  max_concurrent_requests: 20
                  max_queue_size: 10000
                  multipart_threshold: 64MB
                  multipart_chunksize: 16MB
                  max_bandwidth: 50MB/s
                  use_accelerate_endpoint: true
                  addressing_style: path
                api_versions:
                  ec2: '2015-03-01'
                  cloudfront: '2015-09-17'
                tcp_keepalive: false
```

## Development / Contributing

This role is tested using [Molecule](https://molecule.readthedocs.io/en/latest/) and was developed using
[Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

**Prepare your environment**

**Python 3**

```bash
mkdir ansible-roles
cd ansible-roles/

python3 -m venv venv
source venv/bin/activate
pip install pip --upgrade
pip install ansible
pip install molecule">=2.22rc1"
pip install molecule[vagrant]
pip install selinux
pip install docker
pip install pytest
pip install pytest-mock
pip install pylint
pip install rope
pip install autopep8
pip install yamllint
pip install flake8
```

**Python 2.7**

Dependencies

```bash
sudo dnf install redhat-rpm-config
sudo dnf install python-devel
sudo dnf install libselinux-python
```

```bash
mkdir ansible-roles
cd ansible-roles/

python2.7 -m virtualenv venv
source venv/bin/activate
pip install pip --upgrade
pip install ansible
pip install molecule">=2.22rc1"
pip install molecule[vagrant]
pip install selinux
pip install docker
pip install pytest
pip install pytest-mock
pip install pylint
pip install rope
pip install autopep8
pip install yamllint
pip install flake8
```

**Clone the role repository and create symbolic link**

```bash
git clone https://github.com/christiangda/ansible-role-awscli-configure.git
ln -s ansible-role-awscli-configure christiangda.awscli_configure
cd christiangda.awscli_configure
```

**Execute the test**

Using docker in local

```bash
molecule test [--scenario-name default]
```

**Additionally if you want to test it using VMs, I have a very nice [ansible-playground project](https://github.com/christiangda/ansible-playground) that use Vagrant and VirtualBox, try it!.**

## License

This module is released under the GNU General Public License Version 3:

* [http://www.gnu.org/licenses/gpl-3.0-standalone.html](http://www.gnu.org/licenses/gpl-3.0-standalone.html)

## Author Information

* [Christian González Di Antonio](https://github.com/christiangda)
