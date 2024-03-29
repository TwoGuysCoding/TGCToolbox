"Comprehensive toolbox with all of the utils and tools used in various TGC projects."


# Import logger functions
from .logger import setup_custom_logger as TGCLoggerSetup
from .logger import log_result as TGCLogResult
from .logger import log_result as log_result
from .logger import JacobsAmazingLogger as TGCLogger
from .logger import JacobsAmazingResultsLogger as TGCResultsLogger
from .logger import JacobsAmazingLoggerFormatter as TGCLoggerFormatter


# Importing downloaders
from .downloaders import download_vosk_model as download_vosk_model
from .downloaders import download_file as download_file
from .downloaders import download_video_as_wav as download_youtube
from .downloaders import download_video_as_wav as download_video_as_wav

# Import vosk utils
from .vosk import transcribe_vosk as transcribe_vosk

# Importing ffmpeg utils
from .ffmpeg import *

# Importing operations
from .operations import *

# Importing recorder. Be warned that recorder function is just for testing here and is not robust at all.
try:
    from .recorder import *
except ImportError:
    pass

# Importing sound utils
from .sound import *

# Import wrappers
from .wrapper import *

# Import timing utils
from .timing import *

# Import server utils
from .wait_run import *

# Import version
from .meta import __version__ as __version__
from .meta import __author__ as __author__
from .meta import __provider__ as __provider__