import asyncio
import logging

import api.lotr_api_fp as lotr_api_fp

"""
Setting up the logging.
"""
# Configure the logger
logging.basicConfig(
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s %(name)s.%(funcName)s(): %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        logging.StreamHandler(),  # Log to console
    ],
)
logger: logging.Logger = logging.getLogger(__name__)  # Create a logger


# blocking I/O example
def run():
    """
    Example of running in blocking I/O mode
    ```
    def run():
        client = lotr_api_fp.create_api_client(api_key="JN7-d-WtLfdRh75JN0jx")
        output: dict = client["fetch"](endpoint="movie", id=None, query=None, filter=None)
        logger.info(f"output={output}")
        output: dict = client["fetch"](
            endpoint="quote", id=None, query=None, filter="limit=3"
        )
        logger.info(f"output={output}")
        return
    ```
    """

    client = lotr_api_fp.create_api_client(api_key="JN7-d-WtLfdRh75JN0jx")
    output: dict = client["fetch"](endpoint="movie", id=None, query=None, filter=None)
    logger.info(f"output={output}\r\n")
    output: dict = client["fetch"](
        endpoint="quote", id=None, query=None, filter="limit=3"
    )
    logger.info(f"output={output}\r\n")
    return


# Async I/O example
async def async_run():
    """
    Example of running in non-blocking I/O mode
    ```
    async def async_run():
        # Create an API client instance
        client: dict = lotr_api_fp.create_api_client(api_key="##YOUR_API_KEY##")

        # Gathering the enquiry parameters needed.
        movieId: str = "5cd95395de30eff6ebccde5d"
        quoteId: str = "5cd96e05de30eff6ebcce7e9"

        # Create a task for each API call
        tasks: list = [
            asyncio.create_task(client['aio_fetch_all_movies']()),
            asyncio.create_task(client['aio_fetch_all_movies'](filter='budgetInMillions<100')),
            asyncio.create_task(client['aio_fetch_all_movies'](filter='runtimeInMinutes>=160')),
            asyncio.create_task(client["aio_fetch_all_movies"](filter="name=/el/i")),
            asyncio.create_task(client['aio_fetch_movie_by_id'](id=movieId, query=None, filter=None)),
            asyncio.create_task(client['aio_fetch_movie_quote_by_id'](id=movieId, filter='limit=2')),
            asyncio.create_task(client['aio_fetch_all_quotes'](filter='limit=10')),
            asyncio.create_task(client['aio_fetch_quote_by_id'](id=quoteId, query=None, filter=None)),
        ]
        # Collect all the results
        results: list = await asyncio.gather(*tasks)

        # Print out the results
        list(map(lambda result: logger.info(f"result={result}"), results))
        return


    if __name__ == "__main__":
        # synchronized approach
        # run()

        # aiohttp approach
        asyncio.run(main=async_run(), debug=False)
    ```
    """

    # Create an API client instance
    client: dict = lotr_api_fp.create_api_client(api_key="JN7-d-WtLfdRh75JN0jx")

    # Gathering the enquiry parameters needed.
    movieId: str = "5cd95395de30eff6ebccde5d"
    quoteId: str = "5cd96e05de30eff6ebcce7e9"

    # Create a task for each API call
    tasks: list = [
        asyncio.create_task(client['aio_fetch_all_movies']()),
        asyncio.create_task(client['aio_fetch_all_movies'](filter='budgetInMillions<100')),
        asyncio.create_task(client['aio_fetch_all_movies'](filter='runtimeInMinutes>=160')),
        asyncio.create_task(client["aio_fetch_all_movies"](filter="name=/el/i")),
        asyncio.create_task(client['aio_fetch_movie_by_id'](id=movieId, query=None, filter=None)),
        asyncio.create_task(client['aio_fetch_movie_quote_by_id'](id=movieId, filter='limit=2')),
        asyncio.create_task(client['aio_fetch_all_quotes'](filter='limit=10')),
        asyncio.create_task(client['aio_fetch_quote_by_id'](id=quoteId, query=None, filter=None)),
    ]
    # Collect all the results
    results: list = await asyncio.gather(*tasks)

    # Print out the results
    list(map(lambda result: logger.info(f"result={result}\r\n"), results))
    return


if __name__ == "__main__":
    """
    Launcher
    """
    # synchronized approach
    # run()

    # aiohttp approach
    asyncio.run(main=async_run(), debug=False)
