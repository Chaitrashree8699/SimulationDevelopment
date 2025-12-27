import os
from pathlib import Path
from operations_center.auth import get_access_token

# Clear cached tokens
user_token = Path.home() / ".jd_user_token.json"
cc_token = Path.home() / ".jd_cc_token.json"

if user_token.exists():
    user_token.unlink()
    print("Cleared user token cache")

if cc_token.exists():
    cc_token.unlink()
    print("Cleared client credentials token cache")

print("Getting new token with updated scopes...")
token = get_access_token()
print(f"New token obtained: {token[:20]}...")