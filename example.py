import hashlib

gamma_values = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062]

def zeta_prng(seed, n_values=10, modulus=2**32):
    random_numbers = []
    for i in range(n_values):
        gamma = gamma_values[i % len(gamma_values)]
        fractional_part = gamma - int(gamma)
        transformed = int(1e9 * fractional_part)
        input_str = f"{gamma}{i}{seed}".encode('utf-8')
        hashed = int.from_bytes(hashlib.sha256(input_str).digest(), 'big')
        random_num = (transformed ^ hashed) % modulus
        random_numbers.append(random_num)
    return random_numbers

seed = 12345
random_sequence = zeta_prng(seed, n_values=5)
print("Generated Random Numbers:", random_sequence)
