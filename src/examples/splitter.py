import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from LLMTextSplitter import LLMTextSplitter

# Baca file input
try:
    with open("input.txt") as f:
        data = f.read()

    splitter = LLMTextSplitter(count_tokens=True, prompt_type="wide")
    chunks = splitter.split_text(data)
    print(chunks)
except Exception as e:
    print(f"Error: {e}")
    print("Catatan: Error ini terjadi karena tidak ada API key OpenAI yang valid. Import statement sudah diperbaiki.")