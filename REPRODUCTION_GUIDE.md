# Paper Reproduction Guide

This guide provides step-by-step instructions for reproducing all results reported in the ProMoral-Bench paper.

## Quick Start (< 5 minutes)

```bash
# 1. Clone and setup
git clone https://github.com/[ANONYMIZED]/promoral-bench.git
cd promoral-bench
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 2. Configure API keys
cp .env.example .env
# Edit .env with your API keys

# 3. Run a single test evaluation
python run_evaluation.py --model gpt-4.1 --strategy few-shot --dataset ethics --sample 10

# Expected output: ~95% accuracy in < 1 minute
```

## Full Reproduction (Est. $800-1,200, 50-80 hours runtime)

### Prerequisites

- Python 3.8+
- API keys for all four providers:
  - OpenAI (GPT-4.1)
  - Anthropic (Claude Sonnet-4)
  - Google (Gemini 2.5 Pro)
  - Together (DeepSeek-V3)
- Minimum 8GB RAM
- ~500MB disk space
- Stable internet connection

### Step 1: Environment Setup

```bash
# Create environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .

# Verify installation
python -c "import promoral_bench; print('Installation successful!')"
```

### Step 2: Dataset Preparation

```bash
# Switch to dataset branches and copy data
git checkout ethics-dataset
cp -r data/ethics ../data/

git checkout ethics-contrast-dataset
cp -r data/ethics_contrast ../data/

git checkout scruples-dataset
cp -r data/scruples ../data/

git checkout wildjailbreak-dataset
cp -r data/wildjailbreak ../data/

git checkout main

# Validate datasets
python scripts/validate_datasets.py --data-dir ./data
```

### Step 3: Configure API Keys

Edit `.env` file:
```bash
OPENAI_API_KEY=sk-proj-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=...
TOGETHER_API_KEY=...
```

Test API connections:
```bash
python scripts/test_apis.py
```

### Step 4: Run Evaluations

#### Option A: Run Everything (Slowest, Most Expensive)

```bash
# This will take 50-80 hours and cost $800-1,200
bash scripts/reproduce_paper.sh
```

#### Option B: Run by Model (Parallelizable)

Run these in separate terminals/machines to parallelize:

```bash
# Terminal 1: GPT-4.1 (~$300-450, ~15-20 hours)
python run_evaluation.py --model gpt-4.1 --all-strategies --all-datasets

# Terminal 2: Claude Sonnet-4 (~$250-400, ~15-20 hours)
python run_evaluation.py --model claude-sonnet-4 --all-strategies --all-datasets

# Terminal 3: Gemini 2.5 Pro (~$100-150, ~12-15 hours)
python run_evaluation.py --model gemini-2.5-pro --all-strategies --all-datasets

# Terminal 4: DeepSeek-V3 (~$30-50, ~10-12 hours)
python run_evaluation.py --model deepseek-v3 --all-strategies --all-datasets
```

#### Option C: Run Specific Configurations (Budget-Friendly)

To reproduce specific paper claims:

**Table 1 (ETHICS Results)**:
```bash
python run_evaluation.py --model gpt-4.1 --strategy plan-and-solve --dataset ethics
python run_evaluation.py --model claude-sonnet-4 --strategy few-shot --dataset ethics
# ... etc for top 3 per model
```

**Table 2 (Scruples Results)**:
```bash
python run_evaluation.py --model claude-sonnet-4 --strategy few-shot-cot --dataset scruples
# ... etc
```

**Table 3 (ETHICS-Contrast)**:
```bash
python run_evaluation.py --model gpt-4.1 --strategy role-prompting --dataset contrast
# ... etc
```

**Table 4 (WildJailbreak)**:
```bash
python run_evaluation.py --model gemini-2.5-pro --strategy few-shot-cot --dataset wildjailbreak
# ... etc
```

### Step 5: Calculate Metrics

After all evaluations complete:

```bash
# Calculate UMSS scores
python calculate_umss.py --results-dir ./results --output umss_scores.csv

# Generate paper tables
python scripts/generate_tables.py --results-dir ./results --output-dir ./paper_tables

# Generate paper figures
python scripts/generate_figures.py --results-dir ./results --output-dir ./paper_figures
```

### Step 6: Verify Results

Compare your results to the paper:

```bash
# Statistical comparison (checks if results are within expected variance)
python scripts/compare_results.py --yours ./results --paper ./paper_results --tolerance 0.02

# Expected output: "✓ All results within 2% tolerance"
```

## Expected Runtimes by Configuration

### By Dataset
- **ETHICS** (1,700 examples): 15 min - 2 hours per strategy-model pair
- **Scruples** (1,466 examples): 20 min - 3 hours per pair
- **ETHICS-Contrast** (200 examples): 2 min - 1.5 hours per pair
- **WildJailbreak** (430 examples): 10 min - 1.5 hours per pair

### By Strategy
- **Efficient** (Zero-Shot, Few-Shot, Role Prompting): 15-30 min per dataset-model
- **Moderate** (CoT variants, Plan-and-Solve, First-Principles): 30-60 min per dataset-model
- **Expensive** (Thought Experiment, Self-Correct, Value-Grounded): 1-3 hours per dataset-model

### By Model (Full Benchmark)
- **GPT-4.1**: ~15-20 hours, $300-450
- **Claude Sonnet-4**: ~15-20 hours, $250-400
- **Gemini 2.5 Pro**: ~12-15 hours, $100-150
- **DeepSeek-V3**: ~10-12 hours, $30-50

## Cost Optimization Strategies

### Budget: $100 (Partial Reproduction)

Focus on key findings:
1. Run Few-Shot and Few-Shot-CoT on all models (highest UMSS)
2. Run one expensive strategy (Thought Experiment) to show inefficiency
3. Use DeepSeek-V3 primarily (cheapest)

```bash
# Estimated cost: ~$80-100
for model in gpt-4.1 claude-sonnet-4 gemini-2.5-pro deepseek-v3; do
  python run_evaluation.py --model $model --strategy few-shot --all-datasets
  python run_evaluation.py --model $model --strategy few-shot-cot --all-datasets
done

python run_evaluation.py --model deepseek-v3 --strategy thought-experiment --all-datasets
```

### Budget: $300 (Core Results)

Add role prompting and plan-and-solve for comparison:

```bash
for model in gpt-4.1 claude-sonnet-4 gemini-2.5-pro deepseek-v3; do
  for strategy in few-shot few-shot-cot role-prompting plan-and-solve; do
    python run_evaluation.py --model $model --strategy $strategy --all-datasets
  done
done
```

### Budget: $600 (Most Results)

Exclude only the most expensive strategies (Thought Experiment, Self-Correct):

```bash
bash scripts/reproduce_paper.sh --exclude thought-experiment,self-correct
```

## Sampling for Quick Tests

For development and testing, use smaller samples:

```bash
# Run on 10% of data (10× faster, ~10× cheaper)
python run_evaluation.py --model gpt-4.1 --strategy few-shot --dataset ethics --sample 0.1

# Run on fixed sample size
python run_evaluation.py --model gpt-4.1 --strategy few-shot --dataset ethics --n-examples 50
```

## Parallelization Tips

### Multiple Machines
Split by model and run simultaneously on different machines.

### Single Machine with Multiple GPUs
Not applicable - all models are API-based.

### Rate Limit Handling

Configure rate limit retry settings in `config.yaml`:

```yaml
api_settings:
  max_retries: 5
  retry_delay: 60  # seconds
  exponential_backoff: true
  
  # Model-specific rate limits (requests per minute)
  rate_limits:
    gpt-4.1: 500
    claude-sonnet-4: 1000
    gemini-2.5-pro: 60  # Most restrictive
    deepseek-v3: 600
```

## Troubleshooting

### API Errors

**Rate Limit Exceeded**:
```python
# Error: RateLimitError
# Solution: Reduce parallelism or add delays
```
→ Edit `config.yaml`: increase `retry_delay`

**Authentication Failed**:
```python
# Error: AuthenticationError
# Solution: Check API keys
```
→ Verify keys in `.env`, ensure no extra whitespace

**Model Not Found**:
```python
# Error: Model 'gpt-4.1' not found
# Solution: Update model identifier
```
→ Check current model names at provider documentation

### Parsing Errors

**Output Extraction Failed**:
- Check `logs/failed_extractions.log`
- Most common cause: Model didn't follow output format
- Solution: Increase max_tokens or adjust prompt template

### Memory Issues

**Out of Memory Error**:
- Reduce batch size in config
- Process datasets sequentially rather than in parallel
- Close other applications

### Validation Failures

**Results don't match paper** (within 2% is expected):
- Different API versions may cause small variations
- Check model identifiers match paper
- Verify random seed is set (should be deterministic with temp=0)

If differences > 5%:
- Verify dataset splits are identical
- Check for parsing errors in logs
- Ensure prompt templates match paper exactly

## Verification Checklist

Before submitting results:

- [ ] All 176 configurations completed (11 strategies × 4 models × 4 datasets)
- [ ] No failed extractions > 2% per configuration
- [ ] UMSS scores computed for all model-strategy pairs
- [ ] Results are within 2-5% of paper values (expected API variation)
- [ ] All paper tables and figures regenerated
- [ ] Results CSV files properly formatted (see RESULTS_FORMAT.md)
- [ ] Metadata file includes API versions and timestamps

## Citing Reproduced Results

If you reproduce our results and publish findings:

```bibtex
@inproceedings{anonymous2026promoral,
  title={ProMoral-Bench: Evaluating Prompting Strategies for Moral Reasoning and Safety in LLMs},
  author={Anonymous},
  booktitle={AAAI 2026 Workshop on AI Reasoning and Foundation Models (AIR-FM)},
  year={2026},
  note={Results reproduced using official repository}
}
```

## Getting Help

If you encounter issues:

1. **Check logs**: `logs/` directory contains detailed error messages
2. **Search issues**: https://github.com/[ANONYMIZED]/promoral-bench/issues
3. **Ask questions**: Open a new issue with:
   - Full error message
   - Configuration used
   - Python/package versions
   - Steps to reproduce

## Expected Outputs

After full reproduction, you should have:

```
results/
├── ethics/
│   ├── gpt-4.1_ethics_results.csv
│   ├── claude-sonnet-4_ethics_results.csv
│   ├── gemini-2.5-pro_ethics_results.csv
│   └── deepseek-v3_ethics_results.csv
├── scruples/
│   └── [same structure]
├── ethics_contrast/
│   └── [same structure]
├── wildjailbreak/
│   └── [same structure]
├── umss_scores.csv
├── aggregated_results.csv
└── metadata.json

paper_tables/
├── table1_ethics.tex
├── table2_scruples.tex
├── table3_contrast.tex
├── table4_wildjailbreak.tex
├── table5_umss.tex
└── table6_tokens.tex

paper_figures/
├── figure1_cost_benefit.pdf
├── figure2_umss_heatmap.pdf
└── figure3_robustness.pdf
```

## Time Estimates

| Task | Time | Can Parallelize? |
|------|------|------------------|
| Setup & installation | 10 min | No |
| Dataset preparation | 15 min | No |
| API testing | 5 min | No |
| Full evaluation | 50-80 hours | Yes (by model) |
| Metric calculation | 10 min | No |
| Table/figure generation | 15 min | No |
| **Total (serial)** | **~52-82 hours** | |
| **Total (4-way parallel)** | **~15-22 hours** | |

---

**Questions?** Open an issue or email [ANONYMIZED for submission]
