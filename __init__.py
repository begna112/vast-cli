# Root __init__.py - supports "from vastai import VastAI" when installed as package
try:
    from vastai import VastAI
except ImportError:
    pass
