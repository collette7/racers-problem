"""
1. Set to track drivers who have won at least one race
2. Set to track all drivers who appear
3. For each race in the races dictionary:
- Get the top 3 drivers
- Add the winner to the winners set
- Add all 3 drivers to the all_drivers set
4. Find drivers who are in all_drivers but not in winners
5. Return the set of losers 

"""
def non_winners(races):
    if not races:
        return set()
    
    winners = set()
    all_drivers = set()
    
    for outcome in races.values():
        if outcome and len(outcome) > 0:
            winners.add(outcome[0])
            all_drivers.update(driver for driver in outcome if driver is not None)
    
    return all_drivers - winners


races_1 = {
    "Suzuka": ("Tsunoda", "Latifi", "Stroll"),
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
    "Silverstone": ("Hamilton", "Latifi", "Tsunoda")
}
assert non_winners(races_1) == {"Latifi", "Stroll"}

races_2 = {
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
}
assert non_winners(races_2) == {"Hamilton", "Tsunoda"}

races_3 = {
    "Monaco": ("Leclerc", "Verstappen", "Sainz"),
    "Barcelona": ("Sainz", "Verstappen", "Leclerc"),
    "Zandvoort": ("Verstappen", "Sainz", "Leclerc")
}
# If all drivers present in the dictionary won a race
# then the return value should be an empty set
assert non_winners(races_3) == set()

print("All tests passed! Discuss time/space complexity if time remains")