import rsa


def generate_key_pair():
    # Generate a new RSA key pair
    key = RSA.generate(512)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key
    pubKey, privKey = rsa.newkeys(512)

    private_key = privKey.export_key()
    public_key = pubKey.export_key()
    return private_key, public_key

def save_keys(private_key, public_key, private_key_file, public_key_file):
    # Save the keys to files
    with open(private_key_file, 'wb') as f:
        f.write(private_key)
    with open(public_key_file, 'wb') as f:
        f.write(public_key)

def load_keys(private_key_file, public_key_file):
    # Load the keys from files
    with open(private_key_file, 'rb') as f:
        private_key = f.read()
    with open(public_key_file, 'rb') as f:
        public_key = f.read()
    return private_key, public_key

# Example usage
private_key, public_key = generate_key_pair()
save_keys(private_key, public_key, 'private.pem', 'public.pem')

# Later, when you need to use the keys
private_key, public_key = load_keys('private.pem', 'public.pem')

# Now you can use private_key and public_key as needed
