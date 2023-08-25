# What's new in lest.

## Version 0.6.0 (25.08.2023):

### Added:

 + argument `info_level` to function `lest.run`
 + argument `out_format` to function `lest.run`

## Version 0.5.0 (21.07.2023):

### Changed:

 + Improve `AssertionError`'s messages in all assertions

### Removed:

 + Remove attribute `message` from all assertions

## Version 0.4.1 (05.07.2023):

### Added:

 + Exiting with non-zero exit code if some tests weren't passing

## Version 0.4.0 (22.06.2023):

### Added:

 + Printing name of function's module

### Changed:

 + Allow writing, for example, `lest.assert_eq`, but not `lest.assertions.assert_eq`
 + Fix bug in `@lest.setup`: this decorator didn't return function
 + `lest.run` didn't count errors in total

## Version 0.3.0 (12.04.2023):

### Added:

 + module `assertions`
 + decorator `setup`

## Version 0.2.0 (10.04.2023):

### Added:

 + results table
 + handling errors other than `AssertionError`

## Version 0.1.0 (05.04.2023):

First release
