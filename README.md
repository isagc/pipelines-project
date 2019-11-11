# pipelines-project

The aim of this pipeline project is to find the link (if any) between suicide rates in any of the Nordic Countries (Norway, Sweden, Finland, Iceland and Denmark) and Spain (so to have it as a contrast), and the average annual hours of sunshine they get for a given year.

First, I used a database (from kaggle.com) which was built to find signals correlated to increased suicide rates among different cohorts globally, across the socio-economic spectrum. I then used a range of different methods so to clean it and adequate what would be my database to my future needs (i.e, I got rid of all the countries except from the ones mentioned above).

Then I searched the Internet for an API that could tell me the amount of sunshine hours a given country gets in a given year. This turned out to be very difficult, and so I decided to do some web scraping. Once I had the data I wanted from Wikipedia, i threw it all in one dataframe.

Once I had both dataframes clean and tidy, I merged them so to have one which I could directly call from my main function instead of having the program to clean and scrap each time I asked for something.

Finally, I added two parameters to my main function (country and year) which are the two variables the user is going to search for in the terminal. The output will be a sentence which compiles information on suicide rates (total, male and female suicides on average) and average sunchine hours given country gets on given year.
