#Get a string from an input string where all occurrences of first character replaced with 
#‘$’, except first character.
#[eg: onion -> oni$n]

a=input("enter the string:")
b = a[0] + a[1:].replace(a[0], '$')
print(b)