import base64
import codecs
import argparse

def encode_base64(payload):
    """Encodes the payload using Base64."""
    return base64.b64encode(payload.encode()).decode()

def encode_rot13(payload):
    """Encodes the payload using ROT13."""
    return codecs.encode(payload, 'rot_13')

def encode_xor(payload, key):
    """Encodes the payload using a simple XOR key."""
    if not key:
        return "Error: XOR requires a key."
    # Extend the key to match payload length
    extended_key = (key * (len(payload) // len(key) + 1))[:len(payload)]
    obfuscated = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(payload, extended_key))
    # Return as hex so it's readable/printable
    return obfuscated.encode().hex()

def string_obfuscation(payload):
    """Basic string splitting obfuscation."""
    # Splits the payload into chunks of 2 characters and joins them with '+'
    chunks = [payload[i:i+2] for i in range(0, len(payload), 2)]
    return " + ".join(f'"{chunk}"' for chunk in chunks)

def main():
    parser = argparse.ArgumentParser(description="Custom Payload Encoder & Obfuscation Framework")
    parser.add_argument("-p", "--payload", required=True, help="The raw payload string to encode/obfuscate")
    parser.add_argument("-m", "--method", required=True, choices=['base64', 'rot13', 'xor', 'split'], help="Encoding/Obfuscation method")
    parser.add_argument("-k", "--key", help="Key required for XOR encoding")

    args = parser.parse_args()

    print(f"[*] Original Payload: {args.payload}")
    print(f"[*] Applying Method: {args.method.upper()}")

    if args.method == 'base64':
        result = encode_base64(args.payload)
    elif args.method == 'rot13':
        result = encode_rot13(args.payload)
    elif args.method == 'xor':
        if not args.key:
            print("[-] Please provide a key using -k for XOR encoding.")
            return
        result = encode_xor(args.payload, args.key)
    elif args.method == 'split':
        result = string_obfuscation(args.payload)

    print(f"[+] Output: {result}")

if __name__ == "__main__":
    main()
