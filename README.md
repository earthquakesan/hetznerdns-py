## HetznerDNS

An API and CLI tools for Hetzner DNS. It is work in progress, the functionality is added as required.

## Hetzner DNS Docs

* [API Docs](https://dns.hetzner.com/api-docs/)
* [Access Endpoint](https://dns.hetzner.com)

## Installation

```
pip install hetznerdns
```

## Usage

To use the CLI client, you need to generate access token in the [Hetzner DNS web frontend](https://dns.hetzner.com). CLI client configuration is done via environment variables.

```
export HETZNER_DNS_TOKEN=token
```

At the moment, it is possible to get/create/delete zones and records, for example:

```
$ hetznerdns-cli zone get --name ermilov.org
{'id': 'tfJ9nMJckFAV7LBghxWTNB', 'name': 'ermilov.org', 'ttl': 86400, 'registrar': '', 'legacy_dns_host': '', 'legacy_ns': ['oxygen.ns.hetzner.com.', 'helium.ns.hetzner.de.', 'hydrogen.ns.hetzner.com.'], 'ns': ['hydrogen.ns.hetzner.com', 'oxygen.ns.hetzner.com', 'helium.ns.hetzner.de'], 'created': '2021-01-22 13:26:21.526 +0000 UTC', 'verified': '', 'modified': '2021-01-22 13:26:22.479 +0000 UTC', 'project': '', 'owner': '', 'permission': '', 'zone_type': {'id': '', 'name': '', 'description': '', 'prices': None}, 'status': 'verified', 'paused': False, 'is_secondary_dns': False, 'txt_verification': {'name': '', 'token': ''}, 'records_count': 4}

$ hetznerdns-cli zone create --name test-test-example.com
$ hetznerdns-cli zone get --name test-test-example.com
{'id': '5DFHAbGXmHX8ojKh6Prs8H', 'name': 'test-test-example.com', 'ttl': 3600, 'registrar': '', 'legacy_dns_host': '', 'legacy_ns': [], 'ns': ['hydrogen.ns.hetzner.com', 'oxygen.ns.hetzner.com', 'helium.ns.hetzner.de'], 'created': '2021-02-05 12:57:21.941 +0000 UTC', 'verified': '', 'modified': '2021-02-05 12:57:21.941 +0000 UTC', 'project': '', 'owner': '', 'permission': '', 'zone_type': {'id': '', 'name': '', 'description': '', 'prices': None}, 'status': 'verified', 'paused': False, 'is_secondary_dns': False, 'txt_verification': {'name': '', 'token': ''}, 'records_count': 0}

$ hetznerdns-cli zone delete --name test-test-example.com
$ hetznerdns-cli record create --name www --type A --value 127.0.0.1 --zone-name ermilov.org
{'record': {'id': '1ed054dbcc1b6445f10e5a86a6f9539b', 'type': 'A', 'name': 'www', 'value': '127.0.0.1', 'ttl': 3600, 'zone_id': 'tfJ9nMJckFAV7LBghxWTNB', 'created': '2021-02-05 12:58:39.63 +0000 UTC', 'modified': '2021-02-05 12:58:39.63 +0000 UTC'}}

$ hetznerdns-cli record get --name www --zone-name ermilov.org
{'id': '1ed054dbcc1b6445f10e5a86a6f9539b', 'type': 'A', 'name': 'www', 'value': '127.0.0.1', 'ttl': 3600, 'zone_id': 'tfJ9nMJckFAV7LBghxWTNB', 'created': '2021-02-05 12:58:39.63 +0000 UTC', 'modified': '2021-02-05 12:58:39.63 +0000 UTC'}

$ hetznerdns-cli record delete --name www --zone-name ermilov.org
```

## Development

```
# Create virtual environment for python3
# Then inside the environment execute
pip install -e .
pip install -r requirements-dev.txt
make test
```
