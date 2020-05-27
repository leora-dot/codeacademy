#Codecademy Imports
import pandas as pd
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)

#Requirement 2
# We’ve provided a csv file containing data about the game show Jeopardy! in a file named jeopardy.csv.
#Load the data into a DataFrame and investigate its contents.
#Try to print out specific columns.
# Note that in order to make this project as “real-world” as possible, we haven’t modified the data at all — we’re giving it to you exactly how we found it.
#As a result, this data isn’t as “clean” as the datasets you normally find on Codecademy.
#More specifically, there’s something odd about the column names.
#After you figure out the problem with the column names, you may want to rename them to make your life easier the rest of the project.

jeopardy_df = pd.read_csv("jeopardy.csv")

#In order to cut down on runtime, I am limiting the file to the first 1,000 rows. I need to uncomment this line when I'm really testing, but it will be handy when I'm just writing things out.
jeopardy_df = jeopardy_df.iloc[:1000]

#print(jeopardy_df.head(10))

jeopardy_df.rename(columns = {"Show Number":"show_number",
                              " Air Date":"air_date",
                              " Round":"round",
                              " Category":"category",
                              " Value":"value",
                              " Question":"question",
                              " Answer":"answer"},
                   inplace = True)

#print(jeopardy_df.columns)
#print(jeopardy_df.head(10))

#Requirement 3
# Write a function that filters the dataset for questions that contains all of the words in a list of words.
# For example, when the list ["King", "England"] was passed to our function, the function returned a DataFrame of 152 rows.
# Every row had the strings "King" and "England" somewhere in its " Question".
# Note that in this example, we found 152 rows by filtering the entire dataset. You can download the entire dataset at the start or end of this project.
# The dataset used on Codecademy is only a fraction of the dataset so you won’t find as many rows.
# Test your function by printing out the column containing the question of each row of the dataset.

## This function generates a list of words in a text, by removing punctuation and then splitting on space characters. It will be used to split questions into lists of words.  

def list_of_words(text):
    punctuation_signs = [".","?",",",":",";","!","-","/","\""]
    for punctuation in punctuation_signs:
        text = text.replace(punctuation, " ")
    word_list = text.split()
    word_list_lower = []
    for word in word_list:
        word_list_lower.append(word.lower())
    return word_list_lower

## This function creates multiple variations for a list of words (currently just each word and the words plus an "s") and renders them all in lowercase. It will be used to broaden the list of possible keywords.

def word_iterator(word_list):
    all_variations = []
    for word in word_list:
        word_variations = [word, word+"s"]
        all_variations = all_variations + word_variations
    all_variations_lower = []
    for word in all_variations:
        all_variations_lower.append(word.lower())
    return all_variations_lower

def question_finder(word_list):
    #Expands the list of words that we are looking for
    word_list = word_iterator(word_list)
    #This will contain the index numbers of rows with relevant questions
    filtered_indices = []
    #Searches for words in questions
    for i in range(len(jeopardy_df)):
        question_row = jeopardy_df.iloc[i]
        question_words = list_of_words(question_row.question)
        for word in word_list:
            if word.lower() in question_words:
                filtered_indices.append(i)
                break
    #Returns all rows which we added to our list of indices
    return jeopardy_df.iloc[filtered_indices]

#print(question_finder(["King","Queen"]))
#print(question_finder(["Pokemon"]))
#print(question_finder(["pokemon"]))
#print(question_finder(["giraffe"]))

#Requirement 4
#Test your original function with a few different sets of words to try to find some ways your function breaks. Edit your function so it is more robust.
#For example, think about capitalization. We probably want to find questions that contain the word "King" or "king".
#You may also want to check to make sure you don’t find rows that contain substrings of your given words. For example, our function found a question that didn’t contain the word "king", however it did contain the word "viking" — it found the "king" inside "viking".
#Note that this also comes with some drawbacks — you would no longer find questions that contained words like "England's".

#Requirement 5
#We may want to eventually compute aggregate statistics, like .mean() on the " Value" column. But right now, the values in that column are strings.
#Convert the " Value" column to floats. If you’d like to, you can create a new column with the float values.
#Now that you can filter the dataset of question, use your new column that contains the float values of each question to find the “difficulty” of certain topics.
#For example, what is the average value of questions that contain the word "King"?
#Make sure to use the dataset that contains the float values as the dataset you use in your filtering function.

#This lambda function converts dollar values to floats

dollar_to_float = lambda x: None if x=="None" else float(x.replace("$","").replace(",",""))

#These lines add a new, numerical value and delete the old one. The name of the column remains value. 
jeopardy_df["value_numerical"] = jeopardy_df.value.apply(dollar_to_float)
jeopardy_df = jeopardy_df.drop(columns = "value")
jeopardy_df.rename(columns = {"value_numerical":"value"}, inplace = True)

#print(jeopardy_df)
#print(jeopardy_df.columns)

def question_value_by_topic(word_list):
    filtered_questions = question_finder(word_list)
    filtered_values = filtered_questions["value"]
    return filtered_values.mean()

#print(question_value_by_topic(["Pokemon"]))
#print(question_value_by_topic(["Korea"]))
#print(question_value_by_topic(["IBM"]))

#Requirement 6
#Write a function that returns the count of the unique answers to all of the questions in a dataset.
#For example, after filtering the entire dataset to only questions containing the word "King", we could then find all of the unique answers to those questions.
#The answer “Henry VIII” appeared 3 times and was the most common answer.

def unique_answers(word_list):
    # Filtering Relevant Questions
    filtered_questions = question_finder(word_list)
    # Returning Answer Count
    answers_count = filtered_questions.groupby("answer").question.count().reset_index()
    answers_count.rename(columns = {"question":"question_count"}, inplace = True)
    return answers_count

#print(unique_answers(["Pokemon"]))
print(unique_answers(["King"]))
    
#Requirement 7 
#Explore from here! This is an incredibly rich dataset, and there are so many interesting things to discover.
#There are a few columns that we haven’t even started looking at yet. Here are some ideas on ways to continue working with this data:
#Investigate the ways in which questions change over time by filtering by the date. How many questions from the 90s use the word "Computer" compared to questions from the 2000s?
#Is there a connection between the round and the category? Are you more likely to find certain categories, like "Literature" in Single Jeopardy or Double Jeopardy?
#Build a system to quiz yourself. Grab random questions, and use the input function to get a response from the user. Check to see if that response was right or wrong.
#Note that you can’t do this on the Codecademy platform — to do this, download the data, and write and run the code on your own computer!
