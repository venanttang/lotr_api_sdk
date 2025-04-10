# Lord of the Rings SDK in Python
This library is a SDK for supporting the Lord of the Ring API provided by https://the-one-api.dev
Detail could be found in the link https://the-one-api.dev/documentation#5

### Features
- Non-blocking I/O (highly scalable)
- Blocking I/O is also supported (simple workflow)
- Pure Python
- Easy to customize 
- Production Ready

### Version 0.0.1
- initial stage of this project

### API supported
- List of all movies, including the "The Lord of the Rings" and the "The Hobbit" trilogies
'aio_fetch_all_movies'

- Request one specific movie
'aio_fetch_movie_by_id'

- Request all movie quotes for one specific movie (only working for the LotR trilogy)
'aio_fetch_movie_quote_by_id'

- List of all movie quotes
'aio_fetch_all_quotes'

- Request one specific movie quote
'aio_fetch_quote_by_id'

### Advanced user support on API usage
- Fetch the API call in traditional blocking I/O mode.
'fetch'

- Fetch the API call in non-blocking I/O mode.
'aio_fetch'


### Requirements
- python3.8+
- Mac OSX. 
##### Note: It should work fine on windows & linux environment. If not, please contact me for the fix. You are advised to use 'venv' for virtual environment for python. Please install & activate it if you haven't done that yet. 

### Steps for install & setup
1. Download the source code to your local directory of your machine 
```
gh repo clone venanttang/lotr_api_sdk
```
2. Open the command prompt (e.g. terminal app for mac user) and go there
```
cd lotr_api_sdk
```
3. Install it
```
pip install .
```

## Quickstart
### Approach
In order to make a successful API request to the gateway server, you need to have your access token (bearer key) created and managed by the-one-api site. You can check out the [Setup](#setup) section below.

Once you have the access key ready, your next step is to create a client API instance object in your code. Example & detail are in the "api_client_test_fp.py" file.

After creating a client API instance object, it will provide a list of available API methods to the gateway server. You can check out the list of API methods supported in this SDK through the documents in the doc folder. (e.g. aio_fetch_all_movies or aio_fetch_movie_by_id). 

For power user or further customization on the API, you can customize the API endpoint (e.g. /movie/ ), query (e.g. /quote/) & filter (e.g. name=/foot/i) by using the default (e.g. aio_fetch or fetch) function. That will give you the max flexibility to talk to the server. Also, you can study and understand the example below about how you can make use of the non-blocking I/O.

For detail, you may check out the examples in api_client_test_fp.py and documentation under the doc folder.

### Setup
1. Launch a new browser to go to the https://the-one-api.dev and sign up for an access key (bearer key token). 
2. Once you receive an access key (bearer key), you are ready to import this library into your code.

#### For blocking I/O
1. In your class, you need to create a client API instance 
```python
import lotr_api_fp

client = lotr_api_fp.create_api_client(api_key="##YOUR_ACCESS_KEY##")
```
2. Here is the example code for fetching the data of all the movies.
```python
output: dict = client["fetch"](endpoint="movie", id=None, query=None, filter=None)
```

#### For non-blocking I/O (highly scalable & higher concurrency level)
1. Create a client API instance in async function (required for async mode)
```python
async def async_run():
    ...
    client: dict = lotr_api_fp.create_api_client(api_key="##YOUR_ACCESS_KEY##")
    ...
```
2. Create task for each API call
```python
...
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
...
```
3. Call "await asyncio.gather()" to run & collect the results accordingly.
```python
...
    # Collect all the results
    results: list = await asyncio.gather(*tasks)

    # Print out the results
    list(map(lambda result: logger.info(f"result={result}\r\n"), results))
...
```
4. Launch to start by asyncio.run()
```python
if __name__ == "__main__":
    """
    Launcher
    """
    # aiohttp approach
    asyncio.run(main=async_run(), debug=False)
```

#### Here is a complete example code that we just discussed above. That's the demonstration file (api_client_test_fp.py)
```python

import asyncio
import logging

import lotr_api_fp

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
    """

    client = lotr_api_fp.create_api_client(api_key="##YOUR_ACCESS_KEY##")
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
    """

    # Create an API client instance
    client: dict = lotr_api_fp.create_api_client(api_key="##YOUR_ACCESS_KEY##")

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
    run()

    # aiohttp approach
    asyncio.run(main=async_run(), debug=False)
```


## Unit Test
Under the tests folder, it consists of 1 test suite with 2 test cases in it.

### Steps to run the unit test
1. Launch a command prompt (e.g terminal on mac).
2. Open a command prompt (e.g. terminal app for mac) and go to the project folder.
```
e.g. cd /Users/$USER_NAME/venanttang/lotr_api_sdk
```
3. Run the unittest command
```
python3 -m unittest ./tests/api_testsuite.py
```
4. You will see something like this.
```
....
----------------------------------------------------------------------
Ran 4 tests in 3.087s

OK
```


### Documentation
- You can find the detail documentation under the docs directory. You can click anyone of the html file and they are all linked up together so that it will bring to the main page or the index page for your search.

### Future Roadmap
- More the support & development on the SDK for the rest of the API calls
- Combine the API call with map() & reduce() to further extract the data out of the API JSON response
- Create a pseudo gateway server to serve the unit test request so that the unit test could be done anytime without increasing the workload of the production server environment.

### Optimization to be done: 
1. Cache the results to serve the repeated call.
2. After caching the calls, we can apply the sorting or filters locally on the machine so as to minimize the API calls to the gateway.
3. As the DB data won't change much in general, we can further minimize the API calls by building our own cache data structure in the client side so that no further API could be needed in this case. To play it safe, the cache invalidation could be done every last day of a month.

### Yet to be done
- Review on installation steps
- project submission