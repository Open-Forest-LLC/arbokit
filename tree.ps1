param (
    [string]$StartPath = "."
)

function Get-Tree {
    param (
        [string]$Path
    )
    $items = Get-ChildItem -Path $Path -Recurse | Where-Object { $_.FullName -notmatch "__pycache__|.venv|.idea|main.dist|tests|not_encrypted|.pytest_cache|razmetkins.egg-info|app.dist|tests|.vscode|.mypy_cache|.ruff_cache" } | Sort-Object FullName
    $root = (Get-Item $Path).FullName

    foreach ($item in $items) {
        $relativePath = $item.FullName.Substring($root.Length + 1)
        $parts = $relativePath.Split('\')
        $depth = $parts.Count - 1
        $name = $parts[-1]
        $prefix = ""

        for ($i = 0; $i -lt $depth; $i++) {
            $parentPath = $root + "\" + ($parts[0..($i)] -join "\")
            $siblings = $items | Where-Object { $_.FullName -like ($parentPath + "\*") }
            $isLastParent = ($siblings | Sort-Object FullName | Select-Object -Last 1).FullName -eq $item.FullName
            $prefix += if ($i -eq $depth - 1) {
                if ($isLastParent) { "`-- " } else { "+-- " }
            } else {
                if (($items | Where-Object { $_.FullName -like ($parentPath + "\*") } | Sort-Object FullName | Select-Object -Last 1).FullName -eq $parentPath) { "    " } else { "|   " }
            }
        }

        Write-Output ($prefix + $name)
    }
}

Get-Tree -Path $StartPath