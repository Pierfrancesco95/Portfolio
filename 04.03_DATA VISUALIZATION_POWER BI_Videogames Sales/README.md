# Sales Analysis - Videogames sales at 2016

The chart shows the console generations timeline:
<img src="https://upload.wikimedia.org/wikipedia/en/timeline/8a26gtbjuhmz225itk732rfwueowp7w.png" width="900" height="350" />


In this project I analyzed videogames sales using the **Kaggle dataset** downloaded [here](https://www.kaggle.com/datasets/rush4ratio/video-game-sales-with-ratings). For convenience, you can also find the dataset as csv file in the folder named "csv" in this repository.

These are the main information in the dataset:
- ***Name*** --> the videogame name, it could have duplicate because some videogame are cross platforms;
- ***Platforms*** --> the platform where the videogame can be played;
- ***Year_of_Release*** --> the year when the videogame was realesed;
- ***Genre*** --> the videogame type;
- ***Publisher*** --> who published the videogame;
- ***Developer*** --> who developed the videogame;
- ***NA_sales, UE_sales, JP_sales, Other_sales*** --> the videogame sales in North America, Europe, Japan, Other regions;
- ***Global_sales*** --> the videogame sales worldwide;
- ***Critic_Score, Critic_count*** --> the vote that Critics assigned to the videogame (from 0 to 100) and how many Critics voted;
- ***User_Score, User_count*** --> the vote that Users assigned to the videogame (from 0 to 10) and how many Users voted;
- ***Rating*** --> The [ESRB ratings](https://www.esrb.org/).

So first I imported the dataset and I trasformed the data via Power BI. Then I made a visual presentation divided by the following dashboards:
- Overall
- 6th Generation (PS2, GameCube, Xbox)
- 7th Generation (PS3, Wii, Xbox360)
- 8th Generation (PS4, WiiU, XboxOne)
- Generations comparison

## Abstract

In this project I analizye videogames sales of the 3 main console generations that are most recent at the date of the analysis (2023). They are 6h generation, 7th generation and 8th generation. For these generations of console I decide to considered only the not-portable console so that the analysis findings could be homogeneous. Also, in order of that, the console choosed are developped by the main companies in the industry (Sony, Nintendo and Microsoft). These platforms are: 
- Playstation 2, GameCube, Xbox;
- Playstation 3, Wii, Xbox 360;
- Playstation 4, WiiU, Xbox One.
  
First I made an overall analysis about the all time videogames global sales. Then for each generation in scope I compared platforms global sales, the global sales trend by the year of release, the composition of global sales in the main regions, how videogame genres performed and the top videogame by global sales in the generation. Finally I compared the three generations in scope to find who is the better in global sales.

#### Limitations
One big limitation in the analysis is about the 8th generation data. Because, as it is showed in the chart at the beginning, the 8th generation (launched in 2012) is still supported and the data avaible are at 2016. Considered that a console has about 10 years of life cycle, for the 8th generation the data are about half of the its platforms life cycle. 

## Overall

Overall the videogames developed are about 11k and the videogames sold are about 811k. The developers are many more than publisher companies. The platforms are 31 ant the one that made sold more videogames is the Playstation 2 and it was owned by Sony. I'll go in detail about platforms later. The videogame genres are 13 and the most sold ones are action, sports and shooter.

### Developers and Publishers
Nintendo is the company who have sold most videogame as developer and as publisher, that's because Nintendo develops and publishes its own videogames, differently from for example Sony who publishes also videogames developed by other companies.
#### Most sold videogames
- **Nintendo**: videogames for Wii and DS platforms;
- **Elettronics Art**: FIFA;
- **Ubisoft**: Assassin's Creed and Just Dance;
- **Rockstar**: Grand Theft Auto;
- **Activision**: Call of Duty;
- **Sony Company**: Gran Turismo, Final Fantasy and Crash Bandicoot.

Please note these companies are not in order because someone are both developer and publisher, so I reported them one time to not be repetitive. Also I reported not the title of one videogame but the title of series videogames (for example for FIFA series exist FIFA 13, FIFA 14 etc...).

### Years of release
The sales trend is increasing up to 2008 where there is the maximum peak for the games released in that year.
In the all time bestseller videogames for global sales there are 8 Nintendo's videogames and 3 videogames cross platforms ("Call of duty" series). 
Considering that more recently released video games sell more than older ones, it is interesting to find that in this classification there are 2 videogames of 80's (Tetris and Super Mario Bros) and 1 videogame of 90's (Pokemon Red/Pokemon Blue).

##  6th Generation (PS2, GameCube, Xbox)

In the 6h Generation the main consoles were PS2 (Sony), Gamecube (Nintendo) and Xbox (Microsoft). In this generation the most selling platform was the Playstation 2 with 112k videogames sold (where the all generation sold 153k units), which was also the one with more videogame playable (61% of all videogame developed in the generation).

The largest market is North America, followed by Europe.

The bestseller videogames are released in between 2002 and 2004.

The bestseller videogame was "Grand Theft Auto: San Andreas", playable only with Playstation 2 or Xbox.

The most selling genre are in order: Action, Sports and Shooter. In particular:
- for PS2, action and sports with Grand Theft Auto and Gran Turismo;
- for Gamecube, action with Super Smash Bros;
- for Xbox, shooter with Halo.

In this generation we noted a big gap between Sony and others.

## 7th Generation (PS3, Wii, Xbox360)

In the 7h Generation the main consoles were PS3 (Sony), Wii (Nintendo) and Xbox360 (Microsoft). In this generation the most selling platform was the Xbox 360 with 89k videogames sold (where the all generation sold 260k units), while the platform with more videogame playable was the Playstation 3 (33,9% of all videogame developed in the generation) but it is followed by the Xbox360 (33,7% of all videogame developed in the generation).

The largest market is North America, followed by Europe.

The bestseller videogames are released in between 2009 and 2011.

The bestseller videogame was Wii sports, playable only with Wii.

The most selling genre are in order: Action, Sports and Shooter. In particular:
- for PS3, action and shooter with Grand Theft Auto and Call of Duty;
- for Wii, sport with Wii sports and Mario Kart;
- for Xbox360, shooter and action with Kinect, Grand Theft Auto and Call of Duty.

In this generation we noted Microsoft with Xbox360 was the better one, but the difference among the platforms is not so much significative both for videogames sold and developed. It's interesting that, unlike the previous generation, Nintendo e Microsoft filled the gap with Sony in console industry.

## 8th Generation (PS4, WiiU, XboxOne)

In the 8h Generation the main consoles were PS4 (Sony), WiiU (Nintendo) and XboxOne (Microsoft). In this generation the most selling platform was the Playstation 4 with 30k videogames sold (where the all generation sold 52k units), while the platform with more videogame playable was the Playstation 4 (50% of all videogame developed in the generation).

The largest market is North America, followed by Europe.

The bestseller videogames are released in between 2014 and 2015.

The bestseller videogame was "Call of Duty: Black Ops 3", playable only with Playstation 4 or XboxOne.

The most selling genre are in order: Shooter, Action and Sports. In particular:
- for PS4, action and shooter with Grand Theft Auto and Call of Duty;
- for WiiU, platform with Mario games;
- for XboxOne, shooter and action with Grand Theft Auto and Call of Duty.

In this generation we noted Sony returns to be the best one in the market with a big gap with others.
Also we noted the shooter became the favorite genre, it is possible due to spread of online games in this period.

## Generations comparison

In this comparision for the generation I mean to refer to the console descripted above. Please remember the limition in the data about the 8th generation, as mentioned in the abstract. 

The most selling generation was the 7th one with 260k sold videogames, over 100k units than the 6th one.

The 5 bestseller videogame genres are the same in 6th and 7th generation, except for racing and miscellaneous genres they swapped positions (the first one went down). In the 8th there are a consistent change, from the third position the shooter passes to the first one, and role-play and platform genres became popular got fourth and fiveth positions. The change could be due to the diffusion of the online game and the competitions with the e-sports.

Observing the distribution of the global sale by the videogames years of release, we noted they have similir shape. First, both the 6th and the 7th generation had a duration of about 10 years, so maybe it will be the same for the 8th one. Second, the console lifecycle is overlapped so that there are always two generations supported at the same time, the older one is only closed when a new one is released (so to still have two active generations). Third, the bestseller videogame are the one released in the middle of the generation, so maybe for the 8th generation they will be the one released between 2023 and 2025.

With regard to developers and publishers, for the 8th generation the dataset is limited. The best developers for global sales in these 3 generations were Eletronic Arts and Rockstar in particular for the 6th generation, Nintendo and Ubisoft in particular for the 7th generation. The best publishers for global sales in these 3 generations were Sony and Eletronic Arts in particular for the 6th generation,  Activision, Nintendo and Ubisoft in particular for the 7th generation. 

## Future applications

Future applications for this project could be to get an update dataset for the 8th generation to complete the comparison cross generation and to try to predict the trend of the future generation sales based on the findings the research.
