#These are the texts provided by Codeacademy:
#These are the emails you will be censoring.
#The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#These are the lists provided by codeacademy
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

#This is a list of punctuation characters which the censor should ignore. It does not contain every possible character, but it should be good enough while I am working on the project.
punctuation = [".","?",",",":",";","!","-","/","\""]

#This is a function to shuffle that iterates through all the case combinations for a given phrase. For all intents and purposes, it renders censored phrases non-case-senstive.. I haven't figured out how to build it, so I just have the three most likely cases. I would really like to improve it!
def case_shuffler(phrase):
    all_cases = [phrase.upper(),phrase.lower(),phrase.title()]
    return all_cases

# This function sorts a list of phrases in reverse order of length. It is used to ensure that the censor functions remove longer strings first, so that any phrase which contains another phrase is removed in its entirety. For example, we need to remove the word "herself" prior to removing "her." Otherwise "herself" is only partially censored.
def sort_by_reverse_length(list_of_phrases):
    phrases_and_lengths= [[len(phrase),phrase] for phrase in list_of_phrases]
    phrases_and_lengths.sort(reverse = True)
    sorted_phrases = [phrase for num,phrase in phrases_and_lengths]
    return sorted_phrases

# This function generates a replacement for each phrase to be censored. It replaces each character in the phrase with a censor character, defaulting to x.

def replacement_generator(phrase, censor_character = "x"):
    replacement_phrase = ""
    for i in range(len(phrase)):
        replacement_phrase = replacement_phrase + censor_character
    return replacement_phrase

#Excercise 1
#Write a function that can censor a specific word or phrase from a body of text, and then return the text.
#Mr. Cloudy has asked you to use the function to censor all instances of the phrase learning algorithms from the first email, email_one.
#Mr. Cloudy doesn’t care how you censor it, he just wants it done.

def phrase_censor(phrase,text,censor_character = "x"):
    phrases_for_removal = case_shuffler(phrase)
    for phrase_for_removal in phrases_for_removal:
        phrase_instance = text.find(phrase_for_removal)
        while phrase_instance > -1:
            text = text.replace(phrase_for_removal,replacement_generator(phrase_for_removal,censor_character))
            phrase_instance = text.find(phrase_for_removal)
    return text

#Testing Excercise 1
#print(phrase_censor("the system",email_one))
#print(phrase_censor("help",email_four))

#Excercise 2
#Write a function that can censor not just a specific word or phrase from a body of text, but a whole list of words and phrases, and then return the text.
#Mr. Cloudy has asked that you censor all words and phrases from the following list in email_two.

def list_censor(phrase_list,text,censor_character = "x"):
    phrase_list = sort_by_reverse_length(phrase_list)
    for phrase in phrase_list:
        text = phrase_censor(phrase,text,censor_character)
    return text

#Testing Excercise 2
#print(list_censor(proprietary_terms,email_two))

#Excercise 3
#The most recent email update has concerned Mr. Cloudy, but not for the reasons you might think. He tells you, “this is too alarmist for the Board of Investors! Let’s tone down the negative language and remove unnecessary instances of ‘negative words.’”
#Write a function that can censor any occurance of a word from the “negative words” list after any “negative” word has occurred twice, as well as censoring everything from the list from the previous step as well and use it to censor email_three. (reference negative_words)

#This function turns a text into a list of words. It cannot be moved to the top of the code because it uses the list_censor function to remove punctuation.
def text_to_word_list(text):
    text_no_punctuation = list_censor(punctuation,text,"")
    text_words = text_no_punctuation.split()
    text_words = [word.lower() for word in text_words]
    return text_words

def basic_censor(text, negativity_threshold = 2):
    text_words = text_to_word_list(text)
    #Assessing whether any of the negative words appear in the email a sufficient number of times that we want to censor them. The default is that if any negative word appears at least twice, we will do negativity censoring.
    negativity_counter = 0
    for word in negative_words:
        word_count = text.count(word)
        negativity_counter = max(negativity_counter,word_count)
    #Negativity censoring, if needed
    if negativity_counter >= negativity_threshold:
        text = list_censor(negative_words,text)
    else:
        pass
    #Censorship of proprietary terms
    text = list_censor(proprietary_terms,text)
    return text

#Testing Excercise 3
#print(basic_censor(email_three))
#print(basic_censor("he is a bad dog"))
#print(basic_censor("he is a bad, bad dog."))

#Excercise 4
#This final email has Mr. Cloudy in a frenzy. “We can’t let this information get out!” He tells you, “our company would be ruined! Censor it! Censor it all!”
#Write a function that censors not only all of the words from the negative_words and proprietary_terms lists, but also censor any words in email four that come before AND after a term from those two lists.

def adv_censor(text,censor_character = "x"):
    #Creating lists of words and phrases to be censored
    censor_list = negative_words + proprietary_terms
    censor_list = sort_by_reverse_length(censor_list)
    replacement_list = []
    for censor_object in censor_list:
        replacement_list.append(replacement_generator(censor_object, censor_character))
    #Replacing censored words in the text
    text = list_censor(censor_list,text,censor_character)
    #Censoring words which appear before and after. We're going to look for replacements in our text.
    text_words = text_to_word_list(text)
    for word in replacement_list:
        try:
            word_index = text_words.index(word)
        except ValueError:
            continue
        ## generating the before and after words that also need to be removed. Our three cases depend on whether the phrase is in the middle of the text (in which case we add words bothe before and after) or whether it is the first or last word (in which case we only add before or after words).
        if 0<word_index<len(text_words)-1:
            text = phrase_censor(text_words[word_index-1],text)
            text = phrase_censor(text_words[word_index+1],text)
        elif phrase_index == 0:
            text = phrase_censor(text_words[phrase_index+1],text)
        else:
            text = phrase_censor(text_words[phrase_index-1],text)
    return text   
    
#Testing Excercise 4
#print(adv_censor("I am concerned about printing"))
print(adv_censor(email_four))

#Challenge notes
#Great job! The Board of Investors is none the wiser to what is going on in the lab and Mr. Cloudy is very happy.
#Take a moment to look over your functions, are they the best they can be? As a challenge, make sure they:
#Handle upper and lowercase letters.
#Handle punctuation.
#Censor words while preserving their length
