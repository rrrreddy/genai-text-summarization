import unittest
from models.summarizer import TextSummarizer

class TestTextSummarizer(unittest.TestCase):

    def setUp(self):
        self.summarizer = TextSummarizer()

    def test_summarize_text(self):
        input_text = "This is a test text for summarization. The model should return a shorter version of this text."
        summary = self.summarizer.summarize(input_text)
        self.assertIsNotNone(summary)
        self.assertNotEqual(input_text, summary)
    
    def test_summarize_empty_text(self):
        input_text = ""
        summary = self.summarizer.summarize(input_text)
        self.assertEqual(summary, "")
    
    def test_summarize_long_text(self):
        input_text = "This is a test text. " * 100
        summary = self.summarizer.summarize(input_text)
        self.assertIsNotNone(summary)
        self.assertTrue(len(summary) < len(input_text))

if __name__ == '__main__':
    unittest.main()