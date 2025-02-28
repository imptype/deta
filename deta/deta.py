import os
import asyncio
import aiohttp
from .base import Base
from .drive import Drive
from typing import Optional


class Deta:

    def __init__(
        self,
        project_key: Optional[str] = None,
        *,
        session: Optional[aiohttp.ClientSession] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None
    ):
        self.token = project_key or os.getenv('DETA_PROJECT_KEY')
        assert self.token, 'project key is required'
        assert len(self.token.split('_')) == 2, 'invalid project key'
        if not session:
            self.session = aiohttp.ClientSession(loop=loop)
        else:
            self.session = session

    async def __aenter__(self):
        return self

    async def __aexit__(self, _, exc, __):
        await self.session.close()
        if exc:
            raise exc

    async def close(self):
        await self.session.close()

    def base(self, name: str) -> Base:
        return Base(name, self.token, self.session)

    def drive(self, name: str) -> Drive:
        return Drive(name, self.token, self.session)
