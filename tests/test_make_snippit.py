#A function called make_snippet that takes a string as an argument
# and returns the first five words and then a '...' if there are more than that.

#test to see if the function returns a string less than 5 words with no "..."

from lib.make_snippit import make_snippit

def test_returns_string():
    results = make_snippit("hello")
    assert results == "hello"

#Returns the first five if string is longer than 5 words followed by "..."

def test_returns_five_word_string():
    results = make_snippit("hello how are you on this fine day?")
    assert results == "hello how are you on..."

def test_returns_an_empty_string():
    results = make_snippit("")
    assert results == ""