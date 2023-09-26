def the_factors(x) :
    print("these are  the factors of x :")
    for i in range(1, x+1) :
        if x % i == 0 :
            print(i)
the_factors(100)