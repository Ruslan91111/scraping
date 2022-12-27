import asyncio
import aiohttp
from codetiming import Timer

urls = ["http://google.com",
        "http://yahoo.com",
        "http://apple.com",
        "http://microsoft.com",
        "https://habr.com/",
        "https://www.youtube.com/",
        "https://stepik.org/",
        "https://docs.python.org/",
        "https://stackoverflow.com/",
        "https://www.reg.ru/"]


async def main(url):
    with Timer(text=f"Затрачено времени на запрос: {{:.3f}} сек"):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                print(resp.url)


if __name__ == '__main__':
    task = [main(link) for link in urls]
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(asyncio.wait(task))
