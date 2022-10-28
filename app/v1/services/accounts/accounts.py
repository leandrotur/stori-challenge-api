""" Module that acts as controller for  s (es)."""
import pandas as pd


class Accounts:
    """ class to handle client accounts"""
    def __init__(
        self
    ) -> None:
        self.config = self._get_config()

    def send_account_details_mail(
        self,
        data: pd.DataFrame
    ):
        """function that processes the CSV and sends an email to the client"""
        return ''
