#supports the DID alter function
#List of tuples:
# [0] - Alter name
# [1] - Alter gender
default persistent._mental_health_alters = list()
default persistent._mental_health_current_alter = None

#persistent values
default persistent._mental_health_player_has_did = False

#Flag used to avoid continually adding the current player state to the list of alters
default persistent._mental_health_added_initial_entry = False

#Submod header
init -990 python in mas_submod_utils:
    Submod(
        author="Kkrosie123",
        coauthors=["multimokia"],
        name="pls add name here",
        description="pls add description here",
        version="1.0.0",
        version_updates={}
    )

#As a baseline, we can assume the current player information is one of the player's alters.
#If this information is present, let's add it to the list of alters.
init 10 python:
    if (
        not persistent._mental_health_added_initial_entry
        and persistent.gender
        and persistent.playername
    ):
        new_alter_data = (player, persistent.gender)
        persistent._mental_health_alters.append(new_alter_data)

        #We should also set the current alter
        persistent._mental_health_current_alter = persistent._mental_health_alters.index(new_alter_data)
        #Flag so we don't keep appending the playername + current gender
        persistent._mental_health_added_initial_entry = True

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mental_health_did_menu_0",
            category=['you', 'mental health'],
            prompt="I want to change my system and alters.",
            pool=True,
            conditional="persistent._mental_health_player_has_did",
            action=EV_ACT_UNLOCK,
            rules={"no_unlock": None}
        )
    )

label mental_health_did_menu_0:
    if not persistent._mental_health_alters:
        m 3eud "Oh, actually, would you mind telling me your alters names?"
        m 3rksdlb "I'll need to know who they are so I can be sure to refer to you all properly."
        call mental_health_did_add_alter

    python:
        did_fronting_quips = [
            _("I am currently fronting as..."),
            _("My current fronter is...")
        ]

        did_fronting_quip = random.choice(did_fronting_quips)

        did_menu_items = [
            ("I want to add a new alter.", "mental_health_did_add_alter", False, False),
            ("I want to remove an alter.", "mental_health_did_remove_alter", False, False),
            ("[did_fronting_quip]", "mental_health_did_menu_front", False, False)
        ]

        final_item = ("Nevermind.", False, False, False, 20)

    show monika at t21
    call screen mas_gen_scrollable_menu(did_menu_items, mas_ui.SCROLLABLE_MENU_MEDIUM_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, final_item)
    show monika at t11

    if _return:
        call expression _return
    else:
        m 1eka "Oh, alright."

    return

#editing alters
label mental_health_did_add_alter:
    python:
        done = False
        while not done:
            alter_name = mas_input(
                _("So what's their name?"),
                allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_",
                length=10,
                screen_kwargs={"use_return_button": True, "return_button_value": "nevermind"}
            ).strip(' \t\n\r').lower().capitalize()

            if alter_name == "Nevermind":
                m("Oh, alright.")
                break

            renpy.say(m, "What is their gender?", interact=False)
            alter_gender = menu(
                [
                    ("Male", 'M'),
                    ("Female", 'F'),
                    ("Neither", 'X'),
                ]
            )

            persistent._mental_health_alters.append((alter_name, alter_gender))

            renpy.say(m, "Would you like to introduce me to another alter?", interact=False)
            done = menu(
                [
                    ("Yes.", False),
                    ("No.", True)
                ]
            )

    #We only do this dialogue if the player doesn't exit this topic via Nevermind
    if done:
        m 3hua "Perfect, thanks [player]~"
        m 1eua "I should be able to refer to you all properly, all I need you to do is tell me who's fronting."
    return

label mental_health_did_remove_alter:
    label .rm_alter_loop:
    m "Which alter would you like to remove?{nw}"
    python:
        selectable_alters = [
            (alter_data[0], alter_data, False, False)
            for alter_data in persistent._mental_health_alters
        ]

        final_item = ("Nevermind.", False, False, False, 20)
        renpy.say(m, "Which alter would you like to remove?{fast}", interact=False)

    show monika at t21
    call screen mas_gen_scrollable_menu(selectable_alters, mas_ui.SCROLLABLE_MENU_MEDIUM_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, final_item)
    show monika at t11

    if _return:
        $ alter_name = _return[0]
        m "Alright, [player]."

        m "Are you sure you want to remove [alter_name]?{nw}"
        menu:
            m "Are you sure you want to remove [alter_name]?{fast}"

            "Yes":
                m "Alright."
                $ persistent._mental_health_alters.remove(_return)

                m "Would you like to remove another alter?{nw}"
                menu:
                    m "Would you like to remove another alter?{fast}"

                    "Yes":
                        jump .rm_alter_loop

                    "No":
                        pass

            "No":
                m "Alright, [player]."
    return

#fronting menu
label mental_health_did_menu_front:
    python:
        selectable_alters = [
            (alter_name, (alter_name, alter_gender), False, False)
            for alter_name, alter_gender in persistent._mental_health_alters
        ]

        final_item = ("Nevermind.", False, False, False, 20)

    show monika at t21
    $ renpy.say(m, "So who am I spending time with right now?~", interact=False)
    call screen mas_gen_scrollable_menu(selectable_alters, mas_ui.SCROLLABLE_MENU_MEDIUM_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, final_item)
    show monika at t11

    if _return:
        python:
            persistent._mental_health_current_alter = persistent._mental_health_alters.index(_return)

            #Deconstruct the tuple
            alter_name, alter_gender = _return

            #HACK: We set an alter by setting the playername to the alter name. This way it carries over sessions
            persistent.playername = alter_name
            player = alter_name

            #Update the stored gender for session carryover
            persistent.gender = alter_gender

        #And finally update any/all pronoun gender vars
        call mas_set_gender

        m 1hua "Alright [player], what would you like to do today?"

    else:
        m 1eka "Oh, alright."

    return
