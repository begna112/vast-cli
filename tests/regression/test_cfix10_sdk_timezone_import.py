"""CFIX-10: Frozen SDK copy missing timezone import from datetime.

The bug: vast-sdk/vastai/vast.py imports date, datetime, timedelta but NOT
timezone. Any code using datetime.timezone.utc or timezone(...) fails with
NameError or ImportError.

The fix: Add timezone to the import statement.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))


def test_frozen_sdk_has_timezone_import():
    """The frozen SDK copy imports timezone from datetime."""
    # Read the frozen SDK file directly
    sdk_vast_path = os.path.join(
        os.path.dirname(__file__), '..', '..', '..', 'vast-sdk', 'vastai', 'vast.py'
    )
    with open(sdk_vast_path, 'r', encoding='utf-8', errors='replace') as f:
        source = f.read()

    assert 'timezone' in source, (
        "vast-sdk/vastai/vast.py does not import 'timezone' from datetime. "
        "Add it: from datetime import date, datetime, timedelta, timezone"
    )

    # Also verify the import line specifically
    import_found = False
    for line in source.split('\n'):
        if line.startswith('from datetime import') and 'timezone' in line:
            import_found = True
            break

    assert import_found, (
        "Could not find 'from datetime import ... timezone ...' in vast-sdk/vastai/vast.py"
    )


def test_live_vast_has_timezone_import():
    """The live vast.py already has the timezone import (sanity check)."""
    vast_path = os.path.join(os.path.dirname(__file__), '..', '..', 'vast.py')
    with open(vast_path, 'r') as f:
        for line in f:
            if line.startswith('from datetime import') and 'timezone' in line:
                return  # Found it, test passes

    assert False, "Live vast.py missing timezone import"
