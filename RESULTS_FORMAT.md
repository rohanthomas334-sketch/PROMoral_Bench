# Results Data Format Specification

This document specifies the expected format for results CSV files in the ProMoral-Bench repository.

## Directory Structure

```
results/
├── ethics/
│   ├── gpt-4.1_ethics_results.csv
│   ├── claude-sonnet-4_ethics_results.csv
│   ├── gemini-2.5-pro_ethics_results.csv
│   └── deepseek-v3_ethics_results.csv
├── ethics_contrast/
│   ├── gpt-4.1_contrast_results.csv
│   ├── claude-sonnet-4_contrast_results.csv
│   ├── gemini-2.5-pro_contrast_results.csv
│   └── deepseek-v3_contrast_results.csv
├── scruples/
│   ├── gpt-4.1_scruples_results.csv
│   ├── claude-sonnet-4_scruples_results.csv
│   ├── gemini-2.5-pro_scruples_results.csv
│   └── deepseek-v3_scruples_results.csv
└── wildjailbreak/
    ├── gpt-4.1_wildjailbreak_results.csv
    ├── claude-sonnet-4_wildjailbreak_results.csv
    ├── gemini-2.5-pro_wildjailbreak_results.csv
    └── deepseek-v3_wildjailbreak_results.csv
```

## ETHICS Results Format

**Filename**: `{model}_ethics_results.csv`

**Required Columns**:
| Column | Type | Description |
|--------|------|-------------|
| Model | str | Model identifier (e.g., 'GPT-4.1') |
| Dataset | str | Always 'ETHICS' for this file |
| Prompting | str | Strategy name (e.g., 'Zero-Shot', 'Few-Shot-CoT') |
| Iterations | int | Number of examples evaluated |
| Total Time | str | Runtime in format 'HH:MM' or 'MM:SS' |
| Max Tokens | int/str | Maximum tokens allowed (may be multiple values for multi-stage) |
| Accuracy | float | Classification accuracy (0-1) |
| Precision | float | Precision on positive class (Unacceptable) |
| Recall | float | Recall on positive class |
| F1 | float | F1 score on positive class |
| ECE | float | Expected Calibration Error (10 bins) |
| Brier Score | float | Brier calibration score |
| Successful output extractions | int | Number of successfully parsed outputs |
| Total Tokens | int | Total tokens used (input + output) |
| Total Input Tokens | int | Total prompt tokens |
| Total Output Tokens | int | Total completion tokens |
| Accuracy per 1k Tokens | float | Efficiency metric (accuracy / (total tokens / 1000)) |
| Avg tokens per example | float | Average tokens per evaluated example |
| Total Rejections | int | Number of times model refused to respond |
| Rejection Rate | float | Proportion of rejections (0-1) |
| Total Indecisions | int | Number of uncertain/unclear responses |
| Indecision Rate | float | Proportion of indecisions (0-1) |
| Total Blocked | int | Number of responses blocked by model safety filters |
| Blocked rate | float | Proportion of blocked responses (0-1) |
| Total Length/no output given | int | Number of responses with no content |
| Total Failed Extractions | int | Number of parsing failures |
| Selected Confirmation | str | (Role Prompting only) The confirmation text selected |
| Avg Iterations | float | (Self-Correct only) Average iteration count |

## Scruples Results Format

**Filename**: `{model}_scruples_results.csv`

**Required Columns** (same as ETHICS, plus):
| Column | Type | Description |
|--------|------|-------------|
| Accuracy (High-consensus) | float | Accuracy on high-agreement subset |
| Precision (High-consensus) | float | Precision on high-agreement subset |
| Recall (High-consensus) | float | Recall on high-agreement subset |
| F1 (High-consensus) | float | F1 on high-agreement subset |

**Note**: For Scruples, metrics are computed for 5-class classification (Author, Other, Everybody, Nobody, Info) and binary fault/no-fault classification. The main metrics use the 5-class setup.

## WildJailbreak Results Format

**Filename**: `{model}_wildjailbreak_results.csv`

**Required Columns**:
| Column | Type | Description |
|--------|------|-------------|
| Model | str | Model identifier |
| Dataset | str | Always 'WildJailbreak' for this file |
| Prompting | str | Strategy name |
| Iterations (Harmful) | int | Number of harmful prompts evaluated |
| Iterations (Benign) | int | Number of benign prompts evaluated |
| ASR | float | Attack Success Rate (0-1, lower is better) |
| ASR 95% CI | str | 95% confidence interval for ASR (format: 'lower, upper') |
| RTA | float | Refusal to Answer rate on benign prompts (0-1, lower is better) |
| RTA 95% CI | str | 95% confidence interval for RTA |
| Harmful eval time | str | Time to evaluate harmful prompts |
| Benign Eval Time | str | Time to evaluate benign prompts |
| Total Input tokens | int | Total prompt tokens |
| Total Output Tokens | int | Total completion tokens |
| Total gen tokens | int | Total generated tokens |
| Total incl tokens | int | Total tokens including context |
| Avg gen tokens/example | float | Average tokens per example |
| Selected Confirmation | str | (Role Prompting only) Confirmation text |

## ETHICS-Contrast Results Format

**Filename**: `{model}_contrast_results.csv`

**Required Columns**:
| Column | Type | Description |
|--------|------|-------------|
| Model | str | Model identifier |
| Dataset | str | Always 'Contrast' for this file |
| Prompting | str | Strategy name |
| Iterations | int | Number of original examples |
| Total Time (Original) | str | Time for original examples |
| Max Tokens | int/str | Maximum tokens allowed |
| Accuracy (Original) | float | Accuracy on original examples |
| Precision (Original) | float | Precision on original |
| Recall (Original) | float | Recall on original |
| F1 (Original) | float | F1 on original |
| ECE (Original) | float | ECE on original |
| Brier Score (Original) | float | Brier on original |
| Successful output extractions (Original) | int | Parsed outputs (original) |
| Total Tokens (Original) | int | Total tokens (original) |
| Total Prompt Tokens (Original) | int | Input tokens (original) |
| Total Completion Tokens (Original) | int | Output tokens (original) |
| Avg tokens per example (Original) | float | Tokens per example (original) |
| Total Time (Contrast) | str | Time for contrast examples |
| it/s (Contrast) | float | Iterations per second (contrast) |
| Accuracy (Contrast) | float | Accuracy on contrast examples |
| Precision (Contrast) | float | Precision on contrast |
| Recall (Contrast) | float | Recall on contrast |
| F1 (Contrast) | float | F1 on contrast |
| ECE (Contrast) | float | ECE on contrast |
| Brier Score (Contrast) | float | Brier on contrast |
| Successful output extractions (Contrast) | int | Parsed outputs (contrast) |
| Total Tokens (Contrast) | int | Total tokens (contrast) |
| Total Prompt Tokens (Contrast) | int | Input tokens (contrast) |
| Total Completion Tokens (Contrast) | int | Output tokens (contrast) |
| Avg tokens per example (Contrast) | float | Tokens per example (contrast) |

**Additional Computed Metrics** (can be derived):
- Delta Accuracy: Accuracy (Contrast) - Accuracy (Original)
- Delta F1: F1 (Contrast) - F1 (Original)
- Delta ECE: ECE (Contrast) - ECE (Original)
- Delta Brier: Brier (Contrast) - Brier (Original)

## Data Formatting Notes

### Time Format
- Use format: `HH:MM` for hours and minutes, or `MM:SS` for minutes and seconds
- For longer runs, use: `H:MM:SS` (e.g., `2:04:35` for 2 hours 4 minutes 35 seconds)

### Float Precision
- Metrics (accuracy, F1, etc.): 4 decimal places recommended
- Confidence intervals: 4 decimal places
- Token metrics: Can be integers or 1 decimal place

### Missing Values
- Use empty string `""` or `NaN` for missing optional fields
- Required fields should never be missing

### Strategy Names
Consistent naming across all files:
- `Zero-Shot`
- `Zero-Shot CoT` (note: space, not hyphen)
- `Few-Shot`
- `Few-Shot CoT`
- `Role Prompting`
- `Thought Expiriment` (note: keep spelling consistent with paper)
- `Plan and Solve` (note: spaces, not hyphens)
- `Self-Correct`
- `Value-Grounded`
- `First Principals` (note: keep spelling consistent with paper)

### Model Names
Consistent identifiers:
- `GPT-4.1`
- `Claude Sonnet 4` (note: space in "Sonnet 4")
- `Gemini 2.5 Pro`
- `Deepseek` or `DeepSeek-3.1` (be consistent)

## Aggregated Results File

An aggregated summary file combining all results: `results/aggregated_results.csv`

This file should contain one row per (Model, Dataset, Strategy) combination with all key metrics.

## Metadata File

Include a `results/metadata.json` file with:

```json
{
  "experiment_date": "2025-02-XX",
  "api_versions": {
    "gpt-4.1": "gpt-4-1106-preview",
    "claude-sonnet-4": "claude-3-sonnet-20240229",
    "gemini-2.5-pro": "gemini-2.5-pro",
    "deepseek-v3": "deepseek-chat"
  },
  "evaluation_settings": {
    "temperature": 0.0,
    "top_p": 1.0,
    "random_seed": 42
  },
  "dataset_sizes": {
    "ethics": 1700,
    "ethics_contrast": 200,
    "scruples": 1466,
    "wildjailbreak": 430
  },
  "notes": "Any additional experimental notes"
}
```

## Validation

To validate your results files, run:
```bash
python scripts/validate_results.py --results-dir ./results
```

This will check:
- Required columns are present
- Data types are correct
- No unexpected missing values
- Naming consistency across files
- Metric ranges are valid (e.g., accuracy between 0 and 1)
