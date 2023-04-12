def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    first=a//10
    second=a%10
    return (first+second)%2!=0
print(main(45))