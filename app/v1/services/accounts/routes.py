""" Routing Module"""
import traceback
from io import BytesIO
import pandas as pd
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from loguru import logger

from .accounts import Accounts
router = APIRouter()


@router.post(
    '/send_account_details_mail',
    summary="send account details email based on csv file",
    description='''
    '''
)
def send_account_details_mail(
    account_name: str = 'Test account',
    client_name: str = 'Test client',
    authorized_email_to: str = 'leandro.g.bedrinan@gmail.com',

    file: UploadFile = File(...)
):
    """ Send email with account details"""
    try:
        contents = file.file.read()
        buffer = BytesIO(contents)
        dataf = pd.read_csv(buffer, index_col='Id')
        data = Accounts(account_name, client_name).send_account_details_mail(
            authorized_email_to,
            dataf
        )
        response = JSONResponse(data)
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
        data = {
            'status': 500,
            'data': f'{traceback.format_exc()}'
        }
        response = JSONResponse(data, 500)
    return response
