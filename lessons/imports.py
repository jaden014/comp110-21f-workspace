"""examples of imports."""

from lessons import helpers

#import using alias
from lessons import helpers as hp

# Import names directly from globals of a module
from lessons.helpers import powerful


from lessons.helpers import THE_ANSWER
print(powerful(2, 10))
print(helpers.powerful(2, 4))
print(hp.THE_ANSWER)
print(f"imports.py: {__name__}")
print(THE_ANSWER)
