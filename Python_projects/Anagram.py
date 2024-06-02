def are_anagrams(str1, str2):
    # Convert both strings to lowercase and remove spaces
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    # Sort the characters of both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    # Check if the sorted strings are equal
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

if __name__ == "__main__":
    string1 = input("Enter string 1: ")
    string2 = input("Enter string 2: ")
    
    if are_anagrams(string1, string2):
        print("Yes, Strings are anagrams.")
    else:
        print("No, Strings are not anagrams.")
