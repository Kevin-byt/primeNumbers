# Print all the prime numbers within an interval to a file.

lower = int(input("Enter lower number: "))
upper = int(input("Enter upper number: "))

file = open("results.txt", "w")
file.write("The prime numbers between " + str(lower) +
           " and " + str(upper) + " are:" + "\n")

for num in range(2, upper + 1):
    # all prime numbers are greater than 1
    for i in range(2, num//2+1):
        if (num % i) == 0:
            break

    else:
        file.write(str(num) + ", ")

print("The prime numbers are displayed in the resuslts.txt file.")
file.write("\n")
file.close()