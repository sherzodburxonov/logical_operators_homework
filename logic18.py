def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    first=a//10000
    second=a%10000//1000
    third=a%1000//100
    four=a%100//10
    five=a%10
    return five>four>third>second>first
print(main(75421))
    