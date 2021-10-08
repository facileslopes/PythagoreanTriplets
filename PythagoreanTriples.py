#This program finds a list of pythagorean triples and plots them on a graph
import matplotlib.pyplot as plt
import copy
primes = [2]
triplets = []
prime_triplets = []
def prime_factorise(x,list_of_primes):
    #Returns the prime factorisation of a number
    number = x
    is_prime = True
    factors = []
    for prime in list_of_primes:
        if x%prime == 0:
            is_prime = False
            break
    if is_prime:
        #If the number is prime, return -1
        return -1
    else:
        #Else, prime factorise the number
        while number != 1:
            if number in list_of_primes:
                factors.append(number)
                number = 1
                continue
            for prime in list_of_primes:     
                if number%prime == 0:
                    factors.append(prime)
                    number = int(number/prime)

                    continue
        return factors

    
#First ask the user to enter the value of n where n is the length largest non-hypotenuse side to be considered
n = int(input("Enter the largest non-hypotenuse side that you wish to find a triple for: "))
for x in range(3,n+1):
    #First check if x is a prime, a number that can be factored into an odd prime(s), or a power of 2
    factors = prime_factorise(x,primes)
    if factors == -1:
        #If the number is a prime, append it to the list of primes, then divide the square of the prime and add/subtract 0.5 to find the two values it makes a triple with
        primes.append(x)
        tween =  (x**2)/2
        x2 = int(tween-0.5)
        hyp = int(tween+0.5)
        triplets.append((x,x2,hyp))
        prime_triplets.append((x,x2,hyp))
    else:
        #Check if the number is a power of 2 or not
        power_of_2 = True
        for factor in factors:
            if factor != 2:
                power_of_2 = False
        #If the number is a power of 2, create a 3-4-5 pair with it
        if power_of_2:
            inc = len(factors) - 2
            triplets.append((x, 3 * (2**inc), 5 * (2**inc)) )
        #If the number is composite, factorise the number and then find the pythagorean triple of each prime and multiply all three of the triple values to get the triplets    
        else:
            unique_factors = tuple(set(factors))
            for factor in unique_factors:
                if factor == 2:
                    continue
                factors_copy = copy.deepcopy(factors)
                factors_copy.remove(factor)
                inc = 1
                for z in factors_copy:
                    inc *= z
                for a in prime_triplets:
                    if a[0] == factor:
                        p_trip = a
                triplets.append((p_trip[0] * inc , p_trip[1] * inc, p_trip[2] * inc))
                
                
for triplet in triplets:
    plt.plot([triplet[0]],[triplet[1]],'ro')
plt.axis([0,triplets[-1][0],0,triplets[-1][1]])
plt.show()    
    
