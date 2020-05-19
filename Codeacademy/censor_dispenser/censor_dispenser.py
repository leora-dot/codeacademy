# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# These are the lists provided by codeacademy

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

#Write a function that can censor a specific word or phrase from a body of text, and then return the text.

def case_shuffler(phrase):
    all_cases = [phrase.upper(),phrase.lower(),phrase.title()]
    return all_cases

print(case_shuffler("the system"))

def basic_remover(phrase,text):
    if phrase in text:
        # Generating the Cover Phrase
        cover_phrase = ""
        for i in range(len(phrase)):
            cover_phrase = cover_phrase + "x"
        # Removing Phrase 
        phrase_instance = text.find(phrase)
        while phrase_instance > -1:
            text = text.replace(phrase,cover_phrase)
            phrase_instance = text.find(phrase)
        return text
    else:
        return "No censorship needed"

#print(basic_remover("the system",email_one))

#Mr. Cloudy has asked you to use the function to censor all instances of the phrase learning algorithms from the first email, email_one.
#Mr. Cloudy doesn’t care how you censor it, he just wants it done.

#Write a function that can censor not just a specific word or phrase from a body of text, but a whole list of words and phrases, and then return the text.
#Mr. Cloudy has asked that you censor all words and phrases from the following list in email_two. (Reference prorietary_terms)


#The most recent email update has concerned Mr. Cloudy, but not for the reasons you might think. He tells you, “this is too alarmist for the Board of Investors! Let’s tone down the negative language and remove unnecessary instances of ‘negative words.’”
#Write a function that can censor any occurance of a word from the “negative words” list after any “negative” word has occurred twice, as well as censoring everything from the list from the previous step as well and use it to censor email_three. (reference negative_words)

#This final email has Mr. Cloudy in a frenzy. “We can’t let this information get out!” He tells you, “our company would be ruined! Censor it! Censor it all!”
#Write a function that censors not only all of the words from the negative_words and proprietary_terms lists, but also censor any words in email_four that come before AND after a term from those two lists.

#Great job! The Board of Investors is none the wiser to what is going on in the lab and Mr. Cloudy is very happy.
#Take a moment to look over your functions, are they the best they can be? As a challenge, make sure they:
#Handle upper and lowercase letters.
#Handle punctuation.
#Censor words while preserving their length
