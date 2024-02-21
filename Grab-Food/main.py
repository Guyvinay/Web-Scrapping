from Scraper import Scraper
from Persist import Persist


def main() :

    scraper = Scraper()

    persist = Persist()

    scraper.main_scraper()

    data = persist.read_gzip_file()
    print(data)

if __name__=='__main__' :
    main()