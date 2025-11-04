# Detailed Guide: Uploading zipstream-ai to Anaconda Cloud

This guide walks you through uploading your conda package to Anaconda Cloud so others can install it.

## Prerequisites

1. **Anaconda Cloud Account**: You need an account at [anaconda.org](https://anaconda.org)
   - If you don't have one, sign up at: https://anaconda.org/account/register
   - Remember your username (it will be used in the channel URL)

2. **Package Built**: The conda package should already be built
   - Location: `~/miniconda3/conda-bld/noarch/zipstream-ai-1.0.0-py_0.conda`
   - If not built yet, run: `conda build conda-recipe`

3. **anaconda-client Installed**: The upload tool
   - Already installed (we installed it earlier)
   - If missing: `conda install anaconda-client`

## Step-by-Step Upload Process

### Step 1: Verify Package Exists

First, confirm your package file exists:

```bash
# Check if the package file exists
ls -lh ~/miniconda3/conda-bld/noarch/zipstream-ai-1.0.0-py_0.conda

# Expected output:
# -rw-r--r--@ 1 username staff 12K Nov 4 15:51 .../zipstream-ai-1.0.0-py_0.conda
```

If the file doesn't exist, rebuild it:
```bash
cd /Users/pranavmotarwar/Desktop/zipstream-ai
conda build conda-recipe
```

### Step 2: Login to Anaconda Cloud

You have two login options:

#### Option A: Interactive Login (Recommended for First Time)

```bash
anaconda login
```

**What happens:**
1. You'll be prompted for your Anaconda username
2. Enter your username (e.g., `PranavMotarwar`)
3. You'll be prompted for your password
4. Enter your Anaconda Cloud password

**Expected output:**
```
Using Anaconda API: https://api.anaconda.org
Using "defaults" as upload channel
Login successful
```

#### Option B: Using Authentication Token (More Secure)

1. **Get your token:**
   - Go to: https://anaconda.org/settings/access
   - Under "Access" section, click "Create Token"
   - Copy the token (it looks like: `abc123def456...`)

2. **Set the token:**
   ```bash
   anaconda login --token YOUR_TOKEN_HERE
   ```

   Or set it as an environment variable:
   ```bash
   export ANACONDA_TOKEN=YOUR_TOKEN_HERE
   ```

#### Option C: Using .netrc File (For Automation)

Create/edit `~/.netrc` file:
```bash
machine api.anaconda.org
    login YOUR_USERNAME
    password YOUR_PASSWORD_OR_TOKEN
```

Then make it secure:
```bash
chmod 600 ~/.netrc
```

### Step 3: Verify Login Status

Check that you're logged in:

```bash
anaconda whoami
```

**Expected output:**
```
Using Anaconda API: https://api.anaconda.org
Logged in as PranavMotarwar
```

If it says "Not logged in", repeat Step 2.

### Step 4: Upload the Package

#### Basic Upload (Single File)

```bash
anaconda upload ~/miniconda3/conda-bld/noarch/zipstream-ai-1.0.0-py_0.conda
```

**What happens:**
- The package is uploaded to your Anaconda Cloud account
- By default, it uploads to the "main" label (public channel)

**Expected output:**
```
Using Anaconda API: https://api.anaconda.org
Uploading file 'pranavmotarwar/zipstream-ai/1.0.0/linux-64/zipstream-ai-1.0.0-py_0.conda':
[========================================] 100.00% Complete

Package located at:
https://anaconda.org/PranavMotarwar/zipstream-ai
```

#### Advanced Upload Options

**Upload to a specific channel/label:**
```bash
anaconda upload ~/miniconda3/conda-bld/noarch/zipstream-ai-1.0.0-py_0.conda --channel main
```

**Upload to a private label:**
```bash
anaconda upload ~/miniconda3/conda-bld/noarch/zipstream-ai-1.0.0-py_0.conda --channel private
```

**Force overwrite existing package:**
```bash
anaconda upload ~/miniconda3/conda-bld/noarch/zipstream-ai-1.0.0-py_0.conda --force
```

**Upload all packages matching pattern:**
```bash
anaconda upload ~/miniconda3/conda-bld/noarch/zipstream-ai-*.conda
```

### Step 5: Verify Upload

#### Check on Website

1. Visit: `https://anaconda.org/PranavMotarwar/zipstream-ai`
   - Replace `PranavMotarwar` with your actual username

2. You should see:
   - Package name: `zipstream-ai`
   - Version: `1.0.0`
   - Download count
   - Installation instructions

#### Check via Command Line

```bash
anaconda show PranavMotarwar/zipstream-ai
```

**Expected output:**
```
Name:    zipstream-ai
Summary: Stream and query zipped datasets using LLMs
Access:  public
Package Types:  conda
Versions:
   + 1.0.0

To install this package with conda run:
     conda install --channel PranavMotarwar zipstream-ai
```

### Step 6: Test Installation (Optional but Recommended)

Test that others can install it:

```bash
# Create a fresh test environment
conda create -n test-upload python=3.10 -y
conda activate test-upload

# Install from your channel
conda install -c PranavMotarwar zipstream-ai -y

# Verify installation
python -c "from zipstream_ai import ZipStreamReader; print('✓ Installed successfully!')"

# Clean up
conda deactivate
conda env remove -n test-upload -y
```

## Complete Command Sequence

Here's the complete sequence from build to upload:

```bash
# 1. Navigate to project directory
cd /Users/pranavmotarwar/Desktop/zipstream-ai

# 2. Build the package (if not already built)
conda build conda-recipe

# 3. Verify package exists
ls -lh ~/miniconda3/conda-bld/noarch/zipstream-ai-*.conda

# 4. Login to Anaconda Cloud
anaconda login
# Enter username and password when prompted

# 5. Verify login
anaconda whoami

# 6. Upload the package
anaconda upload ~/miniconda3/conda-bld/noarch/zipstream-ai-1.0.0-py_0.conda

# 7. Verify upload
anaconda show PranavMotarwar/zipstream-ai
```

## Sharing with Others

After upload, share this with your users:

### Installation Instructions

**For your users:**
```bash
# Install from your channel
conda install -c PranavMotarwar zipstream-ai

# Install PyPI-only dependencies
pip install openai typer python-dotenv google-generativeai
```

**Or add your channel permanently:**
```bash
conda config --add channels PranavMotarwar
conda install zipstream-ai
pip install openai typer python-dotenv google-generativeai
```

### Share Links

- **Package page**: `https://anaconda.org/PranavMotarwar/zipstream-ai`
- **Install badge**: Add to your README:
  ```markdown
  [![Conda](https://img.shields.io/conda/vn/PranavMotarwar/zipstream-ai.svg)](https://anaconda.org/PranavMotarwar/zipstream-ai)
  ```

## Troubleshooting

### Error: "You are not logged in"

**Solution:**
```bash
anaconda logout
anaconda login
```

### Error: "Package already exists"

**Solution:**
```bash
# Option 1: Force overwrite
anaconda upload ~/miniconda3/conda-bld/noarch/zipstream-ai-1.0.0-py_0.conda --force

# Option 2: Increase build number in meta.yaml
# Edit conda-recipe/meta.yaml: build: number: 1
# Then rebuild
```

### Error: "Authentication failed"

**Solution:**
1. Verify your username and password
2. Try using a token instead (see Step 2, Option B)
3. Check if your account is active at anaconda.org

### Error: "Permission denied"

**Solution:**
- Make sure you're logged in with the correct account
- Verify the package name matches your account/organization

### Package Not Appearing on Website

**Solution:**
- Wait a few minutes (propagation delay)
- Check if upload completed successfully
- Verify the correct label/channel was used
- Try: `anaconda show PranavMotarwar/zipstream-ai`

## Updating the Package

When you release a new version:

1. **Update version in meta.yaml:**
   ```yaml
   {% set version = "1.0.1" %}  # Update version
   ```

2. **Update SHA256 checksum:**
   ```bash
   # Fetch new checksum from PyPI
   curl -s https://pypi.org/pypi/zipstream-ai/json | \
     python3 -c "import sys, json; data = json.load(sys.stdin); \
     version = data['info']['version']; \
     releases = data['releases'].get(version, []); \
     tarball = [r for r in releases if r['packagetype'] == 'sdist'][0]; \
     print(tarball['digests']['sha256'])"
   ```

3. **Update source URL in meta.yaml** (if PyPI URL changed)

4. **Rebuild:**
   ```bash
   conda build conda-recipe
   ```

5. **Upload:**
   ```bash
   anaconda upload ~/miniconda3/conda-bld/noarch/zipstream-ai-1.0.1-py_0.conda
   ```

## Logout (Optional)

When done, you can logout:

```bash
anaconda logout
```

---

**Next Steps:** After successful upload, consider:
1. Adding installation instructions to your GitHub README
2. Creating a conda-forge feedstock for wider distribution
3. Documenting PyPI dependency installation requirement
