import math

pi='3141592653589793238462643383279502884197169399375105820974944592'
e ='2718281828459045235360287471352662497757247093699959574966967627'

# Karatsuba using strings
def Karat(n1,n2):
    if(len(n1)<10 and len(n2)<10):
        return int(n1)*int(n2)
    else:
        mid = len(n1) // 2
        firstpartn1, secondpartn1 = n1[:mid], n1[mid:]
        firstpartn2, secondpartn2 = n2[:mid], n2[mid:]
        ac = Karat(firstpartn1, firstpartn2)
        bd = Karat(secondpartn1, secondpartn2)
        abcd = Karat(str(int(firstpartn1) + int(secondpartn1)), str(int(firstpartn2) + int(secondpartn2)))
        ad_plus_bc = abcd - ac - bd
        return (10**(2 * (len(n1) // 2))) * ac + (10**(len(n1) // 2)) * ad_plus_bc + bd

print(Karat(pi,e))

#Ans = 8539734222673567065463550869546574495034888535721844070265566699894191744893204061683656841229837757663374895871952806582723184