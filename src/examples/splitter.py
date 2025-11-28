import LLMTextSplitter


with open("input.txt") as f:
    data = f.read()

    splitter = LLMTextSplitter(count_tokens=True, prompt_type="wide")
    chunks = splitter.split_text(data)