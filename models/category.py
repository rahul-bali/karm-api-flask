from api import db, ma
import enum


# Category class
class Category(enum.Enum):
    household = "Household"
    specialized_workers = "Specialized Workers"
    photography = "Photography"
    drawing = "Drawing"
    cleaner = "Cleaner"
    handyman = "Handyman"
    computers = "Computers"
    delivery = "Delivery"
    gardening = "Gardening"
