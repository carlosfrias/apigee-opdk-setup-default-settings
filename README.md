# apigee-opdk-setup-default-settings

> Central Ansible role that defines every default variable and resolves per-node network topology for the 70+ role `apigee-opdk-*` framework — the single source of truth for Apigee Edge Private Cloud installations.
> [!NOTE]
> Engineering portfolio note — this project demonstrates Apigee OPDK centralized defaults and topology resolution. See the [skills assessment →](SKILLS-ASSESSMENT.md) for the expertise applied.

[!NOTE]
For the skills, expertise, and engineering rationale reflected in this role, see [SKILLS-ASSESSMENT.md](./SKILLS-ASSESSMENT.md).

## What the role actually does

1. **Declares ~100 default variables** — ports (Cassandra, ZooKeeper, Message Processor, Management Server, Router, Qpid, Postgres, OpenLDAP, InfluxDB, Grafana, BaaS Elasticsearch), paths (`apigee_home`, `opdk_resources_path`, `local_apigee_path`), credentials, SMTP settings, org/env names, and silent-installation configuration file paths — so downstream roles never duplicate or disagree on these values.

2. **Resolves per-node network identity at runtime** — determines the primary network interface (`interface.yml`), resolves private IP (`private_address.yml`), public IP (`public_address.yml`), local management IP (`local_mgmt_ip.yml`), public management IP (`public_mgmt_ip.yml`), LDAP host (`ldap.yml`), and region (`region.yml`). On AWS, it enriches facts from `ec2_metadata_facts` to override addresses with EC2-local IPs.

3. **Caches all resolved values** — every `set_fact` uses `cacheable: yes`, writing into the Ansible fact cache so every subsequent role in the same play reads the same consistent, resolved values without re-discovery.

## Role variables (selected)

| Variable | Default | Purpose |
|---|---|---|
| `opdk_version` | `'4.18.05'` | Apigee Edge Private Cloud version |
| `opdk_resources_path` | `/opt/apigee/customer/installation` | Staging directory for configs and artifacts |
| `apigee_home` | `/opt/apigee` | Apigee installation root |
| `opdk_bind_on_all_interfaces` | `'y'` | Bind services on all network interfaces |
| `opdk_use_cass_cluster` | `'y'` | Use a Cassandra ring |
| `opdk_use_zk_cluster` | `'y'` | Use a ZooKeeper ensemble |
| `opdk_enable_ax` | `'y'` | Enable analytics |
| `cassandra_cql_native_port` | `9042` | Cassandra CQL native port |
| `zk_data_port` | `2181` | ZooKeeper client port |
| `ms_port` | `8080` | Management Server port |
| `router_ext_mgmt_port` | `8081` | Router external management port |
| `mp_ext_mgmt_port` | `8082` | Message Processor external management port |
| `qpid_messaging_port` | `5672` | Qpid AMQP port |
| `pg_db_port` | `5432` | PostgreSQL database port |
| `ldap_data_port` | `10389` | OpenLDAP port |
| `edge_proxy_port` | `9001` | Default proxy port |

See `defaults/main.yml` for the complete variable catalog.

## Usage

```yaml
- hosts: servers
  roles:
    - role: apigee-opdk-setup-default-settings
```

This role must run **first** in any play that uses `apigee-opdk-*` roles, because they depend on the cached facts it produces (`private_address`, `public_address`, `region`, `interface_name`, `target_response_file_path`, etc.).

## Provenance

- **Author:** Carlos Frias
- **Original context:** Apigee Edge Private Cloud (OPDK) — 70+ role Ansible automation framework
- **Last commit:** 2020-01-31

<!-- BEGIN Google Required Disclaimer -->
This is not an officially supported Google product.
<!-- END Google Required Disclaimer -->

## License

Apache License, Version 2.0 — see [LICENSE](./LICENSE).