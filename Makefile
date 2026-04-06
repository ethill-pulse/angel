.PHONY: heartbeat journal search status commit help

# ─── Angel Operations ────────────────────────────────────────────────────────

help:
	@echo "Angel operations:"
	@echo "  make heartbeat          Review journals, consolidate to memories"
	@echo "  make journal            Create and open a new session journal"
	@echo "  make status             Show recent journals and memory files"
	@echo "  make search QUERY=foo   Search journals and memories for a term"
	@echo "  make commit             Stage all changes and commit with AI-generated message"

# Run Angel's heartbeat: review journals, consolidate to long-term memories.
# Runs non-interactively — Angel will read journals and update memories automatically.
heartbeat:
	@claude "$$(cat agent/prompts/heartbeat.md)"

# Open today's journal (creates if it doesn't exist). Append entries with ## HH:MM headers.
journal:
	@file="agent/journals/$$(date +%Y-%m-%d).md"; \
	if [ ! -f "$$file" ]; then \
		printf "# $$(date +%Y-%m-%d)\n\n" > "$$file"; \
		echo "Created $$file"; \
	fi; \
	$${EDITOR:-vi} "$$file"

# Search journals and memories for a term.
# Usage: make search QUERY="token tiers"
search:
	@if [ -z "$(QUERY)" ]; then echo "Usage: make search QUERY=\"your search term\""; exit 1; fi
	@echo "=== Searching memories ===" && grep -r "$(QUERY)" agent/memories/ --include="*.md" -l 2>/dev/null || echo "(none)"
	@echo "=== Searching journals ===" && grep -r "$(QUERY)" agent/journals/ --include="*.md" -l 2>/dev/null || echo "(none)"

# Commit all staged/unstaged changes with an AI-generated summary message.
commit:
	@printf 'You are a commit message writer. Run git diff HEAD to see the changes, then run git add -A and git commit with a concise, accurate message summarizing what changed. Follow conventional commit format (feat/fix/chore/docs/refactor). No co-authored-by lines. Just do it.' | claude --print --allowedTools 'Bash(git*)'
	@git push

# Show recent journals and the current memory index.
status:
	@echo "=== Recent Journals ==="
	@ls -lt agent/journals/*.md 2>/dev/null | head -10 || echo "  (no journals yet)"
	@echo ""
	@echo "=== Memories ==="
	@ls -1 agent/memories/*.md 2>/dev/null | sed 's|agent/memories/||' || echo "  (no memories yet)"
