import yfinance as yf
import pandas as pd
#Todo
#Fetch Depreciation and Amortization from IS or cash flow, Capital expenditure - CapEx and operating cash flow - OCF from CFStatement
# FREE CASH FLOW -> TB calculated manually
# Total debt, total equity, from balance sheet
# Beta => External source - yFinance
# Risk free rate (r_f) US treasury yield
# Market Risk premium (estimated ~5-8%)
# Growth Rate Estimated or historical CAGR
# Shares Outstanding Balance sheet
# 

pd.set_option("display.max_rows", None)  # Show all rows
pd.set_option("display.max_columns", None)  # Show all columns
pd.set_option("display.width", None)  # Adjust width for readability
pd.set_option("display.max_colwidth", None)  # Show full column width


ticker = "AAPL" 
stock = yf.Ticker(ticker)
def fetchFromStatements():
    income_statement = stock.financials  # OR stock.income_stmt for some versions
    balance_sheet = stock.balance_sheet
    cash_flow = stock.cashflow

    revenue = income_statement.loc["Total Revenue"].iloc[0]
    operating_income = income_statement.loc["Operating Income"].iloc[0]
    net_income = income_statement.loc["Net Income"].iloc[0]
    depreciation = cash_flow.loc["Depreciation And Amortization"].iloc[0]
    capex = cash_flow.loc["Capital Expenditure"].iloc[0]
    oprating_cash_flow = cash_flow.loc["Operating Cash Flow"].iloc[0]
    total_debt = balance_sheet.loc["Total Debt"].iloc[0]  # Latest Total Debt value
    shares_issued = balance_sheet.loc["Share Issued"].iloc[0]
    # total_equity = balance_sheet.loc["Total Stockholder Equity"].iloc[0]
    # total_assets = balance_sheet.loc["Total Assets"].iloc[0]
    # total_liabilities = balance_sheet.loc["Total Liabilities"].iloc[0]
    # total_equity = total_assets - total_liabilities
    #free_cash_flow = cash_flow.loc("Free Cash Flow").iloc[0]
    print(balance_sheet)


fetchFromStatements()
