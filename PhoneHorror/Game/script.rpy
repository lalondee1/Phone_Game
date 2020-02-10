#### this code is made for 1920 x 1080 so if you use another dimension youre going to have to fiddle with the numbers to make this work
## rest of the code happens in screens.rpy and options.rpy

define n = Character('[name]')

label start:
    $ name = renpy.input("What is your name?")
    $ name = name.strip()

    if name == "":
     $ name="You"

call phone_start
call screen phonestart
label story_start:
    call phone_msngr
    call message_start("Montague Summers", "Hello there good fellow, how may I help you?")
    call reply_message("SCREEEEEEE")
    call message("Montague Summers", " So your name is [n]?")
    call message("Montague Summers", "Thats a really fucking weird name, you sound like a abomination to me!!")
    call message_img("Montague Summers","I'm coming for you, you bitch","MS portrait.jpg")
    call screen phone_reply("Screeee","choice1","message the dark lord","choice2")

label choice1:

    call phone_after_menu

    call message_start("[name]", "The Dark Lord shall take you, reeeeee")
    call message("nadia", "The dark powers cannot affect me! Montague Summers!")

    call screen home1

label choice2:
    call phone_after_menu
    call message_start("[name]", "My lord ")
    call message("nadia", "well, its a shame but your feelings are valid")

    call screen home1

label aftermenu:
    call phone_end
    call phone_menu
    call screen home_menu

label WitchApp:
    call phone_end
    call witch_app
    n "Guess I could write my feelings into an app which I'm sure will record my information for some nefarious evil"
    call screen phone_reply ("My day went pretty well","choice5", "I'm pretty sure Montague Summers wants me dead","choice6")

label choice5:
    call message_start("[name]", "My day today has been rather good I'd say, lalalalala")
    jump witchapphappy

label choice6:
    call message_start("[name]", "I fear the great Montague Summers, I fear and envy his power")
    jump witchappsad

label witchapphappy:
    call phone_end
    call witch_app_happy
    n "well it looks like I'm okay"
    jump afterwitch

label witchappsad:
    call phone_end
    call witch_app_sad
    n "well I guess this doesn't look good"
    jump afterwitch


label afterwitch:


label choice7:
    call witchagram
    n "Should I make a nice or mean comment?"
    call screen phone_reply("Good Comment","choice8","Mean Comment","choice9")


label choice8:
    call comments
    call message_start("[name]","Hey Summers, looking pretty hot xoxo.")
    call message("Montague Summers","You'll rue the da-, oh thank you?")

label choice9:
    call comments
    call message_start("[name]","Ha!, you look well fat! lol")
    call message("Montague Summers","I'll get you, you little monster!!")
    call screen phone_reply("Phone up Montague","choice11","Check out my photos","choice12")

label gallery1:
    call phone_end
    call gallery
    n "wow! I am so pretty!!"
    n "gotta stop looking so hella good"
    return


label contacts1:
    call phone_end
    call contacts
    call screen phone_reply("Call Montague Summers","choice13","call the dark lord","choice14")


label choice13:
    call phone_call
    "ring ring ring"
    "No one answers"
    return

label choice14:
    call phone_call
    "ring ring ring"
    "No one answers"
    return

return
