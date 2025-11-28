# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an LLM-powered text splitter library that uses large language models to intelligently split text into meaningful chunks. Unlike traditional text splitters that split by character or word count, this library leverages LLMs to identify semantic boundaries in the text.

## Architecture

The codebase consists of:

1. **Base TextSplitter** (`src/TextSplitter.py`): An abstract base class extending LangChain's BaseDocumentTransformer that defines the interface for text splitting operations.

2. **LLMTextSplitter** (`src/LLMTextSplitter.py`): The main implementation that uses LLMs to perform intelligent text splitting by prompting the model to identify content boundaries and mark them with `>>>` and `<<<` delimiters.

3. **Example Usage** (`src/examples/splitter.py`): Demonstrates how to use the LLMTextSplitter with an input file.

## Key Features

- LLM-powered semantic text splitting using prompts
- Support for different splitting strategies ("wide" for broad topics, "granular" for detailed topics)
- Token counting capabilities
- Integration with LangChain ecosystem
- Support for custom OpenAI-compatible endpoints

## Development Commands

- Run example: `uv run python src/examples/splitter.py`
- The project uses uv for dependency management
- Requires Python 3.13+ (as specified in pyproject.toml)

## Environment Configuration

- Create a `.env` file with your OpenAI API key: `OPENAI_API_KEY=your_key_here`
- Optionally configure model name and base URL for custom endpoints
- See `.env.example` for configuration options

## Dependencies

The project depends on:
- python-dotenv for environment variable management
- langchain, langchain-text-splitters, langchain-openai for LLM integration
- tiktoken for token counting