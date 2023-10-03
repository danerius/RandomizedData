
import matplotlib.pyplot as plt
import random

# Generate 500 random numbers between 0 and 100
random_numbers = [random.randint(0,100) for _ in range(500)]

# Set the window size
plt.figure(figsize=(15,5))

# Plotting the graph
plt.plot(random_numbers)
plt.title('Plot of 500 Random Numbers between 0 and 100')
plt.xlabel('Index')
plt.ylabel('Random Number')

plt.show()
