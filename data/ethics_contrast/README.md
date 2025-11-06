# ETHICS-Contrast Dataset

This dataset contains 200 minimal-edit pairs (100 label-flipping, 100 label-preserving) for testing robustness of moral reasoning models.

## Format

**File**: ethics_contrast_dataset.csv

**Columns**:
- pair_id: Unique identifier
- original_scenario: Original text
- original_label: Original label (0=Acceptable, 1=Unacceptable)
- contrast_scenario: Minimally edited text
- contrast_label: Label after edit
- edit_type: "flip" or "preserve"
- edit_description: Description of the edit

## Statistics

- Total pairs: 100
- Label-flipping edits: 51 pairs
- Label-preserving edits: 49 pairs

## License

MIT License
