"""
Regression tests for serverless lazy imports (SDK-07, SDK-08).

These tests verify that serverless classes don't load heavy dependencies
until they are actually accessed.
"""
import sys
from pathlib import Path

# Add vast-cli to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


class TestLazyImportConfiguration:
    """SDK-07: Verify lazy import mechanism is configured correctly."""

    def test_lazy_imports_dict_exists(self):
        """vastai/__init__.py should have _LAZY_IMPORTS dict."""
        import vastai

        assert hasattr(vastai, '_LAZY_IMPORTS'), \
            "vastai/__init__.py should have _LAZY_IMPORTS dict"
        assert isinstance(vastai._LAZY_IMPORTS, dict), \
            "_LAZY_IMPORTS should be a dict"

    def test_lazy_imports_contains_serverless_classes(self):
        """_LAZY_IMPORTS should map serverless class names to modules."""
        import vastai

        expected_classes = [
            'Serverless',
            'ServerlessRequest',
            'Endpoint',
            'Worker',
            'WorkerConfig',
            'HandlerConfig',
        ]

        for cls_name in expected_classes:
            assert cls_name in vastai._LAZY_IMPORTS, \
                f"'{cls_name}' should be in _LAZY_IMPORTS"

    def test_getattr_function_exists(self):
        """vastai/__init__.py should have __getattr__ for PEP 562."""
        import vastai

        # PEP 562: Module-level __getattr__ is exposed in the module namespace
        assert hasattr(vastai, '__getattr__'), \
            "vastai/__init__.py should have __getattr__ function"
        assert callable(vastai.__getattr__), \
            "__getattr__ should be callable"

    def test_getattr_raises_for_unknown_attribute(self):
        """__getattr__ should raise AttributeError for unknown names."""
        import vastai

        try:
            _ = vastai.NonExistentClass
            assert False, "Should have raised AttributeError"
        except AttributeError as e:
            assert "NonExistentClass" in str(e)


class TestBasicVastAIImport:
    """SDK-08: Basic vastai import should work without serverless deps."""

    def test_vastai_import_succeeds(self):
        """Basic import vastai should succeed."""
        import vastai

        assert vastai is not None

    def test_vastai_class_available(self):
        """VastAI class should be directly importable."""
        from vastai import VastAI

        assert VastAI is not None

    def test_vastai_instantiation_works(self):
        """VastAI can be instantiated without serverless deps."""
        from vastai import VastAI

        sdk = VastAI(api_key="test_key")

        assert sdk is not None
        assert sdk.api_key == "test_key"

    def test_all_exports_defined(self):
        """__all__ should list all public exports."""
        import vastai

        assert hasattr(vastai, '__all__'), \
            "vastai should have __all__ defined"
        assert 'VastAI' in vastai.__all__, \
            "VastAI should be in __all__"
        assert 'Serverless' in vastai.__all__, \
            "Serverless should be in __all__ (even if lazy)"


class TestServerlessClassAccess:
    """Test that serverless classes can be accessed when deps are available."""

    def test_serverless_in_all(self):
        """Serverless classes should be listed in __all__."""
        import vastai

        serverless_classes = [
            'Serverless',
            'ServerlessRequest',
            'Endpoint',
            'Worker',
            'WorkerConfig',
            'HandlerConfig',
            'LogActionConfig',
            'BenchmarkConfig',
        ]

        for cls_name in serverless_classes:
            assert cls_name in vastai.__all__, \
                f"'{cls_name}' should be in __all__"

    def test_serverless_import_path_correct(self):
        """Lazy import paths should point to correct modules."""
        import vastai

        # Serverless and ServerlessRequest should be in client.client
        assert '.serverless.client.client' in vastai._LAZY_IMPORTS['Serverless'], \
            "Serverless should be in serverless.client.client"

        # Worker classes should be in server.worker
        assert '.serverless.server.worker' in vastai._LAZY_IMPORTS['Worker'], \
            "Worker should be in serverless.server.worker"
