import fasttext

war_and_peace = fasttext.load_model("lab6_war_and_peace.bin")
print(war_and_peace.get_nearest_neighbors('black'))
