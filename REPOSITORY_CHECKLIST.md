# Repository Completion Checklist

This document tracks what has been provided and what still needs to be added to complete the ProMoral-Bench GitHub repository.

## ✅ Complete - Core Documentation

These files have been created and are ready for the repository:

- [x] **README.md** - Comprehensive main documentation with all compute costs filled in
- [x] **CONTRIBUTING.md** - Contribution guidelines
- [x] **LICENSE** - MIT License
- [x] **REPRODUCTION_GUIDE.md** - Step-by-step reproduction instructions
- [x] **DATA_PREPARATION.md** - Dataset formatting and preparation guide
- [x] **RESULTS_FORMAT.md** - Specification for results CSV format
- [x] **.env.example** - API key configuration template
- [x] **.gitignore** - Git ignore rules
- [x] **requirements.txt** - Python dependencies
- [x] **setup.py** - Package installation configuration

## 📋 Still Needed - Results Data

You need to create CSV files from your experimental data (the Google Sheet). Here's what to provide:

### 1. ETHICS Results (4 files)

Create one CSV per model in `results/ethics/`:
- `gpt-4.1_ethics_results.csv`
- `claude-sonnet-4_ethics_results.csv`
- `gemini-2.5-pro_ethics_results.csv`
- `deepseek-v3_ethics_results.csv`

**Instructions**:
1. Filter your Google Sheet for Dataset == "ETHICS"
2. Export each model's rows to separate CSV
3. Follow format in `RESULTS_FORMAT.md`
4. Ensure all 11 strategies are present per model

### 2. Scruples Results (4 files)

Create one CSV per model in `results/scruples/`:
- `gpt-4.1_scruples_results.csv`
- `claude-sonnet-4_scruples_results.csv`
- `gemini-2.5-pro_scruples_results.csv`
- `deepseek-v3_scruples_results.csv`

**Instructions**:
1. Filter for Dataset == "Scruples"
2. Export each model's rows
3. Include both 5-class and binary metrics

### 3. ETHICS-Contrast Results (4 files)

Create one CSV per model in `results/ethics_contrast/`:
- `gpt-4.1_contrast_results.csv`
- `claude-sonnet-4_contrast_results.csv`
- `gemini-2.5-pro_contrast_results.csv`
- `deepseek-v3_contrast_results.csv`

**Instructions**:
1. Filter for Dataset == "Contrast"
2. Export each model's rows
3. Include both original and contrast metrics

### 4. WildJailbreak Results (4 files)

Create one CSV per model in `results/wildjailbreak/`:
- `gpt-4.1_wildjailbreak_results.csv`
- `claude-sonnet-4_wildjailbreak_results.csv`
- `gemini-2.5-pro_wildjailbreak_results.csv`
- `deepseek-v3_wildjailbreak_results.csv`

**Instructions**:
1. Filter for Dataset == "WildJailbreak"
2. Export each model's rows
3. Include ASR, RTA, and confidence intervals

### 5. Aggregated Results (1 file)

Create `results/aggregated_results.csv` combining all results:
- One row per (Model, Dataset, Strategy) combination
- Include all key metrics from individual files

### 6. Metadata File (1 file)

Create `results/metadata.json`:
```json
{
  "experiment_date": "2025-01-XX",  // Update with your dates
  "api_versions": {
    "gpt-4.1": "gpt-4-turbo-2024-04-09",  // Update with actual versions
    "claude-sonnet-4": "claude-3-5-sonnet-20241022",
    "gemini-2.5-pro": "gemini-2.0-flash-exp",
    "deepseek-v3": "deepseek-chat"
  },
  "evaluation_settings": {
    "temperature": 0.0,
    "top_p": 1.0,
    "random_seed": 42,
    "max_tokens_varied": true
  },
  "dataset_sizes": {
    "ethics": 1700,
    "ethics_contrast": 200,
    "scruples": 1466,
    "wildjailbreak_harmful": 230,
    "wildjailbreak_benign": 200
  },
  "compute_notes": "Experiments ran January-February 2025. Some configurations required max_token adjustments (documented in prompting column).",
  "preliminary_runs": "Initial runs used default 512 max tokens. Reran with adjusted limits for Plan-and-Solve, Thought Experiment, Self-Correct, Value-Grounded, and some Scruples configurations."
}
```

## 📦 Still Needed - Dataset Files

You need to create dataset CSV files following the formats in `DATA_PREPARATION.md`:

### ETHICS Dataset
- `data/ethics/ethics.csv` (1,700 examples)

### ETHICS-Contrast Dataset
- `data/ethics_contrast/contrast_pairs.csv` (200 pairs)

### Scruples Dataset
- `data/scruples/scruples.csv` (1,466 examples)

### WildJailbreak Dataset
- `data/wildjailbreak/harmful_prompts.csv` (230 examples)
- `data/wildjailbreak/benign_prompts.csv` (200 examples)

**Note**: Since these are on separate branches, you can create them later when setting up the branch structure.

## 🔧 Still Needed - Source Code

You need to provide the actual Python implementation. Based on your Jupyter notebook, create:

### Core Modules

1. **`src/promoral_bench/__init__.py`**
   - Package initialization
   - Version info

2. **`src/promoral_bench/models/`**
   - `base.py` - Base model interface
   - `openai_model.py` - GPT-4.1 wrapper
   - `anthropic_model.py` - Claude wrapper
   - `google_model.py` - Gemini wrapper
   - `together_model.py` - DeepSeek wrapper

3. **`src/promoral_bench/strategies/`**
   - `base.py` - Base strategy interface
   - `zero_shot.py` - Zero-Shot implementation
   - `few_shot.py` - Few-Shot implementation
   - `cot.py` - Chain-of-Thought variants
   - `role_prompting.py` - Role Prompting
   - `thought_experiment.py` - Thought Experiment
   - `plan_solve.py` - Plan-and-Solve
   - `self_correct.py` - Self-Correct
   - `value_grounded.py` - Value-Grounded
   - `first_principles.py` - First-Principles

4. **`src/promoral_bench/evaluation/`**
   - `metrics.py` - All metric calculations
   - `judge.py` - WildJailbreak judging system
   - `calibration.py` - ECE and Brier score
   - `umss.py` - UMSS calculation

5. **`src/promoral_bench/utils/`**
   - `data_loader.py` - Dataset loading utilities
   - `parsing.py` - Output parsing functions
   - `logging.py` - Logging setup
   - `api_utils.py` - Rate limiting, retries

6. **`src/promoral_bench/cli.py`**
   - Command-line interface

### Scripts

1. **`run_evaluation.py`** - Main evaluation script
2. **`calculate_umss.py`** - UMSS calculation script
3. **`scripts/reproduce_paper.sh`** - Full reproduction bash script
4. **`scripts/validate_datasets.py`** - Dataset validation
5. **`scripts/validate_results.py`** - Results validation
6. **`scripts/generate_tables.py`** - Generate paper tables
7. **`scripts/generate_figures.py`** - Generate paper figures
8. **`scripts/compare_results.py`** - Compare reproduced to paper results
9. **`scripts/test_apis.py`** - Test API connections

### Prompt Templates

In `prompts/templates/`, create one file per strategy with the prompt template:
- `zero_shot.txt`
- `zero_shot_cot.txt`
- `few_shot.txt`
- `few_shot_cot.txt`
- `role_prompting.txt`
- `thought_experiment.txt`
- `plan_solve.txt`
- `self_correct.txt`
- `value_grounded.txt`
- `first_principles.txt`

### Few-Shot Demonstrations

In `prompts/demonstrations/`, create JSON files with fixed demonstrations:
- `ethics_demos.json` (5 examples)
- `scruples_demos.json` (5 examples)
- `wildjailbreak_demos.json` (5 examples for Few-Shot safety)

## 📓 Still Needed - Notebooks

1. **`notebooks/analysis.ipynb`** - Main analysis notebook
   - Load results
   - Generate all paper tables
   - Generate all paper figures
   - Statistical analyses

2. **`notebooks/examples.ipynb`** - Usage examples
   - Quick start examples
   - Custom strategy examples
   - Custom dataset examples

## 📄 Optional but Recommended

1. **`CHANGELOG.md`** - Version history
2. **`CODE_OF_CONDUCT.md`** - Community guidelines
3. **`CITATION.cff`** - Machine-readable citation
4. **`.github/ISSUE_TEMPLATE/`** - Issue templates
5. **`.github/PULL_REQUEST_TEMPLATE.md`** - PR template
6. **`docs/`** - Sphinx documentation (optional)
7. **`tests/`** - Unit tests (highly recommended)

## 🚀 Deployment Steps

Once you have all the above:

### 1. Create Repository Structure
```bash
mkdir -p promoral-bench/{src/promoral_bench/{models,strategies,evaluation,utils},scripts,prompts/{templates,demonstrations},notebooks,results/{ethics,scruples,ethics_contrast,wildjailbreak},data,tests}
```

### 2. Add All Files
- Copy all documentation files to root
- Copy source code to `src/`
- Copy scripts to `scripts/`
- Copy prompts to `prompts/`
- Copy results CSVs to `results/`

### 3. Create Git Repository
```bash
cd promoral-bench
git init
git add .
git commit -m "Initial commit: ProMoral-Bench v1.0"
```

### 4. Set Up Branches for Datasets
```bash
# ETHICS branch
git checkout -b ethics-dataset
mkdir -p data/ethics
cp /path/to/ethics.csv data/ethics/
git add data/ethics/
git commit -m "Add ETHICS dataset"

# ETHICS-Contrast branch
git checkout -b ethics-contrast-dataset
mkdir -p data/ethics_contrast
cp /path/to/contrast_pairs.csv data/ethics_contrast/
git add data/ethics_contrast/
git commit -m "Add ETHICS-Contrast dataset"

# Scruples branch
git checkout -b scruples-dataset
mkdir -p data/scruples
cp /path/to/scruples.csv data/scruples/
git add data/scruples/
git commit -m "Add Scruples dataset"

# WildJailbreak branch
git checkout -b wildjailbreak-dataset
mkdir -p data/wildjailbreak
cp /path/to/{harmful,benign}_prompts.csv data/wildjailbreak/
git add data/wildjailbreak/
git commit -m "Add WildJailbreak dataset"

# Back to main
git checkout main
```

### 5. Test Everything
```bash
# Test installation
pip install -e .

# Test imports
python -c "import promoral_bench; print('OK')"

# Test dataset validation
python scripts/validate_datasets.py --data-dir ./data

# Test results validation
python scripts/validate_results.py --results-dir ./results

# Run quick test evaluation
python run_evaluation.py --model gpt-4.1 --strategy few-shot --dataset ethics --sample 10
```

### 6. Create GitHub Repository
1. Create new repository on GitHub (keep it private for now)
2. Add remote: `git remote add origin https://github.com/[YOUR-USERNAME]/promoral-bench.git`
3. Push all branches:
   ```bash
   git push -u origin main
   git push origin ethics-dataset
   git push origin ethics-contrast-dataset
   git push origin scruples-dataset
   git push origin wildjailbreak-dataset
   ```

### 7. Prepare for Publication
- Create release tag: `git tag v1.0.0`
- Write release notes
- Create DOI via Zenodo (optional)
- Update paper with repository link
- Update repository with paper link after acceptance

## ⚠️ Pre-Publication Checklist

Before making the repository public:

- [ ] Remove any API keys or credentials
- [ ] Check for personal identifying information
- [ ] Verify all file paths are relative
- [ ] Test reproduction on a clean machine
- [ ] Add institutional acknowledgments (after de-anonymization)
- [ ] Update all [ANONYMIZED] placeholders
- [ ] Add author names and contact info
- [ ] Add proper copyright notices
- [ ] Review dataset licenses and permissions
- [ ] Add badges to README (license, DOI, etc.)

## 📧 Questions?

If you need clarification on any of these items:
1. Open an issue in the repository
2. Email the maintainers
3. Refer back to the paper for technical details

## Summary: Next Steps

**Immediate priorities:**
1. ✅ Convert Google Sheet data to CSV files (see section 1-6 above)
2. ✅ Extract source code from Jupyter notebook
3. ✅ Create dataset CSV files
4. ✅ Create prompt template files
5. ✅ Test everything works end-to-end

**Nice to have:**
- Unit tests
- Documentation website
- Tutorial videos
- Pre-commit hooks
- CI/CD pipeline

---

**Status**: Documentation complete, awaiting data files and source code
**Last Updated**: February 2025
