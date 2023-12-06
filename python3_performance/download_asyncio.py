import asyncio
import aiohttp
import  requests


def download():
    return requests.get('https://www.python.org').content

async def async_download(session, url):
    async with session.get(url) as response:
        return await response.read()

def synchronous():
    for _ in range(5):
        download()


async def asynchronous():
    async with aiohttp.ClientSession() as session:
        coroutines = [async_download(session, 'https://www.python.org') for _ in range(5)]
        await asyncio.gather(*coroutines)

@profile
def main():
    synchronous()
    asyncio.run(asynchronous())

main()