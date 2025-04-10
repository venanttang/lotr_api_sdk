
# This class is likely used for testing movie-related API functionality.
import asyncio
import unittest

import api.lotr_api_fp as lotr_api_fp



class TestMovieAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.movieId:str = '5cd95395de30eff6ebccde5d'

        # max line of log to investigate and understand the root cause of issue encountered.
        # TODO: we may need to change this value to some other number than leaving it unlimited in the future.
        cls.maxDiff = None

        return super().setUpClass()

    def setUp(self):
        self.client: dict = lotr_api_fp.create_api_client(
            api_key="JN7-d-WtLfdRh75JN0jx"
        )
        return super().setUp()

    def test_fetch_movie_with_id1(self):
        asyncio.run(main=self.case_fetch_movie_with_id_and_filter1())
        return

    def test_fetch_movie_with_id2(self):
        asyncio.run(main=self.case_fetch_movie_with_id_and_filter2())
        return

    async def case_fetch_movie_with_id_and_filter1(self):
        task: asyncio.Task = asyncio.create_task(
            self.client["aio_fetch_all_movies"](filter="budgetInMillions<100")
        )
        output: dict = await task
        expected: dict = {
            "docs": [
                {
                    "_id": "5cd95395de30eff6ebccde5b",
                    "name": "The Two Towers",
                    "runtimeInMinutes": 179,
                    "budgetInMillions": 94,
                    "boxOfficeRevenueInMillions": 926,
                    "academyAwardNominations": 6,
                    "academyAwardWins": 2,
                    "rottenTomatoesScore": 96,
                },
                {
                    "_id": "5cd95395de30eff6ebccde5c",
                    "name": "The Fellowship of the Ring",
                    "runtimeInMinutes": 178,
                    "budgetInMillions": 93,
                    "boxOfficeRevenueInMillions": 871.5,
                    "academyAwardNominations": 13,
                    "academyAwardWins": 4,
                    "rottenTomatoesScore": 91,
                },
                {
                    "_id": "5cd95395de30eff6ebccde5d",
                    "name": "The Return of the King",
                    "runtimeInMinutes": 201,
                    "budgetInMillions": 94,
                    "boxOfficeRevenueInMillions": 1120,
                    "academyAwardNominations": 11,
                    "academyAwardWins": 11,
                    "rottenTomatoesScore": 95,
                },
            ],
            "total": 3,
            "limit": 1000,
            "offset": 0,
            "page": 1,
            "pages": 1,
        }
        self.assertDictEqual(output, expected)
        return

    async def case_fetch_movie_with_id_and_filter2(self):
        task: asyncio.Task = asyncio.create_task(
            self.client["aio_fetch_all_movies"](filter="name=/el/i")
        )
        output: dict = await task
        expected: dict = {
            "docs": [
                {
                    "_id": "5cd95395de30eff6ebccde5c",
                    "name": "The Fellowship of the Ring",
                    "runtimeInMinutes": 178,
                    "budgetInMillions": 93,
                    "boxOfficeRevenueInMillions": 871.5,
                    "academyAwardNominations": 13,
                    "academyAwardWins": 4,
                    "rottenTomatoesScore": 91,
                }
            ],
            "total": 1,
            "limit": 1000,
            "offset": 0,
            "page": 1,
            "pages": 1,
        }
        self.assertDictEqual(output, expected)
        return
