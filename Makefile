.PHONY: help setup install install-tui tui lint check-format cite-check verify clean

help:
	@echo "marble-carver -- available make targets:"
	@echo "  make setup       Install everything (including TUI)"
	@echo "  make install     Install core package only"
	@echo "  make install-tui Install with TUI"
	@echo "  make tui         Launch the Textual TUI"
	@echo "  make lint        Run ruff linter"
	@echo "  make check-format Run ruff format check"
	@echo "  make cite-check  Check citations in all markdown files"
	@echo "  make verify      Run citation + Lean checks"
	@echo "  make clean       Remove __pycache__ and build artifacts"

setup:
	pip install -e .[tui]
	@echo "Ready. Try: marble-carver tui"

install:
	pip install -e .

install-tui:
	pip install -e '.[tui]'

tui:
	marble-carver tui

lint:
	ruff check .

check-format:
	ruff format --check .

cite-check:
	python tools/verify_citations.py --check . --report

verify:
	python tools/verify_citations.py --check . --report
	@echo "Run 'lake build' manually inside any math/ subfolder"

clean:
	rm -rf __pycache__ .ruff_cache *.egg-info build dist
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
