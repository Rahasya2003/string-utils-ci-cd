from string_utils import reverse_string,to_lower,to_upper,count_vowels

if __name__ == "__main__":
    sample = "Hello world"
    
    print("Origina : ",sample)
    print("Reversed : ",reverse_string(sample))
    print("UpperCase : ",to_upper(sample))
    print("LowerCase : ",to_lower(sample))
    print("Vowel Count : ",count_vowels(sample))
    
