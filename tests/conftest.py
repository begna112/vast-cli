import pytest
import argparse
from unittest.mock import MagicMock


@pytest.fixture
def mock_args():
    """Minimal argparse.Namespace for testing CLI functions."""
    return argparse.Namespace(
        api_key="test-key",
        url="https://console.vast.ai",
        retry=3,
        raw=False,
        explain=False,
        quiet=False,
        curl=False,
        full=False,
        no_color=True,
        debugging=False,
    )


@pytest.fixture
def mock_response():
    """Mock HTTP response with configurable status and JSON body."""
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {"success": True}
    response.text = '{"success": true}'
    response.content = b'{"success": true}'
    response.headers = {"Content-Type": "application/json"}
    response.raise_for_status = MagicMock()
    return response
