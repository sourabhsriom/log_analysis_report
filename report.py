from newsdb import get_top_authors, get_top_articles, get_fails


def main():

    print("\n \t Here are the best authors in our library : \n")
    for author in get_top_authors():
        print (" \t  * \t" + str(author[0]) + " - "
               + str(author[1]) + " views")

    print("\n \t Here are the top articles of our library : \n")
    for article in get_top_articles():
        print (''' \t  * \t \"''' + str(article[0]) + '''\" - ''' +
               str(article[1]) + ''' views''')

    print("\n \t Here are the days of excess access failures! : \n")
    for fails in get_fails():
        print (" \t  * \t" + str(fails[0]) + "--" + str(fails[1])
               + "% failures \n")

main()
