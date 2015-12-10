import urllib2
from subprocess import call
twitter_handle = "andymcblane"
data = urllib2.urlopen("https://twitter.com/" + twitter_handle)
y = "Tweets are protected"
if y not in data.read():
	print twitter_handle + "'s page is no longer private. Time to snoop."
