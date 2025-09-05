# Settings for the web capture tool

# Output directory
OUTPUT_DIR = "results"

# Browser settings
BROWSER_TYPE = "firefox"
VIEWPORT_WIDTH = 1280
VIEWPORT_HEIGHT = 800
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)

# Wait times (in milliseconds)
COOKIE_BANNER_WAIT = 2000
DYNAMIC_CONTENT_WAIT = 1500
COOKIE_CLICK_WAIT = 1000

# Cookie consent keywords
COOKIE_ACCEPT_KEYWORDS = [
    "akzeptieren",     # German
    "accept",          # English
    "accept all",      # English
    "accept cookies",  # English
    "accepter",        # French
    "accepter tout",   # French
    "ok",              # Common
    "agree",           # English
    "consent",         # English
    "allow all",       # English
    "allow cookies",   # English
    "got it",          # English
    "i understand",    # English
    "continue",        # English
]

# Impressum/Legal notice keywords
IMPRESSUM_KEYWORDS = [
    "impressum",        # German
    "legal notice",    # English
    "legal",           # English (short)
    "mentions légales",# French
    "mentions legales",# French (no accent)
    "notice légale",   # French (variant)
    "notice legale",   # French (no accent)
    "about us",        # English
    "contact",         # fallback, common legal/contact page
]

# File extensions
HTML_EXTENSION = ".html"
PNG_EXTENSION = ".png"

# Subfolder names
HTML_SUBFOLDER = "html"
IMG_SUBFOLDER = "img"

# URL normalization
DEFAULT_PROTOCOL = "https://" 