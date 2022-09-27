"""
EC codebase Python library (AKA the "frontend")

Module mapping details:

TODO: remove module mapping code when backwards-compatibility is no longer required.

The below module mapping is required for backwards-compatibility with old pickle files
generated from before the EC codebase refactor. New files added to the codebase do not
need to be added to the mapping, but if the existing modules are moved, then this the
mapping needs to be updated to reflect the move or rename.

The mapping uses the following pattern:

    sys.modules[<old module path>] = <new module reference>

This is because the previous structure of the codebase was completely flat, and when refactoring
to a hierarchical files, loading previous pickle files no longer works properly. It is important
to retain the ability to read old pickle files generated from official experiments. As a workaround,
the old module paths are included below. A preferable alternative would be to export program state
into JSON files instead of pickle files to avoid issues where the underlying classes change, so that
could be a future improvement to this project. Until then, we use the module mapping workaround.

For more info, see this StackOverflow answer: https://stackoverflow.com/a/2121918/2573242
"""
import sys

from dreamcoder_programs import grammar
from dreamcoder_programs import program
from dreamcoder_programs import task
from dreamcoder_programs import type
from dreamcoder_programs import utilities
from dreamcoder_programs.domains.misc import algolispPrimitives, deepcoderPrimitives
from dreamcoder_programs.domains.misc import RobustFillPrimitives
from dreamcoder_programs.domains.misc import napsPrimitives
from dreamcoder_programs.domains.logo import logoPrimitives
from dreamcoder_programs.domains.list import listPrimitives
from dreamcoder_programs.domains.arithmetic import arithmeticPrimitives
from dreamcoder_programs.domains.text import textPrimitives

sys.modules["grammar"] = grammar
sys.modules["program"] = program
sys.modules["task"] = task
sys.modules["type"] = type
sys.modules["utilities"] = utilities
sys.modules["algolispPrimitives"] = algolispPrimitives
sys.modules["RobustFillPrimitives"] = RobustFillPrimitives
sys.modules["napsPrimitives"] = napsPrimitives
sys.modules["deepcoderPrimitives"] = deepcoderPrimitives
sys.modules["logoPrimitives"] = logoPrimitives
sys.modules["listPrimitives"] = listPrimitives
sys.modules["arithmeticPrimitives"] = arithmeticPrimitives
sys.modules["textPrimitives"] = textPrimitives
