import aiohttp
import asyncio
import aiodbl.utils.errors as errs

class Client:
    def __init__(self, token=None):
        if token:
            self.token = token
        else:
            raise errs.MissingArg('you need a token lol')
        self.loop = asyncio.get_event_loop()
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': self.token
        }
        self.data = None

    async def post(self, id=int, count=int, shard_count=int, shard_id=int):
        if id:
            if shard_count == None:
                shard_count = 0
            else:
                pass
            if shard_id == None:
                shard_id = 0
            else:
                pass
            payload = {
                'server_count': count,
                'shard_count': shard_count,
                'shard_id': shard_id
         }
            async with self.session.post(f'https://discordbots.org/api/bots/{id}/stats',
                                        headers=self.headers, data=payload) as p:
                if p.status == 200:
                    return None
                elif p.status == 401:
                    raise errs.InvalidToken('no')
                else:
                    raise errs.FailedRequest(f'Request returned {p.status}')
        else:
            raise errs.MissingArg('Missing ID to post to')

    async def get(self, id=None):
        if id:
            async with self.session.get(f'https://discordbots.org/api/bots/{id}/stats',
                                        headers=self.headers) as p:
                if p.status == 200:
                    res = await p.json()
                    return res
                elif p.status == 401:
                    raise errs.InvalidToken('no')
                else:
                    raise errs.FailedRequest(f'Request returned {p.status}')
        else:
            raise errs.MissingArg('Missing ID to get info from')

    async def close(self):
        if self.session:
            await self.session.close()
        else:
            raise errs.WTFException('why is the session already closed')
        if not self.loop.is_closed():
            self.loop.stop()
        else:
            raise errs.WTFException('why is the loop already closed')
        if self.token:
            del self.token
        else:
            raise errs.WTFException('you already deleted the token object SERIOUSLY WTF')