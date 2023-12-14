# Introduction

Step into the cricketing arena as we compare Sachin Tendulkar and Virat Kohli's stellar performances. This app is a playground for cricket fans and analysts who want to dig deep into the players' strengths and weaknesses against tough opponents.

Explore the Runs, Centuries, Dismissals, and the thrilling Prediction Game pages. In Runs, check out how many runs a player scored and the speed at which they played. Perfect for understanding their game. Move to Dismissals, where you'll discover the types of dismissals each player faces against specific opponents, revealing their vulnerabilities.

But wait, there's more! Dive into the Prediction Game, where you become the predictor. Guess the runs or the type of dismissal a player might face under different conditions. It's a fun challenge to test your cricket instincts.
## Streamlit app
https://cricketlegends-performance-faceoff.streamlit.app/
## Data Source
Virat Kohli's and Sachin Tendulkar's data have been scraped from the ESPN Cricinfo website.

Virat Kohli's Data:  
https://stats.espncricinfo.com/ci/engine/player/253802.html?class=11;template=results;type=batting;view=innings

Sachin Tendulkar's Data:  
https://stats.espncricinfo.com/ci/engine/player/35320.html?class=11;template=results;type=batting;view=innings


## Data Pre-Processing
 The raw data has a lot of unwanted and wrongly formatted data. So the main task after scraping the data was to clean  it and convert it into the format I wanted.
 -- Steps Performed in Data Pre-Processing
1. Changing the Date format: The Date column has a time attribute associated with it. So It has been processed to only get Date and changed the format to Date format.
2. Adding Match Type Column: The match type has been included in the opposition column. So that needs to be stripped and converted into two columns opposition and Match Type.
3. Formatting Runs and Opposition Column

## Future Work
I would like to update the prediction game. My goal is to take target runs, opposition and balls left as user input and then come up with the strike rate and number of boundaries that the player should have to score to chase down the target.
