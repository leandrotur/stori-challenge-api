""" Routing Module"""
import traceback
import json
from io import BytesIO
import pandas as pd
from fastapi import APIRouter, Response, File, UploadFile
from loguru import logger

from .accounts import Accounts
router = APIRouter()


@router.post(
    '/send_account_details_mail',
    summary="send account details email based on csv file",
    description='''
    '''
)
def send_account_details_mail(file: UploadFile = File(...)):
    """ Send email with account details"""
    try:
        contents = file.file.read()
        buffer = BytesIO(contents)
        dataf = pd.read_excel(buffer, engine='openpyxl', skiprows=1)
        data = Accounts().send_account_details_mail(dataf)
        response = Response(
            content=json.dumps(data, indent=4, sort_keys=True, default=str),
            media_type="application/json",
            status_code=200
        )
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
        data = {
            'status': 500,
            'data': f'{traceback.format_exc()}'
        }
        response = Response(
            content=json.dumps(data),
            media_type="application/json",
            status_code=500
        )
    return response
