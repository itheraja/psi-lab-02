config = (
    "MyApp",
    "1.0",
    ("Development", "Testing", "Production"),
    "localhost"
)

print(config)

try:
    config[0] = "NewApp"
except TypeError:
    print("Cannot modify tuple because it is immutable.")
