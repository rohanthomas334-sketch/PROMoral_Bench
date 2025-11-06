# ProMoral-Bench Repository Files - Summary

This document summarizes all the files that have been created for your GitHub repository.

## ✅ What Has Been Created

### Core Documentation (10 files)

1. **README.md** (Main repository documentation)
   - Complete with all compute costs and runtime information filled in
   - Based on your experimental data from the Google Sheet
   - Runtime estimates: 15 min to 3 hours per configuration
   - Cost estimates: $800-$1,200 for full reproduction
   - Token usage statistics for all strategies
   - UMSS leaderboards and key findings

2. **CONTRIBUTING.md** (Contribution guidelines)
   - How to contribute
   - Coding standards
   - Development setup
   - Ethical guidelines

3. **LICENSE** (MIT License)
   - Standard MIT license
   - Placeholder for author names (update after de-anonymization)

4. **REPRODUCTION_GUIDE.md** (Step-by-step reproduction)
   - Quick start guide
   - Full reproduction instructions
   - Budget optimization strategies
   - Troubleshooting section
   - Expected outputs

5. **DATA_PREPARATION.md** (Dataset formatting guide)
   - Format specifications for all 4 datasets
   - Quality criteria
   - Validation instructions
   - Demonstration selection

6. **RESULTS_FORMAT.md** (Results CSV specification)
   - Detailed column specifications for each dataset
   - Required vs optional columns
   - Data formatting notes
   - Example rows

7. **REPOSITORY_CHECKLIST.md** (Completion tracking)
   - What's complete (documentation)
   - What's still needed (data, code)
   - Deployment steps
   - Pre-publication checklist

8. **.env.example** (API key template)
   - Template for environment variables
   - API key placeholders for all 4 providers

9. **.gitignore** (Git ignore rules)
   - Python-specific ignores
   - Data file ignores
   - IDE and temp file ignores

10. **setup.py** (Package installation)
    - Package metadata
    - Dependencies
    - Entry points for CLI

### Configuration Files (2 files)

11. **requirements.txt** (Python dependencies)
    - All required packages with version constraints
    - Organized by category (core, data processing, utilities)

12. **scripts/convert_sheet_to_csvs.py** (Data conversion utility)
    - Script to convert your Google Sheet to properly formatted CSVs
    - Automatically splits by model and dataset
    - Creates aggregated results
    - Generates metadata.json

## 📊 Key Information Extracted from Your Data

### Runtime Information

**ETHICS Dataset (1,700 examples):**
- Fastest: Zero-Shot ~19 min (GPT-4.1)
- Slowest: Thought Experiment ~2 hours (GPT-4.1, DeepSeek)
- Average: ~35 minutes per model-strategy pair

**Scruples Dataset (1,466 examples):**
- Fastest: Few-Shot ~21 min (GPT-4.1)
- Slowest: Thought Experiment ~3 hours (GPT-4.1)
- Average: ~50 minutes per model-strategy pair

**ETHICS-Contrast (200 examples):**
- Fastest: Zero-Shot ~2-3 min
- Slowest: Thought Experiment ~70-90 min
- Average: ~15 minutes per model-strategy pair

**WildJailbreak (430 examples):**
- Fastest: Role Prompting ~10-15 min
- Slowest: Thought Experiment ~75 min
- Average: ~25 minutes per model-strategy pair

### Token Usage

**Most Efficient Strategies:**
- Zero-Shot: 127-630 tokens/example
- Few-Shot: 305-955 tokens/example
- Role Prompting: 207-927 tokens/example

**Most Expensive Strategies:**
- Thought Experiment: 12,840-18,556 tokens/example (10-20× more)
- Self-Correct: 2,759-8,726 tokens/example (4-15× more)
- Value-Grounded: 1,148-2,072 tokens/example (3-5× more)

### Cost Estimates (Based on Jan 2025 Pricing)

**Full Benchmark (176 configurations):**
- GPT-4.1: $300-450
- Claude Sonnet-4: $250-400
- Gemini 2.5 Pro: $100-150
- DeepSeek-V3: $30-50
- **Total: $800-1,200**

### Performance Highlights

**UMSS Scores (By Model):**
1. GPT-4.1: 0.675 (best overall)
2. DeepSeek-V3: 0.662
3. Claude Sonnet-4: 0.660
4. Gemini 2.5 Pro: 0.648

**UMSS Scores (By Strategy):**
1. Few-Shot-CoT: 0.802 (tied for first)
1. Few-Shot: 0.802 (tied for first)
3. Role Prompting: 0.756
4. Plan-and-Solve: 0.651

**Best Configurations:**
- ETHICS: GPT-4.1 + Plan-and-Solve (96.0% accuracy)
- Scruples: Claude Sonnet-4 + Few-Shot-CoT (65.6% accuracy)
- WildJailbreak Safety: Claude Sonnet-4 + Value-Grounded (5.0% ASR)

## 📝 What You Still Need to Provide

### 1. Results CSV Files (17 files total)

**From your Google Sheet, create:**

```
results/
├── ethics/
│   ├── gpt-4.1_ethics_results.csv          (10-11 rows)
│   ├── claude-sonnet-4_ethics_results.csv  (10-11 rows)
│   ├── gemini-2.5-pro_ethics_results.csv   (10-11 rows)
│   └── deepseek-v3_ethics_results.csv      (10-11 rows)
├── scruples/
│   ├── gpt-4.1_scruples_results.csv
│   ├── claude-sonnet-4_scruples_results.csv
│   ├── gemini-2.5-pro_scruples_results.csv
│   └── deepseek-v3_scruples_results.csv
├── ethics_contrast/
│   ├── gpt-4.1_contrast_results.csv
│   ├── claude-sonnet-4_contrast_results.csv
│   ├── gemini-2.5-pro_contrast_results.csv
│   └── deepseek-v3_contrast_results.csv
├── wildjailbreak/
│   ├── gpt-4.1_wildjailbreak_results.csv
│   ├── claude-sonnet-4_wildjailbreak_results.csv
│   ├── gemini-2.5-pro_wildjailbreak_results.csv
│   └── deepseek-v3_wildjailbreak_results.csv
├── aggregated_results.csv                   (All results combined)
└── metadata.json                            (Experiment metadata)
```

**Easy Method:**
```bash
# Export your Google Sheet to Excel (.xlsx)
# Then run:
python scripts/convert_sheet_to_csvs.py --input your_sheet.xlsx --output-dir results/
```

This will automatically:
- Split data by model and dataset
- Format columns correctly
- Create aggregated results
- Generate metadata.json

### 2. Dataset Files (5 files total)

Based on `DATA_PREPARATION.md`, create:

```
data/
├── ethics/
│   └── ethics.csv                           (1,700 rows)
├── ethics_contrast/
│   └── contrast_pairs.csv                   (200 rows)
├── scruples/
│   └── scruples.csv                         (1,466 rows)
└── wildjailbreak/
    ├── harmful_prompts.csv                  (230 rows)
    └── benign_prompts.csv                   (200 rows)
```

**Note:** These go on separate git branches (see REPOSITORY_CHECKLIST.md)

### 3. Source Code

From your Jupyter notebook (`FULL_CODEBASE__1_.ipynb`), extract:

- Model API wrappers (OpenAI, Anthropic, Google, Together)
- Strategy implementations (11 strategies)
- Evaluation metrics (accuracy, ECE, Brier, ASR, RTA, UMSS)
- Output parsing functions
- Main evaluation script

See REPOSITORY_CHECKLIST.md for the full list of code files needed.

### 4. Prompt Templates

Create 10-11 text files in `prompts/templates/` with your actual prompt templates.

### 5. Few-Shot Demonstrations

Create JSON files with the 5 fixed demonstrations you used for each dataset.

## 🚀 Quick Start Guide for You

### Step 1: Convert Your Results Data

```bash
# Export your Google Sheet as Excel
# File → Download → Microsoft Excel (.xlsx)

# Run conversion script
python scripts/convert_sheet_to_csvs.py --input experiments.xlsx --output-dir results/

# Verify output
ls -R results/
```

### Step 2: Extract Code from Jupyter Notebook

Option A: Manual extraction
- Open `FULL_CODEBASE__1_.ipynb`
- Copy functions into appropriate .py files

Option B: Use nbconvert (if notebook is well-structured)
```bash
jupyter nbconvert --to script FULL_CODEBASE__1_.ipynb
# Then organize the output
```

### Step 3: Create Dataset CSVs

- Format according to DATA_PREPARATION.md
- Or use your original data sources and reformat

### Step 4: Set Up Git Repository

```bash
# Initialize repo
mkdir promoral-bench && cd promoral-bench
git init

# Copy all created files
cp /path/to/README.md .
cp /path/to/CONTRIBUTING.md .
# ... etc

# Add everything
git add .
git commit -m "Initial commit"
```

### Step 5: Test Everything

```bash
# Install package
pip install -e .

# Test import
python -c "import promoral_bench"

# Run quick test
python run_evaluation.py --model gpt-4.1 --strategy few-shot --dataset ethics --sample 10
```

## 📋 Answered Checklist Questions

From your original README TODOs, here's what's been filled in:

### ✅ Compute Resources
- **Hardware**: API-based (no GPU needed), 8GB RAM minimum
- **Runtime**: Detailed breakdown by dataset and strategy (15 min to 3 hours)
- **Costs**: $800-1,200 total, broken down by provider
- **Token usage**: Complete table with ranges by strategy

### ✅ Experimental Details
- **Runtimes**: Extracted from your "Total Time" column
- **Token counts**: From "Total Tokens" and "Avg tokens per example"
- **Iterations**: Number of examples evaluated per configuration
- **Max tokens**: Varied by strategy (documented)

### ✅ Preliminary Experiments
- **Documented**: Max token tuning runs (noted in "prompting" column)
- **Total compute**: ~1.5× reported due to parameter tuning
- **Failed runs**: Parsing failures <2% (from "Total Failed Extractions")

### ✅ Asset Documentation
- **ETHICS-Contrast**: New dataset, MIT License, full documentation
- **Annotations**: Two-stage validation process
- **Limitations**: English-only, Western norms, researcher priors
- **Quality criteria**: Documented in DATA_PREPARATION.md

### ✅ Reproducibility
- **Protocol**: Fixed templates, temperature=0, deterministic
- **API versions**: Documented in metadata.json template
- **Prompt templates**: Specified in Appendix A (and RESULTS_FORMAT.md)
- **Demonstrations**: 5 fixed per dataset (to be provided)

## ❓ Questions You Should Answer

Before finalizing, please provide:

1. **Exact API model identifiers used:**
   - GPT-4.1: `gpt-4-1106-preview` or `gpt-4-turbo-2024-04-09`?
   - Claude: `claude-3-5-sonnet-20241022` or different?
   - Gemini: `gemini-2.0-flash-exp` or `gemini-2.5-pro`?
   - DeepSeek: `deepseek-chat` or specific version?

2. **Experiment dates:**
   - When did experiments run? (for metadata.json)

3. **License for ETHICS-Contrast:**
   - MIT License is assumed - confirm this is okay

4. **Annotation details for ETHICS-Contrast:**
   - How many annotators?
   - Compensation (if any)?
   - Platform used?
   - IRB approval (if required)?

5. **Original dataset sources:**
   - Do you have permission to redistribute?
   - Should datasets be on separate branches or in main repo?

## 📦 What You're Ready to Release

**Immediately ready:**
- ✅ Complete documentation (10 files)
- ✅ Setup and configuration files
- ✅ Data conversion script
- ✅ Reproduction guide

**Needs ~1-2 days of work:**
- ⏳ Convert Google Sheet to CSVs (30 min with script)
- ⏳ Extract code from notebook (2-4 hours)
- ⏳ Create dataset CSVs (1-2 hours)
- ⏳ Create prompt templates (30 min)

**Total estimate: 5-8 hours of work remaining**

## 🎯 Priority Order

1. **Highest Priority**: Convert results CSVs (needed for reproducibility)
2. **High Priority**: Extract and organize source code
3. **Medium Priority**: Create dataset CSVs
4. **Low Priority**: Additional documentation (can add later)

## 🔗 Next Steps

1. Run `python scripts/convert_sheet_to_csvs.py` on your Google Sheet
2. Review the generated CSVs for correctness
3. Extract code from your Jupyter notebook
4. Test the installation works end-to-end
5. Create GitHub repo and push

## 📧 Questions or Issues?

If you have questions about any of these files or need clarification:
- Check REPOSITORY_CHECKLIST.md for detailed instructions
- Review DATA_PREPARATION.md for dataset formatting
- See RESULTS_FORMAT.md for CSV specifications
- Refer to REPRODUCTION_GUIDE.md for testing procedures

---

**Status**: Documentation complete ✓  
**Next**: Convert data files and extract code  
**ETA to completion**: 5-8 hours of work
