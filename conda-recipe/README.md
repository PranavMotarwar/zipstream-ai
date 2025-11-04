# Conda Recipe for zipstream-ai

This directory contains the conda recipe for `zipstream-ai` version 1.0.0.

**📖 For detailed upload instructions, see [UPLOAD_GUIDE.md](UPLOAD_GUIDE.md)**

## Prerequisites

Ensure you have conda installed and configured:

```bash
conda install conda-build anaconda-client
conda config --set anaconda_upload no
```

## Building the Package Locally

Build the conda package:

```bash
cd /Users/pranavmotarwar/Desktop/zipstream-ai
conda build conda-recipe
```

This will:
- Download the source tarball from PyPI
- Verify the SHA256 checksum
- Build the package for your platform
- Output the package location (typically in `~/miniconda3/conda-bld/noarch/` or similar)

Note the output path at the end (e.g., `/Users/pranavmotarwar/miniconda3/conda-bld/noarch/zipstream-ai-1.0.0-py_0.conda`)

## Testing the Package Locally

### Option 1: Install from local build

```bash
# Install from the local build directory
conda install --use-local zipstream-ai

# Or specify the exact path
conda install --use-local /path/to/zipstream-ai-1.0.0-py_0.conda
```

### Option 2: Create a test environment

```bash
# Create a new test environment
conda create -n test-zipstream-ai python=3.10
conda activate test-zipstream-ai

# Install the package
conda install --use-local zipstream-ai

# Install PyPI dependencies
pip install openai typer python-dotenv google-generativeai

# Test imports
python -c "from zipstream_ai import ZipStreamReader, FileParser, ask; print('Success!')"

# Test CLI
zipstream-ai --help

# Clean up
conda deactivate
conda env remove -n test-zipstream-ai
```

## Uploading to Anaconda Cloud

**Quick Start:**
```bash
anaconda login
anaconda upload ~/miniconda3/conda-bld/noarch/zipstream-ai-1.0.0-py_0.conda
```

**For detailed step-by-step instructions, see [UPLOAD_GUIDE.md](UPLOAD_GUIDE.md)**

## Submitting to conda-forge (Optional)

To make `zipstream-ai` available globally via `conda install zipstream-ai` from conda-forge:

### Step 1: Fork conda-forge/staged-recipes

1. Go to https://github.com/conda-forge/staged-recipes
2. Click "Fork" to create your fork

### Step 2: Clone and prepare

```bash
git clone https://github.com/YOUR_USERNAME/staged-recipes.git
cd staged-recipes
git checkout -b zipstream-ai
```

### Step 3: Copy recipe files

```bash
mkdir recipes/zipstream-ai
cp /Users/pranavmotarwar/Desktop/zipstream-ai/conda-recipe/meta.yaml recipes/zipstream-ai/
```

### Step 4: Update meta.yaml for conda-forge

Edit `recipes/zipstream-ai/meta.yaml` and make these changes:

1. Remove or update the `extra.recipe-maintainers` section (use conda-forge format)
2. Ensure `license_file` exists in the source (or remove if not present)
3. Update `about.home` to point to the GitHub repo

### Step 5: Commit and push

```bash
git add recipes/zipstream-ai/meta.yaml
git commit -m "Add zipstream-ai recipe"
git push origin zipstream-ai
```

### Step 6: Open PR

1. Go to https://github.com/conda-forge/staged-recipes
2. Click "New Pull Request"
3. Select your fork and branch
4. Submit the PR

The conda-forge team will review and merge. Once merged, a new feedstock repo will be created automatically.

## Troubleshooting

### Build fails with "LICENSE file not found"

If the build fails because `license_file: LICENSE` is not found:
- Check if LICENSE exists in the PyPI tarball: `tar -tzf zipstream_ai-1.0.0.tar.gz | grep -i license`
- If missing, remove the `license_file:` line from `meta.yaml` (the `license:` field is sufficient)

### Import errors during test

Ensure all dependencies are correctly specified in the `requirements.run` section of `meta.yaml`.
Note: PyPI-only dependencies (openai, typer, python-dotenv, google-generativeai) need to be installed separately via pip.

### CLI command not found

Verify the `entry_points` section in `meta.yaml` matches the entry point defined in `pyproject.toml` or `setup.py`.

## Complete Command Sequence

Here's the full sequence for a fresh build and upload:

```bash
# 1. Build
cd /Users/pranavmotarwar/Desktop/zipstream-ai
conda build conda-recipe

# 2. Test locally
conda install --use-local zipstream-ai
pip install openai typer python-dotenv google-generativeai
python -c "from zipstream_ai import ZipStreamReader; print('OK')"
zipstream-ai --help

# 3. Upload (replace path with actual build output)
anaconda login
anaconda upload ~/miniconda3/conda-bld/noarch/zipstream-ai-1.0.0-py_0.conda

# 4. Verify installation from your channel
conda install -c PranavMotarwar zipstream-ai
pip install openai typer python-dotenv google-generativeai
```
