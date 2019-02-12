# Dict containing all 25 natures and their stats modifiers
NATURES_DICT = {
    'hardy': 'no changes',
    'lonely': '+Atk,-Def',
    'brave': '+Atk,-Spe',
    'adamant': '+Atk,-Spa',
    'naughty': '+Atk,-Spd',
    'bold': '+Def,-Atk',
    'docile': 'no changes',
    'relaxed': '+Def,-Spe',
    'impish': '+Def,-Spa',
    'lax': '+Def,Spd',
    'timid': '+Spe,-Atk',
    'hasty': '+Spe,-Def',
    'serious': 'no changes',
    'jolly': '+Spe,-Spa',
    'naive': '+Spe,-Spd',
    'modest': '+Spa,-Atk',
    'mild': '+Spa,-Def',
    'quiet': '+Spa,-Spe',
    'bashful': 'no changes',
    'rash': '+Spa,-Spd',
    'calm': '+Spd,-Atk',
    'gentle': '+Spd,-Def',
    'sassy': '+Spd,-Spe',
    'careful': '+Spd,-Spa',
    'quirky': 'no changes'
}


# Interact with user on console
def message_user(string, is_question=False):
    print("*" * 64)
    print("")
    if is_question:
        value = input(string)
    else:
        value = print(string)
    print("")
    return value


# Main Algorhythm for determining nature
def calculate_required_experience(new_rem, exp, rem, total):
    new_rem = int(new_rem)
    if (new_rem < rem):
        new_exp = (exp - (rem - new_rem)) + 25
        return int(new_exp)
    elif (new_rem >= rem):
        new_exp = (total * 25) + new_rem
        return int(new_exp)


# Get information about the user's pokemon
def get_pokemon_stats():
    current_experience = int(
        message_user(
            "Please write your GEN1 pokemon's current EXP total: > ",
            is_question=True,
        )
    )

    # The modulo value determines the current nature of the pokemon
    current_nature_value = current_experience % 25
    total = current_experience / 25

    current_nature = list(NATURES_DICT)[current_nature_value]
    current_stat_modifier = NATURES_DICT[current_nature]
    message_user(
        "When transferring your Pokemon to GEN7, "
        f"its nature will be {current_nature}, {current_stat_modifier}",
    )

    wanted_nature = message_user(
        "Which nature are you after?[example: Hasty] > ",
        is_question=True,
    ).lower()
    return (
        current_experience,
        current_nature_value,
        total,
        current_nature,
        current_stat_modifier,
        wanted_nature,
    )


def main():
    (
        current_experience,
        current_nature_value,
        total,
        current_nature,
        current_stat_modifier,
        wanted_nature,
    ) = get_pokemon_stats()

    if wanted_nature in NATURES_DICT.keys():
        # Gets the index number of the chosen nature from the list
        wanted_nature_value = list(NATURES_DICT).index(wanted_nature)
        required_experience = calculate_required_experience(
                                  wanted_nature_value,
                                  current_experience,
                                  current_nature_value,
                                  total,
                              )

        difference = required_experience - current_experience

        message_user(
            f"You are going to have to obtain {difference} more exp points, "
            f"for a total of {required_experience}."
        )
        return
    else:
        message_user("That nature is invalid.")
        return


if __name__ == '__main__':
    main()
