# NigerFlora BioSciences | Scientific Software Engineering Portfolio

**Computational pharmaceutical research · Scientific data engineering · Responsible biomedical AI · MABRIG Technologies**

[Product website](https://nigerflora.mabrigkorie.org) · [Developer profile](https://github.com/mabrig1) · [Contact](https://www.mabrigkorie.org)

NigerFlora is a computational discovery and biomedical research software project. Its original documentation describes network pharmacology, ADMET screening, molecular docking support and research workflows. These descriptions do not independently establish scientific or clinical validation, production availability or regulatory approval.

## Explore the portfolio

- [Conceptual architecture](docs/architecture.md)
- [Engineering case study](docs/case-study.md)
- [Interactive synthetic benchmark](demo/index.html) — download and open locally in a browser.
- [Independent Python model evaluation example](demo/benchmark.py)
- [Automated tests](demo/test_benchmark.py)
- [CI workflow](.github/workflows/demo.yml)

## Reproduce the example

```sh
python demo/benchmark.py
python -m unittest discover -s demo -v
```

Python 3.10+; no dependencies or keys. The example evaluates supplied fictional observed and predicted log-solubility values using absolute error and mean absolute error. It is not a solubility predictor, molecular descriptor calculator or validation of the production engine. No real experimental or clinical records are used.

## Engineering competencies

Scientific data validation, reproducible numerical computation, model evaluation, uncertainty communication, responsible biomedical software design and automated testing.

## Scientific limitations and intellectual property

Computational results are hypothesis-generating, not proof of therapeutic efficacy, clinical safety, patentability or regulatory approval. This demonstration provides no medical advice. See [NOTICE.md](NOTICE.md). Proprietary algorithms, unpublished research, patient data, credentials and original production source are excluded. Recruiters and research collaborators may contact MABRIG Technologies for a guided demonstration or scoped technical discussion.
