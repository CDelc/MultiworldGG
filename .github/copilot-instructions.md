# Archipelago Path of Exile World - AI Agent Instructions

## Architecture Overview

This is an **Archipelago APWorld** for Path of Exile - a read-only integration that monitors the game via API and log files, without directly modifying game files. The integration works through:

- **Client monitoring**: Reads PoE client logs (`client.txt`) and API data to track character state
- **Item filtering**: Generates and updates PoE item filters to highlight Archipelago items
- **Validation system**: Checks character gear/progression against received items and sends location checks
- **TTS integration**: Provides audio feedback for item pickups and unlocks

### Key Components

1. **World Generator** (`__init__.py`): Main APWorld class, handles item/location generation
2. **Client** (`Client.py`): Archipelago client with CLI commands and async task management  
3. **POE Client** (`poeClient/`): Core integration logic, file monitoring, API calls
4. **Rules** (`Rules.py`): Progression logic determining act reachability based on items
5. **Options** (`Options.py`): Extensive dataclass-based configuration system

## Archipelago Framework Conventions

### World Class Structure
- Extends `World` from `worlds.AutoWorld` with required attributes:
  - `game`: Game name string
  - `options_dataclass`: Links to options class (e.g., `PathOfExileOptions`)
  - `web`: WebWorld instance for web interface customization
  - Item/location name mappings: `item_name_to_id`, `location_name_to_id`

### Options System (Core AP Pattern)
- Uses `@dataclass` with `PerGameCommonOptions` base class
- Option classes inherit from `Toggle`, `Choice`, `Range`, etc.
- **Pattern**: `option_value_name = 0` defines choices, `display_name` for UI
- Access via `self.options.option_name` in World class
- **Critical**: When changing option values, update ALL mapping functions and test mocks
- Option documentation uses docstrings (supports reStructuredText if `rich_text_options_doc = True`)
- Options support `random` as generic value for fixed-set options
- Use `alias_old_name = option_new_name` for backward compatibility
- Option visibility controlled via `Visibility` flags: `none`, `template`, `simple_ui`, `complex_ui`, `spoiler`
- Options without groups categorized into "Game Options" and "Item & Location Options"

### WebWorld Integration
- `theme = "stone"` sets visual theme for POE-specific pages
- `tutorials` list contains setup guides with Tutorial objects
- `option_groups` organizes options display on webhost with `OptionGroup`
- `bug_report_page` directs users to issue tracker
- `options_presets` defines preset configurations for common playstyles
- `item_descriptions` and `location_descriptions` provide user-friendly tooltips

### Item/Location Classification
- Items: `ItemClassification.progression` for logic-required items
- Other classifications: `useful`, `filler`, `trap`
- Locations: `LocationProgressType.DEFAULT/PRIORITY/EXCLUDED`
- **Pattern**: Progression items automatically prioritized by fill algorithm
- Fill algorithm forces progression items to priority locations
- Excluded locations prevent progression/useful items from being placed there
- Item/Location IDs must be 1 to 2^53-1 (world-specific), IDs ≤ 0 are reserved

## Development Patterns

### Testing Strategy
- Tests use `unittest.mock` extensively with `side_effect` functions for complex mocking
- `PoeTestBase` provides common test infrastructure with vendor path setup
- **Pattern**: Mock external dependencies (Items module, API calls) with realistic return values
- Run tests: `python -m pytest worlds/poe/test/ -v`

### Async/File Monitoring
- Client uses `asyncio.Task` management for background file monitoring
- `fileHelper.py` provides cancellable file watchers with proper exception handling
- **Pattern**: All long-running operations should be Task-based and handle `asyncio.CancelledError`

### Vendor Dependencies
- External Python packages stored in `poeClient/vendor/vendor_modules.zip`
- `load_vendor_modules()` extracts and adds to `sys.path` at runtime
- **Add new vendors**: Install to temp dir with `pip install --target . package_name`, zip contents, place in `vendor/`

### Settings vs Options
- **Options**: Player-configurable per-generation (in YAML files)
- **Settings**: Installation-wide config (host.yaml) for paths, ROMs, etc.
- **Pattern**: Use `self.options.X` for generation logic, `self.settings.X` for file paths
- Settings use type annotations with classes inheriting from `settings.Group`
- Settings automatically resolve file paths with `UserFilePath`, `LocalFilePath`
- ROM validation via `md5s` list and `validate()` method override

### Generation Phases
- World creation → `generate_early()` → `create_regions()` → `create_items()` → `set_rules()` → `generate_basic()` → `pre_fill()` → fill → `post_fill()` → `generate_output()`
- Use `stage_assert_generate` to check file availability before output generation
- MultiWorld object accessible via `self.multiworld` provides cross-world data

## Critical Workflows

### Running Tests
```bash
# Run all POE tests
python -m pytest worlds/poe/test/ -v

# Run specific test class
python -m pytest worlds/poe/test/test_rules.py::TestCanReachFunction -v

# Run with debug output  
python -m pytest worlds/poe/test/test_rules.py::TestCanReachFunction::test_specific -v -s
```

### APWorld Development
```bash
# Test world generation
python -m worlds.poe

# Generate multiworld with POE
python Generate.py --player_files_path Players/

# Launch POE client standalone
python PathOfExileClient.py
```

### Common Debug Patterns
- Enable debug in `Rules.py`: Set `_debug = True` in `can_reach()` function
- Client logging: `logger = logging.getLogger("poeClient.ComponentName")`
- **Pattern**: Use f-strings for debug output with component prefixes

## Critical Conventions

### Rules System
- `can_reach(act, world, state)` determines progression logic
- Requirements calculated via `get_*_amount_for_act()` functions  
- **Pattern**: All new progression requirements need corresponding test coverage
- Uses `CollectionState` to check item availability with `state.has()`, `state.count()`

### Mock Strategy for Tests
```python
# Pattern for complex state mocking
def mock_count_from_list(items, player):
    return min(10, len(items))  # Return realistic counts

self.mock_state.count_from_list.side_effect = mock_count_from_list
```

### API Integration
- POE API integration in `gggAPI.py` with OAuth flow
- **Pattern**: All API calls should have timeout and error handling
- Character data cached to avoid rate limiting

### File Structure Conventions
- `poeClient/` contains all game-specific integration code
- `test/` mirrors main module structure with comprehensive coverage
- Options use display_name, range validation, and option groups
- Relative imports within APWorld: `from .Options import PathOfExileOptions`
- Absolute imports for AP base: `from worlds.AutoWorld import World`

## Integration Points

### External Dependencies
- **Archipelago Core**: Extends `CommonContext`, `World`, `WebWorld`
- **POE Game**: Monitors `logs/client.txt`, uses POE API, generates item filters
- **Vendor Modules**: pygetwindow, pynput, pymonctl for window/input management
- **TTS**: Text-to-speech for accessibility features

### Client Integration Patterns
- Clients connect via WebSocket to Archipelago server
- Use `CommonContext` base class for client implementation
- Client command processors extend `ClientCommandProcessor`
- Network protocol handles item/location sync between players
- Client status tracking: `ClientStatus.CLIENT_CONNECTED/READY/PLAYING`

### Datapackage System
- Datapackages contain item/location IDs and name mappings for each game
- Generated automatically from world definitions
- Used by clients to map received IDs to game-specific items/locations
- Checksums validate datapackage consistency across clients
- Access via `/api/datapackage` endpoint or specific checksum requests

### Data Flow & WebHost API
1. Game events → `client.txt` log parsing → `validationLogic.py`
2. Character state → POE API → validation against received items  
3. Item received → filter generation → game highlight → location check sent
4. Archipelago server ↔ Client ↔ POE integration ↔ Game state
- Generation API: POST to `/api/generate` with YAML or JSON weights
- Room status: GET `/api/room_status/<room_id>` for active rooms
- Seed tracking: GET `/api/status/<seed_id>` for generation progress

### APWorld Packaging
- Distributed as `.apworld` files (zip archives with `.apworld` extension)
- Must contain folder matching filename: `poe.apworld` contains `poe/` folder
- All lowercase filenames required for frozen Python compatibility

### Critical Files for AI Understanding
- `__init__.py`: World generation, AP integration, extends `World` class
- `Rules.py`: Core progression logic and reachability, uses `CollectionState`
- `poeClient/main.py`: Client event loop and task coordination
- `poeClient/validationLogic.py`: Game state validation and check sending
- `Options.py`: Configuration system extending `PerGameCommonOptions`

## Common Gotchas
- Option value changes require updating mapping functions AND all test mocks
- File monitoring tasks must handle cancellation properly 
- Mock strategy needs realistic item counts for progression tests
- Vendor module loading required before imports in test files
- APWorld imports must use relative imports (`from .module import Class`)
- Item/Location IDs must be unique within game, can overlap between games
- Progression items MUST be classified as `ItemClassification.progression`
- Options with `random` value require special handling in `from_text()` method
- WebWorld `rich_text_options_doc = True` enables reStructuredText in option docs
- Settings validate file paths automatically; use `md5s` for ROM validation
- `stage_assert_generate` prevents generation failures at output stage
- Client commands need proper error handling and user feedback patterns
