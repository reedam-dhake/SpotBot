import requests
import base64, json 
from secrets import CLIENT_ID,CLIENT_SECRET
#curl -X "POST" -H "Authorization: Basic ZjM4ZjAw...WY0MzE=" -d grant_type=client_credentials https://accounts.spotify.com/api/token
authUrl='https://accounts.spotify.com/api/token'
authData={'grant_type':'client_credentials'}
def getaccesstoken(CLIENT_ID,CLIENT_SECRET):
    message = f"{CLIENT_ID}:{CLIENT_SECRET}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    authHeader={"Authorization": "Basic "+base64_message }
    #print(base64_message)
    res=requests.post(authUrl,headers=authHeader,data=authData)
    responseObject=res.json()
    accessToken=responseObject['access_token']
    return(accessToken)
def getPlaylistTracks(token,playlistID):
    playlistEndPoint=f'https://api.spotify.com/v1/me/playlists/{playlistID}'
    getHeader={'Authorisation':'Bearer '+token}
    res=requests.get(playlistEndPoint,headers=getHeader)
    playlistObject=res.json()
    return(playlistObject)
token=getaccesstoken(CLIENT_ID,CLIENT_SECRET)
print(token)
playlistID='https://open.spotify.com/playlist/5sdLFAdbl2qN1I26x5BkS4?si=52d12ee08fbd4504'
tracklist=getPlaylistTracks(token,playlistID)
print(tracklist)
print(json.dumps(tracklist,indent=2))

