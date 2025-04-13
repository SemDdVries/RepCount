#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "Starting RepCount with HTTP on port 5000..."
python3 "$SCRIPT_DIR/../../run.py" --http 