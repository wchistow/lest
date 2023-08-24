# Customizing information quantity

Function `lest.run` has non-required argument `info_level`,
that can be one of these values: `'min'`, `'normal'` and `'max'`.

> **Important:** if argument `out_format` has the not `'text'` value,
> values of argument `info_level` aren't taken into account, except the `'max'` value.

Their differences:

 + `'min'` - output information only about non-successful tests,
   and message `Passed {successful}/{total} tests`;
 + `'normal'` (default value) - output information about every ran test,
   and message `Passed {successful}/{total} tests`;
 + `'max'` - output information about every ran test, and a table with information about
   total tests count, successful tests count, failed tests count, tests with errors count,
   and elapsed time.
