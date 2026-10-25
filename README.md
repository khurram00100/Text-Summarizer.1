# Text Summarizer

A compact Python desktop application that creates an extractive summary from user-provided text.

## How it works

1. NLTK splits the input into sentences.
2. `TfidfVectorizer` converts the sentences into weighted text features.
3. K-means groups related sentences.
4. The application selects representative sentences and combines them into a summary.

The number of output sentences can be selected in the Tkinter interface.

## Stack

- Python and Tkinter
- NLTK sentence tokenization
- scikit-learn TF-IDF vectorization
- scikit-learn K-means clustering

## Run locally

```bash
pip install -r requirements.txt
python "# text_summarizer.py"
```

On its first run, NLTK downloads the `punkt` tokenizer data.

## Limitations

- This is extractive summarization: it selects existing sentences rather than generating new text.
- Results depend on sentence structure and the requested summary length.
- Very short input is returned with a message instead of being summarized.

## Author

**Shamsheer Khan Khurrum**
[GitHub](https://github.com/khurram00100) · [Portfolio](https://khurram00100.github.io/khanai.technology/) · [LinkedIn](https://www.linkedin.com/in/shamsheer-khan-khurram)
