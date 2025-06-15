# GoonLang Makefile
# Build system for GoonLang programming language

.PHONY: all build install test clean docs lint format benchmark coverage help

# Default target
all: build test

# Variables
PYTHON := python3
PIP := pip3
INTERPRETER := goonlang.py
VERSION := $(shell grep '"version"' goon.json | cut -d'"' -f4)
BUILD_DIR := build
DIST_DIR := dist
DOCS_DIR := docs
TEST_DIR := tests

# Colors for output
RED := \033[0;31m
GREEN := \033[0;32m
YELLOW := \033[0;33m
BLUE := \033[0;34m
NC := \033[0m # No Color

# Build targets
build:
	@echo "$(GREEN)Building GoonLang v$(VERSION)...$(NC)"
	@mkdir -p $(BUILD_DIR)
	@$(PYTHON) -m py_compile $(INTERPRETER)
	@echo "$(GREEN)Build complete!$(NC)"

install: build
	@echo "$(GREEN)Installing GoonLang...$(NC)"
	@chmod +x $(INTERPRETER)
	@sudo cp $(INTERPRETER) /usr/local/bin/goon
	@sudo cp $(INTERPRETER) /usr/local/bin/goonlang
	@echo "$(GREEN)Installation complete!$(NC)"
	@echo "$(BLUE)You can now use 'goon' or 'goonlang' commands$(NC)"

uninstall:
	@echo "$(YELLOW)Uninstalling GoonLang...$(NC)"
	@sudo rm -f /usr/local/bin/goon
	@sudo rm -f /usr/local/bin/goonlang
	@echo "$(GREEN)Uninstallation complete!$(NC)"

# Testing
test:
	@echo "$(GREEN)Running tests...$(NC)"
	@$(PYTHON) -m pytest $(TEST_DIR) -v
	@echo "$(GREEN)All tests passed!$(NC)"

test-examples:
	@echo "$(GREEN)Testing example programs...$(NC)"
	@for file in examples/*.goon; do \
		echo "$(BLUE)Testing $$file...$(NC)"; \
		$(PYTHON) $(INTERPRETER) "$$file" > /dev/null || echo "$(RED)Failed: $$file$(NC)"; \
	done
	@echo "$(GREEN)Example tests complete!$(NC)"

# Code quality
lint:
	@echo "$(GREEN)Running linter...$(NC)"
	@$(PYTHON) -m flake8 $(INTERPRETER) --max-line-length=100
	@echo "$(GREEN)Linting complete!$(NC)"

format:
	@echo "$(GREEN)Formatting code...$(NC)"
	@$(PYTHON) -m black $(INTERPRETER)
	@echo "$(GREEN)Formatting complete!$(NC)"

type-check:
	@echo "$(GREEN)Running type checker...$(NC)"
	@$(PYTHON) -m mypy $(INTERPRETER)
	@echo "$(GREEN)Type checking complete!$(NC)"

# Performance
benchmark:
	@echo "$(GREEN)Running benchmarks...$(NC)"
	@$(PYTHON) benchmark.py
	@echo "$(GREEN)Benchmarks complete!$(NC)"

profile:
	@echo "$(GREEN)Profiling interpreter...$(NC)"
	@$(PYTHON) -m cProfile -o profile.stats $(INTERPRETER) examples/comprehensive.goon
	@$(PYTHON) -c "import pstats; pstats.Stats('profile.stats').sort_stats('cumulative').print_stats(20)"
	@echo "$(GREEN)Profiling complete!$(NC)"

# Coverage
coverage:
	@echo "$(GREEN)Running coverage analysis...$(NC)"
	@$(PYTHON) -m coverage run -m pytest $(TEST_DIR)
	@$(PYTHON) -m coverage report -m
	@$(PYTHON) -m coverage html
	@echo "$(GREEN)Coverage report generated in htmlcov/$(NC)"

# Documentation
docs:
	@echo "$(GREEN)Building documentation...$(NC)"
	@mkdir -p $(DOCS_DIR)
	@$(PYTHON) -m sphinx-build -b html $(DOCS_DIR) $(DOCS_DIR)/_build
	@echo "$(GREEN)Documentation built in $(DOCS_DIR)/_build/$(NC)"

docs-serve:
	@echo "$(GREEN)Serving documentation...$(NC)"
	@cd $(DOCS_DIR)/_build && $(PYTHON) -m http.server 8000

# Package management
package:
	@echo "$(GREEN)Creating distribution package...$(NC)"
	@mkdir -p $(DIST_DIR)
	@tar -czf $(DIST_DIR)/goonlang-$(VERSION).tar.gz \
		$(INTERPRETER) examples/ stdlib/ docs/ README.md LICENSE goon.json
	@echo "$(GREEN)Package created: $(DIST_DIR)/goonlang-$(VERSION).tar.gz$(NC)"

# Development
dev-setup:
	@echo "$(GREEN)Setting up development environment...$(NC)"
	@$(PIP) install -r requirements-dev.txt
	@pre-commit install
	@echo "$(GREEN)Development environment ready!$(NC)"

repl:
	@echo "$(GREEN)Starting GoonLang REPL...$(NC)"
	@$(PYTHON) $(INTERPRETER) -i

debug:
	@echo "$(GREEN)Starting GoonLang debugger...$(NC)"
	@$(PYTHON) $(INTERPRETER) -d examples/showcase.goon

# Utilities
clean:
	@echo "$(YELLOW)Cleaning build artifacts...$(NC)"
	@rm -rf $(BUILD_DIR) $(DIST_DIR) __pycache__ *.pyc .pytest_cache .coverage htmlcov profile.stats
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -delete
	@echo "$(GREEN)Clean complete!$(NC)"

version:
	@echo "GoonLang v$(VERSION)"

info:
	@echo "$(BLUE)GoonLang Build Information$(NC)"
	@echo "Version: $(VERSION)"
	@echo "Python: $(shell $(PYTHON) --version)"
	@echo "Platform: $(shell uname -s)"
	@echo "Architecture: $(shell uname -m)"

# Docker support
docker-build:
	@echo "$(GREEN)Building Docker image...$(NC)"
	@docker build -t goonlang:$(VERSION) .
	@docker tag goonlang:$(VERSION) goonlang:latest
	@echo "$(GREEN)Docker image built!$(NC)"

docker-run:
	@echo "$(GREEN)Running GoonLang in Docker...$(NC)"
	@docker run -it --rm goonlang:latest

# CI/CD
ci: lint type-check test coverage
	@echo "$(GREEN)CI pipeline complete!$(NC)"

release: clean build test package
	@echo "$(GREEN)Release $(VERSION) ready!$(NC)"

# Help
help:
	@echo "$(BLUE)GoonLang Build System$(NC)"
	@echo ""
	@echo "$(YELLOW)Available targets:$(NC)"
	@echo "  build         - Compile the interpreter"
	@echo "  install       - Install GoonLang system-wide"
	@echo "  uninstall     - Remove GoonLang from system"
	@echo "  test          - Run test suite"
	@echo "  test-examples - Test example programs"
	@echo "  lint          - Run code linter"
	@echo "  format        - Format source code"
	@echo "  type-check    - Run type checker"
	@echo "  benchmark     - Run performance benchmarks"
	@echo "  profile       - Profile interpreter performance"
	@echo "  coverage      - Generate coverage report"
	@echo "  docs          - Build documentation"
	@echo "  docs-serve    - Serve documentation locally"
	@echo "  package       - Create distribution package"
	@echo "  dev-setup     - Setup development environment"
	@echo "  repl          - Start interactive REPL"
	@echo "  debug         - Start debugger"
	@echo "  clean         - Clean build artifacts"
	@echo "  version       - Show version"
	@echo "  info          - Show build information"
	@echo "  docker-build  - Build Docker image"
	@echo "  docker-run    - Run in Docker container"
	@echo "  ci            - Run CI pipeline"
	@echo "  release       - Prepare release"
	@echo "  help          - Show this help"
