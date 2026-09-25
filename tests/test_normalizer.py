from ingestion.producer.app.normalizer import normalize
def test_normalize_preserves_usgs_payload():
 feature={'id':'us-test','properties':{'time':1700000000000,'updated':1700000100000,'mag':4.2,'magType':'mb','type':'earthquake'},'geometry':{'coordinates':[12.3,-4.5,10]}}
 event=normalize(feature)
 assert event['event_id']=='us-test';assert event['latitude']==-4.5;assert event['raw_payload']==feature
