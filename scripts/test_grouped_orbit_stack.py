import json
import math
import re
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path("/Users/subhajkar/Developer/GitHub-Profile-Transformation")
REF_STACK_PATH = ROOT / "reference-base/stack.svg"

with open(ROOT / "profile/technology-stack.json", "r", encoding="utf-8") as f:
    techs = json.load(f)

print(f"Loaded {len(techs)} technologies.")
