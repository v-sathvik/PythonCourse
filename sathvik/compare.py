s1 = input("Enter the first Word: ");
s2 = input("Enter the second Word: ");

def are_anagram1(s1, s2):
   return [False, True][sum([ord(x) for x in s1]) == sum([ord(x) for x in s2])]

test = are_anagram1(s1,s2)

if test == True:
	print("Anagram");
else:
	print("Not an Anagram");	
