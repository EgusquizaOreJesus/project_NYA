# uwu
import os
import time 
import libtorrent as lt 

class Scrapper():
   pass


class Anime():
    def __init__(self, name=None, fansub=None , quality=None , chapter=None , languages=None , release_date=None , torrent_link=None  , season=None , year=None  , save_path = os.getcwd() ,keep_time = float('inf')):
      self.name = name
      self.fansub = fansub
      self.quality = quality
      self.chapter = chapter
      self.languages = {}
      self.release_date = release_date
      self.torrent_link = torrent_link
      self.season = season 
      self.year = year 
      self.save_path = save_path
      self.keep_time = keep_time
    def downloader(self): # CLient torrent to down
        torrent_path = self.path_formater()

        session = lt.session()
        params =  {
            'save_path':torrent_path,
            'storage_mode':lt.storage_mode_t.storage_mode_sparse,
           }
        

        handle = lt.add_magnet_uri(session , self.torrent_link , params)

        print('Download metadata')

        while not handle.has_metadata():
           time.sleep(1)

        print(f'Starting download of {handle.name()}...')

       
        while not handle.is_seed():
            s = handle.status()
            print(f'Download rate: {s.download_rate / 1000} kB/s, '
                  f'Upload rate: {s.upload_rate / 1000} kB/s, '
                  f'Progress: {s.progress * 100:.2f}%')
            time.sleep(1)
        self.update_episode()

        print("Ya tienes troyano de lolis yuristas :3 uwu")

    def path_formater(self ):
        
        path = self.save_path + f'/{self.year}'+f'/{self.season}'+f'/{self.fansub}'+f'/{self.name}'
        print("This is the way -->", path)
        if not os.path.exists(path):
          os.makedirs(path)
          print(f'Directory {path} creaated ...')
        else: 
           print(f'Directory {path} already creadted')

        return path



    def update_info(self, name=None, fansub=None, quality=None, chapter=None, languages=None, release_date=None, torrent_link=None, season=None, year=None, save_path=os.getcwd(), keep_time=None):
        if name is not None:
            self.name = name
        if fansub is not None:
            self.fansub = fansub
        if quality is not None:
            self.quality = quality
        if chapter is not None:
            self.chapter = chapter
        if languages is not None:
            self.languages = languages
        if release_date is not None:
            self.release_date = release_date
        if torrent_link is not None:
            self.torrent_link = torrent_link
        if season is not None:
            self.season = season
        if year is not None:
            self.year = year
        if save_path is not None:
            self.save_path = save_path
        if keep_time is not None:
            self.keep_time = keep_time
    def deleate_anime (self):
       pass 
    
    def update_episode(self):
       self.chapter+=1


if __name__=='__main__':
    magnet = "magnet:?xt=urn:btih:1fd9d7fa5df32afe12a2c4c76b9baa9d097ffaba&dn=MAYONAKA%20PUNCH%20S01E01%20The%20Canceled%20Girl%20and%20the%20Sleepy%20Vampire%201080p%20CR%20WEB-DL%20AAC2.0%20H%20264-VARYG%20%28Multi-Subs%29&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce"
    mayonaka = Anime(
        name="Mayonaka punch",
        fansub="MultiSu",
        quality="1080p",
        chapter="01",
        torrent_link=magnet,
        season="Summer",
        year="2024",
        languages="MultiSubs",
        release_date="2024-07-08"
    )
    mayonaka.downloader()
