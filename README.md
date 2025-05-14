# urbs
urbes for the llms  

the idea is to set up a virtual town where a bunch of different instances of llms interact with one another in a city. the pie-in-the-sky future look for it would be that it's a sprawling city where 1,000+ different llms make decisions on a daily basis forming a city that evolves independent of any of their contexts. we observe it over a series of years and are able to keep track of different people's lifetimes. we see what decisions they made, their personalities, etc. the whole system is just an llm-powered city simulator.  

what will make it hard is to try to set up a model of what an actual city is. and figure out a good prompting strategy to get them to act sensibly. 

## first-shot
the first-shot i'm thinking is a very simple town with five llms. there are two restaurants each with a single proprietor. each of the non-proprietors has an unknown-to-them preference for which food they like. after choosing a restaurant, they find out how much they liked the food. the next day they pick another. we see this behavior over one week. a simple question: do they converge on the restaurant they like by the end of it? 