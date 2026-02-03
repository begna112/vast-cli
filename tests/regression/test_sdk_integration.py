"""
Regression tests for SDK integration (SDK-01, SDK-09).

These tests verify the SDK wrapper integrates correctly with the live vast module
and supports all documented features.
"""
import sys
from pathlib import Path

# Add vast-cli to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


class TestSDKLiveModuleImport:
    """SDK-01: SDK must import from live vast module, not frozen copy."""

    def test_sentinel_attribute_visible(self):
        """Adding sentinel to vast module should be visible through SDK."""
        import vast

        # Add sentinel attribute
        vast._SDK_TEST_SENTINEL = "phase6_integration_test"

        # Import SDK internals
        from vastai import sdk

        # Verify SDK's imported vast module sees the sentinel
        assert hasattr(sdk._vast, '_SDK_TEST_SENTINEL'), \
            "SDK's vast module should see runtime-added attributes"
        assert sdk._vast._SDK_TEST_SENTINEL == "phase6_integration_test", \
            "Sentinel value should match"

        # Cleanup
        del vast._SDK_TEST_SENTINEL

    def test_parser_from_vast_module(self):
        """Parser should be imported from vast module."""
        import vast
        from vastai import sdk

        # The parser used by SDK should be the same object as vast.parser
        assert sdk.parser is vast.parser, \
            "SDK parser should be the same object as vast.parser"

    def test_apikey_file_from_vast_module(self):
        """APIKEY_FILE should be imported from vast module."""
        import vast
        from vastai import sdk

        # APIKEY_FILE should match
        assert sdk.APIKEY_FILE == vast.APIKEY_FILE, \
            "SDK APIKEY_FILE should match vast.APIKEY_FILE"
