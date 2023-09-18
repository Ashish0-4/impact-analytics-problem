def calculate_probability(N):
    # Initialize an array to store the number of ways to attend without missing 4 consecutive days
    dp = [0] * (N + 1)

    # Initialize the base cases
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    dp[3] = 7

    # Calculate the number of ways for each day using dynamic programming.
    for i in range(4, N + 1):
        # The number of ways to attend on day i is the sum of ways for the previous four days
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

    # Calculate the probability of missing the ceremony and represent it as a fraction
    probability = dp[N] / (2 ** N)
    # print("probability is ",+probability)
    
    # Convert the fraction to the desired string format

    # Calculate the number of ways to attend classes over N days (denominator)
    total_ways_to_attend = 2 ** N
    
    # Calculate the probability of missing the ceremony (numerator)
    probability_of_missing = dp[N]
    
    # Represent the probability as a fraction (numerator/denominator)
    probability_fraction = f"{probability_of_missing}/{total_ways_to_attend}"

    return probability_fraction

def main():
    try:
        N = int(input("Enter the number of days (N): "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for days.")
        return

    result = calculate_probability(N)
    print(f"For {N} days: {result}")

if __name__ == "__main__":
    main()