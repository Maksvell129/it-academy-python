# def create_racer(name, team, speed, country):
#     return {"name": name, "team": team, "speed": speed, "country": country}
#
# def print_racer_info(racer):
#     print(f"{racer['name']} ({racer['team']}) — {racer['speed']} км/ч, {racer['country']}")
#
# def main():
#     racers = [
#         create_racer("Max Verstappen", "Red Bull", 320, "Netherlands"),
#         create_racer("Lewis Hamilton", "Mercedes", 315, "UK"),
#         create_racer("Charles Leclerc", "Ferrari", 312, "Monaco"),
#     ]
#
#     for r in racers:
#         print_racer_info(r)



class Racer2:
    def __init__(self, name: str, team: str, speed: int, country: str) -> None:
        self.name = name
        self.team = team
        self.speed = speed
        self.country = country

    def __str__(self) -> str:
        return f"{self.name} ({self.team}) — {self.speed} км/ч, {self.country}"

def main():
    racers = [
        Racer2("Max Verstappen", "Red Bull", 320, "Netherlands"),
        Racer2("Lewis Hamilton", "Mercedes", 315, "UK"),
        Racer2("Charles Leclerc", "Ferrari", 312, "Monaco"),
    ]

    for r in racers:
        print(r)


from dataclasses import dataclass

@dataclass
class Racer:
    name: str
    team: str
    speed: int
    country: str

    def __str__(self) -> str:
        return f"{self.name} ({self.team}) — {self.speed} км/ч, {self.country}"

def main():

    racers = [
        Racer("Max Verstappen", "Red Bull", 320, "Netherlands"),
        Racer("Lewis Hamilton", "Mercedes", 315, "UK"),
        Racer("Charles Leclerc", "Ferrari", 312, "Monaco"),
    ]
    for r in racers:
        print(r)

main()

