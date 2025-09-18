Set operations allow you to perform operations on one or more libraries. To access these, click the **Actions** button in the upper right of the [main page listing all of your libraries]({% if include.ads %}{{ site.ads_base_url }}{% else %}{{ site.scix_base_url }}{% endif %}/user/libraries/).

The Actions button will take you to the **Library Operations** page, where you can select one of the available set operations:
* *Union*: take the union of the primary and all of the secondary libraries. The result, which includes all papers in any of the input libraries, is saved to a new library
* *Intersection*: take the intersection of the primary and all of the secondary libraries. The result, which includes only papers present in all of the input libraries, is saved to a new library
* *Difference*: take the difference between the primary and all of the secondary libraries. The result, which includes papers present in the primary library but in none of the secondary libraries, is saved to a new library
* *Copy*: copy the contents of the source library into the target library. The target library is not emptied first; use the empty operation on the target library first in order to create a duplicate of the source library in the target library
* *Empty*: empty the source library of its contents (no secondary library is needed)

After selecting the set operation, select the primary (or source) library, and any secondary (or target) libraries, as needed. Note that more than one secondary library is allowed when taking the union, intersection, or difference; click the **Add Library** button to add another secondary library.

You may also choose to supply a new library name for the result of the union, intersection, or difference operations. If no name is supplied, a default name will be used, which can be edited after the library is created.
