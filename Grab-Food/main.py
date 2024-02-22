from Scraper import Scraper
# from Persist import Persist

#Main function of the application
def main() :

    #Creating instance of Scraper class
    scraper = Scraper()

    # persist = Persist()

    #Exceting main_scraper() method of Scraper
    scraper.main_scraper()

    #To read data from Gzip file
    # data = persist.read_gzip_file()
    # print(data)

if __name__=='__main__' :
    main()