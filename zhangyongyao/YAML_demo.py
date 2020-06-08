import yaml

print(yaml.load("""
a: 1
    """, Loader=yaml.FullLoader))