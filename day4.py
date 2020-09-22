#appliaction based on zodiac sign
next = True
while next == True:
    print(''' Pick Your Zodaic Sign
    1. Aries
    2. Tauras
    3. Gemini
    4. Cancer
    5. Leo
    6. Virgo
    7. Libra
    8. Scorpio
    9. Sagittarian
    10. Capricon
    11. Aquaris
    12. Pisces
    ''')

    s = int(input("Pick your sign number & Know about your day : "))
    print(s)

    if s == 1:
        print("Your tidy nature should drive you to clean it up. In the course of wading through the mess, don't be surprised if you discover some objects you thought you'd lost forever. Once you finish, you'll probably find that the place looks beautiful, better than it did before it was messed up. Something good can indeed come out of chaos.")
    elif s ==2:
        print("An exciting phone call or email could come from a friend who has some great news for you, Taurus. Love, romance, and success in the arts are all highlighted now, and this communication could bring it to your attention. Conversations could bring inspiration your way, and your mind is apt to be going a thousand miles an hour for most of the day. Make the most of it!")
    elif s == 3:
        print("An online group could form today, Gemini, perhaps friends who are involved in the arts or meditation or spiritual studies. This group is likely to be close, probably through mutual interests, so communicating with them this evening should be both intellectually stimulating and emotionally gratifying. What takes place today could also bring healing of some kind, either for you or for someone else.")
    elif s == 4:
        print(" Communication involving romance could come unexpectedly today, Cancer. You may get a loving message from a romantic partner, or you could hear of a wedding to take place in the future amongst your circle of friends. You could also read a love poem or romance novel or write something along the same lines yourself! Someone might also express affection to you. Don't be surprised. You deserve it!")
    elif s == 5:
        print(" A chance to increase your income by participating in an artistic project of some kind could come your way today, Leo. You might take part in the creative work or you could promote it in a business capacity. Whichever it is, you're likely to form some firm friendships in the process. If you're single, one of your colleagues might turn out to be a potential love partner. Enjoy!")
    elif s == 6:
        print("Have you been feeling stagnant lately, Virgo, as if your life is going nowhere? What happens today could change that. An unusual group event could put you in touch with people who open new intellectual, career, or spiritual doors for you. Stimulating conversations could turn your head toward opportunities that you were never aware of before. Onward and upward!")
    elif s == 7:
        print("Inspiration could hit today, Libra. It's a beautiful feeling, but you might not be sure how to channel it. It could represent a spiritual breakthrough, artistic inspiration, increased understanding of others, or all of the above. What's almost certain is that you'll want to spend time alone to take it all in and figure out how to use it. Don't dismiss any possibility, however outrageous it may seem.")
    elif s == 8:
        print("You might have the chance to speak with new people in interesting fields, perhaps from foreign lands, Scorpio. Your conversational abilities are at an all-time high, so you'll not only enjoy talking with everyone, but they'll enjoy talking with you, too. Intriguing ideas and useful information could have your mind buzzing all night. Try to take a walk in the evening to clear your head.")
    elif s == 9:
        print("Information gleaned from surprising sources could lead to sudden, fortunate career breaks, Sagittarius. You might explore totally new fields, although this could be temporary. Your efforts should attract the attention of those who matter and eventually lead to advancement or a raise. Don't be afraid to continue to explore these sources. Keep up the good work!")
    elif s == 10:
        print("If you've been having trouble reaching a romantic partner, Capricorn, it might be a good idea to stop trying. Your friend is having a rough day and might not make the best company. In fact, your beloved could view a call from you as an unwelcome interruption and be short, if not downright rude. If you speak with your friend, keep it brief and plan to get together - just not today.")
    elif s == 11:
        print("Have you been feeling less than your normal self, Aquarius? If so, today you may suddenly regain your strength and be raring to go. You might even be tempted to start a rigorous exercise program. Go ahead and start, but pace yourself and try not to make up for lost time all at once. You need to ease into these things. Maybe start with walking and yoga.")
    elif s == 12:
        print("Too many people could be vying for your attention today, Pisces. All of them want advice or help. This could be flattering, and you'll probably want to help them, but it can also be unsettling and make it hard to focus. Don't let this set your temper on edge and cause you to snap at your friends. Take each request one at a time, make no promises, and do your best.")
    else :
        print("Are you sure about coz this isn't exist ")


    next = True if input("\n Do you wanna do it again?? (Y/N) ") == "Y" else False
