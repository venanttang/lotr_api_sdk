import asyncio
import unittest

import api.lotr_api_fp as lotr_api_fp



class TestQuoteAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.quoteId:str = '5cd96e05de30eff6ebcce7e9'

        # max line of log to investigate and understand the root cause of issue encountered.
        # TODO: we may need to change this value to some other number than leaving it unlimited in the future.
        cls.maxDiff = None
        return super().setUpClass()

    def setUp(self):
        self.client: dict = lotr_api_fp.create_api_client(
            api_key="JN7-d-WtLfdRh75JN0jx"
        )
        return super().setUp()

    def test_fetch_quote_with_id1(self):
        asyncio.run(main=self.case_fetch_quote_with_id_and_filter1())
        return
    
    def test_fetch_quote_with_id2(self):
        asyncio.run(main=self.case_fetch_quote_with_id_and_filter2())
        return
    

    async def case_fetch_quote_with_id_and_filter1(self):
        task: asyncio.Task = asyncio.create_task(
            self.client["aio_fetch_all_quotes"](filter="limit=10")
        )
        output: dict = await task
        expected: dict = {
            "docs": [
                {
                    "_id": "5cd96e05de30eff6ebcce7e9",
                    "dialog": "Deagol!!",
                    "movie": "5cd95395de30eff6ebccde5d",
                    "character": "5cd99d4bde30eff6ebccfe9e",
                    "id": "5cd96e05de30eff6ebcce7e9",
                },
                {
                    "_id": "5cd96e05de30eff6ebcce7ea",
                    "dialog": "Deagol!",
                    "movie": "5cd95395de30eff6ebccde5d",
                    "character": "5cd99d4bde30eff6ebccfe9e",
                    "id": "5cd96e05de30eff6ebcce7ea",
                },
                {
                    "_id": "5cd96e05de30eff6ebcce7eb",
                    "dialog": "Deagol!",
                    "movie": "5cd95395de30eff6ebccde5d",
                    "character": "5cd99d4bde30eff6ebccfe9e",
                    "id": "5cd96e05de30eff6ebcce7eb",
                },
                {
                    "_id": "5cd96e05de30eff6ebcce7ec",
                    "dialog": "Give us that! Deagol my love",
                    "movie": "5cd95395de30eff6ebccde5d",
                    "character": "5cd99d4bde30eff6ebccfe9e",
                    "id": "5cd96e05de30eff6ebcce7ec",
                },
                {
                    "_id": "5cd96e05de30eff6ebcce7ed",
                    "dialog": "Why?",
                    "movie": "5cd95395de30eff6ebccde5d",
                    "character": "5cd99d4bde30eff6ebccfca7",
                    "id": "5cd96e05de30eff6ebcce7ed",
                },
                {
                    "_id": "5cd96e05de30eff6ebcce7ee",
                    "dialog": "Because', it's my birthday and I wants it.",
                    "movie": "5cd95395de30eff6ebccde5d",
                    "character": "5cd99d4bde30eff6ebccfe9e",
                    "id": "5cd96e05de30eff6ebcce7ee",
                },
                {
                    "_id": "5cd96e05de30eff6ebcce7ef",
                    "dialog": "Arrghh!",
                    "movie": "5cd95395de30eff6ebccde5d",
                    "character": "5cd99d4bde30eff6ebccfca7",
                    "id": "5cd96e05de30eff6ebcce7ef",
                },
                {
                    "_id": "5cd96e05de30eff6ebcce7f0",
                    "dialog": "They cursed us!",
                    "movie": "5cd95395de30eff6ebccde5d",
                    "character": "5cd99d4bde30eff6ebccfe9e",
                    "id": "5cd96e05de30eff6ebcce7f0",
                },
                {
                    "_id": "5cd96e05de30eff6ebcce7f1",
                    "dialog": "Murderer!",
                    "movie": "5cd95395de30eff6ebccde5d",
                    "character": "5cd99d4bde30eff6ebccfe9e",
                    "id": "5cd96e05de30eff6ebcce7f1",
                },
                {
                    "_id": "5cd96e05de30eff6ebcce7f2",
                    "dialog": "'Murderer' they called us. They cursed us and drove us away.",
                    "movie": "5cd95395de30eff6ebccde5d",
                    "character": "5cd99d4bde30eff6ebccfe9e",
                    "id": "5cd96e05de30eff6ebcce7f2",
                },
            ],
            "total": 2384,
            "limit": 10,
            "offset": 0,
            "page": 1,
            "pages": 239,
        }
        self.assertDictEqual(output, expected)
        return

    async def case_fetch_quote_with_id_and_filter2(self):
        task: asyncio.Task = asyncio.create_task(
            self.client["aio_fetch_quote_by_id"](id=self.quoteId, query=None, filter=None)
        )
        output: dict = await task
        expected: dict = {
            "docs": [
                {
                    "_id": "5cd96e05de30eff6ebcce7e9",
                    "dialog": "Deagol!!",
                    "movie": "5cd95395de30eff6ebccde5d",
                    "character": "5cd99d4bde30eff6ebccfe9e",
                    "id": "5cd96e05de30eff6ebcce7e9",
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