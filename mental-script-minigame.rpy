#setting up some win and loss quips
init python:
    #loss
    mental_minigame_loss_quips = ["Game over!", "I win!", "Sorry!", "You lose!"]
    mental_minigame_loss_quip = random.choice(mental_minigame_loss_quips)
    #win
    mental_minigame_win_quips = ["Congrats!", "You did it!", "You win!", "You won!"]
    mental_minigame_win_quip = random.choice(mental_minigame_win_quips)

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mental_minigame1",category=["minigames"],prompt="Can we play three truths and a lie?",pool=True,unlocked=True))

default persistent._mental_minigame1play = False
#variables: mentaltheme (number that sets the theme of the 3 truths and a lie)
#
label mental_minigame1:
    if mas_isMoniNormal(higher=True):
        m "Of course we can play!"
        if persistent._mental_minigame1play == False:
            if persistent._mas_pm_cares_about_dokis == True:
                call mental_minigame_doki_concern
            call mental_minigame_tutorial
        call mentalminigametheme
        jump threetruthsandaliegame
    elif mas_isMoniDis(lower=True):
        "Maybe I should wait until I am more affectionate with Monika before I ask her to play anything with me..."
        m "..."
        return

    else:
        $ mentalgamechance = renpy.random.randint(1,10)
        if 7 > mentalgamechance:
            m "Oh..."
            m "You want to play a game with me?"
            m "I guess we can play..."
            if persistent._mental_minigame1play == False:
                if persistent._mas_pm_cares_about_dokis == True:
                    m "Well, before we can play can I ask you something [player]?"
                    m "This minigame that I have created for us to play has some dark topics that can be talked about..."
                    menu:
                        m "Are you still uncomfortable talking about the other Dokis?"
                        "No":
                            $ persistent._mas_pm_cares_about_dokis = False
                            m "Alright [player]."
                            m "If you ever change your mind you can always let me know later."
                            m "Anyways [player]."
                        "Yes":
                            $ persistent._mas_pm_cares_about_dokis = True
                            m "Alright [player]."
                            m "I will try my best to not include anything that can be dark about the others for you."
                            m "Anyways..."
                    m "I guess since it is our first time playing this, do you want to know how to play?"
                menu:
                    "Yes":
                        m "The rules should be pretty simple for you to get..."
                        m "I will give you 4 options to choose from, and you have to find the lie from them all."
                        m "It is a really simple game, so you shouldn't have any trouble playing it."
                    "No":
                        m "Okay."
                        jump mentalminigametheme
        else:
            m "I am not in the mood to play with you [player]."
return

#this key will be needed! 
#1=Doki Doki Lore/characters 
#2=Monika Knowledge (dialog she says and stuff about her in general)
# 3=Mental Disability Knowledge (pretty useful to know since it fits in of course) 
#4=philosophy 
#5=misc [For now]

label mentalminigametheme:
    m "Do you want to have a theme for this game [player]?"
    menu:
        m "Do you want to have a theme for this game [player]{fast}?"
        "Surprise me [m_name]!":
            $ mentalminigametheme = renpy.random.randint(1,5)
            "Okay [player]!"
                #jump threetruthsandaliegame
        "Can the theme be about you [m_name]?":
            m "About {w=0.1}me?"
            if mas_isMoniNormal(higher=True):
                m "Hehe~"
                m "You always know how to flatter me [player]."
                $ mentalminigametheme = 2 #sets the theme to knowledge about Monika
            else:
                m "I didn't think you cared about me that much [player]..."
                m "Anyways... Thank you for playing with me [player]."
                m "It means a lot that you want to spend time with me."
                $ mentalminigametheme = 2 #sets the theme to knowledge about Monika
        "Can the theme be about Doki Doki Liturature Club":
            m "Sure!"
            m "Give me a moment to think of something [player]..."
            $ mentalminigametheme = 1 #sets the theme to Doki Doki Lore/character facts
            jump threetruthsandaliegame
        "Can the theme be about mental disabilities?":
            m "Sure!"
            m "I hope you have been studying [player]!"
            #jump threetruthsandaliegame
        "Can the theme be about philosophy":
            m "Sure!"
            m "I hope you have been paying attention to me [player]!"
            #jump threetruthsandaliegame
return
#seed keys 1: general stuff (if pm_cares_about_dokis minimum is 2) 2: Obscure Facts 3: Media
#4: general stuff w/o insensitive stuff 5: Misc
label threetruthsandaliegame:
    m "Let me think of something..."
    $ persistent._mental_minigame1play = True
    $ speciallieDon = False
    #$ mentalminigameseed = renpy.random.randint(1,5)
    $ mentalminigameseed = 1 #Force the seed to always be one for now! #All games with the seed 1 modifier, will branch out to the other themes
    if mentalminigameseed == 1:
        if mentalminigametheme == 1: #Doki Doki Lore/characters
            python:
                mentalminigameliepool = [
                    _("Doki Doki Literature Club was released in 2016."), 
                    _("Natsuki does not have her own route."), 
                    _("Don Salvato is the creator of DDLC."),
                    _("Sayori is the shortest Doki."),
                    _("There are four character routes in the game."), 
                    _("Sayori will give you a special poem if you tell her you love her."),
                    _("Yuri is younger than me.")
                    ]
                mentalminigamelie = random.choice(mentalminigameliepool)
                if mentalminigamelie == "Don Salvato is the creator of DDLC.":
                    speciallieDon = True

            m "This is a test right now!"
            m "I chose [mentalminigamelie]!"
            python:
                import random
                mentalminigametruthpool = [
                    _("There are secret messages hidden inside of the game."), 
                    _("There is a secret ending if you delete Sayori immediately."), 
                    _("Right before Yuri's confession there will be a file titled 'haveaniceweekend'."), 
                    _("There are 11 special poems in the game"), 
                    _("There is a secret poem if you complete the girl's routes in a special order.")
                    ]
                mentalminigametruth1 = random.choice(mentalminigametruthpool)
                for truth in mentalminigametruthpool:
                    if truth == mentalminigametruth1:
                        mentalminigametruthpool.remove(truth)
                mentalminigametruth2 = random.choice(mentalminigametruthpool)
                for truth in mentalminigametruthpool:
                    if truth == mentalminigametruth2:
                        mentalminigametruthpool.remove(truth)
                mentalminigametruth3 = random.choice(mentalminigametruthpool)
                for truth in mentalminigametruthpool:
                    if truth == mentalminigametruth3:
                        mentalminigametruthpool.remove(truth)
                if mentalminigamelie == "Don Salvato has made DDLC.":
                    speciallieDon = True
                mentalminigametruthpool = [
                    _("There are secret messages hidden inside of the game."), 
                    _("There is a secret ending if you delete Sayori immediately."), 
                    _("Right before Yuri's confession there will be a file titled 'haveaniceweekend'."), 
                    _("There are 11 special poems in the game"), 
                    _("There is a secret poem if you complete the girl's routes in a special order.")
                    ]
            $ mentalminigamemenurandomizer = renpy.random.randint(1,4)
            if mentalminigamemenurandomizer == 1:
                menu:
                    "[mentalminigamelie]":
                        if speciallieDon == True:
                            call special_lie_don_salvato
                        else:
                            m "This was the lie. [mental_minigame_win_quip]"
                    "[mentalminigametruth1]":
                        m "This was the truth! [mental_minigame_loss_quip]"
                    "[mentalminigametruth2]":
                        m "This was a truth! [mental_minigame_loss_quip]"
                    "[mentalminigametruth3]":
                        m "This was also a truth! [mental_minigame_loss_quip]"
            elif mentalminigamemenurandomizer == 2:
                menu:
                    "[mentalminigametruth1]":
                        m "This is a truth! [mental_minigame_loss_quip]"
                    "[mentalminigamelie]":
                        if speciallieDon == True:
                            call special_lie_don_salvato
                        else:
                            m "This was the lie! [mental_minigame_win_quip]"
                    "[mentalminigametruth2]":
                        m "This was a truth! [mental_minigame_loss_quip]"
                    "[mentalminigametruth3]":
                        m "This was a truth! [mental_minigame_loss_quip]"
            elif mentalminigamemenurandomizer == 3:
                menu:
                    "[mentalminigametruth1]":
                        m "This was a truth! [mental_minigame_loss_quip]"
                    "[mentalminigametruth2]":
                        m "This was a truth! [mental_minigame_loss_quip]"
                    "[mentalminigamelie]":
                        if speciallieDon == True:
                            call special_lie_don_salvato
                        else:
                            m "This was the lie! [mental_minigame_win_quip]"
                    "[mentalminigametruth3]":
                        m "This was a truth! [mental_minigame_loss_quip]"
            else:
                menu:
                    "[mentalminigametruth1]":
                        m "This is a truth! [mental_minigame_loss_quip]"
                    "[mentalminigametruth2]":
                        m "This is a truth! [mental_minigame_loss_quip]"
                    "[mentalminigametruth3]":
                        m "This was a truth! [mental_minigame_loss_quip]"
                    "[mentalminigamelie]":
                        if speciallieDon == True:
                            call special_lie_don_salvato
                        else:
                            m "This was a lie! [mental_minigame_win_quip]"
        jump mentalminigameplayagain
    else:
        return
                
label mentalminigameplayagain:
    menu:
        m "Would you like to play again [player]?"
        "Yes":
            m "Do you want to play with a different theme [player]?"
            menu:
                "Yes":
                    jump mentalminigamethemere
                "No":
                    m "Alright [player]!"
                    jump threetruthsandaliegame
        "No":
            m "Alright [player]."
            m "Let's play again soon!"
            return
            
label mentalminigamethemere:
    m "What new theme do you want to play with [player]?"
    menu:
        m "What new theme do you want to play with [player]{fast}?"
        "Surprise me [m_name]!":
            $ mentalminigametheme = renpy.random.randint(1,5)
            "Okay [player]!"
                #jump threetruthsandaliegame
        "Can the theme be about you [m_name]?":
            m "About {w=0.1}me?"
            if mas_isMoniNormal(higher=True):
                m "Hehe~"
                m "You always know how to flatter me [player]."
                $ mentalminigametheme = 2 #sets the theme to knowledge about Monika
            else:
                m "I didn't think you cared about me that much [player]..."
                m "Anyways... Thank you for playing with me [player]."
                m "It means a lot that you want to spend time with me."
                $ mentalminigametheme = 2 #sets the theme to knowledge about Monika
        "Can the theme be about Doki Doki Liturature Club":
            m "Sure!"
            m "Give me a moment to think of something [player]..."
            $ mentalminigametheme = 1 #sets the theme to Doki Doki Lore/character facts
            jump threetruthsandaliegame
        "Can the theme be about mental disabilities?":
            m "Sure!"
            m "I hope you have been studying [player]!"
            #jump threetruthsandaliegame
        "Can the theme be about philosophy":
            m "Sure!"
            m "I hope you have been paying attention to me [player]!"
            #jump threetruthsandaliegame


return

#asks played if dokis are still cared for
label mental_minigame_doki_concern:
    m "Well, before we play, is it alright if I ask you something [player]?"
    m "This minigame that I have created for us to play features some dark topics..."
    menu:
        m "Are you still uncomfortable talking about the other Dokis?"
        "No":
            $ persistent._mas_pm_cares_about_dokis = False
            m "Alright, [player]."
            m "If you ever change your mind you can always let me know later."
        "Yes":
            $ persistent._mas_pm_cares_about_dokis = True
            m "Alright, [player]."
            m "I will try my best to not include anything that can be dark about the others for you."
    m "Anyways..."
    return
    
#tutorial
label mental_minigame_tutorial:
    m "Since it's out first time playing, would you like me to explain the rules?"
    menu:
        "Yes":
            m "In this minigame I will tell you three truthful statments and one lie."
            m "And from the four statments I tell you... You will try to pick the lie!"
            m "It's a pretty simple game, and it challenges how well you know someone or something!"
        "No":
            m "Alright [player]!"
    return

#special lies
#"don salvato"
label special_lie_don_salvato:
    m "Darn! I really thought I'd get you!"
    m "The lie said {i}Don,{/i} not Dan."
    m "This one was a bit of a trick question, ahaha!"
    m "You must be a very careful reader!"
    m "Anyways [player]..."
    m "This is a lie! You win!"
    return