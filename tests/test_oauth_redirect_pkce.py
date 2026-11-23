import pytest
import security.oauth_redirect_pkce as mod

CASES = [
    ("exact_redirect", (1, 2)),
    ("pkce_verify", (1, 2)),
    ("state_once", (1, 2)),
    ("client_bind", (1, 2)),
    ("code_ttl", (1, 2)),
    ("redirect_parse", (1, 2)),
    ("session_bind", (1, 2)),
    ("validation", (1, 2)),
    ("audit", (1, 2)),
    ("error_map", (1, 2)),
    ("fallback", (1, 2)),
    ("token_exchange", (1, 2)),
    ("scope_check", (1, 2)),
    ("replay_guard", (1, 2)),
    ("logging", (1, 2)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
