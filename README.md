# Vast.ai CLI & SDK

[![PyPI version](https://badge.fury.io/py/vastai.svg)](https://badge.fury.io/py/vastai)
[![CI](https://github.com/vast-ai/vast-python/actions/workflows/ci.yml/badge.svg)](https://github.com/vast-ai/vast-python/actions/workflows/ci.yml)
[![Documentation](https://img.shields.io/badge/docs-mkdocs-blue)](https://vast-ai.github.io/vast-python/)

Command-line interface and Python SDK for the [Vast.ai](https://vast.ai) GPU cloud platform.

## Features

- **120+ CLI Commands**: Full coverage of the Vast.ai REST API
- **Python SDK**: Programmatic access with type hints and docstrings
- **Serverless Framework**: Async client/server for distributed GPU workloads
- **Three Installation Modes**: Standalone script, pip package, or full installation

## Quick Start

### Installation

**Standalone (wget)**
```bash
wget https://raw.githubusercontent.com/vast-ai/vast-python/master/vast.py
chmod +x vast.py
./vast.py set api-key YOUR_API_KEY
```

**Package (pip)**
```bash
pip install vastai
vastai set api-key YOUR_API_KEY
```

**With Serverless Support**
```bash
pip install "vastai[serverless]"
```

### CLI Usage

```bash
# Search for GPU offers
vastai search offers --limit 10

# Filter by requirements
vastai search offers 'num_gpus >= 4 gpu_ram >= 24'

# Create an instance
vastai create instance OFFER_ID --image pytorch/pytorch:latest

# List your instances
vastai show instances

# Destroy an instance
vastai destroy instance INSTANCE_ID
```

### SDK Usage

```python
from vastai import VastAI

# Initialize client
client = VastAI(api_key="YOUR_API_KEY")

# Search for offers
offers = client.search_offers(query="num_gpus >= 2")

# Create an instance
result = client.create_instance(
    id=offers[0]["id"],
    image="pytorch/pytorch:latest"
)

# List instances
instances = client.show_instances()

# Destroy instance
client.destroy_instance(id=instances[0]["id"])
```

### Serverless Usage

```python
import asyncio
from vastai import Serverless, Endpoint

async def main():
    client = Serverless(api_key="YOUR_API_KEY")
    response = await client.request({"prompt": "Hello!"})
    print(response)

asyncio.run(main())
```

## Documentation

Full documentation available at [https://vast-ai.github.io/vast-python/](https://vast-ai.github.io/vast-python/)

- [Installation Guide](https://vast-ai.github.io/vast-python/installation/)
- [CLI Reference](https://vast-ai.github.io/vast-python/cli/commands/)
- [SDK Reference](https://vast-ai.github.io/vast-python/sdk/reference/vastai/)
- [Serverless Framework](https://vast-ai.github.io/vast-python/serverless/)
- [Migration Guide](https://vast-ai.github.io/vast-python/guides/migration/)

## Requirements

- Python 3.10+
- For standalone script: `requests`, `python-dateutil`
- For serverless: `pip install "vastai[serverless]"`

## Authentication

Get your API key from [https://vast.ai/console/cli/](https://vast.ai/console/cli/)

```bash
# CLI
vastai set api-key YOUR_API_KEY

# SDK
client = VastAI(api_key="YOUR_API_KEY")

# Environment variable
export VAST_API_KEY="YOUR_API_KEY"
```

## Global CLI Options

| Option | Description |
|--------|-------------|
| `--api-key KEY` | Override stored API key |
| `--raw` | Output JSON for scripting |
| `--explain` | Show API endpoint details |
| `--retry N` | Set retry attempts (default: 3) |

## Development

```bash
# Clone repository
git clone https://github.com/vast-ai/vast-python.git
cd vast-python

# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run linting
ruff check .

# Run type checking
mypy vastai/
```

## Contributing

Contributions welcome! Please read the contributing guidelines and submit pull requests.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Links

- [Vast.ai Website](https://vast.ai)
- [API Documentation](https://vast-ai.github.io/vast-python/)
- [GitHub Repository](https://github.com/vast-ai/vast-python)
- [PyPI Package](https://pypi.org/project/vastai/)
- [Changelog](CHANGELOG.md)
