from dataclasses import dataclass


@dataclass
class Tile:
    value: int
    score: int
    state: str  # {'OPEN'|'EXACT'|'CLOSED'}
