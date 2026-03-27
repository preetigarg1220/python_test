from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:Demo123@cluster0.9hitnm3.mongodb.net/")
print("Connected:", client.list_database_names())