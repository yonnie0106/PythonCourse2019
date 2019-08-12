## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test file in the terminal and see your results.
def count_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    n_vowels = 0
    if type(word) is str:
        for i in vowels:
            n_vowels += word.count(i)
        return n_vowels
    else:
        raise TypeError("The object has an inappropriate type : Integer")
