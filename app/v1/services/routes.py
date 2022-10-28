''' main route'''
from fastapi import APIRouter
from .accounts.routes import router as accounts_router


router = APIRouter()

"""
    accounts
"""
router.include_router(accounts_router, prefix="/accounts")
