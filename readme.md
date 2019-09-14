# What is pluto?

pluto is a compute cloud for exploratory financial data analysis.

# Why?

## Financial data is expensive and dirty

* Multiple vendors, different formats, orthogonal assumptions
* Upfront investment in licensing, database setup and cleaning
* Time-stamped meta-data is non-existent

## Analysis is incomplete

* Almost all analysis is done by practitioners who may not have a background in statistics
* Non-replicable
* Only positive backtests are shared
* Impossible to share research and solicit feedback

# What are the unsolved problems in this space?

## Bringing data to code is hard (Quandl, IEX)

* High bandwidth requirement – piping different data to different endpoints
* Usage is not predictable – should a dataset be hot/warm/tepid/cold
* Data needs to be metered

## Bringing code to data is harder (Quantopian)

* Prevent malicious code
* Prevent data leakage
* Compute needs to be metered 

## Defining the user is the hardest

Who are we building for? Academic? Trader? Investor? Student?

Hard Problems + Business Model = Product Design

***pluto is primarily built for the academic in you.***

# What are pluto's design goals and constraints?

* Data leak-proof
* Metered database load
* Metered compute
* Facilitate collaboration
* Familiar interface
* Documented datasets

# How does it work?

Jupyterlab is setup on the cloud where users can login with their github account, start a python or R notebook and get started. The homepage, [pluto.studio](https://pluto.studio), has recepies and links to working notebooks. If you run into issues, either raise an issue here or post it on [slack](https://join.slack.com/t/plutonation/shared_invite/enQtNzI5Njg3NTkzNzYwLWE2NzI0ODM5N2FjMDQ2ZjMwMWRlY2FmNWZkYzU1OGFhY2NhNzg3MDM0MjEwMmZjNWI2MThlMjZiNWJiMjEwYjM)

* python data-set package: [plutoPy](https://github.com/shyams80/plutoPy), [samples](https://github.com/shyams80/plutons/tree/master/docs-py)
* R data-set package: [plutoR](https://github.com/shyams80/plutoR), [samples](https://github.com/shyams80/plutons/tree/master/docs-R)

Read to give it a whirl? Explore on [pluto.studio](https://pluto.studio)

