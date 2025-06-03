The non-trivial zeros of the Riemann zeta function (RZF) offer unique possibilities for the design of random number generators (RNGs) due to their mathematical complexity and quasi-randomness. Furthermore, their deep connection to the distribution of prime numbers can contribute to enhancing the complexity and security of random number generation. This paper explores the design principles, mathematical strengths, practical applications, and limitations of pseudo-random number generators (PRNGs) based on the zeros of the Riemann zeta function. In particular, it proposes a new approach to random number generation by utilizing the distribution of the zeros of the Riemann zeta function and their relationship with prime numbers.
# 1. Introduction
Random number generators play a key role in various fields, including cryptography, simulation, and blockchain. Random number generators are broadly classified into two types: true random number generators (TRNGs) based on physical phenomena and pseudo-random number generators (PRNGs) that use deterministic algorithms. PRNGs generate repeatable random number sequences using seed values, and their quality is evaluated based on periodicity, uniformity, and unpredictability. This study proposes a new random number generation method that overcomes the limitations of existing PRNGs by leveraging the characteristics of non-trivial zeros of the Riemann zeta function and the distribution of prime numbers, thereby achieving high complexity and security.
# 2. Characteristics of the Riemann zeta function and zeros
The Riemann zeta function is defined in the complex plane, and when the complex number s is divided into a real part (sigma) and an imaginary part (t), the non-trivial zeros are estimated to lie on the critical line where the real part is 1/2, according to the Riemann hypothesis. These zeros are composed of a real part of 1/2 and an imaginary part (gamma), where the imaginary part (gamma) exists infinitely and has unique values. The distribution of these zeros is closely related to the distribution of prime numbers, which is explained by the correlation between the error term of the prime number theorem and the zero intervals. In particular, the imaginary part values of the zeros exhibit a quasi-irregular pattern, providing the complexity suitable for random number generation.
# 3. PRNG Design Using Riemann Zeta Function Zeros
## 3.1 Design Principles
The imaginary part values of the non-trivial zeros of the Riemann zeta function can be obtained precisely through high-speed numerical calculations, and these values can be used as seeds or periodicity generation functions. The intervals between zeros exhibit characteristics close to randomness, so random number sequences based on these intervals can enhance unpredictability compared to conventional linear PRNGs.
## 3.2 Random Number Generation Algorithm
The following are the specific design steps for a PRNG utilizing the zeros of the Riemann zeta function:
**Zero-based period calculation**: Calculate the remainder when the imaginary part of the zero is divided by 1 to extract the fractional part.
**Irreversible integer transformation**: Multiply the fractional part by a large number (e.g., 10^9), take the integer part, and apply modulus operation to restrict it to a specific range, thereby generating an integer random number sequence.
**Bit Uniformity Enhancement**: Apply a hash function such as SHA-256 or Blake3 to the generated values to enhance statistical uniformity. For example, hash the input combining the zero value, index, and seed, then limit it to a specific number of bits to generate the final random number sequence.  
This structure leverages the unique distribution characteristics of zeros to generate a random number sequence distinct from existing PRNGs.
## 3.3 Example Python Code
Below is a simple PRNG implementation example using the zero points of the Riemann zeta function. Actual zero values use pre-calculated data, but here we have hard-coded a few values for illustrative purposes. The process of enhancing uniformity using a hash function is included.

*python*
```
import hashlib

# Imaginary part values of non-trivial zeros of the Riemann zeta function (hard-coded as an example)
gamma_values = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062]

def zeta_prng(seed, n_values=10, modulus=2**32):
    """
    Pseudorandom number generator based on the zeros of the Riemann zeta function
    seed: early seed value
    n_values: numbers of random number to generate
    modulus: Output range limitation
    """
    random_numbers = []
    for i in range(n_values):
        # Select zero value (cyclical use)
        gamma = gamma_values[i % len(gamma_values)]
        # Extracting and converting decimal places
        fractional_part = gamma - int(gamma)
        transformed = int(1e9 * fractional_part)
        # Hash function to ensure uniformity
        input_str = f"{gamma}{i}{seed}".encode('utf-8')
        hashed = int.from_bytes(hashlib.sha256(input_str).digest(), 'big')
        # Range limitation with modular arithmetic
        random_num = (transformed ^ hashed) % modulus
        random_numbers.append(random_num)
    return random_numbers

# Usage example
seed = 12345
random_sequence = zeta_prng(seed, n_values=5)
print("Generated Random Numbers:", random_sequence)
```

The above code generates a random number sequence based on the imaginary part of the Riemann zeta function zeros and enhances statistical uniformity through the SHA-256 hash function. In actual implementation, it is necessary to pre-calculate and use more zero data.
# 4. Mathematical Strengths
A PRNG based on the Riemann zeta function zeros has the following mathematical strengths:
**Enhanced Non-Deterministic**: The intervals between zeros do not follow a consistent pattern and exhibit quasi-randomness, thereby improving the randomness of the random number sequence.
**Uncertainty of Periodicity**: Unlike typical linear PRNGs, zero-based PRNGs make it difficult to analyze clear periodicity. This contributes to enhanced security.
**Difficulty in Reverse Calculation**: Zero values are highly complex numbers, making it computationally nearly impossible to infer the input seed or the next value.
# 5. Connection to Prime Number Distribution
Prime number distribution is deeply connected to the zeros of the Riemann zeta function, and the error term of the prime number theorem can be refined by the distribution of zeros. Utilizing the distribution of primes in random number generation can introduce additional complexity. For example, seed values can be generated based on prime gaps, or the logarithmic function of the prime distribution can be integrated into random number sequence generation. This contributes to further strengthening the statistical properties of the random number sequence.
# 6. Practical Applications
PRNGs based on the Riemann zeta function zeros have potential applications in various fields:
**Blockchain**: They can be used as non-periodic elements in block difficulty adjustment or proof-of-work (PoW) puzzles.
**Cryptographic protocols**: They can increase entropy during cryptographic key generation and be used for seed strengthening.
**Secure Hash Generation**: It can be used to design hash functions with enhanced collision resistance by utilizing zero-based input values.
# 7. Limitations and Countermeasures
### 7.1 Limitations
**Computational Cost**: Zero calculations require high-speed numerical analysis, making real-time generation costly.
**Asymmetric Distribution**: The imaginary part intervals of zero points are inconsistent, making it difficult to ensure statistical uniformity.
**Implementation Complexity**: The structure is more complex than that of a general PRNG, limiting its use in small devices.  
### 7.2 Mitigation Strategies  
**Pre-computation**: Pre-computing and storing thousands of zero points reduces the burden of real-time computation.
**Post-processing**: Ensures statistical uniformity through post-processing steps such as hash functions.
**Hybrid approach**: Combines with existing PRNGs to simultaneously ensure computational efficiency and security.
# 8. Conclusion
PRNGs utilizing the non-trivial zeros and prime number distribution of the Riemann zeta function offer distinct complexity and security compared to existing random number generation methods. The quasi-irregular distribution of zeros and their mathematical connection to primes enhance the unpredictability of the random number sequence, presenting promising possibilities for high-security applications such as cryptography and blockchain. However, computational costs and statistical uniformity issues remain challenges to be addressed. Future research should focus on improving the efficiency of zero calculations and exploring the connection with prime number distributions in greater detail to enhance practicality.



***References***
Edwards, H. M. (1974). *Riemann's Zeta Function*. Academic Press.
Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta-Function*. Oxford University Press.
Odlyzko, A. M. (1987). "On the distribution of spacings between zeros of the zeta function." *Mathematics of Computation*, 48(177), 273-308.
Montgomery, H. L. (1973). "The pair correlation of zeros of the zeta function." *Analytic Number Theory*, 24, 181-193.
Akatsuka, H. (2024). *Maximal order for divisor functions and zeros of the Riemann zeta-function*. arXiv:2411.19259.
Enoch, O. A., & Salaudeen, A. (2024). *Some Numerical Significance of the Riemann Zeta Function*. Retrieved from https://www.semanticscholar.org/paper/f52cf8040f4f64a5cf91e9c9100bf1014bc178de
Castillo, V., Muñoz, C., Poblete, F., & Salinas, V. (2024). *The Generalized Riemann Zeta heat flow*. arXiv:2402.10154.
Moser, J. (2023). *Jacob’s ladders and vector operator producing new generations of L2-orthogonal systems connected with the Riemann’s ζ(1/2+it) function*. arXiv:2302.07508.
Forrester, P. J., & Odlyzko, A. M. (1996). *Gaussian unitary ensemble eigenvalues and Riemann zeta function zeros: A nonlinear equation for a new statistic*. Physical Review E, 54(5), R4493–R4495. https://doi.org/10.1103/PhysRevE.54.R4493


Used Deepl.com
