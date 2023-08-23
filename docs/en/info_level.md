# Customizing information quantity

Function `lest.run` has non-required argument `info_level`,
that can be one of these values:  `'min'`, `'normal'` and `'max'`.

Their differences:

 + `'min'` - output information only about non-successful tests,
   and message `Passed {successful}/{total} tests`;
 + `'normal'` (default value) - output information about every ran test,
   and message `Passed {successful}/{total} tests`;
 + `'max'` - output information about every ran test, and a table with information about
   total tests count, failed tests count, tests with errors count, and elapsed time.
