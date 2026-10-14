import os
import sys
from pathlib import Path
from dotenv import dotenv_values

root = Path(__file__).resolve().parent
values = dotenv_values(root / ".env")

for name in ("HF_API_KEY", "HF_SECRET"):
    value = values.get(name)
    if not value or value.startswith("your-"):
        print(f"Missing or placeholder value: {name}", file=sys.stderr)
        sys.exit(1)
    os.environ[name] = value

python = root / ".venv" / "bin" / "python"
os.execv(str(python), [str(python), "-m", "higgsfield_mcp.server"])
