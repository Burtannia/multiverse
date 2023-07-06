from dataclasses import dataclass
import random
from typing import Literal, Optional

from ..prelude import print

type Move = Literal["Rock", "Paper", "Scissors"]

type Outcome = Literal["Win", "Lose", "Draw"]

@dataclass(frozen=True)
class RPS:
    player_score: int = 0
    computer_score: int = 0
    games_played: int = 0

def random_move() -> Move:
    return random.choice(["Rock", "Paper", "Scissors"])

# Takes two moves and returns an outcome
# pertaining to the first move.

# > eval("Rock", "Scissors")
# "Win"
def eval(x: Move, y: Move) -> Outcome:
    match (x,y):
        case ("Rock", "Scissors"):
            return "Win"
        case ("Rock", "Paper"):
            return "Lose"
        case ("Scissors", "Paper"):
            return "Win"
        case ("Scissors", "Rock"):
            return "Lose"
        case ("Paper", "Rock"):
            return "Win"
        case _:
            return "Draw"

def parse_move(input: str) -> Optional[Move]:
    match input.lower():
        case "rock":
            return "Rock"
        case "scissors":
            return "Scissors"
        case "paper":
            return "Paper"
        case _:
            print("Unknown move: ", input)
            return None

def update_score(rps: RPS, outcome: Outcome) -> RPS:
    match outcome:
        case "Win":
            return RPS(rps.player_score + 1, rps.computer_score, rps.games_played + 1)
        case "Lose":
            return RPS(rps.player_score, rps.computer_score + 1, rps.games_played + 1)
        case "Draw":
            return RPS(rps.player_score, rps.computer_score, rps.games_played + 1)

def play_round(rps: RPS) -> RPS:
    move = None
    while move == None:
        move = parse_move(input("Enter a move: "))

    computer_move = random_move()
    print("Computer plays ", computer_move)

    outcome = eval(move, computer_move)
    print("You ", outcome, "!")

    new_rps = update_score(rps, outcome)
    print(new_rps)

    return new_rps

def play() -> None:
    rps = RPS()
    while True:
        rps = play_round(rps)
