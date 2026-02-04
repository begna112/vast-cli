# VastAI API Reference

This page documents all public methods on the `VastAI` class.

The VastAI class provides programmatic access to the Vast.ai GPU cloud platform.
Each CLI command is available as a method on this class.

## Class Overview

```python
from vastai import VastAI

client = VastAI(
    api_key: str | None = None,      # API key (reads from file if not provided)
    server_url: str | None = None,   # Override API server URL
    retry: int = 3,                  # Max retry attempts for transient failures
    raw: bool = True,                # Return JSON instead of printing (SDK default)
    explain: bool = False,           # Print API endpoint info for debugging
    quiet: bool = False,             # Suppress non-essential output
    curl: bool = False,              # Print equivalent curl commands
)
```

The SDK provides **130+ methods** corresponding to CLI commands. All methods return either:

- `dict[str, Any]` - Single object responses
- `list[dict[str, Any]]` - Collection responses

Most responses include a `success` boolean and `msg` string for error details.

## Method Categories

The SDK provides methods organized by resource type:

### Offers and Search

| Method | Description | Returns |
|--------|-------------|---------|
| `search_offers(query, limit, order, **kwargs)` | Search available GPU offers | `list[dict]` |
| `search_templates(query, limit, **kwargs)` | Search available templates | `list[dict]` |
| `search_benchmarks(query, **kwargs)` | Search benchmark results | `list[dict]` |
| `show_connections(id)` | Show peer connections for an offer | `dict` |

### Instances

| Method | Description | Returns |
|--------|-------------|---------|
| `show_instances()` | List your instances | `list[dict]` |
| `show_instance(id)` | Get instance details | `dict` |
| `create_instance(id, image, **kwargs)` | Create a new instance | `dict` |
| `start_instance(id)` | Start a stopped instance | `dict` |
| `stop_instance(id)` | Stop a running instance | `dict` |
| `destroy_instance(id)` | Delete an instance | `dict` |
| `reboot_instance(id)` | Reboot an instance | `dict` |
| `label_instance(id, label)` | Set instance label | `dict` |
| `logs(id, tail)` | Get instance logs | `str` |
| `execute(id, command)` | Execute command on instance | `dict` |

### Volumes

| Method | Description | Returns |
|--------|-------------|---------|
| `show_volumes()` | List your volumes | `list[dict]` |
| `create_volume(name, size, **kwargs)` | Create a new volume | `dict` |
| `delete_volume(id)` | Delete a volume | `dict` |
| `attach_volume(volume_id, instance_id)` | Attach volume to instance | `dict` |
| `detach_volume(volume_id, instance_id)` | Detach volume from instance | `dict` |

### SSH and File Transfer

| Method | Description | Returns |
|--------|-------------|---------|
| `ssh_url(id)` | Get SSH connection URL | `str` |
| `scp_url(id, path)` | Get SCP URL for file transfer | `str` |
| `copy(src, dst)` | Copy files to/from instances | `dict` |

### Billing

| Method | Description | Returns |
|--------|-------------|---------|
| `show_invoices(**kwargs)` | List invoices (deprecated) | `list[dict]` |
| `show_invoices_v1(**kwargs)` | List invoices and charges | `dict` |
| `show_user()` | Get user/billing info | `dict` |
| `add_credit(amount, **kwargs)` | Add credit to account | `dict` |
| `transfer_credit(amount, recipient)` | Transfer credit between accounts | `dict` |

### Teams

| Method | Description | Returns |
|--------|-------------|---------|
| `show_teams()` | List teams | `list[dict]` |
| `create_team(name, **kwargs)` | Create a new team | `dict` |
| `delete_team(id)` | Delete a team | `dict` |
| `select_team(id)` | Switch team context | `dict` |
| `invite_team(id, email)` | Invite user to team | `dict` |

### Autoscaling / Worker Groups

| Method | Description | Returns |
|--------|-------------|---------|
| `show_autoscalers()` | List autoscaler groups | `list[dict]` |
| `create_autoscaler(**kwargs)` | Create autoscaler | `dict` |
| `delete_autoscaler(id)` | Delete autoscaler | `dict` |
| `update_autoscaler(id, **kwargs)` | Update autoscaler settings | `dict` |
| `show_workergroups()` | List worker groups (alias) | `list[dict]` |
| `create_workergroup(**kwargs)` | Create worker group (alias) | `dict` |

### Environment Variables

| Method | Description | Returns |
|--------|-------------|---------|
| `show_env_vars()` | List environment variables | `list[dict]` |
| `set_env_var(key, value)` | Set an environment variable | `dict` |
| `delete_env_var(key)` | Delete an environment variable | `dict` |

### API Keys

| Method | Description | Returns |
|--------|-------------|---------|
| `show_api_keys()` | List API keys | `list[dict]` |
| `create_api_key(name, **kwargs)` | Create new API key | `dict` |
| `delete_api_key(id)` | Delete an API key | `dict` |

### SSH Keys

| Method | Description | Returns |
|--------|-------------|---------|
| `show_ssh_keys()` | List SSH keys | `list[dict]` |
| `create_ssh_key(name, public_key)` | Add SSH key | `dict` |
| `delete_ssh_key(id)` | Delete SSH key | `dict` |

### Endpoints (Serverless)

| Method | Description | Returns |
|--------|-------------|---------|
| `show_endpoints()` | List serverless endpoints | `list[dict]` |
| `create_endpoint(**kwargs)` | Create endpoint | `dict` |
| `delete_endpoint(id)` | Delete endpoint | `dict` |
| `update_endpoint(id, **kwargs)` | Update endpoint | `dict` |

## Common Patterns

### Error Handling

```python
from vastai import VastAI

client = VastAI(api_key="your-key")

result = client.create_instance(id=12345, image="pytorch/pytorch")

if result.get("success"):
    instance_id = result["new_contract"]
    print(f"Created instance: {instance_id}")
else:
    print(f"Error: {result.get('msg', 'Unknown error')}")
```

### Filtering Results

```python
# Use query parameter for server-side filtering
offers = client.search_offers(
    query="num_gpus >= 4 gpu_ram >= 24 dph_total < 2.0",
    order="dph_total",
    limit=10
)
```

### Debug Mode

```python
# See API calls being made
client = VastAI(api_key="key", explain=True)
client.search_offers(limit=1)
# Prints: GET https://console.vast.ai/api/v0/bundles?...
```

## Return Types

All methods return one of:

- `dict[str, Any]` - Single object responses
- `list[dict[str, Any]]` - Collection responses

Most responses include a `success` boolean and `msg` string for error details.

## See Also

- [Quick Start Guide](../quickstart.md) - Working examples
- [CLI Command Reference](../../cli/commands.md) - Full CLI documentation
- [Migration Guide](../../guides/migration.md) - Upgrading from old SDK
