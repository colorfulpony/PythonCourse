from pathlib import Path

p1 = Path('files/ghj.txt')

if not p1.exists():
    with open(p1, 'w') as file:
        file.write("Text 3")

print(p1.name)
print(p1.stem)
print(p1.suffix)

p2 = Path("files")
print(p2.iterdir())
for item in p2.iterdir():
    print(item.name)