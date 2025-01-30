from functools import lru_cache

# Using LRU (Least Recently Used) cache to optimize function calls
@lru_cache(maxsize=3)
def expensive_computation(n):
    print(f"Computing {n}...")
    return n * n

# Test with caching
print(expensive_computation(2))  # Computing 2...
print(expensive_computation(3))  # Computing 3...
print(expensive_computation(2))  # Cached result
print(expensive_computation(4))  # Computing 4...
