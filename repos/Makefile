REPOS := infrastructure kustomize polaris pulse terraform

.PHONY: update

update:
	@for repo in $(REPOS); do \
		echo "==> $$repo"; \
		git -C $$repo checkout main 2>&1 && git -C $$repo pull 2>&1 || echo "  [skipped]"; \
		echo; \
	done
