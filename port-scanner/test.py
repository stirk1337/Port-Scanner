from aiohttp.test_utils import AioHTTPTestCase
from src.app import get_app


class PortScannerTestCase(AioHTTPTestCase):
    async def get_application(self):
        return get_app()


class TestCase(PortScannerTestCase):
    async def test_habr(self):
        async with self.client.request("GET", "/scan/habr.com/1/100") as resp:
            self.assertEqual(resp.status, 200)
            json = await resp.json()
        self.assertEqual(80, json[79]["port"])
        self.assertEqual("open", json[79]["status"])
        self.assertEqual(2, json[1]["port"])
        self.assertEqual("close", json[1]["status"])

    async def test_bitcoin(self):
        async with self.client.request("GET", "/scan/bitcoin.com/1/500") as resp:
            self.assertEqual(resp.status, 200)
            json = await resp.json()
        self.assertEqual(80, json[79]["port"])
        self.assertEqual("open", json[79]["status"])
        self.assertEqual(443, json[442]["port"])
        self.assertEqual("open", json[442]["status"])
        self.assertEqual(300, json[299]["port"])
        self.assertEqual("close", json[299]["status"])

    async def test_python_org(self):
        async with self.client.request("GET", "scan/python.org/79/450") as resp:
            self.assertEqual(resp.status, 200)
            json = await resp.json()
        self.assertEqual(80, json[1]["port"])
        self.assertEqual("open", json[1]["status"])
        self.assertEqual(443, json[364]["port"])
        self.assertEqual("open", json[364]["status"])
        self.assertEqual(379, json[300]["port"])
        self.assertEqual("close", json[300]["status"])

    async def test_wrong_host(self):
        async with self.client.request("GET", "/scan/abakaca2005.site/1/500") as resp:
            self.assertEqual(resp.status, 200)
            text = await resp.text()
        self.assertEqual("Invalid host.", text)

    async def test_wrong_ports(self):
        async with self.client.request("GET", "scan/vk.com/port1/650") as resp:
            self.assertEqual(resp.status, 200)
            text = await resp.text()
        self.assertEqual("Invalid port.", text)

    async def test_minus_ports(self):
        async with self.client.request("GET", "scan/vk.com/-100/300") as resp:
            self.assertEqual(resp.status, 200)
            json = await resp.json()
        self.assertEqual(80, json[79]["port"])
        self.assertEqual("open", json[79]["status"])





