custom_values = {"name": "pinto", "default_code": "p001", "default_value": 100}
new_values = {}

for key, value in custom_values.items():
    if 'default_' in key:
        new_key = key[8::]
        new_values[new_key] = value
    else:
        new_values[key] = value

print(new_values)
