
# main formula for determining nature
def new_expcalc(new_rem, exp, rem, total):
    new_rem = int(new_rem)
    if (new_rem < rem):
        new_exp = (exp - (rem - new_rem)) + 25
        return int(new_exp)
    elif (new_rem >= rem):
        new_exp = (total * 25) + new_rem
        return int(new_exp)
 
def main(): 
    # list containing all 25 natures
    nature = ['hardy', 'lonely', 'brave', 'adamant', 'naughty',
              'bold', 'docile', 'relaxed', 'impish', 'lax',
              'timid', 'hasty', 'serious', 'jolly', 'naive',
              'modest','mild', 'quiet', 'bashful', 'rash',
              'calm', 'gentle', 'sassy', 'careful', 'quirky']

    # list containing the attributes of all 25 natures, in order
    stat_changes = ['no changes', '+Atk,-Def', '+Atk,-Spe', '+Atk,-Spa',
            '+Atk,-Spd', '+Def,-Atk', 'no changes', '+Def,-Spe',
            '+Def,-Spa', '+Def,Spd', '+Spe,-Atk', '+Spe,-Def',
            'no changes', '+Spe,-Spa', '+Spe,-Spd', '+Spa,-Atk',
            '+Spa,-Def', '+Spa,-Spe', 'no changes', '+Spa,-Spd',
            '+Spd,-Atk', '+Spd,-Def', '+Spd,-Spe', '+Spd,-Spa',
            'no changes']


    separator = "*" * 64

    print("\033c") #clears the screen
    print(separator)
    print("")
    exp = raw_input("Please write your GEN1 pokemon\'s current EXP total: > ") 
    print("")
    print(separator) 

    exp = int(exp) # converts exp into an integer
    rem = exp % 25 # the modulo value determines the nature of the pokemon
    total = exp / 25

    # as written above, rem stores the actual value of the nature, from 0 to 24,
    # therefore we call rem into both arrays.

    print("")
    print("When transferring your Pokemon to GEN7, its nature will be %s[%s]"
            % (nature[rem].title(),stat_changes[rem]))
    print("")
    print(separator) 
    print("")

    # now the fun part, we want to select our nature
    wanted_nature = raw_input("Which nature are you after?[example: Hasty] > ")

    if wanted_nature.lower() in nature:
        # gets the index number of the chosen nature from the list
        # and assigns it to new_rem
        new_rem = nature.index(wanted_nature.lower())
        new_exp = new_expcalc(new_rem, exp, rem, total) 
        diff = new_exp - exp 

        print("")
        print("You are going to have to obtain %s more exp points,for a total of %s."
                % (diff, new_exp))
        print("")
        print(separator) 
    else:
        print "That nature is invalid."
        exit(0)

if __name__ == '__main__':
    main()
