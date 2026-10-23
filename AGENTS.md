# Working instructions

- Implement the requested RF modules independently, using documented behavior and evidence from the selected local RF files.
- Never claim a module is implemented, compatible, built or tested without corresponding evidence.
- Feature names are scope labels, not sufficient behavior specifications. Record unknowns in docs/FEATURES.md.
- Current stage is inventory/specification. All game modules remain pending until actual implementation and integration tests exist.
- Read docs/NEXT_STEPS.md before local RF analysis. Locate the target client/server with the user; never assume F:\\rea-main is the game folder.
- Use available REA MCP tools for static inspection first. Do not invent offsets, hook addresses, packet definitions, database schemas or compatibility results.
- Work with local test copies. Keep original RF files and production databases unchanged during analysis.
- Keep credentials, player data, database backups, third-party binaries and raw sensitive analysis outputs out of Git.
- Before adding migrations, inspect the actual schema; document backup, rollback limitations, and reward/currency consistency tests.
- Mark draft API/schema proposals as proposals. Do not imitate an engine integration with empty functions or success-returning stubs.
- Distribute a game patch only after a real build and target integration testing. The inventory tool is not a game patch.
