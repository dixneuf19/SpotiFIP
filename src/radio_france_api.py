from gql import gql, Client                                                                                                                                                                                
from gql.transport.requests import RequestsHTTPTransport                                                                                                                                                   


sample_transport=RequestsHTTPTransport( 
    url='https://openapi.radiofrance.fr/v1/graphql?x-token=SECRET-TOKEN', 
    use_json=True, 
    headers={ 
        "Content-type": "application/json", 
    }, 
    verify=True 
)

client = Client( 
    retries=3, 
    transport=sample_transport, 
    fetch_schema_from_transport=True, 
    )

query = gql(''' 
    { 
        grid(start: 1588005000, end: 1588023000, station: FIP) { 
        ... on TrackStep { 
            track { 
            title 
            albumTitle 
            mainArtists 
            } 
        } 
        } 
    } 
''')

print(client.execute(query))