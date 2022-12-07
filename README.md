# Video Game Sales Data Science Project 


## Introduction
The objective of this project was to take is to take data regarding video games sales from 1980 to 2016 and analyze it to see what factors in to the average successful video game. To do this we put ourselves in the shoes of up and coming game developers who want to develop a financial successful video game. 

As prospective game developers we want to know what genres, platforms, and publishers yield the highest video games sales. To find the best factors for each category we use python and the data science skills we learned this semester to analyze our data set. 

Given my knowledge and experience with this market as a gamer I hypothisized that shooters and actions games would be top contenders for the highest selling genres. I also hypothesized that Sony’s Playstation 4 will probably be the highest selling platform, but Microsofts Xbox One sales would still probably be comparable to its Sony competitor. For the highest selling publishers I hypothesized with less certainty that it may be either Activision or Electonic Arts.



## Selection of Data
We source our dataset from a website called Kaggle that hosts various datasets ranging across various topics. Our data set has various columns  of data such as name, platform, year of release, genre, publisher, sales for various regions, critics score, number of critics, users score, number of users, developer, and maturity rating. The data most relevant to us as prospective game developers are the global sales, publisher, genre, and year of release.

Here is a preview of our data (year of release not displayed for readability)
![image](https://user-images.githubusercontent.com/59743835/206031469-b411eb90-57df-4da3-a99a-4c1b4ebc2615.png)

 

## Methods
Tools:
- Seaborn, Pandas, and Matplotlib for data analysis and vizualiztion 
- Pycharm  as IDE

Vizualization methods used with Matplotlib and Seaborn:
- Scatterplot
- Lineplot(Conley Deleon)

## Results
The first visualization we did was a scatter plot for sales by genre overtime:
![image](https://user-images.githubusercontent.com/59743835/206031165-09669deb-0476-4c5b-99a8-477fefcc57cb.png)
There are 2 graphs here one for all sales over time and another for all sales within the standard deviation of that year. This standard deviation plot allows us to see a version of the plot without all of the outliers and statistical anomalies and other contains. One example of a statistical anomaly that can be seen in the graph on the left is WII Sports. It is the highest selling point on the scatter plot on the left with over 80 million global sales. This beats the next highest selling title by around 30 million, but this is an abnormal piece of data as the sales do not tell the full picture. This game was given away with the Wii console and this game was never sold in the traditional way, this inflates the sales number. Wii Sports and other anomalies are not visible on the standard deviation plot; instead we can only see titles closer to the average giving us more reliable data to look at. We use this same principle on all of our graphs.

When looking at the graph we can see that in more recent years that shooter and action games have been very dominant in the high end of sales. Sports seem to be in the middle of the pack when it comes to sales. Strategy games appear to be on the lower end of global sales when compared to other genres. 

The next visualization is a line plot for sales by genre overtime:
(Conley Deleon)
![image](https://user-images.githubusercontent.com/59743835/206031219-8bb20057-4e2e-49a3-b666-56f1fc47bbdf.png)
These line plots show us that action games are the clear winners of the highest selling genre for the past five years. Shooter games are the second highest sales per genre recently, while sports and adventure games are neck and neck for the third highest selling genre of the past five years. Puzzle games are clearly the lowest selling genre for the five past years.

2 more types of visualization that we did was 5 Year Moving Average by Genre Overtime and Number of Titles Published by Genre Over Time:
![image](https://user-images.githubusercontent.com/59743835/206031246-a3cf184e-8ba6-4ad7-bd88-dda1255f36ce.png)
A 5 year moving average is something used often in stock to see how certain stocks are trending over time. We used this same method on the genres to see their trends over time. We found that action had the highest trend recently although it was on a downward trend but so are all the other genres so it is still the highest selling. We see similar results to the other graphs for the other genres too. We also can see that action has the most titles published recently which could factor into the high sales for this genre.

Another visualization we made was for market share by genre over time:
![image](https://user-images.githubusercontent.com/59743835/206031278-63349592-52e3-4d63-8821-461657388544.png)
These plots show us which genres have the highest market share over the years. Like you may have guessed, action is at the top with shooters coming very close. When accounting for standard deviation you can see that shooters have actually passed action games in market share over the past couple of years. This could indicate that trends may be changing  in the near future.

One more visualization we made is the Top 10 Publishers of Action games by Sales Over Time:
(Conley Deleon)
![image](https://user-images.githubusercontent.com/59743835/206031316-0e189724-446e-41d8-a0cd-0a85b5f20121.png)
These plots show that the publisher Take Two Interactive has the highest sales overall but when you adjust for standard deviation they do average as most of their big titles are blockbusters like Grand Theft Auto or the 2K series. These are games in high selling franchises and IP’s they are not your average game that a new development team could just decide to work on. Ubisoft on the other hand does well when you look at both graphs as it has consistently sold a good amount of games throughout its history. In recent years Ubisoft has been one of the top sellers neck and neck with Warner Brothers Interactive, although Warner Brother does not have the consistency of Ubisoft.

The final visualization we made was a line plot of Global sales by Platforms Over Time:
(Conley Deleon)
![image](https://user-images.githubusercontent.com/59743835/206031336-64884688-88d3-4738-834f-fcb23580584a.png)
These plots shows us that over the past 15 years the Wii, Xbox 360, and PS3 were the highest selling platforms. When you look closer at the past couple years you can start to see that those consoles are trending downward. This is due to the new generation of consoles coming out causing a transitional period as consumers are adopting the newer tech and phasing out their old consoles. We can see that as PS4 and Xbox One sales rise, the PS3 and Xbox 360 sales are starting to fall.

This visualizations have shown us how the best selling genre of video games is the action game genre, with shooters coming in second. It also has shown us the most consistent best selling publisher is Ubisoft, while the highest total sales goes to Take Two Interactive. It also shows us that we are currently in a transitional period as consumers are cycling out their old platforms like the PS3 and Xbox 360 for the newer platforms like the PS4 and Xbox One. Given this information our best bet as game developers is to make an action game that is published by Ubisoft for the Playstation 4, Playstation 3, Xbox 360, and Xbox One.




## Discussion
Our results imply that as game developers we should make an action game that is published by Ubisoft for the Playstation 4, Playstation 3, Xbox 360, and Xbox one. These factors should give our game a decent shot at being financially successful in the current video game market, given we make a game that is actually fun. These results are in line with research we have done, according to business insider as of may 2016 Playstation 4 was the highest selling console. Also Statista did research in 2018 on video games sales by genre and the highest selling genre was action followed by shooters. Given more data and time we could there is much more we could discover about video games sales. If we had data on factors such as the game's graphical budget, multiplayer capabilities, or price we could use this data to see what effect it had on sales. There is also an emerging trend of free to play video games with built in micro transactions such as power boosts, in game cosmetics, and in game currencies that could be researched to see how this monetization models factor into a video games financial success. 



## References
https://www.businessinsider.com/playstation-4-sales-2016-5

https://www.statista.com/statistics/189592/breakdown-of-us-video-game-sales-2009-by-genre/

https://www.kaggle.com/datasets/rush4ratio/video-game-sales-with-ratings?resource=download
