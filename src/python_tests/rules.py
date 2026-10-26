def use_potion(health, potions):
    if health == 0 or health == 100:
        return (health, potions)
    elif potions == 0:
        return (health, potions)
    elif health + 25 > 100:
        return (100, potions - 1)
    else:
        return (health + 25, potions - 1)

def take_damage(health, damage):
    if damage < 0:
        raise ValueError("Damage cannot be negative")

    if damage >= health:
        return 0
    elif damage == 0:
        return health
    else:
        return health - damage

def can_trigger_extra_life(health, now, ready_at):
    # Return True or False
    # return health == 0 and now >= ready_at
    if health == 0 and now >= ready_at:
        return True
    else:
        return False

def try_extra_life(health, now, ready_at):
    if can_trigger_extra_life(health, now, ready_at):
        health = 25
        ready_at = now + 1800
    return health, ready_at

def resolve_damage(health, damage, now, ready_at, armor=0):
    if damage < 0:
        raise ValueError("Damage cannot be negative")
    reduce_damage = apply_armor(damage, armor)
    after_damage = take_damage(health, reduce_damage)
    return try_extra_life(after_damage, now, ready_at)

def buy_potion(credits, potions):
    cost = 10
    if credits >= cost:
        potions += 1
        credits -= cost
    return credits, potions

def apply_armor(damage, armor):
    real_damage = damage
    if armor == 0:
        return real_damage
    
    if armor >= real_damage:
        return 0

    return real_damage - armor