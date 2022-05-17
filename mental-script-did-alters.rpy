#supports the DID alter function
default persistent._mental_health_alters = list()
default persistent._mental_health_current_alter = None

#persistent values
default persistent._mental_health_player_has_did = False


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
        m "Oh, actually, would you mind telling me your alters names?"
        m "I'll need to know who they are so I can be sure to refer to you all properly."
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

    call screen mas_gen_scrollable_menu(did_menu_items, mas_ui.SCROLLABLE_MENU_MEDIUM_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, final_item)

    if _return:
        call expression _return
    else:
        m "Oh, alright."

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
            ).strip(' \t\n\r').lower()

            if alter_name == "nevermind":
                m "Oh, alright."
                done = True
                break

            persistent._mental_health_alters.append(alter_name)
            
    menu:
        m "What gender is this person?"
        "Male":
            $ alter_gender == "M"
        "Female":
            $ alter_gender == "F"
        "Neither":
            $ alter_gender == "X"

    persistent._mental_health_alters_gender.append(alter_gender)
            
            m("Would you like to add another alter?")
            done = display_menu(
                [
                    ("Yes.", False),
                    ("No.", True)
                ]
            )
    return

label mental_health_did_remove_alter:
    label .rm_alter_loop:
    m "Which alter would you like to remove?{nw}"
    python:
        selectable_alters = [
            (alter_name, alter_name, False, False)
            for alter_name in persistent._mental_health_alters
        ]

        final_item = ("Nevermind.", False, False, False, 20)

    renpy.say(m, "Which alter would you like to remove?{fast}", interact=False)
    call screen mas_gen_scrollable_menu(selectable_alters, mas_ui.SCROLLABLE_MENU_MEDIUM_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, final_item)

    if _return:
        m "Alright, [player]."

        m "Are you sure you want to remove [_return]?{nw}"
        menu:
            m "Are you sure you want to remove [_return]?{fast}"

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

label mental_health_did_player_empty:
    m "Oh, sorry [player]."
    m "You haven't set up this alter yet."
    m "Once you set it up, I'll be happy to talk to you about it!"
    return

#fronting menu
label mental_health_did_menu_front:
    python:
        selectable_alters = [
            (alter_name, alter_name, False, False)
            for alter_name in persistent._mental_health_alters
        ]

        final_item = ("Nevermind.", False, False, False, 20)

    call screen mas_gen_scrollable_menu(did_menu_front_items, mas_ui.SCROLLABLE_MENU_MEDIUM_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, final_item)

    if _return:
        persistent._mental_health_current_alter = index(_return)
        m "Alright!"

        #HACK: We set an alter by setting the playername to the alter name. This way it carries over sessions
        persistent.playername = _return
        player = _return
        #attempt to set gender
        persistent.gender = alter_gender

    else:
        m "Oh, alright."

    return
