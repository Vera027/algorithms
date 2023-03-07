from pathlib import Path

path = Path('ecommerce')
path.exists()
print(path.exists())
print(path.glob('*.*'))
for file in path.glob('*.py'):
    print(file)
