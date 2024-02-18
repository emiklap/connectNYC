# connectNYC

**About**
ABOUT CONNECTNYC Welcome to connectNYC, a website dedicated to connecting New Yorkers with their fellow community members. This is a platform for users to share any and all information related to the various neighborhoods in NYC. Not only is this a great way for users to explore new neighborhoods, but this is also a place for neighbors to discuss important issues within their community.

**WHAT INSPIRED US** We were inspired by the modern-day segregation that exists in our city as a result of many historical and ongoing issues such as red-lining and gentrification. Our city is a hub of many cultures, yet many residents across New York City don't venture out of the inner city atmosphere to go explore. We wish to bridge this gap so that all New Yorkers, rich or poor, Black or White, English-Speaking or Not, can begin to appreciate and critically think about the city around them.

**ABOUT THE TEAM** We are a team of four sophomore undergraduates Daedalus honors students studying Computer Science at CUNY Hunter College. As native New Yorkers, we want to foster community between the diverse neighborhoods that make our city one of a kind. That is why we created ConnectNYC: a platform for sharing the good and the bad in our city. The first step to education is realization. We want to both highlight the beauty of New York City, while still keeping it real and addressing the socioeconomic disparities between our neighborhoods. We hope to enlighten and inspire through this project.


**What it does**
- Users can login/sign up to access main content
- Users are able to make blog-style posts, defaulted as filtered by neighbors, to see posts from fellow community members
- Users can use an interactive map to see where all of the neighborhoods in NYC are, including the name of the neighborhood they hover/click on


**How we built it**
Tech Stack: HTML, CSS, JavaScript, Python, Flask, SQLite
We created the front-end using HTML, CSS, JavaScript. Python was used for both front-end and back-end. SQLite was used to create a local database and back-end handling. Flask was used for back-end.


**Challenges we ran into**
We are by no means Web Developers, so we have rarely used frameworks like Flask and have never created a database before, so this was a big learning curve for all of us. We had trouble with templating and the limited flexibility of the interactive map made with the Python folium module and a GeoJSON file. We wanted to link the neighborhoods on the map with our blog page, but due to the short time frame and our limited experience, we were not able to implement this feature this time around. Our alternative was to add a tagging feature based off data we would read/parse through but, again, we were out of time. In addition, we did not know how to handle authentication with a database that could not be shared through our project repo for security reasons and this is not being hosted anywhere, so profiles made are only locally saved.


**Accomplishments that we're proud of**
This was out first and second hackathons that we've attended, so it was both overwhelming yet exciting. We were experimenting with various technologies and concepts that we've never tackled before, much less in such a short time frame. We are proud we are able to present the main idea behind our project.


**What we learned**
We learned new technologies like SQLite and Flask. We got to learn more about the relationship between data and mapping which was interesting. We learned more about UI and front-end development, as this is probably the most complex UI we have ever built in our lives up until now.


**What's next for ConnectNYC**
Future goals include implementing a filter/tagging feature for the neighborhoods, getting around to fixing authentication so that profiles can be probably saved in one database, creating posts in real time, recommended activity, and geolocation for relevant information.
