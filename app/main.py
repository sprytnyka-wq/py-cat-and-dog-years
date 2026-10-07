def get_human_age(cat_age: int, dog_age: int) -> list:
    # TODO: Implement this function
    cat_human_age = 0
    while cat_age >= 28:
        cat_age = cat_age - 4
        cat_human_age += 1
    if cat_age >= 24 and cat_age <= 28:
        cat_human_age += 1
        cat_age = cat_age - 9
    if cat_age < 24 and cat_age >= 15:
        cat_human_age += 1
        cat_age -= 15

    dog_human_age = 0
    while dog_age >= 29:
        dog_age = dog_age - 5
        dog_human_age += 1
    if dog_age >= 24 and dog_age <= 28:
        dog_human_age += 1
        dog_age = dog_age - 9
    if dog_age < 24 and dog_age >= 15:
        dog_human_age += 1
        dog_age -= 15

    return [cat_human_age, dog_human_age]
