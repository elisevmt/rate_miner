import time
from rate_miner.internal.exchanger.const import ExchangerEnum
from ..dto import PairShot, PairTimeLine
from abc import ABC, abstractmethod
from typing import Optional
from rate_miner.internal.miner.usecase.binance import BinanceAPI
from rate_miner.internal.miner.usecase.okx import OkxAPI
from rate_miner.internal.miner.usecase.pancakeswap import PancakeSwapAPI
from rate_miner.internal.miner.usecase.uniswap import UniswapAPI

__all__ = ["BinanceAPI", "OkxAPI", "PancakeSwapAPI", "UniswapAPI"]


class UseCase(ABC):
    def __init__(self, name: ExchangerEnum):
        self.name = name

    @abstractmethod
    async def get(self,
                  token_from: str,
                  token_to: str,
                  exchanger: ExchangerEnum = None,
                  time_from: time.time = None,
                  time_to: time.time = None
                  ) -> PairShot:
        pass

    @abstractmethod
    async def fetch(self,
                    token_from: str,
                    token_to: str,
                    time_from: time.time = None,
                    time_to: time.time = None,
                    limit: int = None
                    ) -> PairTimeLine:
        pass

    @abstractmethod
    async def save(self,
                   pair: Optional[PairShot] = None) -> None:
        pass
