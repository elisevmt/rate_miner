from dataclasses import dataclass


@dataclass
class Token:
    id: int
    name: str
    chain_id: int
