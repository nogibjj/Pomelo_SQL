from google.cloud import bigquery
from google.oauth2 import service_account

def access():
    credentials = service_account.Credentials.from_service_account_file('/workspaces/Pomelo_SQL/gcp.json')
    project_id = 'centering-seer-367902'
    return credentials, project_id

def pop_artist():
    cred, proj = access()
    client = bigquery.Client(credentials= cred, project=proj)
    query_job = client.query("""
        SELECT artist_name, COUNT(*) as artist_num
        FROM `listenbrainz.listenbrainz.listen` gt
        GROUP BY artist_name
        ORDER BY artist_num DESC
        LIMIT 5;
        """)
    results = query_job.result()
    return results

def pop_track():
    cred, proj = access()
    client = bigquery.Client(credentials= cred, project=proj)
    query_job = client.query("""
        SELECT track_name, COUNT(*) as track_num
        FROM `listenbrainz.listenbrainz.listen` gt
        GROUP BY track_name
        ORDER BY track_num DESC
        LIMIT 5;
        """)
    results = query_job.result()
    return results

def pop_album():
    cred, proj = access()
    client = bigquery.Client(credentials= cred, project=proj)
    query_job = client.query("""
        SELECT release_name, COUNT(*) as album_num
        FROM `listenbrainz.listenbrainz.listen` gt
        GROUP BY release_name
        ORDER BY album_num DESC
        LIMIT 5;
        """)
    results = query_job.result()
    return results

list = pop_artist()
for i in list:
    print(i)


print('this is a test')
print('testing testing')
