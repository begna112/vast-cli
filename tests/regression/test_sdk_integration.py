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


class TestSDKFeatureCompleteness:
    """SDK-09: VastAI class must support all documented features."""

    def test_instantiation_with_api_key(self):
        """VastAI can be instantiated with api_key parameter."""
        from vastai import VastAI

        sdk = VastAI(api_key="test_key_12345")

        assert sdk.api_key == "test_key_12345"
        assert sdk._creds == "CODE"  # API key provided in code

    def test_raw_mode_default(self):
        """VastAI defaults to raw=True for SDK usage."""
        from vastai import VastAI

        sdk = VastAI(api_key="test_key")

        assert sdk.raw is True, "SDK should default to raw=True"

    def test_raw_mode_toggle(self):
        """VastAI raw mode can be toggled."""
        from vastai import VastAI

        sdk_raw = VastAI(api_key="test_key", raw=True)
        sdk_human = VastAI(api_key="test_key", raw=False)

        assert sdk_raw.raw is True
        assert sdk_human.raw is False

    def test_server_url_parameter(self):
        """VastAI accepts server_url parameter."""
        from vastai import VastAI

        sdk = VastAI(api_key="test_key", server_url="https://custom.vast.ai")

        assert sdk.server_url == "https://custom.vast.ai"

    def test_retry_parameter(self):
        """VastAI accepts retry parameter."""
        from vastai import VastAI

        sdk = VastAI(api_key="test_key", retry=5)

        assert sdk.retry == 5

    def test_explain_parameter(self):
        """VastAI accepts explain parameter."""
        from vastai import VastAI

        sdk = VastAI(api_key="test_key", explain=True)

        assert sdk.explain is True

    def test_quiet_parameter(self):
        """VastAI accepts quiet parameter."""
        from vastai import VastAI

        sdk = VastAI(api_key="test_key", quiet=True)

        assert sdk.quiet is True

    def test_imported_methods_populated(self):
        """VastAI should have imported_methods dict populated."""
        from vastai import VastAI

        sdk = VastAI(api_key="test_key")

        assert hasattr(sdk, 'imported_methods')
        assert isinstance(sdk.imported_methods, dict)
        # Should have many methods (vast.py has 115+ commands)
        assert len(sdk.imported_methods) > 50, \
            f"Expected 50+ methods, got {len(sdk.imported_methods)}"

    def test_dynamic_method_binding(self):
        """VastAI should have methods dynamically bound from vast.py."""
        from vastai import VastAI

        sdk = VastAI(api_key="test_key")

        # Check some well-known methods exist
        assert hasattr(sdk, 'search_offers'), "search_offers should be bound"
        assert hasattr(sdk, 'show_instances'), "show_instances should be bound"
        assert hasattr(sdk, 'show_machines'), "show_machines should be bound"
        assert callable(sdk.search_offers), "search_offers should be callable"

    def test_workergroup_and_autoscaler_aliases(self):
        """SDK-06: Both workergroup and autoscaler/autogroup aliases should work."""
        from vastai import VastAI

        sdk = VastAI(api_key="test_key")

        # Workergroup naming (primary method names from CLI)
        assert hasattr(sdk, 'create_workergroup') or 'create_workergroup' in sdk.imported_methods, \
            "create_workergroup should exist"
        assert hasattr(sdk, 'show_workergroups') or 'show_workergroups' in sdk.imported_methods, \
            "show_workergroups should exist"
        assert hasattr(sdk, 'delete_workergroup') or 'delete_workergroup' in sdk.imported_methods, \
            "delete_workergroup should exist"
        assert hasattr(sdk, 'update_workergroup') or 'update_workergroup' in sdk.imported_methods, \
            "update_workergroup should exist"

        # Autoscaler/autogroup backwards compatibility aliases (SDK-06 requirement)
        # Base class provides aliases: create_autogroup, delete_autoscaler, show_autoscalers, update_autoscaler
        assert hasattr(sdk, 'create_autogroup'), \
            "create_autogroup alias should exist (SDK-06)"
        assert hasattr(sdk, 'show_autoscalers'), \
            "show_autoscalers alias should exist (SDK-06)"
        assert hasattr(sdk, 'delete_autoscaler'), \
            "delete_autoscaler alias should exist (SDK-06)"
        assert hasattr(sdk, 'update_autoscaler'), \
            "update_autoscaler alias should exist (SDK-06)"


class TestSDKMethodCoverage:
    """Verify SDK method coverage against CLI commands."""

    def test_method_count_matches_cli_commands(self):
        """SDK should have methods for most CLI commands."""
        from vastai import VastAI
        import vast

        sdk = VastAI(api_key="test_key")

        # Count CLI commands (functions with double underscore)
        cli_commands = [
            name for name in dir(vast)
            if callable(getattr(vast, name))
            and '__' in name
            and not name.startswith('_')
        ]

        # SDK should have at least 80% coverage
        # (some commands like 'help' are excluded)
        min_expected = int(len(cli_commands) * 0.80)
        actual_count = len(sdk.imported_methods)

        assert actual_count >= min_expected, \
            f"SDK has {actual_count} methods but CLI has {len(cli_commands)} commands. " \
            f"Expected at least {min_expected} methods."

    def test_all_critical_methods_exist(self):
        """SDK must have all commonly-used methods."""
        from vastai import VastAI

        sdk = VastAI(api_key="test_key")

        critical_methods = [
            'search_offers',
            'create_instance',
            'destroy_instance',
            'show_instances',
            'start_instance',
            'stop_instance',
            'show_machines',
            'logs',
            'execute',
            'copy',
            'show_user',
        ]

        for method in critical_methods:
            assert hasattr(sdk, method) or method in sdk.imported_methods, \
                f"Critical method '{method}' missing from SDK"
