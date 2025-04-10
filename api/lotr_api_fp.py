from asyncio.log import logger
from functools import partial
import json
from typing import Callable, Union
import aiohttp
import requests

# Default base URL for lord of the ring API.
BASE_URL: str = "https://the-one-api.dev/v2"


def get_headers(api_key: str) -> dict:
    """
    get_headrs() return a dictionary bearer http header.
    Args:
        api_key (str): [API key]

    Returns:
        dict: [Dictionary object to be put into the http header for HTTP API calls]
    """
    return {"Authorization": f"Bearer {api_key}"}


def fetch_data(endpoint: str, api_key: str, id: str, query: str, filter: str) -> json:
    """
    Blocking I/O for HTTP GET request.

    Args:
        endpoint (str): [path to the API function call]
        api_key (str): [API key]
        id (str): [Search for a specific ID. E.g. movie ID or Quote ID]
        query (str): [Additional sub-path for the API. E.g. /movie/{id}/quote]
        filter (str): [Filtering of the result.]

    Returns:
        json: [JSON response from the API call]
    """
    # url:str = f"{BASE_URL}/{endpoint}"
    url: str = __composeUrl__(endpoint=endpoint, id=id, query=query, filter=filter)
    response: requests.Response = requests.get(
        url, headers=get_headers(api_key=api_key)
    )
    return response.json()


def __composeUrl__(endpoint: str, id: str, query: str, filter: str) -> str:
    """
    Combine all the parameters into a URL for the API call.

    Args:
        endpoint (str): [path to the API function call]
        id (str): [Search for a specific ID. E.g. movie ID or Quote ID]
        query (str): [Additional sub-path for the API. E.g. /movie/{id}/quote]
        filter (str): [Filtering of the result.]

    Returns:
        str: [URL path to the API call]
    """
    url: str = f"{BASE_URL}/{endpoint}"
    if id is not None and not id.isspace():
        url = url + "/" + id
    if query is not None and not query.isspace():
        url = url + "/" + query
    if filter is not None and not filter.isspace():
        url = url + "?" + filter
    return url


async def aio_fetch_data(
    endpoint: str, api_key: str, id: str, query: str, filter: str
) -> json:
    """
    Non-blocking I/O for HTTP GET request

    Args:
        endpoint (str): [path to the API function call]
        api_key (str): [API key]
        id (str): [Search for a specific ID. E.g. movie ID or Quote ID]
        query (str): [Additional sub-path for the API. E.g. /movie/{id}/quote]
        filter (str): [Filtering of the result.]

    Returns:
        json: [JSON response from the API call]
    """
    url: str = __composeUrl__(endpoint=endpoint, id=id, query=query, filter=filter)

    logger.info(f"Making request to url={url}")

    async with aiohttp.ClientSession() as session:
        async with session.get(
            url=url, headers=get_headers(api_key=api_key)
        ) as response:
            # return await response.text()
            return await response.json()


def __safe_api_call__(fn: Callable) -> Callable:
    """
    Wrap API calls to handle exceptions functionally.
    Embrace the error message into the returned value so that user can handle the error accordingly.
    The fn would be wrapped by a try-except block.
    Normally, if the function is called, whatever fn defined would be expected to be returned.
    However, if exception happens in the chain of call,
    it will be caught and returned a dictionary object with error message in it.

    Args:
        fn (Callable): [function to be enabled to handle exception]

    Returns:
        Callable: [returned new function]
    """

    def wrapper(*args, **kwargs) -> Union[dict, str]:
        try:
            return fn(*args, **kwargs)
        # except requests.RequestException as e:
        #     return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    return wrapper


def create_api_client(api_key: str) -> dict:
    """
    Return a set of API functions bound to an API key.
    Args:
        api_key (str): [API key]

    Returns:
        dict [API methods]
    
        # Blocking I/O API call for advance usage
        'fetch'

        # Non-blocking I/O API call for advance usage and this is the method being used by other API methods under the hood.
        'aio_fetch'

        # List of all movies, including the "The Lord of the Rings" and the "The Hobbit" trilogies
        'aio_fetch_all_movies'

        # Request one specific movie
        'aio_fetch_movie_by_id'

        # Request all movie quotes for one specific movie (only working for the LotR trilogy)
        'aio_fetch_movie_quote_by_id'

        # List of all movie quotes
        'aio_fetch_all_quotes'

        # Request one specific movie quote
        'aio_fetch_quote_by_id'
    """
    return {
        "fetch": partial(
            __safe_api_call__(fetch_data),
            api_key=api_key,
            id=None,
            query=None,
            filter=None,
        ),
        "aio_fetch": partial(__safe_api_call__(aio_fetch_data), api_key=api_key),
        # List of all movies, including the "The Lord of the Rings" and the "The Hobbit" trilogies
        "aio_fetch_all_movies": partial(
            __safe_api_call__(aio_fetch_data),
            endpoint="movie",
            api_key=api_key,
            id=None,
            query=None,
            filter=None,
        ),
        # Request one specific movie
        "aio_fetch_movie_by_id": partial(
            __safe_api_call__(aio_fetch_data), endpoint="movie", api_key=api_key
        ),
        # Request all movie quotes for one specific movie (only working for the LotR trilogy)
        "aio_fetch_movie_quote_by_id": partial(
            __safe_api_call__(aio_fetch_data),
            endpoint="movie",
            api_key=api_key,
            query="quote",
        ),
        # List of all movie quotes
        "aio_fetch_all_quotes": partial(
            __safe_api_call__(aio_fetch_data),
            endpoint="quote",
            api_key=api_key,
            id=None,
            query=None,
            filter=None,
        ),
        # Request one specific movie quote
        "aio_fetch_quote_by_id": partial(
            __safe_api_call__(aio_fetch_data), endpoint="quote", api_key=api_key
        ),
    }
