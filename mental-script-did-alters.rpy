#supports the DID alter function
#defaults:
#there are 10 slots
default persistent._mental_health_did_alter_1 = "Empty"
default persistent._mental_health_did_alter_2 = "Empty"
default persistent._mental_health_did_alter_3 = "Empty"
default persistent._mental_health_did_alter_4 = "Empty"
default persistent._mental_health_did_alter_5 = "Empty"
default persistent._mental_health_did_alter_6 = "Empty"
default persistent._mental_health_did_alter_7 = "Empty"
default persistent._mental_health_did_alter_8 = "Empty"
default persistent._mental_health_did_alter_9 = "Empty"
default persistent._mental_health_did_alter_10 = "Empty"
#persistent values
default persistent.mental_player_has_did = False
#default for the database
#alternative slot definitions
default player_1 = persistent._mental_health_did_alter_1
default player_2 = persistent._mental_health_did_alter_2
default player_3 = persistent._mental_health_did_alter_3
default player_4 = persistent._mental_health_did_alter_4
default player_5 = persistent._mental_health_did_alter_5
default player_6 = persistent._mental_health_did_alter_6
default player_7 = persistent._mental_health_did_alter_7
default player_8 = persistent._mental_health_did_alter_8
default player_9 = persistent._mental_health_did_alter_9
default player_10 = persistent._mental_health_did_alter_10

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mental_health_did_menu_0",
            category=['you', 'mental health'],
            prompt="I want to change my system and alters.",
            pool=True,
            #if persistent.mental_player_has_did = True:
                #unlocked=True
            #enabled permanently for now
            unlocked = True
        )
    )

label mental_health_did_menu_0:
    python:
        did_fronting_quips = [
            _("I am currently fronting as..."),
            _("My current fronter is...")
        ]
        did_fronting_quip = random.choice(did_fronting_quips)
        did_menu_items = [
            ("I want to edit my alters.", "mental_health_did_setup", False, False),
            ("[did_fronting_quip]", "mental_health_did_fronting", False, False)
        ]
        final_item = ("Nevermind.", False, False, False, 20)

    call screen mas_gen_scrollable_menu(did_menu_items, mas_ui.SCROLLABLE_MENU_MEDIUM_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, final_item)

    if _return:
        call expression _return
    else:
        m "Oh, alright."

    return

#fronting and choosing predefined alters

label mental_health_did_fronting:
    m "Who do you want to front as?"
    call mental_health_did_menu_front
    return

#editing alters

label mental_health_did_setup:
    m "Oh? Do I get to meet someone new?"
    return

label mental_health_did_player_empty:
    m "Oh, sorry [player]."
    m "You haven't set up this alter yet."
    m "Once you set it up, I'll be happy to talk to you about it!"
    return

#fronting menu
label mental_health_did_menu_front:
    python:
        did_menu_front_items = [
            ("[player_1]", "front_player_1", False, False),
            ("[player_2]", "front_player_2", False, False),
            ("[player_3]", "front_player_3", False, False),
            ("[player_4]", "front_player_4", False, False),
            ("[player_5]", "front_player_5", False, False),
            ("[player_6]", "front_player_6", False, False),
            ("[player_7]", "front_player_7", False, False),
            ("[player_8]", "front_player_8", False, False),
            ("[player_9]", "front_player_9", False, False),
            ("[player_10]", "front_player_10", False, False)
        ]
        final_item = ("Nevermind.", False, False, False, 20)

    call screen mas_gen_scrollable_menu(did_menu_front_items, mas_ui.SCROLLABLE_MENU_MEDIUM_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, final_item)

    if _return:
        call expression _return
    else:
        m "Oh, alright."

    return

label front_player_1:
    if player_1 == "Empty":
        call mental_health_did_player_empty
    else:
        m "Test"
    return

label front_player_2:
    if player_2 == "Empty":
        call mental_health_did_player_empty
    else:
        m "Test"
    return

label front_player_3:
    if player_3 == "Empty":
        call mental_health_did_player_empty
    else:
        m "Test"
    return

label front_player_4:
    if player_4 == "Empty":
        call mental_health_did_player_empty
    else:
        m "Test"
    return

label front_player_5:
    if player_5 == "Empty":
        call mental_health_did_player_empty
    else:
        m "Test"
    return

label front_player_6:
    if player_6 == "Empty":
        call mental_health_did_player_empty
    else:
        m "Test"
    return

label front_player_7:
    if player_7 == "Empty":
        call mental_health_did_player_empty
    else:
        m "Test"
    return

label front_player_8:
    if player_8 == "Empty":
        call mental_health_did_player_empty
    else:
        m "Test"
    return

label front_player_9:
    if player_9 == "Empty":
        call mental_health_did_player_empty
    else:
        m "Test"
    return

label front_player_10:
    if player_10 == "Empty":
        call mental_health_did_player_empty
    else:
        m "Test"
    return

