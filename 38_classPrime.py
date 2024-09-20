# 38. Create your own class prime to return all primes between two given numbers



class Prime:
    # Initialize the class with the range of numbers
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # Method to check if a number is prime
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Method to return all prime numbers between the start and end
    def get_primes(self):
        primes = []
        for num in range(self.start, self.end + 1):
            if self.is_prime(num):
                primes.append(num)
        return primes

# Input: Take the start and end range from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Create an instance of the Prime class
prime_numbers = Prime(start, end)

# Get the list of prime numbers in the range and print them
primes = prime_numbers.get_primes()
print(f"Prime numbers between {start} and {end}: {primes}")
