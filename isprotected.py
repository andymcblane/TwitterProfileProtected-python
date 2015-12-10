import urllib2
twitter_handle = ""
data = urllib2.urlopen("https://twitter.com/" + twitter_handle)
y = "Tweets are protected"
if y not in data.read():
	print twitter_handle + "'s page is no longer private. Time to snoop."
