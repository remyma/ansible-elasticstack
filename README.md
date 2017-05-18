# Ansible Elasticstack Root

This role installs common prerequisites for all elastic products (elasticsearch, logstash, beats, kibana) :
* Version of elatic product to use
* Install java with compatible version

## Requirements

* *java* : elastic products needs java to run. This role can handle java install for you. But you can also install it on your own.

## Role Variables

| Variable     | Default       | Description    |
| ------------ | ------------- | -------------- |
| elastic_java_install | true | true to install java / false if java is already installed on you own |
| elastic_update_java | false | if true, will update java |
| elastic_use_repository | true | if true, install elastic products from repository |
| elastic_major_version | 5.x | Major version of elastic product to install |
| elastic_version | 5.2.2 | Version of elastic product to install |

# Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

## Example Playbook

### Basic install

    - hosts: elastic-servers
      roles:
        - { role: ansible-elasticstack-root }

## License

BSD
