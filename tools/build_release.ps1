param(
    [string]$OkfTool,
    [string]$OutDir = "dist",
    [string]$StageDir = ".scratch\release-bundle",
    [string]$PackageName = "gtfs-schedule-catalog.zip",
    [string]$VizName = "gtfs-schedule-catalog-viz.html",
    [switch]$KeepStage
)

$ErrorActionPreference = "Stop"

$RepoRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot ".."))
$OutPath = [System.IO.Path]::GetFullPath((Join-Path $RepoRoot $OutDir))
$StagePath = [System.IO.Path]::GetFullPath((Join-Path $RepoRoot $StageDir))
$ScratchRoot = [System.IO.Path]::GetFullPath((Join-Path $RepoRoot ".scratch"))

if (-not $StagePath.StartsWith($ScratchRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "StageDir must resolve under .scratch: $StagePath"
}

if (-not $OkfTool) {
    $PluginRoot = Join-Path $env:USERPROFILE ".codex\plugins\cache\okf-bundle-smith\okf-bundle-smith\0.4.0+codex.20260630024744"
    $Candidate = Join-Path $PluginRoot "tools\okf_tool.py"
    if (Test-Path -LiteralPath $Candidate) {
        $OkfTool = $Candidate
    } else {
        throw "Pass -OkfTool or set the script default to an installed OKF Bundle Smith okf_tool.py path."
    }
}

Set-Location -LiteralPath $RepoRoot

if (Test-Path -LiteralPath $StagePath) {
    Remove-Item -LiteralPath $StagePath -Recurse -Force
}

try {
New-Item -ItemType Directory -Path $StagePath -Force | Out-Null
New-Item -ItemType Directory -Path $OutPath -Force | Out-Null

$Files = git -C $RepoRoot ls-files
foreach ($File in $Files) {
    $Source = Join-Path $RepoRoot $File
    $Target = Join-Path $StagePath $File
    $TargetDir = Split-Path -Parent $Target
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
    Copy-Item -LiteralPath $Source -Destination $Target -Force
}

$ZipPath = Join-Path $OutPath $PackageName
$VizPath = Join-Path $OutPath $VizName

python $OkfTool lint $StagePath --format markdown
python $OkfTool stats $StagePath
python $OkfTool visualize $StagePath -o $VizPath
python $OkfTool package $StagePath $ZipPath --format zip

Add-Type -AssemblyName System.IO.Compression.FileSystem
$Zip = [System.IO.Compression.ZipFile]::OpenRead($ZipPath)
try {
    $BadEntries = $Zip.Entries |
        Where-Object {
            $_.FullName -like ".git/*" -or
            $_.FullName -like "dist/*" -or
            $_.FullName -like ".scratch/*"
        } |
        Select-Object -ExpandProperty FullName

    if ($BadEntries) {
        throw "Publication package contains local-only entries: $($BadEntries -join ', ')"
    }
} finally {
    $Zip.Dispose()
}

Write-Host "Release artifacts written:"
Write-Host "  $ZipPath"
Write-Host "  $VizPath"
} finally {
    if (-not $KeepStage -and (Test-Path -LiteralPath $StagePath)) {
        Remove-Item -LiteralPath $StagePath -Recurse -Force
    }
}
