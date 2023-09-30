from dataclasses import dataclass
from rate_miner.internal.exchanger.const import ExchangerEnum


@dataclass
class PairGetBody:
    token_from: str
    token_to: str
    exchanger: ExchangerEnum = None
