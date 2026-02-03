# CLI Overview

The Vast.ai CLI provides command-line access to all Vast.ai platform features using a simple "verb-object" pattern.

## Installation

=== "Standalone (wget)"

    ```bash
    wget https://raw.githubusercontent.com/vast-ai/vast-python/master/vast.py
    chmod +x vast.py
    ./vast.py --help
    ```

=== "Package (pip)"

    ```bash
    pip install vastai
    vastai --help
    ```

## Command Pattern

Commands follow a **verb-object** pattern:

```
vastai <verb> <object> [arguments] [options]
```

Examples:

| Command | Description |
|---------|-------------|
| `vastai search offers` | Search for available GPU offers |
| `vastai show instances` | List your running instances |
| `vastai create instance` | Create a new instance |
| `vastai destroy instance` | Destroy an instance |
| `vastai set api-key` | Set your API key |

## Authentication

Get your API key from [https://vast.ai/console/cli/](https://vast.ai/console/cli/).

```bash
vastai set api-key YOUR_API_KEY
```

The key is stored in `~/.config/vastai/vast_api_key`.

## Global Options

All commands support these options:

| Option | Description |
|--------|-------------|
| `--api-key KEY` | Override stored API key |
| `--url URL` | Override server URL |
| `--raw` | Output machine-readable JSON |
| `--explain` | Show API endpoint being called |
| `--curl` | Show equivalent curl command |
| `--retry N` | Set retry limit (default: 3) |

## Output Formats

### Human-Readable (default)

```bash
vastai show instances
```

Output is formatted as tables for easy reading.

### JSON (--raw)

```bash
vastai show instances --raw
```

Output is valid JSON for scripting:

```bash
vastai show instances --raw | jq '.[0].id'
```

## Tab Completion

Enable tab completion with argcomplete:

```bash
pip install argcomplete
activate-global-python-argcomplete
```

Or for a single session:

```bash
eval "$(register-python-argcomplete vastai)"
```

## Command Categories

### Client Commands

For renting and using GPU instances:

- `search offers` - Find available machines
- `create instance` - Launch an instance
- `show instances` - List your instances
- `destroy instance` - Terminate an instance
- `ssh-url` - Get SSH connection info
- `copy` - Copy files to/from instances

### Host Commands

For GPU providers hosting on Vast.ai:

- `show machines` - List your machines
- `set min-bid` - Set minimum bid price
- `self-test machine` - Test a machine

### Account Commands

- `show user` - Show account info
- `show invoices` - List invoices
- `transfer credit` - Transfer credits

## Next Steps

- [Command Reference](commands.md) - Full list of all commands
- [Examples](examples.md) - Common usage patterns
