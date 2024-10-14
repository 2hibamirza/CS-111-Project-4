# Project 4 - Movie Review Sentiment Analysis App
# Name: Hiba Mirza
# Date: 10/22/22
# Course: CS 111
# Semester: Fall 2022
# Displays Movie Review Sentiment Analysis App interface where user can get the average scores for a list of words

# This void function prints out the menu.
def display_menu(isFirstTime):
  # if True, print welcome message.
  if isFirstTime == True:
    print("Welcome to the Movie Review Sentiment Analysis App!")
    print("1. Load word list file.")
    print("2. Load movie review file.")
    print("3. Get average score of a word.")
    print("4. Get average scores for a list of words.")
    print("5. Plot average scores for a list of words.")
  else:
    # if False, do not print welcome message.
    isFirstTime == False
  
# This function reads in a file of word list
def make_list(file_name):
    file = open(file_name)
    list = file.readlines()
    file.close()
    # make new empty list
    make_list2 = []
    for i in list:
        make_list2.append(i.strip())
    return (make_list2)

# This function reads in a file of movie reviews.
def make_dict(file_name):
    file = open(file_name)
    list = file.readlines()
    # create empty dictionary
    dictionary = {}
    for line in list:
      review = line[2:]
      score = int(line[0])
      # each review and associated score are stored as a key/value pair in a dictionary
      dictionary[review] = score
    return dictionary

# This function searches the dictionary for wordToFind, counts instances of wordToFind, and calculates the average score.  The word search is case insensitive, however, search is looking for full match not partial match.  For example, if wordToFind is "terrific", movie reviews with "terrific" and "Terrific" are both a match.  However, movie reviews with "terrifically" would not be a match.
def search_word(dict, wordToFind):
    word_count = 0
    sum = 0
    for line in dict:
      words = line.split()
      for word in words:
        if word.lower() == wordToFind.lower():
          word_count += 1
          sum += dict[line]
    # if the number is divided by 0
    if word_count > 0:
      # calculates average
      average = sum / word_count
    else:
      average = 0
    return word_count, average

# This function is similar to search_word, except instead of searching for a single word, it searches for a list of words stored in list.
def search_all_words(list, dict):
    # creates empty list
    list_scores = []
    for words in list:
      count,average = search_word(dict,words)
      # list of the average score for each word in the input parameter list
      list_scores.append(average)
    # if the number is divided by 0
    if len(list_scores) > 0:
      # avg_score is the average score of all words in list
      avg_score = sum(list_scores) / len(list_scores)
    else:
      avg_score = 0
    return list_scores, avg_score

# This void function displays the words (stored in list) and their associated scores (stored in list_scores) to screen
def print_lists(list, list_scores):
    i = 0
    while i < len(list):
      print(list[i] + ": " + str(list_scores[i]))
      i += 1

# This is the main code.  It calls all the functions above. It sets up the interaction with the user.
if __name__ == '__main__':
  isFirstTime = True
  # displays menu
  display_menu(isFirstTime)
  # prompts user for input
  number = input("Enter a number (0 to exit): ")
  while (number is not '0'):
    if number == '1':
      file = input("Enter word list filename: ")
      list = make_list(file)
      print("Word list is loaded.")
    elif (number == '2'):
      file = input("Enter movie review filename: ")
      dict = make_dict(file)
      print("Movie reviews are loaded.")
    elif (number == '3'):
      word_tofind = input("Enter word to search: ")
      word_count, average = search_word(dict, word_tofind)
      print(word_tofind + " appears " + str(word_count) + " times")
      print("The average score for the reviews containing the word " + word_tofind + " is: " + str(average))
    elif (number == '4'):
        list_scores, avg_score = search_all_words(list, dict)
        print_lists(list, list_scores)
        print("Average score all of words: " + str(avg_score) + " which means this text is " )
        # outputs positive or negative average
        if avg_score >= 2:
          print("positive",end='')
        else:
          print("negative",end='')
    else:
      # any other number? will not display menu
      isFirstTime = False
    display_menu(isFirstTime)
    # prompts user again
    number = input("Enter a number (0 to exit): ")
  else:
    # if number is 0, will not display menu
    isFirstTime = False