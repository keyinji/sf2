def isPalindrome(lst):
    '''
    determine is lst is palindrome
    :param lst: lst is a list
    :return: True is lst is a palindrom; False other wise
    '''
    temp = lst[:]
    temp.reverse()
    return temp == lst

def silly(n):
    '''
    get n inputs from user. Print yes if the sequence of inputs form 
    a palindrome; no otherwisr
    :params n: n is an integer > 0
    :return: None
    '''

    result = []
    for i in range(n):
        elem = input('enter element: ')
        result.append(elem)

    if isPalindrome(result):
        print("Yes")
    else:
        print("No")

silly(2)