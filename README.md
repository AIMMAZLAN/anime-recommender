# Anime recommender

Anime recommender is an automated decision maker, python-based-model that suggests an anime title to its user. Intended to be up-to-date with current released animes, it obtains a list from [Jikan](https://github.com/jikan-me/jikan),  an open-source API. For further details on what this API can do, please read [Jikan's
documentation.](https://jikan.docs.apiary.io/#) 


Due to Jikan V3 deprecation, response url of change to V4 and because we only need a list of anime data, `/anime` were added to Jikan API can be made:
-	`request url`: The url that was requested: `https://api.jikan.moe/v4/anime`
-	`headers`: response header from Jikan [here.](https://jikan.docs.apiary.io/#introduction/information/caching)
This method also valid if you need to get different response data e.g. genre, `/genre`.

Example of data after being clean and sorted up into pandas dataframe. 

| anime_title   | genre         | total_eps  | rating_score | anime_status |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Cowboy Bebop  | Action | 26  | 8.75  | Finished Airing  |
| Cowboy Bebop: Tengoku no Tobira	| Action	| 1 |	8.38	| Finished Airing |
|	Trigun	| Action	| 26	| 8.22	| Finished Airing |
|	Witch Hunter Robin|	Action|	26|	7.26|	Finished Airing|
|	Bouken Ou Beet	|Adventure	|52	|6.95|	Finished Airing|
| Eyeshield 21	|Sports	|145|	7.92|	Finished Airing|
|Hachimitsu to Clover	|Comedy	|24|	8.02	|Finished Airing|
|Hungry Heart: Wild Striker	|Comedy	|52|	7.55|	Finished Airing|
|Initial D Fourth Stage|	Action	|24|	8.15	|Finished Airing|
|Monster	|Drama|	74	|8.84|	Finished Airing|
|Naruto	|Action	|220	|7.97	|Finished Airing|
