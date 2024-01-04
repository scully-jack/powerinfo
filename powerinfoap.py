!pip install -r https://raw.github.com/scully-jack/powerinfo/master/requirements.txt
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy import delete
import numpy as np
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas

user_name = 'JACK.SCULLY@KMART.COM.AU'


def splits():
    data = pd.read_sql("SELECT * FROM INVENTORY_PVT.SPLITS_VW", connection)
    if not data.empty:
        df = pd.DataFrame(data)
        print(df)

engine = create_engine(URL(
    user = user_name,
    account='kmartau.ap-southeast-2',
    authenticator='externalbrowser',
    warehouse='KSF_INVENTORY_ANALYST_WH',
    database='KSFPA'
    )
)
try:
    with engine.connect() as connection:
        splits()
finally:
    engine.dispose()
