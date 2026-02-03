# VastAI API Reference

This page documents all public methods on the `VastAI` class.

The VastAI class provides programmatic access to the Vast.ai GPU cloud platform.
Each CLI command is available as a method on this class.

## Class Overview

::: vastai.VastAI
    options:
      show_root_heading: true
      show_source: false
      members_order: source
      docstring_style: google
      show_signature_annotations: true
      merge_init_into_class: true
      filters:
        - "!^_"
        - "!^import_cli"
        - "!^create_wrapper"
        - "!^generate_signature"

## Method Categories

The SDK provides methods organized by resource type:

### Offers and Search

- `search_offers()` - Search available GPU offers
- `search_templates()` - Search available templates
- `search_benchmarks()` - Search benchmark results

### Instances

- `show_instances()` - List your instances
- `show_instance()` - Get instance details
- `create_instance()` - Create a new instance
- `start_instance()` - Start a stopped instance
- `stop_instance()` - Stop a running instance
- `destroy_instance()` - Delete an instance
- `reboot_instance()` - Reboot an instance
- `label_instance()` - Set instance label

### Volumes

- `show_volumes()` - List your volumes
- `create_volume()` - Create a new volume
- `delete_volume()` - Delete a volume
- `attach_volume()` - Attach volume to instance
- `detach_volume()` - Detach volume from instance

### SSH and File Transfer

- `ssh_url()` - Get SSH connection URL
- `scp_url()` - Get SCP URL for file transfer
- `copy()` - Copy files to/from instances

### Billing

- `show_invoices()` - List invoices
- `show_user()` - Get user/billing info
- `add_credit()` - Add credit to account
- `transfer_credit()` - Transfer credit between accounts

### Teams

- `show_teams()` - List teams
- `create_team()` - Create a new team
- `delete_team()` - Delete a team
- `select_team()` - Switch team context
- `invite_team()` - Invite user to team

### Autoscaling

- `show_autoscalers()` - List autoscaler groups
- `create_autoscaler()` - Create autoscaler
- `delete_autoscaler()` - Delete autoscaler
- `update_autoscaler()` - Update autoscaler settings

### Environment Variables

- `show_env_vars()` - List environment variables
- `set_env_var()` - Set an environment variable
- `delete_env_var()` - Delete an environment variable

### API Keys

- `show_api_keys()` - List API keys
- `create_api_key()` - Create new API key
- `delete_api_key()` - Delete an API key

## Return Types

All methods return one of:

- `dict[str, Any]` - Single object responses
- `list[dict[str, Any]]` - Collection responses

Most responses include a `success` boolean and `msg` string for error details.
