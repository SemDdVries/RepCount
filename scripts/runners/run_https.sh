#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "Starting RepCount with HTTPS..."
python3 "$SCRIPT_DIR/../../run.py" 