import unittest
from src.agent.stream_agent import stream_agent

class TestAgent(unittest.TestCase):
    def test_common_letter(self):
        response = stream_agent("What's the most common letter in 'mississippi'?")
        self.assertIn("s", response.lower())

if __name__ == "__main__":
    unittest.main()
