This is a HTML parser written in Python 2.7.6.
It fetches the dates, names, quotes, percentage changes and day's ranges of stocks from Yahoo Finance.

Usage: python parser.py "ibb socl pnqi xsd ita iai vbk qqq ewi dfe pbd eirl" > output.txt
Sample output in different trading sessions:

After hours
05/05/2014	ibb	iShares Nasdaq Biotechnology (IBB)	233.28	1.85%	225.34	233.28
05/05/2014	socl	Global X Social Media Index ETF (SOCL)	17.48	0.17%	17.12	17.53
05/05/2014	pnqi	PowerShares NASDAQ Internet (PNQI)	62.61	0.35%	61.46	62.74
05/05/2014	xsd	SPDR S&P Semiconductor ETF (XSD)	67.15	0.12%	66.20	67.41
05/05/2014	ita	iShares US Aerospace & Defense (ITA)	110.34	1.15%	108.62	110.56
05/05/2014	iai	iShares US Broker-Dealers (IAI)	37.42	-0.21%	36.86	37.42
05/05/2014	vbk	Vanguard Small Cap Growth ETF (VBK)	119.97	-0.03%	118.37	120.09
05/05/2014	qqq	PowerShares QQQ (QQQ)	87.95	0.53%	86.76	87.97
05/05/2014	ewi	iShares MSCI Italy Capped (EWI)	17.86	-0.56%	17.65	17.89
05/05/2014	dfe	WisdomTree Europe SmallCap Dividend (DFE)	62.33	-0.11%	61.94	62.39
05/05/2014	pbd	PowerShares Global Clean Energy (PBD)	13.03	0.00%	12.97	13.05
05/05/2014	eirl	iShares MSCI Ireland Capped (EIRL)	38.52	-0.16%	38.39	38.60

Pre-market
06/05/2014	ibb	iShares Nasdaq Biotechnology (IBB)	233.28	05/05/2014
06/05/2014	socl	Global X Social Media Index ETF (SOCL)	17.48	05/05/2014
06/05/2014	pnqi	PowerShares NASDAQ Internet (PNQI)	62.61	05/05/2014
06/05/2014	xsd	SPDR S&P Semiconductor ETF (XSD)	67.15	05/05/2014
06/05/2014	ita	iShares US Aerospace & Defense (ITA)	110.34	05/05/2014
06/05/2014	iai	iShares US Broker-Dealers (IAI)	37.42	05/05/2014
06/05/2014	vbk	Vanguard Small Cap Growth ETF (VBK)	119.97	05/05/2014
06/05/2014	qqq	PowerShares QQQ (QQQ)	87.95	05/05/2014
06/05/2014	ewi	iShares MSCI Italy Capped (EWI)	17.86	05/05/2014
06/05/2014	dfe	WisdomTree Europe SmallCap Dividend (DFE)	62.33	05/05/2014
06/05/2014	pbd	PowerShares Global Clean Energy (PBD)	13.03	05/05/2014
06/05/2014	eirl	iShares MSCI Ireland Capped (EIRL)	38.52	05/05/2014

Trading hours
06/05/2014	ibb	iShares Nasdaq Biotechnology (IBB)	232.01	-0.54%	231.59	232.53
06/05/2014	socl	Global X Social Media Index ETF (SOCL)	17.43	-0.29%	17.43	17.54
06/05/2014	pnqi	PowerShares NASDAQ Internet (PNQI)	62.15	-0.74%	62.15	62.64
06/05/2014	xsd	SPDR S&P Semiconductor ETF (XSD)	67.06	-0.13%	67.06	67.06
06/05/2014	ita	iShares US Aerospace & Defense (ITA)	109.77	-0.52%	109.77	110.39
06/05/2014	iai	iShares US Broker-Dealers (IAI)	37.17	-0.67%	37.17	37.28
06/05/2014	vbk	Vanguard Small Cap Growth ETF (VBK)	119.60	-0.31%	119.60	119.60
06/05/2014	qqq	PowerShares QQQ (QQQ)	87.74	-0.24%	87.68	87.84
06/05/2014	ewi	iShares MSCI Italy Capped (EWI)	17.82	-0.25%	17.81	17.86
06/05/2014	dfe	WisdomTree Europe SmallCap Dividend (DFE)	62.43	0.16%	62.37	62.43
06/05/2014	pbd	PowerShares Global Clean Energy (PBD)	13.03	0.00%	12.97	13.03
06/05/2014	eirl	iShares MSCI Ireland Capped (EIRL)	38.53	-0.13%	38.39	38.60

I have written a blog article (in Chinese) on this program
http://blog.csdn.net/winark/article/details/24890513

For more information on HTMLParser, see
https://docs.python.org/2/library/htmlparser.html
