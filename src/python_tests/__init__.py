import time
from .rules import (
    use_potion,
    take_damage,
    can_trigger_extra_life,
    try_extra_life,
    resolve_damage,
    buy_potion,
    apply_armor,
)
from .storage import initialize_database, load_player, save_player

def main():
    database = "practice_check.db"
    initialize_database(database)
    saved_player = load_player(database, 1)

    if saved_player is None:
        print("Player not found.")
        return

    player_id, player_name, player_health, player_potions, player_credits, player_ready_at, player_armor = saved_player

    player = {
        "id": player_id,
        "name": player_name,
        "health": player_health,
        "potions": player_potions,
        "ready_at": player_ready_at,
        "credits": player_credits,
        "armor": player_armor,
    }


    while True:
        print("Health:", player["health"])
        print("Armor:", player["armor"])
        print("Potions:", player["potions"])
        print("Credits:", player["credits"])

        action = input("choose heal, hit, buy, save or quit: ").strip().lower()
        if action == "quit":
            print("Goodbye!")
            break
        elif action == "heal":
            player["health"], player["potions"] = use_potion(
                player["health"], player["potions"]
            )
        elif action == "hit":
            now = time.time()
            damage = 30

            previous_ready_at = player["ready_at"]

            player["health"], player["ready_at"] = resolve_damage(
                player["health"], 
                damage, 
                now, 
                player["ready_at"],
                armor=player["armor"],
            )

            if previous_ready_at != player["ready_at"]:
                print("Extra Life activated! Restored to 25 health.")

            if damage > 0 and apply_armor(damage, player["armor"]) == 0:
                print("Enemy failed to damage you.")

            if player["health"] == 0:
                print("You were defeated")
                break
        elif action == "buy":
            previous_credits = player["credits"]

            player["credits"], player["potions"] = buy_potion(
                player["credits"], player["potions"])

            if previous_credits != player["credits"]:
                print("Bought one potion for 10 credits.")
            else:
                print("Not enough credits")
        elif action == "save":
            save_player(database, player)
            print("Player Saved!")
        else:
            print("Unknown Command")


if __name__ == "__main__":
    main()