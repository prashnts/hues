# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) 
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Fixed
- Fixed old reference name in a test, which was causing builds to fail.
- Many many readme fixes.
- Test coverage setup.
- Moved codeclimate test reporting to `after_success` so it won't break forks.

## [0.2.2] - 2016-10-02
### Fixed
- Important fix. Setup.py was missing `include_package_data` flag.


## [0.2.1] - 2016-10-02
### Fixed
- Configuration wasn't being updated. Fixed.


## [0.2.0] - 2016-10-02
### Added
- Helpers funcs: hues.log, hues.error etc.
- Powerline-ish theme!
- Sane, new API.

### Changed
- Added multiple API enhancements. Particularly, enabling shortcut functions.
- Reduced the complexity of the `console` class.
- Configuration is stored in a `.hues.yml` file.


## [0.1.1] - 2016-09-10
### Fixed
- Missing `MANIFEST.in` caused pip builds to fail..
- Added `__unicode__` for Python 2.

### Added
- Test coverage.


## [0.1.0] - 2016-09-09
### Added
- Implementation and tests for a deterministic PDA routine helpers.
- Color tables generator.
- Alpha release.

### Changed
- Readme updated.


## 0.0.1 - 2016-09-09
### Added
- Initial project, this CHANGELOG.
- Test skeleton.
- Project skeleton.


[UNRELEASED]: https://github.com/prashnts/hues/compare/0.2.1...HEAD
[0.2.2]: https://github.com/prashnts/hues/compare/0.2.1...0.2.2
[0.2.1]: https://github.com/prashnts/hues/compare/0.2.0...0.2.1
[0.2.0]: https://github.com/prashnts/hues/compare/0.1.1...0.2.0
[0.1.1]: https://github.com/prashnts/hues/compare/0.1.0...0.1.1
[0.1.0]: https://github.com/prashnts/hues/compare/0.0.1...0.1.0

