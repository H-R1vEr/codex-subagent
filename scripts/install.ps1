# Requires PowerShell 5.1+ and Python 3.10+. Does not alter execution policy.
[CmdletBinding()]
param(
    [ValidateSet('user', 'project')][string]$Scope = 'user',
    [string]$ProjectRoot,
    [string]$Destination,
    [string[]]$Skill,
    [switch]$DryRun,
    [string]$Python
)
$ErrorActionPreference = 'Stop'
$taskArguments = @((Join-Path $PSScriptRoot 'install.py'), '--scope', $Scope)
if ($ProjectRoot) { $taskArguments += @('--project-root', $ProjectRoot) }
if ($Destination) { $taskArguments += @('--destination', $Destination) }
foreach ($taskSkill in $Skill) { $taskArguments += @('--skill', $taskSkill) }
if ($DryRun) { $taskArguments += '--dry-run' }
if ($Python) {
    & $Python @taskArguments
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 @taskArguments
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    & python @taskArguments
} else {
    throw 'Python 3.10+ is required. Install Python or pass -Python with its executable path.'
}
if ($LASTEXITCODE -ne 0) { throw "Installer failed (exit $LASTEXITCODE); see diagnostics above." }
