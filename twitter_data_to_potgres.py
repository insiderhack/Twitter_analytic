import pandas as pd
import sqlalchemy
import time
import twitter_data

from sqlalchemy import create_engine
from tokens import postgres_cred

#run sqlalchemy engine
engine = create_engine(postgres_cred())

#pharshing Data json
#global tw_data
#tw_data = ""
#tw_data = tw_data()

# def renew_twdata():
#     global tw_data
#     tw_data = tw_data()
#     return tw_data

def upload_json():
    # renew_twdata()
    data_tw = twitter_data.main()
    tw_df = pd.read_json(data_tw)
    count = tw_df['id'].shape
    tw_df.to_sql('tw_data', engine, if_exists='append' , index=False)
    results = print("{} data updated successfully.".format(count))
    del tw_df, count
    engine.dispose()
    return results

def failupload_json():
    #results = print("Error Data Already exists: {}".format(e))
    results = print("Error Data Already exists. Please Wait it will resume in 10 second ...")
    engine.dispose()
    time.sleep(10)
    upload_json()
    return results

if __name__ == "__main__":
    try:
        upload_json()
        
    except sqlalchemy.exc.IntegrityError as e:
        failupload_json()
    #     try:
    #         renew_twdata()
    #         upload_json()
        
    #     except:
    #         print("Second Resume")
    #         failupload_json()
    #         try:
    #             renew_twdata()
    #             upload_json()
            
    #         except:
    #             print("Third Resume")
    #             failupload_json()
    #             try:
    #                 renew_twdata()
    #                 upload_json()
                
    #             except:
    #                 print("Third Resume Fail too, please check your query or try again later :')\nProces now stoped to safe your resource :')")
    #                 engine.dispose()