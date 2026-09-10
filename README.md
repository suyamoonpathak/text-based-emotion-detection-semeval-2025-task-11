# Text-Based Emotion Detection — SemEval-2025 Task 11

Multilabel emotion classification for the English dataset, **SemEval-2025 Task 11 (Track A)**.

📄 **Published in the ACL Anthology** — [2025.semeval-1.243](https://aclanthology.org/2025.semeval-1.243/)

## Result

**Macro-F1 0.7344** on the test set, from a fully fine-tuned transformer ensemble.

## What was tried

The interesting part of this work is the comparison, not just the final number. Three
fine-tuning strategies were implemented and evaluated against each other:

| Strategy | Idea | Outcome |
|---|---|---|
| **Full fine-tuning + classification head** | Update all encoder weights, add a multilabel head | **Best** — used in the final ensemble |
| **Adapter models** | Freeze the encoder, train small inserted modules | Cheaper, did not match full fine-tuning here |
| **Entailment-based reformulation** | Recast "does this text express anger?" as an NLI entailment problem | Promising framing; underperformed the direct approach on this dataset |

The final system is an **ensemble of transformer models** with additional classification layers,
which outperformed every individual configuration.

## Why multilabel matters here

Emotion detection isn't single-label — a sentence can carry anger *and* fear *and* sadness at
once. That rules out plain softmax classification and changes both the loss (per-label binary
cross-entropy rather than categorical) and the evaluation (macro-F1 across labels, so rare
emotions count as much as common ones and can't be ignored by a majority-class shortcut).

## Stack

PyTorch · HuggingFace Transformers · multilabel classification heads · model ensembling

## Citation

```bibtex
@inproceedings{pathak-2025-semeval,
    title = "Text-Based Emotion Detection",
    author = "Pathak, Suyamoon and others",
    booktitle = "Proceedings of the 19th International Workshop on Semantic Evaluation (SemEval-2025)",
    year = "2025",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.semeval-1.243/",
}
```

---

Work done at **IIT Kanpur** with Dr. Ashutosh Modi.
