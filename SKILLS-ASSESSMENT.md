# Skills Assessment — apigee-opdk-setup-default-settings

> **Skill domain:** Apigee OPDK infrastructure-as-code — the centralized defaults and runtime topology resolver that every other role in the 70+ role framework depends on. Part of the broader Apigee platform-operations portfolio; see the [`bap_coe` portfolio hub →](https://github.com/carlosfrias/apigee-hybrid-workspace/blob/master/SKILLS-ASSESSMENT.md) for the full corpus.

---

## Why this role is notable

- **The single source of truth for ~100 default variables.** Ports, paths, credentials, SMTP settings, org/env names, and silent-installation configuration file paths — all declared in one role so downstream roles never duplicate or disagree on values.
- **Runtime network topology resolution.** Determines the primary interface, resolves private/public IP addresses, local/management IPs, LDAP host, and region — per node, at runtime. On AWS, enriches facts from `ec2_metadata_facts`.
- **Cacheable fact injection.** Every `set_fact` uses `cacheable: yes`, so subsequent roles in the same play read the same consistent, resolved values without re-discovery.
- **Foundation for 70+ roles.** Every other `apigee-opdk-*` role depends on the facts this role produces. It must run first in any play.

---

## Expertise demonstrated

> Ansible is the medium. The engineering evidence lives in the [project README →](README.md). What follows is the skills assessment for the business reader.

- **Infrastructure-as-code at scale** — a single role that declares the entire OPDK default variable catalog and resolves per-node network topology, so 70+ downstream roles share a consistent, cacheable fact base.
- **Runtime network topology resolution** — interface detection, private/public IP resolution, AWS EC2 metadata enrichment. The role handles the hard part (which IP? which interface?) so downstream roles just reference `private_address` or `local_mgmt_ip`.
- **Cacheable fact architecture** — `set_fact` with `cacheable: yes` means the fact cache persists across plays. No re-discovery, no stale facts.
- **Port matrix as code** — every OPDK port (Cassandra 9042, ZooKeeper 2181, MS 8080, Router 8081, MP 8082, Qpid 5672, Postgres 5432, LDAP 10389, etc.) declared as a default variable, overridable per-environment.

---

## How this shows the expertise

This role is the foundation of the entire `apigee-opdk-*` framework. The expertise is not "declaring variables" — it is **designing a single role that resolves network topology at runtime and injects it as cacheable facts, so 70+ roles never duplicate or disagree on IP addresses, ports, or paths**. The port matrix alone (every OPDK service port declared as a variable) encodes institutional knowledge of the Apigee Edge Private Cloud architecture.

The runtime resolution pattern (detect interface → resolve IPs → enrich with AWS metadata → cache) is the same pattern used in cloud-native infrastructure: the node knows its own identity at runtime, and the automation adapts.

---

## Related expertise

| Skill | Repository | Assessment |
|-------|-----------|-----------|
| Apigee Hybrid / K8s automation (collection) | [`apigee-hybrid-workspace`](https://github.com/carlosfrias/apigee-hybrid-workspace) | [SKILLS-ASSESSMENT.md →](https://github.com/carlosfrias/apigee-hybrid-workspace/blob/master/SKILLS-ASSESSMENT.md) ✅ portfolio hub |
| Rolling upgrade / DR / traffic fencing | [`apigee-opdk-playbook-maintenance-opdk-upgrade`](https://github.com/carlosfrias/apigee-opdk-playbook-maintenance-opdk-upgrade) | [SKILLS-ASSESSMENT.md →](https://github.com/carlosfrias/apigee-opdk-playbook-maintenance-opdk-upgrade/blob/master/SKILLS-ASSESSMENT.md) ✅ |
| Multi-datacenter expansion | [`apigee-opdk-playbook-maintenance-expand-region`](https://github.com/carlosfrias/apigee-opdk-playbook-maintenance-expand-region) | [SKILLS-ASSESSMENT.md →](https://github.com/carlosfrias/apigee-opdk-playbook-maintenance-expand-region/blob/master/SKILLS-ASSESSMENT.md) ✅ |

---

## Provenance

Authored and maintained by **Carlos Frias** during his tenure on Apigee Edge Private Cloud. This skills assessment is the companion to the engineering [README →](README.md).

## License

See [LICENSE](./LICENSE).