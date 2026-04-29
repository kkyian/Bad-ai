words_and_answers = {"hi":"hi", "how are you": "good"}
# add to this later
def main_part():
    what_you_say = input("Say something:")
    if what_you_say in words_and_answers:
        print(words_and_answers[what_you_say])
    else:
        learn = input(f"If you said {what_you_say} how would you reply:")
        words_and_answers[what_you_say] = learn
        print(words_and_answers[what_you_say])
main_part()
while True:
    countinue_or_not = input("do you want to countinue:")
    if countinue_or_not in ["y", "yes"]:
        main_part()
    else:
        exit()
# upload to github