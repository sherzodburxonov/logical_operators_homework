def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    first=a//100
    second=a%100//10
    third=a%10
    x=first+second+third
    return x%2!=0
print(main(152))