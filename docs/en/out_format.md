# Customizing outputs format

Function `lest.run` has non-required argument `out_format`,
that can be one of these values: `'text'` or `'json'`.

Their differences:

 + `'text'` (default value) - information outputs in the plain text format,
   as described in the section ["Customizing information quantity"](https://github.com/wchistow/lest/blob/master/docs/en/info_level.md).
 + `'json'` - information outputs in the JSON format: output is a dictionary,
   where keys - tests names, and values - dictionaries with key `"status"`,
   which value can be one of `"ok"`, `"failed"` or `"error"`.
   If argument [`info_level`](https://github.com/wchistow/lest/blob/master/docs/en/info_level.md) has value `'max'`,
   the key `"<result>"` adds with information about
   total tests count - key `"total"`, successful tests count - key `"successful"`,
   failed tests count - key `"failed"`, tests with errors count - key `"errors"`,
   and elapsed time - key `"time elapsed"`.
