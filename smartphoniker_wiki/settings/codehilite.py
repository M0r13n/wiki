from smartphoniker_wiki.settings import *
from smartphoniker_wiki.settings.local import *

# Test codehilite with pygments

WIKI_MARKDOWN_KWARGS = {
    "extensions": ["codehilite", "footnotes", "attr_list", "headerid", "extra",]
}
