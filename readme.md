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

The public facing website is a customized JupyterHub that allows you to login through your github account and run either python or R code. To access data-sets provided by pluto, just include some standard headers and get going. When you hit "execute", the entire notebook is executed by a local compute instance and the entire result is sent back. This happens through a mongodb queue. And everything is updated on your github account under a repo called *plutons*. [/media](media) has presentations and a screencast of the POC.

* server-side repo: [plutoX](https://github.com/shyams80/plutoX)
* python data-set package: [plutoPy](https://github.com/shyams80/plutoPy), [samples](https://github.com/shyams80/plutons/tree/master/docs-py)
* R data-set package: [plutoR](https://github.com/shyams80/plutoR), [samples](https://github.com/shyams80/plutons/tree/master/docs-R)

Read to give it a whirl? Explore on [pluto.studio](http://pluto.studio)

