import time
from couchpotato import CPLog
from couchpotato.core.plugins.base import Plugin
from .index import ReleaseIndex, MediaIMDBIndex, TitleIndex

log = CPLog(__name__)


class NoSQL(Plugin):

    db = None

    def test(self):

        db = self.db

        try: db.add_index(ReleaseIndex(db.path, 'release'))
        except: log.debug('Index already exists')

        for id in range(10):
            media = db.insert({
                'type': 'media',
                'tmdb': id,
                'imdb': 'tt%s' % id,
                'last_edit': 0,
                'status': 'active',
                'title': 'Lord of the Rings: The Return of the King',
                'year': 2011,
                'profile_id': 0,
                'category_id': 0,
            })

            db.insert({
                'media_id': media['_id'],
                'type': 'title',
                'title': 'Lord of the Rings: The Return of the King',
            })

            for x in range(40):
                db.insert({
                    'media_id': media['_id'],
                    'type': 'release',
                    'name': 'Release %s' % x
                })

        print db.count(db.all, 'media')

        m = db.get('media', 'tt0')
        db.get('id', m['_id'])

        start = time.time()
        print list(db.get_many('media_title', 'lord of'))
        print time.time() - start

        return

        return

        for media in db.all('media', with_doc = True):
            doc = media['doc']
            for r in db.run('release', 'for_media', media['_id']):
                db.delete(r)

            db.delete(doc)
            break

        start = time.time()
        db.reindex()
        print time.time() - start

        print db.count(db.all, 'media')
        print db.count(db.all, 'release')