<#
.SYNOPSIS
    Normalizes Martin's paper corpus on Drive G into canonical folder+filename structure.

.DESCRIPTION
    Moves Drive G papers into the canonical PHAROS_PAPERS_DB folder on C:.
    Target: C:\Users\softinfo\Documents\PHAROS_PAPERS_DB\drive-g\

    Local C: papers are already handled by migrate_to_pharos_papers_db.py.
    This script handles only the Google Drive for Desktop files (Drive G).

    Files are MOVED (from Drive G) into PHAROS_PAPERS_DB\drive-g\.
    Old versions go to _archive\ inside the paper folder. Nothing is deleted.

    Run with -DryRun to preview all moves before executing.
    Run without -DryRun to execute.

.PARAMETER DryRun
    Print each move without executing it.

.EXAMPLE
    .\migrate_corpus.ps1 -DryRun
    .\migrate_corpus.ps1
#>

param(
    [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$DRIVE  = "G:\Mon disque"
$PAPERS = "C:\Users\softinfo\Documents\PHAROS_PAPERS_DB\drive-g"
$b      = [char]0x2022   # bullet • — PowerShell 5.1 reads UTF-8 scripts as ANSI; use this instead of literal •

$moved   = 0
$skipped = 0
$errors  = 0

function Move-ToCanonical {
    param(
        [string]$Source,
        [string]$Dest,
        [bool]$Archive = $false
    )

    if (-not (Test-Path $Source)) {
        Write-Host "  SKIP (not found): $Source" -ForegroundColor Yellow
        $script:skipped++
        return
    }
    if (Test-Path $Dest) {
        Write-Host "  SKIP (dest exists): $Dest" -ForegroundColor Yellow
        $script:skipped++
        return
    }

    $destDir = Split-Path $Dest -Parent
    $label = if ($Archive) { "ARCHIVE" } else { "MOVE" }

    Write-Host "  [$label] $Source" -ForegroundColor Cyan
    Write-Host "      --> $Dest" -ForegroundColor Green

    if (-not $DryRun) {
        try {
            if (-not (Test-Path $destDir)) {
                New-Item -ItemType Directory -Path $destDir -Force | Out-Null
            }
            $ext = [System.IO.Path]::GetExtension($Source).ToLower()
            if ($ext -in @(".gdoc",".gsheet",".gslides")) {
                # Google Drive stubs are online-only virtual files — standard copy/move fails.
                # Try reading stub content (JSON with doc URL/ID) and writing it to dest.
                try {
                    $stubContent = [System.IO.File]::ReadAllText($Source)
                    [System.IO.File]::WriteAllText($Dest, $stubContent, [System.Text.Encoding]::UTF8)
                    $script:moved++
                } catch {
                    # Stub is truly inaccessible — record as bounded item, not an error
                    Write-Host "  BOUNDED (gdoc cloud-only, not copyable): $Source" -ForegroundColor Magenta
                    $script:skipped++
                }
            } else {
                Move-Item -Path $Source -Destination $Dest -ErrorAction Stop
                $script:moved++
            }
        } catch {
            Write-Host "  ERROR: $_" -ForegroundColor Red
            $script:errors++
        }
    } else {
        $script:moved++
    }
}

function Ensure-Dir {
    param([string]$Path)
    if (-not $DryRun -and -not (Test-Path $Path)) {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
    }
    Write-Host "  [MKDIR] $Path" -ForegroundColor DarkGray
}

function Write-Status {
    param([string]$Path, [string]$Slug)
    if ($DryRun) { return }
    if (-not (Test-Path $Path)) {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
    }
    if (Test-Path "$Path\_status.md") { return }
    $content = @"
# $Slug — Status

## Current status
draft

## Journal / venue


## Submission date


## Last action


## Missing companion artifacts
- [ ] abstract
- [ ] references
- [ ] cover-letter
- [ ] reviewer-response

## Notes

"@
    Set-Content -Path "$Path\_status.md" -Value $content -Encoding UTF8
}

# Destination directories are created on demand by Move-ToCanonical.


# ─────────────────────────────────────────────────────────────
# AI ANXIETY  (AI Society submission)
# ─────────────────────────────────────────────────────────────

Write-Host "`n=== ai-anxiety ===" -ForegroundColor Magenta
$dest   = "$PAPERS\ai-governance\ai-anxiety"
$phase2 = "C:\Users\softinfo\Documents\PAPERS_MASTER_CONSOLIDATED_2026-04-10\PHASE_2_RECURSIVE_GOVERNANCE_UNDER_CONSTRAINT"

# ai-anxiety companions live on C:, already copied to PHAROS_PAPERS_DB by the Python script.
# This block moves the Drive G .gdoc stub only (if it exists there).
Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\01_AI_Anxiety_to_Recursive_Governance_AI_Society_Manuscript.gdoc" `
    "$dest\ai-anxiety_manuscript.gdoc"

# Remaining companions are sourced from C: local (authoritative copies).
# They were already landed at PHAROS_PAPERS_DB\ai-governance\phase-2\ by migrate_to_pharos_papers_db.py.
# Move-ToCanonical calls below are intentionally skipped to avoid duplication.

Write-Status $dest "ai-anxiety"


# ─────────────────────────────────────────────────────────────
# GOVERNANCE BY DENIAL  (JPP submission)
# ─────────────────────────────────────────────────────────────

Write-Host "`n=== governance-by-denial ===" -ForegroundColor Magenta
$dest = "$PAPERS\ai-governance\governance-by-denial"

# Canonical version: the numbered working draft (most recent naming)
Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\10_Governance_by_Denial_working_draft.docx" `
    "$dest\governance-by-denial_manuscript.docx"

Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\10_Governance_by_Denial_working_draft.md" `
    "$dest\governance-by-denial_manuscript.md"

Move-ToCanonical `
    "$DRIVE\Governance by Denial-JPP.gdoc" `
    "$dest\governance-by-denial_manuscript.gdoc"

Move-ToCanonical `
    "$DRIVE\Governance by Denial - Journal of Political Power submission alignment note.md" `
    "$dest\governance-by-denial_notes.md"

# Archive older working draft versions
Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\Governance by Denial - revised working draft.docx" `
    "$dest\_archive\Governance by Denial - revised working draft.docx" -Archive $true

Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\Governance by Denial - revised working draft.md" `
    "$dest\_archive\Governance by Denial - revised working draft.md" -Archive $true

Write-Status $dest "governance-by-denial"


# ─────────────────────────────────────────────────────────────
# RECURSIVE DETERMINISTIC AI GOVERNANCE
# ─────────────────────────────────────────────────────────────

Write-Host "`n=== recursive-det-gov ===" -ForegroundColor Magenta
$dest = "$PAPERS\ai-governance\recursive-det-gov"

Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\01_Master__Recursive_Deterministic_AI_Governance.docx" `
    "$dest\recursive-det-gov_manuscript.docx"

Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\01_Master__Recursive_Deterministic_AI_Governance.md" `
    "$dest\recursive-det-gov_manuscript.md"

Write-Status $dest "recursive-det-gov"


# ─────────────────────────────────────────────────────────────
# RECURSIVE CONTINUITY WITHOUT MEMORY
# ─────────────────────────────────────────────────────────────

Write-Host "`n=== recursive-continuity ===" -ForegroundColor Magenta
$dest = "$PAPERS\ai-governance\recursive-continuity"

Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\08_Recursive_Continuity_Without_Memory__journal_manuscript.docx" `
    "$dest\recursive-continuity_manuscript.docx"

# Note: there is also a variant without double underscore — archive it
Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\08_Recursive_Continuity_Without_Memory_journal_manuscript.docx" `
    "$dest\_archive\08_Recursive_Continuity_Without_Memory_journal_manuscript.docx" -Archive $true

Write-Status $dest "recursive-continuity"


# ─────────────────────────────────────────────────────────────
# FIRST METHOD PAPER  (Very Long / Long / Medium Narratives)
# ─────────────────────────────────────────────────────────────

Write-Host "`n=== first-method-paper ===" -ForegroundColor Magenta
$dest = "$PAPERS\ai-governance\first-method-paper"

Move-ToCanonical `
    "$DRIVE\$b$b$b Recursive AI Governance as Executable Method_ The Very Long Narrative.gdoc" `
    "$dest\first-method-paper_very-long-narrative.gdoc"

Move-ToCanonical `
    "$DRIVE\$b$b From Recursive Pressure to Institutional Governance Method_ The Long Narrative of the AI-Governance Architecture.gdoc" `
    "$dest\first-method-paper_long-narrative.gdoc"

Move-ToCanonical `
    "$DRIVE\$b From Recursive Output to Governable Method  A Short Narrative of the AI-Governance Architecture.gdoc" `
    "$dest\first-method-paper_medium-narrative.gdoc"

Move-ToCanonical `
    "$DRIVE\Recursive AI Governance as Executable Method_ The Very Long Narrative.md" `
    "$dest\first-method-paper_very-long-narrative.md"

# The •••  .docx version (from official_paper_gaps cluster)
Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\$b$b$b Recursive AI Governance as Executable Method_ The Very Long Narrative.docx" `
    "$dest\first-method-paper_very-long-narrative.docx"

# PDFs from Downloads Intake
Move-ToCanonical `
    "C:\Users\softinfo\Documents\AI GOVERNANCE LIBRARY\Downloads Intake 2026-03-29\$b From Recursive Pressure to Institutional Method_ The Medium Narrative of the AI-Governance Architecture-MEDIUM.pdf" `
    "$dest\first-method-paper_medium-narrative.pdf"

Move-ToCanonical `
    "C:\Users\softinfo\Documents\AI GOVERNANCE LIBRARY\Downloads Intake 2026-03-29\$b$b From Recursive Pressure to Institutional Governance Method_ The Long Narrative of the AI-Governance Architecture.pdf" `
    "$dest\first-method-paper_long-narrative.pdf"

Move-ToCanonical `
    "C:\Users\softinfo\Documents\AI GOVERNANCE LIBRARY\Downloads Intake 2026-03-29\$b$b$b Recursive AI Governance as Executable Method_ The Very Long Narrative.pdf" `
    "$dest\first-method-paper_very-long-narrative.pdf"

Write-Status $dest "first-method-paper"


# ─────────────────────────────────────────────────────────────
# ANTHRO PHAROS
# ─────────────────────────────────────────────────────────────

Write-Host "`n=== anthro-pharos ===" -ForegroundColor Magenta
$dest = "$PAPERS\ai-governance\anthro-pharos"

Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\ANTHRO_PHAROS.docx" `
    "$dest\anthro-pharos_manuscript.docx"

Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\ANTHRO_PHAROS.pdf" `
    "$dest\anthro-pharos_manuscript.pdf"

Write-Status $dest "anthro-pharos"


# ─────────────────────────────────────────────────────────────
# AI GOVERNANCE WHO'S THE BOOB
# ─────────────────────────────────────────────────────────────

Write-Host "`n=== ai-governance-whos-the-boob ===" -ForegroundColor Magenta
$dest = "$PAPERS\ai-governance\ai-governance-whos-the-boob"

Move-ToCanonical `
    "$DRIVE\AI_Governance_Whos_the_Boob_Whos_the_Trap_40k_revised.md" `
    "$dest\ai-governance-whos-the-boob_manuscript.md"

Move-ToCanonical `
    "$DRIVE\AI_Governance_Whos_the_Boob_Whos_the_Trap_40k_Target.docx" `
    "$dest\ai-governance-whos-the-boob_manuscript.docx"

# Archive original 40k (pre-revision)
Move-ToCanonical `
    "$DRIVE\AI_Governance_Whos_the_Boob_Whos_the_Trap_40k.md" `
    "$dest\_archive\AI_Governance_Whos_the_Boob_Whos_the_Trap_40k.md" -Archive $true

Move-ToCanonical `
    "$DRIVE\AI_Governance_Whos_the_Boob_Whos_the_Trap_40k_Target (2).docx" `
    "$dest\_archive\AI_Governance_Whos_the_Boob_Whos_the_Trap_40k_Target (2).docx" -Archive $true

Write-Status $dest "ai-governance-whos-the-boob"


# ─────────────────────────────────────────────────────────────
# PHAROS INVENTION DISCLOSURE
# ─────────────────────────────────────────────────────────────

Write-Host "`n=== pharos-invention-disclosure ===" -ForegroundColor Magenta
$dest = "$PAPERS\ai-governance\pharos-invention-disclosure"

# Canonical: v12 (latest numbered version)
Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\05_PHAROS_Invention_Disclosure_v12.docx" `
    "$dest\pharos-invention-disclosure_v12.docx"

Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\05_PHAROS_Invention_Disclosure_v12.pdf" `
    "$dest\pharos-invention-disclosure_v12.pdf"

Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\PHAROS_Invention_Disclosure_v11.docx" `
    "$dest\pharos-invention-disclosure_v11.docx"

Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\PHAROS_Invention_Disclosure_v11.pdf" `
    "$dest\pharos-invention-disclosure_v11.pdf"

# Patent counsel working draft
Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\PHAROS_Invention_Disclosure_v6_patent_counsel_working_draft.docx" `
    "$dest\pharos-invention-disclosure_patent-counsel.docx"

Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\PHAROS_Invention_Disclosure_v6_patent_counsel_working_draft.pdf" `
    "$dest\pharos-invention-disclosure_patent-counsel.pdf"

# Archive v5, v6, v7, v8, v9, v10
foreach ($v in @("v5","v6","v7","v8","v9","v10")) {
    foreach ($ext in @(".docx",".pdf")) {
        $src = "$DRIVE\Shared with ChatGPT\Papers\PHAROS_Invention_Disclosure_$v$ext"
        if (Test-Path $src) {
            Move-ToCanonical $src "$dest\_archive\PHAROS_Invention_Disclosure_$v$ext" -Archive $true
        }
    }
}

Write-Status $dest "pharos-invention-disclosure"


# ─────────────────────────────────────────────────────────────
# BUFFY
# ─────────────────────────────────────────────────────────────

Write-Host "`n=== buffy ===" -ForegroundColor Magenta
$dest = "$PAPERS\media-studies\buffy"

# Canonical: BUFFY_FINAL
Move-ToCanonical `
    "$DRIVE\AI\buyff AND ai\BUFFY_FINAL_with_selected_bibliography.docx" `
    "$dest\buffy_manuscript.docx"

# Archive the revised-with-bibliography variant
Move-ToCanonical `
    "$DRIVE\AI\buyff AND ai\BUFFY_revised_with_bibliography.docx" `
    "$dest\_archive\BUFFY_revised_with_bibliography.docx" -Archive $true

# (1) variant is same file — archive
Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\BTVS\BUFFY_FINAL_with_selected_bibliography (1).docx" `
    "$dest\_archive\BUFFY_FINAL_with_selected_bibliography (1).docx" -Archive $true

Write-Status $dest "buffy"


# ─────────────────────────────────────────────────────────────
# COMPRESS WITHOUT OPACITY
# ─────────────────────────────────────────────────────────────

Write-Host "`n=== compress-without-opacity ===" -ForegroundColor Magenta
$dest = "$PAPERS\media-studies\compress-without-opacity"

# Canonical: most complete = latest CITED version (has references; latest timestamp)
Move-ToCanonical `
    "$DRIVE\AI\SEALED CARD MASTER MARKDOWN\COMPRESS\CompressOpaq-FINAL-CITED-20260228-165347.docx" `
    "$dest\compress-without-opacity_manuscript.docx"

# Archive all earlier/backup/non-cited variants
$compressArchive = @(
    "Compress without Opacity-DRAFT2.docx",
    "Compress without opacity (1).docx",
    "Compress without opacity (2).docx",
    "Compress without opacity.docx",
    "CompressOpaq-FINAL-BACKUP-20260228-161530.docx",
    "CompressOpaq-FINAL-BACKUP-20260228-164858.docx",
    "CompressOpaq-FINAL-BACKUP-20260228-165347.docx",
    "CompressOpaq-FINAL-CITED-20260228-164858.docx",
    "CompressOpaq-FINAL.docx",
    "CompressOpaq-TRUE.docx",
    "CompressOpaq-TRUE.odt",
    "VISIBILITY.docx",
    "introduction.docx"
)

foreach ($f in $compressArchive) {
    Move-ToCanonical `
        "$DRIVE\AI\SEALED CARD MASTER MARKDOWN\COMPRESS\$f" `
        "$dest\_archive\$f" -Archive $true
}

# .gdoc versions from Google Drive folder
$gdocVersions = @(
    "Compress without Opacity-DRAFT2.gdoc",
    "Compress without opacity-First draft.gdoc",
    "Compress without opacity.gdoc",
    "CompressOPCv3.gdoc",
    "VISIBILITY.gdoc"
)
foreach ($f in $gdocVersions) {
    Move-ToCanonical `
        "$DRIVE\AI\SEALED CARD MASTER MARKDOWN\Compress without Opacity\$f" `
        "$dest\_archive\$f" -Archive $true
}

Write-Status $dest "compress-without-opacity"


# ─────────────────────────────────────────────────────────────
# SEALED CARD PROTOCOL
# ─────────────────────────────────────────────────────────────

Write-Host "`n=== sealed-card-protocol ===" -ForegroundColor Magenta
$dest = "$PAPERS\media-studies\sealed-card-protocol"

# Canonical: originals without copy-number suffix (TRUE without (1)/(2))
# The .gdoc is the live editable source; .pdf is the most complete rendered form
Move-ToCanonical `
    "$DRIVE\The Sealed Card Protocol - TRUE.gdoc" `
    "$dest\sealed-card-protocol_manuscript.gdoc"

Move-ToCanonical `
    "$DRIVE\AI\SEALED CARD MASTER MARKDOWN\The Sealed Card Protocol - TRUE.pdf" `
    "$dest\sealed-card-protocol_manuscript.pdf"

Move-ToCanonical `
    "$DRIVE\AI\SEALED CARD MASTER MARKDOWN\Sealed_Card_Protocol_FINAL (1).pdf" `
    "$dest\sealed-card-protocol_final.pdf"

# Archive all copy-suffix and rewrite variants
$sealedArchive = @(
    "Sealed_Card_Protocol_FINAL.gdoc",
    "Sealed_Card_Protocol_MERGED_with_Audit_Appendices_v3.gdoc",
    "Sealed_Card_Protocol_Rewrite_9000_words.gdoc",
    "Sealed_Card_Protocol_Rewrite_9000_words (1).gdoc",
    "Sealed_Card_Protocol_Rewrite_9000_words (2).gdoc",
    "Sealed_Card_Protocol_Rewrite_9000_words (3).gdoc",
    "Sealed_Card_Protocol_Rewrite_9000_words_MERGED.gdoc",
    "The Sealed Card Protocol - TRUE (1).docx",
    "The Sealed Card Protocol - TRUE (1).pdf",
    "The Sealed Card Protocol - TRUE (2).docx"
)

foreach ($f in $sealedArchive) {
    $src = "$DRIVE\AI\SEALED CARD MASTER MARKDOWN\$f"
    if (Test-Path $src) {
        Move-ToCanonical $src "$dest\_archive\$f" -Archive $true
    }
    $src2 = "$DRIVE\$f"
    if (Test-Path $src2) {
        Move-ToCanonical $src2 "$dest\_archive\$f" -Archive $true
    }
}

Write-Status $dest "sealed-card-protocol"


# ─────────────────────────────────────────────────────────────
# AUTHORITY WITHOUT ETHICS
# ─────────────────────────────────────────────────────────────

Write-Host "`n=== authority-without-ethics ===" -ForegroundColor Magenta
$dest = "$PAPERS\media-studies\authority-without-ethics"

# Canonical: REVISED version
Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\Soumis\Authority Without Ethics.gdoc" `
    "$dest\authority-without-ethics_manuscript.gdoc"

Move-ToCanonical `
    "$DRIVE\Authority Without Ethics_REVISED.gdoc" `
    "$dest\authority-without-ethics_revised.gdoc"

Write-Status $dest "authority-without-ethics"


# ─────────────────────────────────────────────────────────────
# RECURSO
# ─────────────────────────────────────────────────────────────

Write-Host "`n=== recurso ===" -ForegroundColor Magenta
$dest = "$PAPERS\media-studies\recurso"

Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\RECURSO-DRAFT1.docx" `
    "$dest\recurso_manuscript.docx"

Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\RECURSO-DRAFT1.gdoc" `
    "$dest\recurso_manuscript.gdoc"

Write-Status $dest "recurso"


# ─────────────────────────────────────────────────────────────
# THIS PAPER MAY NOT EXIST
# ─────────────────────────────────────────────────────────────

Write-Host "`n=== this-paper-may-not-exist ===" -ForegroundColor Magenta
$dest = "$PAPERS\media-studies\this-paper-may-not-exist"

Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\This Paper May Not Exist-AI.gdoc" `
    "$dest\this-paper-may-not-exist_manuscript.gdoc"

Move-ToCanonical `
    "$DRIVE\Shared with ChatGPT\Papers\This Paper May Not Exist-AI.docx" `
    "$dest\this-paper-may-not-exist_manuscript.docx"

Write-Status $dest "this-paper-may-not-exist"


# ─────────────────────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────────────────────

Write-Host "`n=== Summary ===" -ForegroundColor Magenta
$mode = if ($DryRun) { "DRY RUN" } else { "EXECUTED" }
Write-Host "Mode: $mode" -ForegroundColor $(if ($DryRun) { "Yellow" } else { "Green" })
Write-Host "Moved/planned: $moved"
Write-Host "Skipped (not found or dest exists): $skipped"
Write-Host "Errors: $errors"

if ($DryRun) {
    Write-Host "`nRun without -DryRun to execute." -ForegroundColor Yellow
}
