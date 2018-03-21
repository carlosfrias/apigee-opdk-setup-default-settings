OPDK Setup Default Settings
===========================

This role provides a set of default attributes that are persisted to the local Ansible cache and are used to install the 
Apigee OPDK. 

Requirements
------------

No requirements

Role Variables
--------------
    
| Variable Name | Default Value | Description |
|---------------|---------------|-------------|
| jdk_version | '1.8' | Target Java JDK version |
| java_home | /usr/lib/jvm/java-openjdk | System file path to use in JAVA_HOME |
| opdk_user_name |  '' | OPDK OS user name |
| opdk_group_name |  '' | OPDK OS group name|
| opdk_user_email | '' | OPDK User Email |
| opdk_user_pass | '' | OPDK User Password |
| opdk_user_home | /home/{{ opdk_user_name }} | Home folder of the Apigee user |
| admin_user | '{{ opdk_user_name }}' | Apigee admin user name |
| admin_pass | '{{ opdk_user_name }}' | Apigee admin user password |
| opdk_version |  '4.18.01' | Default Apigee Edge Private Cloud Version |
| apigee_mirror_version | '4.18.01' | Default version of the Apigee mirror to use |
| opdk_installer_path | "/tmp/edge" | Apigee staging installation folder |
| apigee_data_backup_archive_name | apigee_data_backup.tar.gz | Default name of the backup archive of the apigee data folder |
| apigee_archive_storage_folder | '{{ opdk_installer_path }}' | Default folder in which the apigee data backup archive will be stored. |
| apigee_installation_home | /opt/apigee | Default apigee installation home |
| apigee_service | '{{ apigee_installation_home }}/apigee-service/bin/apigee-service' | Apigee service command for 4.16.xx |
| nodetool | '{{ apigee_installation_home }}/apigee-cassandra/bin/nodetool' | Cassandra nodetool command |
| apigee_setup | '{{ apigee_installation_home }}/apigee-setup/bin/setup.sh' | Apigee setup command for 4.16.xx |
| apigee_update | '{{ apigee_installation_home }}/apigee-setup/bin/update.sh' | Apigee update command for 4.16.xx |
| apigee_all | '{{ apigee_installation_home }}/apigee-service/bin/apigee-all' | Apigee all command for 4.16.xx |
| opdk_license_target_file_path | "{{ opdk_installer_path }}/license.conf" | Apigee license file path |
| opdk_license_source_file_name | '~/.apigee/license.txt' | Apigee license file provided by customer |
| opdk_installation_config_file | "{{ opdk_installer_path }}/silent-install.conf" | Apigee silent installation configuration file |
| provided_response_file | '' | Silent installation configuration file that is provided manually |
| apigee_validate_config_file | '{{ opdk_installer_path }}/apigee-validate.conf' | Apigee validate config file path |
| apigee_repo_user | '{{ opdk_user_name }}' | Apigee bootstrap download user name |
| apigee_repo_uri | 'software.apigee.com' | Apigee bootstrap download uri |
| apigee_repo_url | 'https://{{ apigee_repo_uri }}' | Apigee bootstrap download url |
| copy_archive | yes | Choose whether to copy the Apigee Mirror archive from your control machine or use an existing archive on the server |
| archive_folder | /tmp/ | Storage folder for the Apigee archive |
| archive_name | apigee-{{ opdk_version }}.tar.gz | Apigee archive that is created when a mirror is used. |
| archive_path | '{{ apigee_installation_home }}/data/apigee-mirror/{{ archive_name }}' | Path to the Apigee archive that is created by apigee-mirror package |
| mp_pod | gateway | Apigee edge default pod for silent-config file |
    
Apigee Edge Ports

    cassandra_jmx_port: 7199
    cassandra_thrift_client_port: 9160
    cassandra_cql_native_port: 9042
    cassandra_non_ssl_gossip_port: 7000
    cassandra_ssl_gossip_port: 7001
    
    zk_data_port: 2181
    zk_leader_port: 2888
    zk_voter_port: 3888
    
    mp_int_mgmt_port: 4528
    mp_ext_mgmt_port: 8082
    mp_jmx_port: 1101
    mp_router_port: 8998
    
    ms_jmx_port: 1099
    ms_ext_mgmt_port: 8080
    
    router_jmx_port: 1100
    router_ext_mgmt_port: 8081
    router_int_mgmt_port: 4527
    
    qpid_jmx_port: 1102
    qpid_int_mgmt_port: 4529
    qpid_messaging_port: 5672
    qpid_ext_mgmt_port: 8083
    
    pg_jmx_port: 1103
    pg_int_mgmt_port: 4530
    pg_db_port: 5432
    pg_ext_mgmt_port: 8084
    
    ui_http_port: 9000
    
    edge_proxy_port: 9001
    
    ldap_data_port: 10389
    
    influxdb_system_port: 25826
    influxdb_port: 8086
    
    grafana_username: ''
    grafana_password: ''
    
Default collectd installation file
   
    collectd_installation_config: collectd-installation.conf

Default influxdb host

    influxdb_host: 127.0.0.1
    
Local folder in which to store logs and config files

    conf_logs_dir: planet_resources
 
Organization name used in Edge and Baas setups

    org_name: opdk

Default for creating a new user in org

    new_user: 'y'

Default for first_name in creating new user

    first_name: Opdk

Default for last_name in creating new user

    last_name: User

Virtual host port for the org

    virtual_host_port: 9001

Virtual Host name for the org

    virtual_host_name: default

Virtual host alias

    virtual_host_alias: '127.0.0.1'

Environment name

    env_name: test

Default analytics group

    ax_group: axgroup001

Default onboarding provisioning file name

    onboarding_config: 'apigee-provision.conf'

Default onboarding provisioning file path

    onboarding_config_file_path: "{{ opdk_installer_path }}/{{ onboarding_config }}"

Default onboarding provisioning directory

    apigee_provision_dir: '{{ apigee_installation_home }}/apigee-provision'
    
Default location and name of the Baas Silent Install file

    opdk_baas_silent_install_file_path: /tmp/baas-silent-install.conf
    
Baas silent install file provided by customer

    opdk_baas_provided_silent_install_file: ''
    
Define the API BaaS administrator account.

    baas_admin_name: ''
    baas_admin_email: ''
    baas_admin_pass: ''
    baas_superuser_name: ''
    baas_superuser_email: ''
    baas_superuser_pass: ''
    
Cassandra username and password must be provided regardless of whether you enable authentication.

    opdk_cass_username: ''
    opdk_cass_password: ''

Default setting to use a cassandra ring

    opdk_use_cass_cluster: 'y'

Default silent-install configuration file settings for OpenLDAP

    opdk_ldap_type: '1'
    use_opdk_ldap_remote_host: 'n'
    opdk_ldap_pass: ''

Default to enable analytics

    opdk_enable_ax: 'y'

Default pod

    opdk_mp_pod: 'gateway'

Default to enable use of the zookeeper cluster

    opdk_use_zk_cluster: 'y'

SMTP settings for Edge Configuration

    opdk_smtp_skip: 'y'
    opdk_smtp_host: 'smtp.example.com'
    opdk_smtp_port: '25'
    opdk_smtp_user: ''
    opdk_smtp_password: ''
    opdk_smtp_ssl: 'n'

Default to bind OPDK on all network interfaces

    opdk_bind_on_all_interfaces: 'y'    
    
Default cluster name is "apigee_baas"

    baas_cluster_name: 'apigee_baas'
    
URL and port of the load balancer for the API BaaS Stack nodes or IP/DNS and port of a single Stack node with no load balancer.

    baas_load_balancer_host: ''
    baas_load_balancer_port: '8080'
    
Portal port. Default value is 9000.

    baas_portal_port: '9000'
    
Elastic search ports. Default values

    baas_elasticsearch_port_low: '9200'
    baas_elasticsearch_port_high: '9300'
    
SMTP information. BaaS requires an SMTP server.

    baas_smtp_host: 'smtp.gmail.com'
    baas_smtp_port: '465'
    baas_smtp_user: ''
    baas_smtp_user_pass: ''
    baas_smtp_ssl: 'n'
    
Default system config files to download

    system_config_files:
      - { dir: '/etc/', name: 'hosts' }
      - { dir: '/etc/', name: 'hosts.allow' }
      - { dir: '/etc/', name: 'hosts.deny' }
      - { dir: '/etc/', name: 'environment' }
      - { dir: '/etc/', name: 'profile' }
      - { dir: '/etc/', name: 'bashrc' }
      - { dir: '/etc/', name: 'resolv.conf' }
      - { dir: '/var/log/', name: 'messages' }
      - { dir: '/etc/', name: 'sysctl.conf' }
      - { dir: '/etc/', name: 'sudoers' }
      - { dir: '/etc/security/', name: 'limits.conf' }
      - { dir: '/etc/security/limits.d/', name: '*conf' }
    
    apigee_config_files:
      - { dir: '{{ opdk_installer_path }}/', name: '*conf' }
      - { dir: '{{ apigee_installation_home }}/customer/', name: '*' }
      - { dir: '{{ apigee_installation_home }}/apigee-cassandra/', name: '*yaml' }
      - { dir: '{{ apigee_installation_home }}/etc/', name: 'default*.sh' }
    
    apigee_log_files:
      - { dir: '{{ opdk_installer_path }}/', name: '*.log' }
      - { dir: '{{ opdk_installer_path }}/var/log/', name: '*.log' }
      - { dir: '{{ opdk_installer_path }}/', name: '*.txt' }
      - { dir: '{{ apigee_installation_home }}/var/log/', name: '*.log' }
      - { dir: '{{ apigee_installation_home }}/', name: '*.out' }

Default settings for removing data on rollback

    remove_apigee: false

Dependencies
------------

No dependencies

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: apigee-opdk-setup-default-settings }

License
-------

Apache License Version 2.0, January 2004

Author Information
------------------

Carlos Frias
<!-- BEGIN Google Required Disclaimer -->

# Not Google Product Clause

This is not an officially supported Google product.
<!-- END Google Required Disclaimer -->