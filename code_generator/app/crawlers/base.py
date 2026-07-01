from abc import ABC, abstractmethod
from code_generator.domain.documents import NoSQLBaseDocument

class BaseCrawler(ABC):
    model: type[NoSQLBaseDocument]

    @abstractmethod
    def extract(self, link: str, **kwargs) -> None: ...
