from flask import Flask, request, redirect, url_for

from newsdb import get_top_authors, get_top_articles, get_fails

#app = Flask(__name__)


def main():


  #print (get_top_authors()[0][0] )
  print("\n \t Here are the best authors in our library : \n")
  for author in get_top_authors():
      print (" \t  * \t" + str(author[0]) + " - " + str(author[1]) + " views")

    #print (get_top_articles()[0][0])
  print("\n \t Here are the top articles of our library : \n")
  for article in get_top_articles():
      print (''' \t  * \t \"''' + str(article[0]) + '''\" - ''' +
      str(article[1]) +''' views''')
  #print (str(get_fails()[0][0]) + " -- "+str(get_fails()[0][1]) + "%")

  print("\n \t Here are the days of excess access failures! : \n")
  for fails in get_fails():
      print (" \t  * \t" +str(fails[0]) + "--" + str(fails[1]) + "% failures \n")






main()
