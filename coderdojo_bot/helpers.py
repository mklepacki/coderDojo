def largest_product(digits, substring_length):
    products = []
    for x in range(len(digits)-substring_length+1):
        substring = digits[x:x+substring_length]
        substring_multi = 1
        for i in substring:
            substring_multi *= int(i)
        products.append(substring_multi)
    return max(products)