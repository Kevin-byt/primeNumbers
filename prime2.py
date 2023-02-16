# Print all the prime numbers within an interval to a file.

lower = int(input("Enter lower number: "))
upper = int(input("Enter upper number: "))

file = open("results.txt", "w")
file.write("The prime numbers between " + str(lower) +
           " and " + str(upper) + " are:" + "\n")

primelist = [x for x in range(lower,upper+1)]
print(primelist)


for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num < 2:
        if num in primelist:
            primelist.remove(num)
    if num > 1:
        for i in range(2, num//2+1):
            if (num % i) == 0:
                primelist.remove(num)
                break

for prime in primelist:
    file.write(str(prime) + ', ')    

print("The prime numbers are displayed in the resuslts.txt file.")
# file.write("\n")
file.close()