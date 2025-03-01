# 1. Fibonacci Series

def fib(c):
    a, b = 0, 1
    for i in range(c):
        lst.append(a)
        a, b = b, a + b

lst = []
fib(10)
print (f"Here is a Fibo Series: {lst}")


# 2. Odd Indices

lst2 = []
for i in range(1, len(lst), 2):
    lst2.append(i)

print(f"Here is the odd indices list: {lst2}")


# 3 Word Count

string = '''I have provided this text to provide tips on creating interesting paragraphs.
First, start with a clear topic sentence that introduces the main idea.
Then, support the topic sentence with specific details, examples, and evidence.
Vary the sentence length and structure to keep the reader engaged.
Finally, end with a strong concluding sentence that summarizes the main points.
Remember, practice makes perfect!'''

word = len(string.split())
print(f"There are total of {word} words")


#4 Vovels

vowels = "aeiouAEIOU"
vov = sum(string.count(vowel) for vowel in vowels)
print(f"There are total of {vov} vowels")


#5 Caps

animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
anime = []
for i in animals:
    anime.append(i.upper())

print(f"Here is a caps list of animals: {anime}")


#6 Odd or Even

for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} is even,", end=" ")
    else:
        print(f"{i} is odd,", end=" ")

print("\n")


# 7 Addition of user's numbers
def sum_of_integers(a, b):
    return a + b

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
print("Sum:", sum_of_integers(num1, num2))
print("\n")
print("THAT'S ALL FOR TODAY, THANK YOU.")