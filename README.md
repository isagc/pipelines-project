# pipelines-project

The aim of this pipeline project is to find the link (if any) between suicide rates in any of the Nordic Countries (Norway, Sweden, Finland, Iceland and Denmark) and Spain (so to have it as a contrast), and the average annual hours of sunshine they get for a given year.

First, I used a database (https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016) which was built to find signals correlated to increased suicide rates among different cohorts globally, across the socio-economic spectrum. I then used a range of different methods so to clean it and adequate what would be my database to my future needs (i.e, I got rid of all the countries except from the ones mentioned above).


Finally, I added two parameters to my main function (country and year) which are the two variables the user is going to search for in the terminal. The output will be a sentence which compiles information on suicide rates (total, male and female suicides on average) and average sunchine hours given country gets on given year.
