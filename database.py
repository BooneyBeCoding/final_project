




from sqlalchemy import create_engine

import psycopg2




 
# Note: There was some late confusion on whether the data in process (Initial Data => VADER => MLM => Final) was going to be split
# into seperate dataframes at each stage or if it would be iteratively added to the same dataframe. At the moment, below tables/dataframes
# do not match those described in the ERD (along with some field names/positions), but induction should generally follow the same format. 
# Will rectify in next segment.




         

alchemyEngine           = create_engine('postgresql+psycopg2://test:test@127.0.0.1/test', pool_recycle=3600);

postgreSQLConnection    = alchemyEngine.connect();

postgreSQLTable         = "Initial_Reddit_Data";

 

try:

    frame           = reddit_df.to_sql(postgreSQLTable, postgreSQLConnection, if_exists='fail');

except ValueError as vx:

    print(vx)

except Exception as ex:  

    print(ex)

else:

    print("PostgreSQL Table %s has been created successfully."%postgreSQLTable);

finally:

    postgreSQLConnection.close();






   
alchemyEngine           = create_engine('postgresql+psycopg2://test:test@127.0.0.1/test', pool_recycle=3600);

postgreSQLConnection    = alchemyEngine.connect();

postgreSQLTable         = "MLM_Output";

 

try:

    frame           = results.to_sql(postgreSQLTable, postgreSQLConnection, if_exists='fail');

except ValueError as vx:

    print(vx)

except Exception as ex:  

    print(ex)

else:

    print("PostgreSQL Table %s has been created successfully."%postgreSQLTable);

finally:

    postgreSQLConnection.close();