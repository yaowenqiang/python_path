from pathlib import Path

for filename in Path('/').rglob('*.py'):
    print(filename)
