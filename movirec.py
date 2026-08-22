import random
from textblob import TextBlob
movies=[
["Interstellar","Sci-Fi",8.7,"Exciting","A team travels through space."],
["Toy Story","Comedy",8.3,"Happy","Toys go on a fun adventure."],
["The Dark Knight","Action",9.0,"Exciting","Batman fights a dangerous criminal."],
["The Pursuit of Happyness","Drama",8.0,"Inspiring","A father works hard for his family."]
]
print("1. Genre")
print("2. Mood")
print("3. IMDB Rating")
print("4. Random")
choice=input("Choose: ")
if choice=="1":
   value=input("Genre: ")
   results=[m for m in movies if m[1].lower()==value.lower()]
elif choice=="2":
   value=input("Mood: ")
   results=[m for m in movies if m[3].lower()==value.lower()]
elif choice=="3":
   value=float(input("Minimum rating: "))
   results=[m for m in movies if m[2]>=value]
else:
   results=movies
movie=random.choice(results)
sentiment=TextBlob(movie[4]).sentiment.polarity
print("\nTitle:",movie[0])
print("Genre:",movie[1])
print("IMDB Rating:",movie[2])
print("Mood:",movie[3])
print("Sentiment:",sentiment)
