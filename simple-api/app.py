from fastapi import FastAPI
import random

app = FastAPI()

#we will build two simple get endpoints
#tech_&_digital
#money-qoutes

tech_and_digital = [
    "Web Development: Build websites or landing pages for small businesses or individuals.",
    "App Development: Create and sell mobile apps or offer custom development services.",
    "Graphic Design: Design logos, social media posts, or branding materials.",
    "Content Writing: Write blogs, articles, or website copy for clients.",
    "Video Editing: Edit videos for YouTubers, businesses, or influencers.",
    "Social Media Management: Manage and grow social media accounts for businesses.",
    "SEO Services: Optimize websites for better search engine rankings.",
    "Data Entry: Perform simple data entry tasks for companies.",
    "Tech Support: Offer remote tech support to individuals or small businesses.",
    "Game Development: Create and sell small games or work on indie projects.",
]

money_quotes = [
    "The best way to predict the future is to create it.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "The only place where success comes before work is in the dictionary.", 
    "The only way to do great work is to love what you do.",    
    "The future belongs to those who believe in the beauty of their dreams.",
    "The best way to predict the future is to create it.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "The only place where success comes before work is in the dictionary."
]

@app.get("/tech_and_digital")
def get_tech_and_digital():
    """Returns a random tech and digital business idea."""
    return {random.choice(tech_and_digital)}


@app.get("/money_quotes")
def get_money_quotes():
    """Returns a random money quote."""
    return {random.choice(money_quotes)}
