# write a function to count vowels and consonants from the given word
# Example- input-Apple -- Output- vowel-2 ,consonants-3
def count_vowel_consonant(text):
    vowels="aeiouAEIOU"
    count_vowel=0
    count_consonant=0
    for char in text:
        if char.isalpha():
            if char==vowels:
                count_vowel=count_vowel+1
            else:  
             count_consonant=count_consonant+1
    return count_vowel,count_consonant

#Test
text=input("Enter a random word:")
v,c =count_vowel_consonant(text)
print("The text is:",text)
print("The count of vowel is:",{v},"and the count of the consonant is:",{c})

