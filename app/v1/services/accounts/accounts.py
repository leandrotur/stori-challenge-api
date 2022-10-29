""" Module that acts as controller for  s (es)."""
import pandas as pd
from .utils import send_mail


class Accounts:
    """ class to handle client accounts"""
    def __init__(
        self,
        account_name: str,
        client_name: str
    ) -> None:
        self.account_name = account_name
        self.client_name = client_name

    def send_account_details_mail(
        self,
        email_to: str,
        data: pd.DataFrame
    ):
        """function that processes the CSV and sends an email to the client"""
        total_balance = data['Transaction'].sum()
        data['Date'] = data['Date'].astype('datetime64[ns]')
        data['month'] = data.Date.dt.strftime('%b')
        data['year'] = data.Date.dt.year
        data.drop('Date', inplace=True, axis=1)
        transaction_count_by_month = data.groupby(
            [(data.year), (data.month)]
        ).count().rename(columns={'Transaction': 'Number of transactions'})
        avg_credit_by_month = data[data['Transaction'] >= 0]
        avg_credit_by_month = avg_credit_by_month.groupby(
            [(avg_credit_by_month.year), (avg_credit_by_month.month)]
        ).mean().rename(columns={'Transaction': 'Average credit amount'})
        avg_debit_by_month = data[data['Transaction'] < 0]
        avg_debit_by_month = avg_debit_by_month.groupby(
            [(avg_debit_by_month.year), (avg_debit_by_month.month)]
        ).mean().rename(columns={'Transaction': 'Average debit amount'})
        htmlbody = f'Dear {self.client_name} <br> <br>'
        htmlbody = htmlbody + 'Below you will find you account details. <br>'
        htmlbody = htmlbody + 'Total balance is ' + str(total_balance) + '\n\n'
        htmlbody = htmlbody + transaction_count_by_month.to_html() + "\n\n"
        htmlbody = htmlbody + avg_credit_by_month.to_html() + "\n\n"
        htmlbody = htmlbody + avg_debit_by_month.to_html()
        htmlbody = htmlbody + "<br> Best regards. <br><br> stori team"
        send_mail(
            'Account summary - ' + self.account_name,
            htmlbody,
            'leandroturdera1982@gmail.com',
            email_to)
        return ''
