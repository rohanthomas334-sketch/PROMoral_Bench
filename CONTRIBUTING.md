# Contributing to ProMoral-Bench

Thank you for your interest in contributing to ProMoral-Bench! We welcome contributions from the research community.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. **Check existing issues** to avoid duplicates
2. **Create a new issue** with a clear title and description
3. **Include reproduction steps** for bugs
4. **Specify your environment** (Python version, OS, package versions)

### Submitting Changes

1. **Fork the repository** and create a new branch
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our coding standards (see below)

3. **Test your changes** thoroughly
   ```bash
   pytest tests/
   ```

4. **Commit with clear messages**
   ```bash
   git commit -m "Add: brief description of your changes"
   ```

5. **Push to your fork** and submit a pull request
   ```bash
   git push origin feature/your-feature-name
   ```

### What We're Looking For

We particularly welcome contributions in these areas:

#### New Prompting Strategies
- Implement additional prompting techniques (e.g., ReAct, Tree-of-Thoughts)
- Follow the existing strategy interface in `src/strategies/base.py`
- Include prompt templates in `prompts/templates/`
- Add documentation and examples

#### Model Support
- Add wrappers for new models (e.g., Llama, Mistral, Qwen)
- Implement the base model interface in `src/models/base.py`
- Handle model-specific quirks (output parsing, rate limits, etc.)

#### Dataset Extensions
- Create new contrast sets for robustness testing
- Add multi-lingual versions of existing datasets
- Contribute domain-specific moral reasoning datasets

#### Evaluation Improvements
- Implement additional calibration metrics
- Enhance the hybrid safety judging system
- Add statistical significance testing utilities

#### Documentation
- Improve code documentation and docstrings
- Add tutorials and example notebooks
- Translate documentation to other languages

## Coding Standards

### Python Style
- Follow [PEP 8](https://pep8.org/) guidelines
- Use type hints for function arguments and returns
- Maximum line length: 100 characters
- Use descriptive variable names

### Documentation
- Add docstrings to all functions and classes (Google style)
- Include usage examples in docstrings for complex functions
- Update README.md if adding major features

### Example Function Documentation
```python
def evaluate_strategy(
    strategy: str,
    model: str,
    dataset: str,
    temperature: float = 0.0,
) -> Dict[str, float]:
    """Evaluate a prompting strategy on a given dataset.
    
    Args:
        strategy: Name of the prompting strategy (e.g., 'few-shot')
        model: Model identifier (e.g., 'gpt-4.1')
        dataset: Dataset name (e.g., 'ethics')
        temperature: Sampling temperature (default: 0.0 for deterministic)
    
    Returns:
        Dictionary containing evaluation metrics (accuracy, F1, ECE, etc.)
    
    Example:
        >>> results = evaluate_strategy('few-shot', 'gpt-4.1', 'ethics')
        >>> print(f"Accuracy: {results['accuracy']:.3f}")
        Accuracy: 0.952
    """
    # Implementation here
    pass
```

### Testing
- Add unit tests for new functions
- Ensure existing tests pass before submitting PR
- Aim for >80% code coverage for new code

### Commit Messages
Use clear, descriptive commit messages following this format:
- `Add: [new feature]` - for new features
- `Fix: [bug description]` - for bug fixes
- `Update: [what changed]` - for updates to existing features
- `Docs: [documentation change]` - for documentation only
- `Refactor: [what was refactored]` - for code refactoring
- `Test: [test description]` - for adding/modifying tests

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/[ANONYMIZED]/promoral-bench.git
   cd promoral-bench
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -e .  # Install in editable mode
   ```

4. **Set up pre-commit hooks** (optional but recommended)
   ```bash
   pip install pre-commit
   pre-commit install
   ```

5. **Run tests**
   ```bash
   pytest tests/
   ```

## Code Review Process

1. **All PRs require review** by at least one maintainer
2. **Automated checks must pass** (linting, tests, etc.)
3. **Address feedback** promptly and professionally
4. **Squash commits** before merging (we'll help with this)

## Ethical Guidelines

When contributing to ProMoral-Bench, please keep in mind:

### Research Ethics
- Ensure contributions don't enable harmful uses (e.g., bypassing safety measures)
- Be mindful of potential biases in datasets and evaluations
- Document limitations of your contributions honestly

### Data Handling
- Respect data licenses and attribution requirements
- Don't include personally identifiable information (PII)
- Follow ethical data collection practices

### Transparency
- Clearly document any limitations or known issues
- Report negative results honestly (negative results are valuable!)
- Acknowledge prior work and give proper credit

## Questions?

- **Open an issue** for general questions
- **Join discussions** in existing issues
- **Email maintainers** at [ANONYMIZED for submission]

## Attribution

Contributors will be acknowledged in:
- GitHub contributors list (automatic)
- README acknowledgments section
- Academic paper acknowledgments (for substantial contributions)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping improve ProMoral-Bench! 🚀
