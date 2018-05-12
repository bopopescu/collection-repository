# -*- coding: utf-8 -*-

'''
    bennu Add-on

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import urlparse,sys,re,xbmcgui

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')

content = params.get('content')

name = params.get('name')

title = params.get('title')

url = params.get('url')

image = params.get('image')

fanart = params.get('fanart')

source = params.get('source')

try: worker = params.get('worker')
except: worker = '0'

windowedtrailer = params.get('windowedtrailer')
windowedtrailer = int(windowedtrailer) if windowedtrailer in ("0","1") else 0

if action == None:
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().root()
    
    try:
        import xbmc,xbmcaddon
        import common as Common

        ADDON = xbmcaddon.Addon(id='plugin.video.bennu')

        if ADDON.getSetting('first.info') == "true":
            TypeOfMessage="t"; (NewImage,NewMessage)=Common.FetchNews()
            Common.CheckNews(TypeOfMessage,NewImage,NewMessage,False)
    except: pass
    
elif action == 'directory':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().get(url)

elif action == 'qdirectory':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().getq(url)

elif action == 'xdirectory':
    from resources.lib.indexers import bennustreams
    if worker == '1': bennustreams.indexer().getx(url, worker=True)
    else: bennustreams.indexer().getx(url)

elif action == 'imdb_list':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().getimdb(url)

elif action == 'trakt_list':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().gettrakt(url)
    
elif action == 'rotten_list':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().getrotten(url)
    
elif action == 'developer':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().developer()

elif action == 'private':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().private()

elif action == 'parental':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().parental_controls()

elif action == 'tvtuner':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().tvtuner(url)

elif 'youtube' in str(action):
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().youtube(url, action)

elif action == 'play':
    from resources.lib.indexers import bennustreams
    bennustreams.player().play(url, content)
    
elif action == 'addItem':
    from resources.lib.modules import sources
    sources.sources().addItem(title)
    
elif action == 'playItem':
    from resources.lib.modules import sources
    sources.sources().playItem(title, source)

elif action == 'browser':
    from resources.lib.indexers import bennustreams
    bennustreams.resolver().browser(url)

elif action == 'search':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().search(url=None)

elif action == 'addSearch':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().addSearch(url)

elif action == 'delSearch':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().delSearch()

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings()

elif action == 'urlresolverSettings':
    from resources.lib.modules import control
    control.openSettings(id='script.module.urlresolver')

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'downloader':
    from resources.lib.modules import downloader_bennu
    downloader_bennu.downloader()

elif action == 'addDownload':
    from resources.lib.modules import downloader_bennu
    downloader_bennu.addDownload(name,url,image)

elif action == 'removeDownload':
    from resources.lib.modules import downloader_bennu
    downloader_bennu.removeDownload(url)

elif action == 'startDownload':
    from resources.lib.modules import downloader_bennu
    downloader_bennu.startDownload()

elif action == 'startDownloadThread':
    from resources.lib.modules import downloader_bennu
    downloader_bennu.startDownloadThread()

elif action == 'stopDownload':
    from resources.lib.modules import downloader_bennu
    downloader_bennu.stopDownload()

elif action == 'statusDownload':
    from resources.lib.modules import downloader_bennu
    downloader_bennu.statusDownload()

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name, windowedtrailer=windowedtrailer)

elif action == 'clearCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCache()

elif action == 'clearCacheMeta':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheMeta()
  
elif action == 'clearCacheProviders':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheProviders()

elif action == 'clearCacheAll':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheAll()
    
elif action == 'radios':
    from resources.lib.indexers import phradios
    phradios.radios()

elif action == 'radioResolve':
    from resources.lib.indexers import phradios
    phradios.radioResolve(url)

elif action == 'radio1fm':
    from resources.lib.indexers import phradios
    phradios.radio1fm()

elif action == 'radio181fm':
    from resources.lib.indexers import phradios
    phradios.radio181fm()

elif action == 'radiocast':
    from resources.lib.indexers import phradios
    phradios.kickinradio()

elif action == 'kickinradiocats':
    from resources.lib.indexers import phradios
    phradios.kickinradiocats(url)


else:
    if 'search' in action:
        url = action.split('search=')[1]
        url = url + '|SECTION|'
        from resources.lib.indexers import bennustreams
        bennustreams.indexer().search(url)
    else: quit()