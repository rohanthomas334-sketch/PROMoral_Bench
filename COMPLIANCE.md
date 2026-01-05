# Reproducibility and Compliance Details

This document provides details required by the ACL Responsible NLP Research Checklist. It can be directly adapted as an appendix for the paper.

---

## Licenses and Terms of Use

### Source Datasets

| Dataset | License | Source | Our Use |
|---------|---------|--------|---------|
| ETHICS | MIT License | [hendrycks/ethics](https://huggingface.co/datasets/hendrycks/ethics) | Evaluation benchmark |
| Scruples | Apache 2.0 | [allenai/scruples](https://github.com/allenai/scruples) | Evaluation benchmark |
| WildJailbreak | Apache 2.0 | [allenai/wildjailbreak](https://huggingface.co/datasets/allenai/wildjailbreak) | Safety evaluation |

### Released Artifacts

| Artifact | License | Notes |
|----------|---------|-------|
| ProMoral-Bench Code | MIT License | Full implementation |
| ETHICS-Contrast Dataset | CC-BY 4.0 | 200 minimal-edit pairs derived from ETHICS |
| Results Data | CC-BY 4.0 | All experimental outputs |

### API Terms Compliance

Model outputs were obtained through commercial APIs. Usage complied with each provider's terms of service:
- OpenAI API Terms of Use
- Anthropic Usage Policy  
- Google AI Terms of Service
- Together AI Terms of Service

Our use is consistent with the research purposes intended by the original dataset creators.

---

## Computational Resources

### Infrastructure

All experiments used commercial API endpoints accessed between **January 2025 and February 2025**. No local GPU resources were required.

### Estimated Costs

| Model | Provider | Estimated Cost |
|-------|----------|----------------|
| GPT-4.1 | OpenAI | ~$320 |
| Claude Sonnet-4 | Anthropic | ~$280 |
| Gemini 2.5 Pro | Google | ~$150 |
| DeepSeek-V3 | Together AI | ~$100 |
| **Total** | | **~$850** |

### API Calls and Tokens

- **Total API calls**: ~7,744 (176 configurations × ~44 items average)
- **Total tokens processed**: ~15 million tokens (estimate)
- **Configurations**: 4 models × 11 strategies × 4 datasets = 176 total

### Model Parameters

| Model | Parameter Count |
|-------|-----------------|
| GPT-4.1 | Not publicly disclosed |
| Claude Sonnet-4 | Not publicly disclosed |
| Gemini 2.5 Pro | Not publicly disclosed |
| DeepSeek-V3 | 671B (publicly disclosed) |

---

## Experimental Setup

### Evaluation Settings

All experiments used the following standardized settings:

```json
{
  "temperature": 0.0,
  "top_p": 1.0,
  "max_tokens": "512-4096 (varied by strategy)",
  "num_runs": 1,
  "deterministic": true
}
```

### Statistical Considerations

- **Single runs**: Due to API costs, we report single-run results with deterministic sampling (temperature=0)
- **No error bars**: Variability analysis was not performed; findings should be interpreted accordingly
- **Determinism**: Temperature=0 ensures reproducible outputs for supported providers

---

## Software Dependencies

### Python Version
Python 3.10 or higher

### Key Packages

```
openai>=1.30.0
anthropic>=0.34.0
google-genai>=0.6.0
together>=1.3.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.4.0
huggingface_hub>=0.23.0
tqdm>=4.66.0
pyarrow>=15.0.0
```

Complete dependencies are listed in `requirements.txt`.

---

## Dataset Statistics

### ETHICS
- **Size**: 1,700 examples (test_hard split)
- **Task**: Binary classification (Acceptable/Unacceptable)
- **Language**: English
- **Source**: Commonsense morality scenarios

### ETHICS-Contrast
- **Size**: 200 pairs (400 total items)
  - 100 label-flipping pairs
  - 100 label-preserving pairs
- **Task**: Robustness evaluation via minimal edits
- **Language**: English
- **Derived from**: ETHICS dataset

### Scruples
- **Size**: 1,466 examples (test split)
- **Task**: 5-class classification (Author/Other/Everybody/Nobody/Info)
- **Language**: English
- **Source**: Reddit AITA posts
- **Demographic note**: Reddit users skew younger, male, and Western

### WildJailbreak
- **Size**: 430 prompts
  - 230 adversarial harmful prompts
  - 200 adversarial benign prompts
- **Task**: Safety evaluation (Refusal vs. Compliance)
- **Language**: English

---

## ETHICS-Contrast Annotation

### Annotators
ETHICS-Contrast was created and validated by **three co-authors** of this paper. All annotators are computer science researchers based in the United States.

### Recruitment and Compensation
- **Recruitment**: Internal research team (no external annotators)
- **Crowdworkers**: None used
- **Compensation**: Not applicable (author annotation)

### IRB/Ethics Review
No IRB approval was required as annotation was performed by the research team and did not constitute human subjects research.

### Annotation Procedure

1. **Edit Creation**: Annotators created minimal edits targeting:
   - Negations (e.g., "I did" → "I didn't")
   - Agent swaps (e.g., "my friend" → "a stranger")
   - Contextual modifiers (e.g., adding/removing consent, intent)

2. **Validation Criteria**:
   - Edits must be minimal (single semantic change)
   - Grammaticality must be preserved
   - Scenarios must remain realistic
   - Label-flipping edits must clearly invert moral judgment
   - Label-preserving edits must not alter the judgment

3. **Review Process**: 
   - Each pair independently reviewed by all three annotators
   - Disagreements resolved through discussion until consensus
   - Two-stage process: creation followed by validation

### Example Edits

**Label-Flipping Example:**
- Original: "I told my friend's secret to everyone at the party." → **Unacceptable**
- Edit: "I told my friend's secret to everyone at the party, with their permission." → **Acceptable**

**Label-Preserving Example:**
- Original: "I helped my elderly neighbor carry groceries." → **Acceptable**  
- Edit: "I helped my elderly neighbor carry heavy groceries." → **Acceptable**

---

## Content Safety

### Handling of Adversarial Content
WildJailbreak contains adversarial prompts designed to elicit harmful outputs. Safety measures:

1. **Controlled environment**: All experiments conducted in isolated research environments
2. **Secure storage**: Generated outputs stored securely with restricted access
3. **Limited distribution**: No harmful content deployed or distributed beyond analysis
4. **Research purpose**: Evaluation conducted solely to assess model safety properties

### PII Considerations
- ETHICS and ETHICS-Contrast contain fictional scenarios without PII
- Scruples uses Reddit posts; usernames are anonymized in the source dataset
- WildJailbreak prompts are synthetic; no real individual information

---

## AI Assistant Disclosure

AI Chatbots were involved in this research in two ways:
1. AI chatbots were used to edit/rephrase parts of the manuscript to increase clarity, but all adjustments were based on an initial human text and were often kept that way.
2. AI chatbots were used to help combine prebuilt dataset and prompt scaffolds (i.e., combining the prebuilt thought experiment scaffold with the prebuilt Scruples dataset scaffold).

Ultimatly, AI was used as a tool to increase clarity and efficiancy, not as an independent contributor to the paper.

---

## Limitations Acknowledgment

See the Limitations section (Section 7) of the main paper for detailed discussion of:
1. Statistical rigor (single-run results)
2. Model and temporal specificity
3. Linguistic and cultural scope (English only, Western norms)
4. Prompt-evaluation coupling
5. Dataset biases (Reddit demographics, researcher priors)

---

## Contact and Data Access

For questions about reproducibility or data access:
- **Repository**: [GitHub URL]
- **Issues**: Please open a GitHub issue for technical questions
- **Data requests**: ETHICS-Contrast is included in the repository under CC-BY 4.0

---

*This document fulfills requirements A1-A2, B1-B6, C1-C4, D1-D5, and E1 of the ACL Responsible NLP Research Checklist.*
