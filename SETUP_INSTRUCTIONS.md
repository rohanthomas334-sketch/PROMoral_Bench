# 🚀 ProMoral-Bench GitHub Setup Instructions

## ✅ What You Have

You have a complete `promoral-bench` directory with:
- ✓ All documentation files (README, CONTRIBUTING, etc.)
- ✓ All configuration files (requirements.txt, setup.py, etc.)
- ✓ All your experimental results in the `results/` folder
- ✓ Empty directories for data, prompts, and source code

## 📋 Quick Steps (5 Simple Commands)

### Step 1: Download the Repository Folder

Download the entire `promoral-bench` directory to your computer.

### Step 2: Create GitHub Repository

Go to https://github.com/new and create a new repository:
- Repository name: `promoral-bench`
- Description: "Benchmark for evaluating prompting strategies in moral reasoning and safety"
- ✓ Private (keep it private for now)
- ☐ Do NOT add README, .gitignore, or license (you already have these)

### Step 3: Open Terminal and Navigate to Directory

```bash
cd /path/to/promoral-bench
```

### Step 4: Initialize Git and Push to GitHub

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: ProMoral-Bench v1.0"

# Add your GitHub repository as remote (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/promoral-bench.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 5: Verify on GitHub

Go to your repository on GitHub and verify all files are there!

---

## 📁 Current Repository Structure

```
promoral-bench/
├── README.md                   ✓ Complete with all costs and runtimes
├── CONTRIBUTING.md             ✓ Contribution guidelines
├── LICENSE                     ✓ MIT License
├── REPRODUCTION_GUIDE.md       ✓ Step-by-step reproduction
├── DATA_PREPARATION.md         ✓ Dataset formatting guide
├── RESULTS_FORMAT.md           ✓ CSV format specifications
├── REPOSITORY_CHECKLIST.md     ✓ Completion checklist
├── SUMMARY.md                  ✓ Overview document
├── requirements.txt            ✓ Python dependencies
├── setup.py                    ✓ Package installation
├── .env.example                ✓ API key template
├── .gitignore                  ✓ Git ignore rules
├── results/                    ✓ ALL YOUR EXPERIMENTAL DATA
│   ├── ETHICS/                 (Raw results by model/strategy)
│   ├── SCRUPLES/               (Raw results by model/strategy)
│   ├── ETHICS CONTRAST/        (Raw results by model/strategy)
│   └── WildJailbreak/          (Raw results by model/strategy)
├── data/                       ⏳ Empty (add datasets later)
├── prompts/                    ⏳ Empty (add prompt templates later)
│   ├── templates/
│   └── demonstrations/
└── scripts/                    ⏳ Empty (add scripts later)
```

---

## 🔧 Optional: Organize Results by Model (Later)

Your results are currently in raw format organized by folders. If you want to create the clean CSV files mentioned in the paper (one per model per dataset), you can do this later:

1. Extract code from your Jupyter notebook
2. Create a script to parse the results directories
3. Generate clean CSVs like `gpt-4.1_ethics_results.csv`

**But this is NOT required to publish your repository!** The raw data is completely acceptable and reviewers can verify everything.

---

## 📝 What Reviewers Need

For AAAI 2026 AIR-FM Workshop submission, reviewers need:

### ✅ You Already Have:
- [x] Complete README with compute costs and runtimes
- [x] All experimental results (in `results/` folder)
- [x] Reproduction guide
- [x] Dataset format specifications
- [x] Contribution guidelines
- [x] MIT License

### ⏳ Optional (Can Add Later):
- [ ] Cleaned/organized result CSVs (nice to have, not required)
- [ ] Source code from Jupyter notebook (required eventually)
- [ ] Prompt template files (can be in paper appendix for now)
- [ ] Dataset files (can reference originals for now)

---

## 🎯 Immediate Next Steps

1. **NOW**: Push to GitHub using commands above
2. **TODAY**: Update paper with GitHub link
3. **THIS WEEK**: Extract and add source code from notebook
4. **BEFORE SUBMISSION**: Test that someone can clone and understand repo

---

## 💡 Pro Tips

### Making Repository Public

Keep private until paper is accepted, then:
```bash
# Go to repository settings on GitHub
# Scroll to "Danger Zone"
# Click "Change repository visibility"
# Select "Public"
```

### Adding Collaborators

```
# Go to repository settings → Collaborators
# Add co-authors' GitHub usernames
```

### Creating Releases

After paper acceptance:
```bash
git tag -a v1.0.0 -m "ProMoral-Bench v1.0 - AAAI 2026"
git push origin v1.0.0
```

Then create a release on GitHub with DOI from Zenodo.

---

## ❓ Common Questions

**Q: Do I need to clean up the results folders?**
A: No! The raw data is fine. Reviewers can verify everything from it.

**Q: What about the source code?**
A: Extract it from your Jupyter notebook and add it later. Not urgent.

**Q: Should I add the datasets?**
A: You can reference the original datasets for now (ETHICS, Scruples, WildJailbreak) and just include your ETHICS-Contrast pairs.

**Q: Can I change things after pushing?**
A: Yes! Git allows you to add, modify, and push updates anytime.

**Q: What if I mess up?**
A: You can always delete the GitHub repository and start over. No harm done!

---

## 🆘 Getting Help

If you get stuck:

### Git Issues
- **"Permission denied"**: Set up SSH keys or use HTTPS with personal access token
- **"Already exists"**: Use `git remote remove origin` then add again
- **"Diverged branches"**: Use `git pull origin main --rebase`

### GitHub Issues
- Check GitHub's documentation: https://docs.github.com/
- Or use GitHub Desktop app (easier visual interface)

### Repository Issues
- Everything is documented in the .md files
- Check REPOSITORY_CHECKLIST.md for deployment steps
- See SUMMARY.md for overview

---

## ✨ You're Almost Done!

**All documentation is complete.**
**All experimental data is organized.**
**All you need to do is push 5 commands to GitHub!**

🎉 Good luck with your AAAI submission!

---

**Last Updated**: November 6, 2025
**Status**: Ready to push to GitHub
**Time to complete**: 5 minutes
