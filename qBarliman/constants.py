import os

"""
Temporary flags
"""
VERBOSE = 3  # Temporary good functions because I don't want accidental import bloat
WARN = "❌‼️‼️"  # 0
GOOD = "✅"  # 1
INFO = "✏️"  # 2
DEBUG = "🐞"  # 3


def warn(*args):
    if VERBOSE >= 0:
        print(WARN, *args)


def good(*args):
    if VERBOSE >= 1:
        print(GOOD, *args)


def info(*args):
    if VERBOSE >= 2:
        print(INFO, *args)


def debug(*args):  # Add debug level logging
    if VERBOSE >= 3:
        print(DEBUG, *args)


"""
Query string (QS) file names
"""

ALLTESTS_QS_F_1 = "interp-alltests-query-string-part-1.scm"
ALLTESTS_QS_F_2 = "interp-alltests-query-string-part-2.scm"
EVAL_QS_F_1 = "interp-eval-query-string-part-1.scm"
EVAL_QS_F_2 = "interp-eval-query-string-part-2.scm"
BARLIMAN_QUERY_SIMPLE_SCM = "barliman-query-simple.scm"
BARLIMAN_QUERY_ALLTESTS_SCM = "barliman-query-alltests.scm"

"""
Minikanren file names
"""
MK_VICARE_F = "mk-vicare.scm"
MK_F = "mk.scm"

"""
File paths
"""

TMP_DIR = os.path.join(os.environ.get("TMP", "/tmp"), "barliman_tmp")
os.makedirs(TMP_DIR, exist_ok=True)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MINIKANREN_CORE_DIR = os.path.join(BASE_DIR, "minikanren", "core")
REL_INTERP_DIR = os.path.join(BASE_DIR, "minikanren", "rel-interp")
TEMPLATES_DIR = os.path.join(BASE_DIR, "minikanren", "templates")

MK_VICARE = os.path.join(MINIKANREN_CORE_DIR, MK_VICARE_F)
MK = os.path.join(MINIKANREN_CORE_DIR, MK_F)

INTERP_ALLTESTS_P_1 = os.path.join(TEMPLATES_DIR, ALLTESTS_QS_F_1)
INTERP_ALLTESTS_P_2 = os.path.join(TEMPLATES_DIR, ALLTESTS_QS_F_2)
INTERP_EVAL_P_1 = os.path.join(TEMPLATES_DIR, EVAL_QS_F_1)
INTERP_EVAL_P_2 = os.path.join(TEMPLATES_DIR, EVAL_QS_F_2)

"""
System paths and configuration
"""
# Process timeouts in milliseconds - increase for debugging
TEST_TIMEOUT_MS = 60000  # 60 seconds for testing
PROCESS_TIMEOUT_MS = 120000  # 120 seconds for processes

# Find Scheme executable
SCHEME_EXECUTABLE = None
potential_executables = ["chez", "scheme"]
for executable in potential_executables:
    if any(
        os.access(os.path.join(path, executable), os.X_OK)
        for path in os.environ["PATH"].split(os.pathsep)
    ):
        SCHEME_EXECUTABLE = executable
        good(f"Found Scheme executable: {executable}")
        break
else:
    warn(
        f"Could not find Scheme executable in PATH. Looked for: {', '.join(potential_executables)}"
    )
    exit(1)

"""
Load query strings from files
"""

ALLTESTS_STRING_PART_1 = ""
ALLTESTS_STRING_PART_2 = ""
EVAL_STRING_PART_1 = ""
EVAL_STRING_PART_2 = ""

try:
    with open(INTERP_ALLTESTS_P_1, "r", encoding="utf-8") as f:
        ALLTESTS_STRING_PART_1 = f.read()
        good(f"loaded {INTERP_ALLTESTS_P_1}")
except Exception as e:
    warn(f"LOAD_ERROR -- reading {INTERP_ALLTESTS_P_1}: {e}")

try:
    with open(INTERP_ALLTESTS_P_2, "r", encoding="utf-8") as f:
        ALLTESTS_STRING_PART_2 = f.read()
        good(f"loaded {INTERP_ALLTESTS_P_2}")
except Exception as e:
    warn(f"LOAD_ERROR -- reading {INTERP_ALLTESTS_P_2}: {e}")

try:
    with open(INTERP_EVAL_P_1, "r", encoding="utf-8") as f:
        EVAL_STRING_PART_1 = f.read()
        good(f"loaded {INTERP_EVAL_P_1}")
except Exception as e:
    warn(f"LOAD_ERROR -- reading {INTERP_EVAL_P_1}: {e}")

try:
    with open(INTERP_EVAL_P_2, "r", encoding="utf-8") as f:
        EVAL_STRING_PART_2 = f.read()
        good(f"loaded {INTERP_EVAL_P_2}")
except Exception as e:
    warn(f"LOAD_ERROR -- reading {INTERP_EVAL_P_2}: {e}")

"""
Default value fields
"""

DEFAULT_DEFINITIONS = [
    "(define ,A",
    "    (lambda ,B",
    "        ,C))",
]

DEFAULT_TEST_INPUTS = [
    "(append '() '5)",
    "(append '(a) '6)",
    "(append '(e f) '(g h))",
    "",
    "",
    "",
]

DEFAULT_TEST_EXPECTED_OUTPUTS = [
    "5",
    "'(a . 6)",
    "'(e f g h)",
    "",
    "",
    "",
]


"""
Scheme code constants
"""

LOAD_MK_VICARE = f'(load "{MK_VICARE}")'
LOAD_MK = f'(load "{MK}")'


SIMPLE_Q = "simple"
INDIVIDUAL_Q = "individual test"

EVAL_FLAGS_FAST = "(allow-incomplete-search)"
EVAL_FLAGS_COMPLETE = "(disallow-incomplete-search)"

EVAL_STRING_FAST = f"(begin {EVAL_FLAGS_FAST} (results))"
EVAL_STRING_COMPLETE = f"(begin {EVAL_FLAGS_COMPLETE} (results))"
