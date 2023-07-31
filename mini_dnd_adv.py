import dice

special_attack_used = False


player_name = str(input("??: What will be your name in this new world?\n->"))
player_class = int(input("??: Who do you want to be?"
                         "\n->1. A Human Mage\n->2. A Dwarf Warrior\n->3. Human Rogue\n->4. Halfling Archer\n"
                         "-->"))

goat_stats = {"strength": 12, "dexterity": 10, "intelligence": 2, "wisdom": 13, "constitution": 11, "charisma": 5,
              "life": 10}

match player_class:
    case 1:
        class_name = "Mage"
        player_stats = {"strength": 14, "dexterity": 18, "intelligence": 18, "wisdom": 11, "constitution": 19,
                        "charisma": 16, "life": 10}
        player_power = {"Magic Missile": (dice.dice_roll(4) + 1) * 3}
        normal_attack = dice.dice_roll(6)

    case 2:
        class_name = "Warrior"
        player_stats = {"strength": 20, "dexterity": 14, "intelligence": 14, "wisdom": 15, "constitution": 18,
                        "charisma": 15, "life": 14}
        player_power = {"My Fight": dice.dice_roll(6) + dice.dice_roll(6)}
        normal_attack = dice.dice_roll(6)

    case 3:
        class_name = "Rogue"
        player_stats = {"strength": 16, "dexterity": 19, "intelligence": 16, "wisdom": 12, "constitution": 13,
                        "charisma": 16, "life": 9}
        player_power = {"Stab in Back": dice.dice_roll(8) + dice.dice_roll(4) + 4}
        normal_attack = dice.dice_roll(6)

    case 4:
        class_name = "Archer"
        player_stats = {"strength": 17, "dexterity": 16, "intelligence": 15, "wisdom": 11, "constitution": 18,
                        "charisma": 13, "life": 12}
        player_power = {"Right in": dice.dice_roll(6) + dice.dice_roll(4)}
        normal_attack = dice.dice_roll(6)

player_life = player_stats['life']

special_attack_used = False


def goat_fight():
   # global special_attack_used
    while player_life > 0 and goat_stats["life"] > 0:
        print(f"The Great Helper: {player_name.title()}, go on, do something\n")
        print("->1. Normal Attack\n")
        if not special_attack_used:
            print("->2. Special Attack\n")

        action = int(input("The Great Helper: What will you do?\n"))

        if action == 1:
            damage = normal_attack
            goat_stats["life"] -= damage
            print(f"The Great Helper: You dealt {damage} damage to the goat... Not bad!")
        elif action == 2 and not special_attack_used:
            power_name, power_value = player_power.popitem()
            damage = power_value
            goat_stats['life'] -= damage
            print(f"The Great Helper: You used {power_name} and dealt {damage} damage to the goat!! HOLY!!\n")
            special_attack_used = True
        else:
            print("The Great Helper: Are you dumb? Try again..\n")

        if goat_stats['life'] <= 0:
            print("The Great Helper: Oh no! You defeated the poor gore goat :c\n")
            break

        print("The Great Helper: Let's go, Goaty!\n")
        goat_damage = dice.dice_roll(4) * 2
        player_stats['life'] -= goat_damage
        print(f"The Great Helper: The goat is furious and attacked you!\n"
              f"It dealt {goat_damage} damage!\n"
              f"The Great Helper: Now you have {player_life} life points")

        if player_life <= 0:
            print(f"The Great Helper: Oh no! You were defeated by a simple goat!\n"
                  f"The Great Helper: HAHAHAHAHAHA\n"
                  f"The Great Helper: LOOOOOOSEEEERRRR!\n"
                  f"The Great Helper: Now, {player_name.title()}, you have to rebirth. Sorry *GIGGLES*")
            raise SystemExit
            break


print(f"??: *Gigles* Ok, {player_name.title()}... So you will be a {class_name} with these stats:\n {player_stats}\n")

print("??: Let's start here... \n"
      "    You live in a small town with a few adventurers (all newbies, like you) *giggles*\n"
      "    Now I, The Great Helper, will stop here and you have to live like you want~~.\n\n\n"
      "---> a year later...\n\n"
      "The Great Helper: OH YEAH , I am back to help you ! I will narrate your story\n"
      f"{player_name.title()}: NO, YOU DON'T HAVE TO...\n"
      f"The Great Helper: Shhh {player_name.title()} you don't know nothing...\n"
      "                   *Hem hem* As I was saying...\n"
      "                   5 years later...\n"
      "                   You enter a tavern, life is not as easy as you thought it would be\n"
      f"Tavern's Owner: Hey {player_name.title()}, I heard a lot about you and I know that\n"
      "                 *starts to whisper* You want some job to 'help' the others *blink*\n"
      "                 Guess what? I have something very sPeCiAl for you\n"
      "The Great Helper: Life is hard, and you don't have another choice than accept the job...\n"
      "                  Your 6 displacer kittens need to eat and they only like first-class meat\n"
      "                  or high elf meat (i think this one is illegal) \n"
      f"{player_name.title()}: OK... What is the job?...\n"
      "Tavern's Owner: So... I have a product here that needs to be delivered to a partner of mine, \n"
      "                The gun shop owner in the next town\n"
      "                You will earn some good gold and meat.\n"
      f"{player_name.title()}: Oof, ok... Tomorrow at 15h I will be here to do this\n"
      "The Great Helper: The next day...\n"
      f"Tavern Owner: Here, {player_name.title()}, take this package and beware, you have 7 hours to deliver it!\n"
      "               Say that Copia send it to him.\n"
      "The Great Helper: You see that the package is somehow heavy for its size.\n"
      "                  And found it strange, but ok, all for the kittens\n"
      "                  You look at the map and see that you have to choose between two ways:\n"
      "                  -1. By the forest\n"
      "                  -2. By the low road\n")

way_choice = int(input("                  What path will you choose?\n                  -->"))

if way_choice == 1:  # Vai pela floresta
    print(
        f"The Great Helper: Walking about 30 min {player_name.title()} starts to see some blood on the road and hear "
        "screams ...\n"
        "                  OOH,scary\n"
        "                  You want to turn back but the clock goes like TICK TOCK F*CK YOU\n"
        "                  So you see a cute goat ... a cute furious one...\n"
        "                  So you will.....\n ")

    goat_choice = int(input("                 -1.Sneak past it \n"
                            "                 -2.I will go straight ahead... It's only a goat, anything I slap its face\n"
                            "                 -3.Find another way to deal with this situation\n-->"))

    if goat_choice == 1:  # Stealth check

        if player_stats['wisdom'] >= goat_stats['wisdom']:
            print("The Great Helper: You sneaked through the trees and the horned berserker\n"
                  "                  Didn't even notice your presence, continuing to gore its victim\n")
        else:
            print("The Great Helper: You made too much sound 'ninja' XD... \n")
            goat_choice = 2

    if goat_choice == 2:  # porrada
        print("The Great Helper: You really don't value your life... \n"
              "                  Of course the cute horned killer looked at you and.. \n"
              "                  The great helper rolls the initiative for you and the goat *rolls the dice*\n")
        goat_fight()

    elif goat_choice == 3:  # Outro jeito de lidar
        print("The Great Helper: You think that has only two options :\n"
              "                  -1.Try to jump when it comes and then run\n"
              "                  -2.Try to befriend with the furious thing\n ")

        peaceful_choice = int(input("                  What you will choose?\n                  -->"))

        if peaceful_choice == 1:
            print("The Great Helper: You caught the attention of the extremely cute angry goat\n"
                  "                  It's looked at you with its angry eyes and started to charge !\n"
                  "                  You waited for the right time and jump and you ...\n *Rolls the dice*\n")

            if player_stats['dexterity'] - 20 + dice.dice_roll(20) >= 10:
                print(
                    "The Great Helper: Manage to pass and soon after returning to the ground you run desperately and "
                    "lose the goat\n")

            else:
                player_life -= dice.dice_roll(5)
                print(
                    f"The Great Helper: You fall and lose hurt yourself very bad and full of shame {player_name.title()} play dead,\n"
                    "                  the goat smells you and felt the fear you made in your pants\n"
                    "                  It's decided to leave because you are so pathetic...\n"
                    "                  Note ? Do (Brazilian joke) ...\n "
                    f"                  If you put in numbers it's like you have {player_life} of your health point\n")


        elif peaceful_choice == 2:
            print(
                "The Great Helper: You try befriend with the collision angry beast\n"
                "                  You have a suspicious corn that in you bag *eew* and tried to give it to him\n"
                "                  Let's see if you will trick it")

            if dice.dice_roll(20) + goat_stats['wisdom'] - player_stats['wisdom'] + player_stats['charisma'] >= 10:
                print(
                    "The Great Helper: OK...\n"
                    "                  I don't know how but the dangerous beast liked the suspicious corn...\n"
                    "                  YAY ＼(٥⁀▽⁀ )／\n")
            else:
                print(
                    "The Great Helper: The beast was more intelligent than you, and didn't accept the suspicious corn\n"
                    "                  (Neither you would accept that thing that look like a cthulhu baby which was trodden\n"
                    "                  on with a boot full of rusty iron and then , as the chef 's touch , acid was added\n"
                    "                  With this look (눈_눈), as if you hear it's thinking -You f*cker\n"
                    "                  He seems to pull away but he's actually pulling away to punish his ill-fated\n "
                    "                  attempt to befriend the piece of shit.\n"
                )
                print("                  You have lost some health and your dignity\n")

                player_life -= dice.dice_roll(5)
                print(f"                  Now you have have something like {player_life}, little one\n")


elif way_choice == 2:# Vai pela estrada baixa
    other_choice ={}
    print("The Great Helper: Oh , what a lovely  rainy\n"
          "                  Nothing will going to be wrong..\n"
          f"                  It's what {player_name.title()} thinks...\n"
          f"{player_name.title()}: But I didn't...\n"
          "The Great Helper: SHUT UP! *AHEM* \n"
          "*BIG THUNDER NOISES*\n"
          "The Great Helper: Oh , WhAt A pItY! It seems the bridge is almost falling! *EVIL GIGLES*\n")

    low_choice = int(input("The Great Helper:What you will do ?\n"
                           "                 -1.As you are so skinny, why not try to pass? \n"
                           "                 -2.I guess you can try swimming across the river \n"
                           "                 -3.Try to get a natural help to pass across the river\n-->"))

    if low_choice == 1:  #d20 vai na sorte
        print(f"The Great Helper: {player_name.title()} tried using luck and... *rolls the dice*")

        if dice.dice_roll(20) > 15 :
            print("                  Hmmm, not bad, you passed ~~")

        else:
            player_life -= dice.dice_roll(5)
            print("                  The bridge fall and you are hurt , of course,\n"
                  f"                  now you have {player_life} of life, little one\n"
                  "                  Bro, you don't know how to use your brain, do you? \n")

            other_choice = int(input("The Great Helper: Now you are on the ground and you have the others choice\n"
                                     "                 -1.I guess you can try swimming across the river \n"
                                     "                 -2.Try to get a natural help to pass across the river\n-->"))


    if low_choice == 2 or other_choice == 1:  # passar nadando
        print("The Great Helper: Now you can show that your childhood swimming lessons were not in vain *rolls the dice*")

        if player_stats['strength'] + dice.dice_roll(5) > 18:
            print("                  OOOOH NICE! I THOUGHT YOU WERE A FISH!\n")

        else:
            player_life -= dice.dice_roll(5)
            print("                  OOF , you almost drown yourself... I think you are not born to be a swimmer\n"
                  f"                 now you have {player_life}, little mermaid \n"
                  "                  Better try to get help of a lovely creature~~\n")
            low_choice = 3


    if low_choice == 3 or other_choice == 2:  # pedir ajuda do crocodilo (10) wisdom +d4

        print("The Great Helper: 2 options, baby :\n"
              "                 -1.Try to ask the crocodile with a big smile \n"
              "                 -2.Try to ask the crocodile with aggressiveness\n ")

        crocodile_choice = int(input("                  What you will choose?\n                  -->"))

        if crocodile_choice == 1:
            print(f"The Great Helper: So, {player_name.title()} try to ask with the most gentle way possible\n"
                  f"                  to the crocodile and...")
            if player_stats['charisma'] >= 10:
                print("                  Oh... You're really good with the words and the crocodile agreed to help you.\n"
                      "                  Good education is a really powerful weapon!\n")

            else:
                print(f"                  I guess you don't know how to talk with a reptilian and it bits you...\n"
                      f"                  You evade but the crocodile scratch you and now you have... *roll the dice* \n")
                player_life -= dice.dice_roll(5)
                print(f"                  *making the calculations*...{player_life} of life")
                crocodile_choice = 2


        if crocodile_choice == 2:
            print("The Great Helper: You take a deep breath and try to exert dominance over the reptilian beast..\n"
                "                  Let's see if you are the crocodile master! *rolls the dice*\n ")

            if player_stats['wisdom'] + player_stats['charisma'] >= 10 + dice.dice_roll(20):
                print(
                    "The Great Helper: OK... You are an awsome creature! The crocodile now see you as a superior and\n"
                    "                  agreed to carry you to the OTHER SIIIIIIIIIIDEEEEEE!"
                )
            else:
                print(
                    "The Great Helper: Why such rudeness? *OOF*\n"
                    "                  The crocodile didn't like your act and tried to bite you *rolls the dice*"
                )
                player_life -= dice.dice_roll(5)
                print(f"                  Let's see... You lost some blood and now have {player_life} "
                      "and a guilty conscience ")

print("The Great Helper:Good job , now you are half-way there and it's on time!\n"
      "                 Yeah, I didn't expect anything from y... I always trusted :)!\n"
      "                 *AHEM* ...Something is specially strange in this package and you...\n")
see_or_not = int(input(f"                 -1 {player_name.title()} is a creature very curious!\n"
                       f"                 -2 {player_name.title()} doesn't care and just wants to get this over"
                       f" with and go home\n                 -->"))

if see_or_not == 1:# Ve
    print(f"The Great Helper: The curious cat, aka:{player_name.title()} though:"
          "                  'What's a fart to someone who shitty himself?' and looked inside...\n"
          "                  Inside of it there's a... Sprite, not the one you drink, but the one that look like a fairy...?\n"
          "                  Ook,it's an cute little sprite that looks like it's been put into a sleep state\n"
          f"                  Congratulations {player_name.title()}, now you are smuggler~~ I bet your mommy is crying right now!\n")

    sprite_choice = int(input("                  Now that you know what is inside, what you will do ?\n"
                              "                  1-Why not help this cute guy?\n"
                              "                  2- kekeke Now it's better to change the deal and increase the reward\n"))

    if sprite_choice == 1:#Ajuda a fada
        print("The Great Helper: Oh little one, I guess there's something good in your little body\n"
              f"                  So {player_name.title()} freed the little sprite and woke it up\n"
              f"{player_name.title()}: Hey listen! Hey listen! Hey listen! * drop some water on it*\n"
              "Sprite: OOF! Wha What What happened?\n"
              f"{player_name.title()}: You were caught by a bandit and they tried to sell you to someone, but I freed you :)\n"
               "Sprite: ...Holy... I will never drink again... Thank you,bro ...  I will be always gratefull to you\n"
              "         Hey, why don't you come with me to my master in fairy land ? I'm sure that my boss will be grateful\n"
              "          Come , come !  You can live with us , I'm sure !\n"
              "The Great Helper: NICE ! I guess this is the best choice possible !\n"
              f"                 {player_name.title()} will go with the sprite, but before the kittens will be magically\n"
              "                   teleported to the fairy world to live a peaceful life with you.")


    elif sprite_choice == 2 : # vai pra cidade
        print("The Great Helper: You are a very bad creature... The karma will chase you... life snakes...\n"
              "                  So... The city is not far from here and you already see the local to retrieve the package!\n"
              "                  Luck of you! You can't stand having to take that package anymore,\n"
              "                  you think it's been a while since you've been away from the kittens...\n"
              f"{player_name.title()}: Finnaly I can see the gun shop and I've got a good feeling.... a profitable feeling...\n"
              f"The Great Helper: So, {player_name.title()} entered the gun shop\n"
              "Gun Shop Owner: Oh, welcome to the gun shop! What you want?\n"
              f"{player_name.title()}: So... Tavern's Owner, Copia, told me to bring this package to you *smirks*...\n"
              "Gun Shop Owner: Oh, nice nice nice ! Give to me , give to me ! \n"
              f"{player_name.title()}: He he , wait a minute my friend... I was thinking and i guess you can rise the reward...\n"
              "The Great Helper: HOHOHOHO THE BAD GUY IS REALLY BAD! *rolls the charisma dice*")
        if player_stats['charisma'] > dice.dice_roll(20):
            print("Gun Shop Owner: hm , er, hm , OK OK , I WILL RISE IT BUT DON'T TELL ANYONE ABOUT IT...\n"
                  f"{player_name.title()}: Good.. Here you package, good sir!"
                  "Gun Shop Owner: Urg...")
        else:
            print("Gun Shop Owner: Are you out of mind? *pull a BIG gun*\n"
                 f"{player_name.title()}:Kyaaan, STOP NIICHAN~\n"
                  "Gun Shop Owner: WHAT DID YOU SAY?\n"
                 f"{player_name.title()}: No-No....NOthinG Sir... here here...\n"
                  "Gun Shop Owner: Good... Now Bye bye little B1tch * Fires the BIG gun*"
                  "The Great Helper: LOOOOL I didn't expect this ... now YOU'RE DEAD! LIFE SNAKES, BRO! (((o(*°▽°*)o)))")



elif see_or_not == 2 :#VAi pra cidade
    print("The Great Helper: Yeah...It's better to leave it alone...\n"
          "                  So... The city is not far from here and you already see the local to retrieve the package!\n"
          "                  Luck of you! You can't stand having to take that package anymore,\n"
          "                  you think it's been a while since you've been away from the kittens...\n"
          f"{player_name.title()}: Finnaly I can see the gun shop and leave this open world...\n"
          f"The Great Helper: So, {player_name.title()} entered the gun shop\n"
          "Gun Shop Owner: Oh, welcome to the gun shop! What you want?\n"
          f"{player_name.title()}: So... Tavern's Owner, Copia, told me to bring this package to you...\n"
          "Gun Shop Owner: Oh, nice nice nice ! Give to me , give to me ! *look inside the package*\n"
          "                Did you happen to peek into the contents of the package?\n"
          f"{player_name.title()}: Of course not , sir! I only want my reward and go home...\n"
          "Gun Shop Owner: Hmmm... good , Take this * retrieve the reward*\n"
          f"{player_name.title()}: Oh , Thanks pal!\n")

print(f"The Great Helper: And this is the end of {player_name.title()}'s journey! See ya!\n"
      "	              ☆ ～('▽^人)\n "
      " --------------------------THE END--------------------------")


