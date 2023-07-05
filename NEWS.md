# What's new in lest.

## Version 0.4.1 (??.07.2023):

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
