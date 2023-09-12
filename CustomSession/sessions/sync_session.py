from __future__ import annotations
from dataclasses import dataclass, field
from requests import Session
import ua_generator
from typing import *
from ua_generator.useragent import UserAgent
from requests import Response
from requests.exceptions import Timeout, ReadTimeout, ConnectTimeout, ChunkedEncodingError
try:
    from models import SessionMetaData
    from exceptions import RetriesExceeded
except ImportError:
    from ..models import SessionMetaData
    from ..exceptions import RetriesExceeded


@dataclass
class SyncSession(Session):
    proxy: str | None = field(default=None)
    ignore_exceptions: Tuple[Type[Exception]] = field(repr=False, default_factory=tuple)
    user_agent: UserAgent = field(init=False, repr=False, default=ua_generator.generate(device='desktop'))
    meta_data: SessionMetaData | dict = field(default_factory=SessionMetaData)

    def __post_init__(self):
        super().__init__()
        self.headers["user-agent"] = self.user_agent.text
        if self.proxy is None:
            proxies = None
        else:
            proxies = {
                "http": f"http://{self.proxy}",
                "https": f"http://{self.proxy}",
            }
        self.proxies = proxies
        if not isinstance(self.meta_data, SessionMetaData):
            self.meta_data = SessionMetaData(self.meta_data)

    def get(self, url, retries: int = 3, **kwargs) -> Response:
        for _ in range(retries):
            try:
                r = super().get(url, **kwargs)
                return r
            except self.ignore_exceptions:
                pass
        raise RetriesExceeded(f"Failed request {retries}/{retries} times", retries)

    def post(self, url, data: dict = None, json: dict = None, retries: int = 3, **kwargs) -> Response:
        for _ in range(retries):
            try:
                r = super().post(url, data=data, json=json, **kwargs)
                return r
            except self.ignore_exceptions:
                pass
        raise RetriesExceeded(f"Failed request {retries}/{retries} times", retries)

    def put(self, url, data: dict = None, retries: int = 3, **kwargs) -> Response:
        for _ in range(retries):
            try:
                r = super().put(url, data=data, **kwargs)
                return r
            except self.ignore_exceptions:
                pass
        raise RetriesExceeded(f"Failed request {retries}/{retries} times", retries)

    def delete(self, url, retries: int = 3, **kwargs) -> Response:
        for _ in range(retries):
            try:
                r = super().delete(url, **kwargs)
                return r
            except self.ignore_exceptions:
                pass
        raise RetriesExceeded(f"Failed request {retries}/{retries} times", retries)

    def patch(self, url, data: dict = None, retries: int = 3, **kwargs) -> Response:
        for _ in range(retries):
            try:
                r = super().patch(url, data=data, **kwargs)
                return r
            except self.ignore_exceptions:
                pass
        raise RetriesExceeded(f"Failed request {retries}/{retries} times", retries)

    def head(self, url, retries: int = 3, **kwargs) -> Response:
        for _ in range(retries):
            try:
                r = super().head(url, **kwargs)
                return r
            except self.ignore_exceptions:
                pass
        raise RetriesExceeded(f"Failed request {retries}/{retries} times", retries)

    def options(self, url, retries: int = 3, **kwargs) -> Response:
        for _ in range(retries):
            try:
                r = super().options(url, **kwargs)
                return r
            except self.ignore_exceptions:
                pass
        raise RetriesExceeded(f"Failed request {retries}/{retries} times", retries)

