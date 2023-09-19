import os

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0,10):
    os.rename(f"data/day{i+1}") # we can rename the folders by using os.rename(f"data/day{i+1}", f"data/tutorial{i+1}")

# for i in range(0,10):
#     os.rename(f"data/day{i+1}",f"data/tutorial{i+1}") # we can rename the folders by using os.rename(f"data/day{i+1}", f"data/tutorial{i+1}") 

