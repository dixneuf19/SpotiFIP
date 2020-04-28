# SpotiFIP

Save the songs which are broadcoasted on the great radio FIP to my Spotify playlists

Each night (let's say around midnight in France), I want to fetch the song played on **FIP** during the evening, and save them as a new Spotify Playlist.

## Development process

### France Radio API

First, I need to fetch the songs played during the day on my favorite station : **FIP**. I considered using some scraping but *France Radio* conveniently offers an [graphql API](https://www.radiofrance.fr/lopen-api-radio-france). After registering an account, I requested a token (you need to specify for which project) and received it in a few minutes. Note that I'm limited to 1000 calls per day, but that's not an issue since I only plan to query it once a day.

Now I can mess around with the interactiv API at <https://openapi.radiofrance.fr/v1/graphql?x-token=*************>.

After looking at the examples and the schema, I want to do the following *graphql* request :

```graphql
{
  grid(start: START_TS, end: END_TS, station: FIP) {
    ... on TrackStep {
      track {
        title
        albumTitle
        mainArtists
      }
    }
  }
}
```

The monday evening 27/04/2020 was particularely good, the timestamps for these evening are :

| French human readable time | RFC unusable time | timestamp |
| -------------------------- | ----------------- | --------- |
| 18:30 27/04/2020           | Tuesday, April 27, 2020 06:30:00 PM GMT+02:00 | **1588005000** |
| 23:30 27/04/2020           | Tuesday, April 27, 2020 11:30:00 PM GMT+02:00 | **1588023000** |

I'll need to generate for a specific days these correct timestamps.

### Secrets

https://tech.preferred.jp/en/blog/working-with-configuration-in-python/ maybe ?
python-dotenv