from summarizer.bert import Summarizer

model = Summarizer()

def extractive_summary(text, length='medium'):
    if not text or len(text.strip().split()) < 10:
        return "Not enough content to summarize."

    length_map = {
        'short': 0.2,
        'medium': 0.4,
        'long': 0.6
    }
    ratio = length_map.get(length, 0.4)

    summary = model(text, ratio=ratio)
    return summary.strip()
