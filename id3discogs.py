import discogs_client as discogs
import os,sys,re, eyeD3

from pprint import pprint

version = '0.1.2'

discogs.user_agent = 'id3discogs/1.0 +http://www.claudiodangelis.it/projects/id3discogs'

def main():
	""" It inits the program and reads directory's content looking for albums (subdirs)	"""

	albums = []
	for name in os.listdir('.'):
		if os.path.isdir(os.path.join(('.'), name)):
			albums.append(name)

	for album in albums:
		search(album)

def search(album):
	""" This function parses the album folder's name and pings the db with gathered keywords"""

	searchQuery	= re.sub(r'[\W\d]', ' ', album)
	searchQuery	= re.sub(' +',' ',searchQuery)

	s = discogs.Search(searchQuery)

	check(album,s)

def check(album,s):
	""" `s` holds discogs' response """

	for i in s.results():
		if i.__class__.__name__ != 'MasterRelease' and i.data['formats'][0]['name'] == 'CD':
			print 'Release:'
			print i.data['id']
			print 'Master:'

			try:
				print i.master.data['id']
				print i.master.data['year']
			except Exception, e:
				print 'Unable to retrieve Master data'
				pass

			print i.data['artists'][0]['name']
			print i.title
			for j in i.tracklist:
				print j['title']
				print j['position']
				print j['duration']


if __name__ == "__main__":
    main()