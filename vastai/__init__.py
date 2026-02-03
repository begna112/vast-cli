"""
vastai - Vast.ai SDK and CLI package.

Main entry point for the SDK. Provides VastAI class for programmatic access
to the Vast.ai API, plus lazy-loaded serverless client/server classes.
"""

from .sdk import VastAI

# Lazy imports for serverless classes (PEP 562)
# These are only loaded when accessed, avoiding heavy dependencies
# for users who only need the core SDK.
_LAZY_IMPORTS = {
    "Serverless": ".serverless.client.client",
    "ServerlessRequest": ".serverless.client.client",
    "Endpoint": ".serverless.client.endpoint",
    "Worker": ".serverless.server.worker",
    "WorkerConfig": ".serverless.server.worker",
    "HandlerConfig": ".serverless.server.worker",
    "LogActionConfig": ".serverless.server.worker",
    "BenchmarkConfig": ".serverless.server.worker",
}

__all__ = [
    "VastAI",
    "Serverless",
    "ServerlessRequest",
    "Endpoint",
    "Worker",
    "WorkerConfig",
    "HandlerConfig",
    "LogActionConfig",
    "BenchmarkConfig",
]


def __getattr__(name):
    if name in _LAZY_IMPORTS:
        import importlib
        module = importlib.import_module(_LAZY_IMPORTS[name], __name__)
        return getattr(module, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
