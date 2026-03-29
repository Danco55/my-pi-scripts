import hashlib

# Ask user for password
password = input("Enter a password to hash: ")

# Convert to bytes
password_bytes = password.encode()

# Create hashes
md5_hash = hashlib.md5(password_bytes).hexdigest()
sha256_hash = hashlib.sha256(password_bytes).hexdigest()
sha512_hash = hashlib.sha512(password_bytes).hexdigest()

# Print results
print("\nHashes for your password:")
print(f"MD5    : {md5_hash}")
print(f"SHA256 : {sha256_hash}")
print(f"SHA512 : {sha512_hash}")

# Save to file
with open("hashed_passwords.txt", "w") as f:
    f.write(f"Password: {password}\n")
    f.write(f"MD5    : {md5_hash}\n")
    f.write(f"SHA256 : {sha256_hash}\n")
    f.write(f"SHA512 : {sha512_hash}\n")

print("\nHashes saved to hashed_passwords.txt")
