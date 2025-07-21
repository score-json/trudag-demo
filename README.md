# trudag-demo

### Demo:
- WFJ-01 references test_primitive_types.py -> changing the test file makes new review necessary
- WFJ-02 uses a test suite validator (i.e. checks if `json_test_suite` is in `passed_tests.txt`) -> removing the test from `passed_tests.txt` makes new review necessary

### Useful commands:
- `trudag manage create-item TA BEHAVIOURS trustable`
- `trudag manage show-item TA-BEHAVIOURS`
- `trudag manage lint`
- `trudag manage set-item TA-BEHAVIOURS` (i.e. review)
- `trudag manage set-link JLEX-01 WFJ-01`
- `trudag score --validate`
- `trudag plot` (produces graph.svg at top level)
- `trudag publish --validate` (results will be in docs/doorstop)

### Lessons learned
- Use  `trudag plot --pick item_name num_parents:num_children` to look at subgraphs
- The `--help` flag is really useful
- Put all configuration data in the items between --- 
- `trudag score` only calculates scores for reviewed items (-> run `trudag manage lint` beforehand)
- SME and validator scores do not seem to be supported in a single item (-> split in multiple items)
- Use the exact function signature (including type hints) for validators

