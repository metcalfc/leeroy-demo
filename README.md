# Leeroy Demo

This repository demonstrates [Leeroy](https://github.com/metcalfc/leeroy-jenkins) - transparent attribution for AI-assisted code contributions.

## What You'll See Here

All commits in this repository include AI attestations that show:
- Which AI tool and model were used
- What files were modified by AI
- What prompts guided the AI
- Cryptographic signatures proving authenticity

![Leeroy Demo](demo.gif)

## Viewing Attestations

```bash
# List all commits with AI attestations
leeroy list

# Show attestation for a specific commit
leeroy show HEAD
leeroy show <commit-sha>

# View repository statistics
leeroy stats

# Verify attestation signatures
leeroy verify HEAD
```

## How It Works

1. Developer uses AI assistant (like Claude Code) to write code
2. Leeroy automatically tracks:
   - Session metadata (tool, model, timestamps)
   - Files modified during the session
   - User prompts that guided the AI
3. On commit, Leeroy:
   - Formats an attestation with all session data
   - Signs it cryptographically with ed25519
   - Attaches it as a git note
4. The attestation travels with the commit and is visible on GitHub

## Try It Yourself

Install Leeroy in your own projects:

```bash
# Clone and install the toolkit
git clone https://github.com/metcalfc/leeroy-jenkins.git
cd leeroy-jenkins
./install.sh

# In your project directory
cd /path/to/your/project
leeroy install-hooks

# Now use Claude Code or other AI tools as usual
# Attestations are automatically created on commit!
```

## Example Attestation

```
-----BEGIN AI ATTESTATION-----
Version: 1.0
Tool: claude-code/0.5.2
Model: claude-sonnet-4-5-20250929
Session-ID: a1b2c3d4e5f6
Started-At: 2026-01-16T10:30:00Z
Committed-At: 2026-01-16T10:45:00Z

Files-Modified:
  - src/calculator.py [created] @ 2026-01-16T10:32:15Z
  - tests/test_calculator.py [created] @ 2026-01-16T10:35:42Z

Prompts:
  [2026-01-16T10:30:05Z] Create a calculator module with add, subtract, multiply, divide
  [2026-01-16T10:35:00Z] Add unit tests for all calculator functions

Human-Review-Attested: true

Tool-Signature: ed25519:MEUCIQDx...
Tool-Key-Fingerprint: sha256:abc123...
-----END AI ATTESTATION-----
```

## Why This Matters

See [What This Gets Us](https://github.com/metcalfc/leeroy-jenkins/blob/master/docs/WHAT-THIS-GETS-US.md) for the full explanation.

**TL;DR:** Makes honest AI disclosure easy. No friction, no guessing, just transparent attribution.
