import unittest
from tichaiti_live_github_actions import __version__
from tichaiti_live_github_actions.main import koman_ou_rele


class TestMwenAn(unittest.TestCase):
    def test_vesyon(self):
        self.assertEqual(__version__, '0.1.0')

    def test_non(self):
        non = koman_ou_rele()
        self.assertEqual(non, 'tichaiti')
