# 🚀 Custom Tokenizer — BPE & WordPiece (Transformer-Compatible)

## 📘 Overview
This project implements a **custom tokenizer framework** written entirely in **Python**, featuring both **Byte Pair Encoding (BPE)** and **WordPiece** algorithms.  
It includes a **Transformer-compatible tokenizer wrapper** for direct use in NLP models such as BERT or any custom Transformer architecture.

---

## ⚙️ Features
- 🧩 **BPE Tokenizer:** Frequency-based subword merging  
- 🧠 **WordPiece Tokenizer:** Probabilistic subword selection (BERT-style)  
- 🔄 **Transformer Integration:** Model-ready encoding (input IDs, masks, etc.)  
- 💾 **Custom Vocabulary Learning:** Train, save, and load vocabularies  
- 🧰 **Pure Python:** Minimal dependencies, simple to extend

---

## 🧠 Theory
- **Byte Pair Encoding (BPE):** Iteratively merges the most frequent symbol pairs in a corpus to form subword units.  
- **WordPiece:** Similar to BPE but selects merges based on maximum likelihood estimation. Commonly used in BERT and related models.
