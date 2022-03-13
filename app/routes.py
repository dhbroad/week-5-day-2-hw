from app import app # need to import app
from flask import render_template # render_template is a flask function that we will use to take in the name of our files 

# now we start defining our routes
@app.route('/') # routes() takes in the route you want. "/" takes you to index.html
def home():
    return render_template('index.html')

@app.route('/verses')
def myVerses():
    verse1 = "I can do all things through Him who strengthens me.  Phillipians 4:13 "
    verse2 = "Come now, you who say, “Today or tomorrow we will go into such and such a town and spend a year there and trade and make a profit”— yet you do not know what tomorrow will bring. What is your life? For you are a mist that appears for a little time and then vanishes. Instead you ought to say, “If the Lord wills, we will live and do this or that.”  James 4:13-15 "
    verse3 = "Do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God.  Pillipians 4:6 "
    verse4 = "A new commandment I give to you, that you love one another: just as I have loved you, you also are to love one another. By this all people will know that you are My disciples, if you have love for one another.  John 13:34-35 "
    verse5 = "Come to me, all who labor and are heavy laden, and I will give you rest.  Matthew 11:28 "
    my_verses = [verse1,verse2,verse3,verse4,verse5]
    return render_template('verses.html', my_verses_list=my_verses)