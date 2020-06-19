def find_taxicab():
    """This function loops through all numbers from 1000 to 9999 and finds taxicab numbers."""
    for num in range(1000, 10000):
        # taxicab numbers get counted twice because they can be expressed as the sum of two different cubes twice.
        count_times_found = 0
        for a in range(1, 23):
            # we make 2 loops that search all numbers from which cubes are less than 10000
            for b in range(a, 23):
                # we check if it is a sum of perfect cubes.
                if a ** 3 + b ** 3 == num:
                    # we found a number that is a sum of 2 perfect cubes.
                    count_times_found += 1

        if count_times_found == 2:
            # we found a taxicab number therefore, we print it.
            print(num)


find_taxicab()
