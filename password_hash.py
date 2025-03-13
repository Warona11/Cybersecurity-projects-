import bcrypt

# Input password (must be bytes)
password = b"password-123"

# Generate salt with a specific cost factor (12 rounds is default)
salt = bcrypt.gensalt(rounds=14)

# Generate hashed password
hashed_password = bcrypt.hashpw(password, salt)

# Print results
print(f"Password: {password.decode()}")
print(f"Salt: {salt}")
print(f"Hashed Password: {hashed_password.decode()}")
