import re


def validate_linkedin(url):

    pattern = r"^https://(www\.)?linkedin\.com/.*"

    return bool(re.match(pattern, url))


def validate_name(name):

    return len(name.strip()) > 1
