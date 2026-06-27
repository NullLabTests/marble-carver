#!/usr/bin/env bash
set -e

echo "Setting up marble-carver..."

python -m pip install --upgrade pip
pip install -e .[tui]

echo ""
echo "Installation complete!"
echo ""
echo "Quick start:"
echo "  marble-carver tui          # Launch the beautiful interface"
echo "  make tui                   # Same thing via make"
echo ""
echo "Or use purely as a GitHub template -- no Python required."
echo ""
echo "Now go carve something true."
