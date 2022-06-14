#               NAIVE BAYES CLASSIFIER


# Declaring the initial text-category list
sports = ["A great game", "Very clean match", "A clean but forgettable game"]
nonSports = ["The election was over", "It was a close election"]

# Initializing the list to store each words of each elements of sports and nonSports
sportsWords = []
nonSportsWords = []
uniqueWords = []

# Initializing the unique word count to 0
uniqueWordCount = 0

for sentence in sports:
    # Splitting the sentence into words
    words = sentence.split() # Returns a list
    for word in words:
        word = word.lower()
        if word not in uniqueWords:
            uniqueWords.append(word)
        # Appending the word to the sportsWords list
        sportsWords.append(word)
        
for sentence in nonSports:
    # Splitting the sentence into words
    words = sentence.split() # Returns a list 
    for word in words:
        word = word.lower()
        if word not in uniqueWords:
            uniqueWords.append(word)
        # Appending the word to the nonSportsWords list
        nonSportsWords.append(word)

# Calculating total number of words in each category
sportsWordCount = len(sportsWords)
nonSportsWordCount = len(nonSportsWords)
uniqueWordCount = len(uniqueWords)

# Function to calculate probability of each word in a text
def probabilityOfWord(word, category):
    wordCount = 0
    word = word.lower()
    if category == "sports":
        for sportWord in sportsWords:
            if sportWord == word:
                wordCount += 1
        return (wordCount + 1) / sportsWordCount 
    elif category == "nonSports":
        for nonSportWord in nonSportsWords:
            if nonSportWord == word:    
                wordCount += 1
        return (wordCount + 1) / nonSportsWordCount

# Function to calculate the probability in terms of each category and categorize it
def probabilityCategorizer(text):
    probabilitySports = 1
    probabilityNonSports = 1
    sentence = text.split()
    # Iterating through ever word in sentence
    for word in sentence:
        probabilitySports *= probabilityOfWord(word, "sports")
        probabilityNonSports *= probabilityOfWord(word, "nonSports")
    # Comparing both values
    if probabilitySports > probabilityNonSports:
        print("The text belongs to sports category.")
    elif probabilityNonSports > probabilitySports:
        print("The text belongs to non-sports category.")        

testText = "A very close game"
probabilityCategorizer(testText)