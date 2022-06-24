import pyshorteners


def sample_res(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)
