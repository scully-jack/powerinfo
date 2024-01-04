#!/usr/bin/env python
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy import delete
import numpy as np
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime
from datetime import timedelta
import xlsxwriter
import pathlib
import os
import sys
import win32com.client
import shutil
import pythoncom
import re
import time

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
