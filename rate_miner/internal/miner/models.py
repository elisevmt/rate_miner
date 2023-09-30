import time
from dataclasses import dataclass


@dataclass
class Miner:
    id: int
    token_from_id: int
    token_to_id: int
    exchanger_id: int
    enabled: bool
