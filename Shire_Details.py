import pandas as pd
import ace_tools as tools

# Creating a DataFrame for the Shire layout
shire_layout = pd.DataFrame([
    ["Tavern", "The Green Dragon Inn", "A cozy tavern where hobbits gather for hearty meals and cheerful conversation. Serves local ales with a crackling fireplace.", "Doug (Barkeeper) - A short, round hobbit with curly brown hair and bright green eyes.\nAlyssa (Bar Maiden) - A petite young woman with wavy chestnut hair and a cheerful personality."],
    ["Mayor's Residence", "The Mayor’s Hall", "A modest home adorned with flower boxes and maps of the Shire. Reflects the history of the community.", "Kilnbo Bergins - A slightly taller hobbit with hazel eyes, bushy eyebrows, and a formal tunic vest."],
    ["Outfitter Shop", "Hobbiton Outfitters", "A shop filled with clothing, tools, and supplies for hobbit life. Stocked with waistcoats, boots, and more.", "Colin - A brown-eyed male hobbit in ragged brown trousers with a green tunic vest, carrying a dagger."],
    ["Community", "Hobbiton", "Cozy hobbit holes with rounded doors and gardens, connected by winding pathways lined with hedges.", "N/A"],
    ["Pathways", "Village Paths", "Well-trodden dirt paths connecting homes, the tavern, and the outfitter. Lined with wildflowers and grass.", "N/A"],
    ["Gardens", "Hobbit Gardens", "Each home has a garden with vegetables, herbs, and flowers. Community gardens foster collaboration.", "N/A"],
    ["Creeks", "Hobbiton Creek", "A gentle creek with crystal-clear water, smooth stones, and playful fish. A popular spot for relaxation and picnics.", "N/A"],
    ["Entry Point", "North Gate", "A welcoming archway made of timber, adorned with colorful flowers, greeting visitors to Hobbiton.", "N/A"],
    ["Entry Point", "South Path", "A winding dirt road leading to neighboring villages, shaded by tall trees.", "N/A"],
    ["Entry Point", "West Bridge", "A charming wooden bridge crossing the creek, a popular spot to enjoy the water view.", "N/A"],
    ["Entry Point", "East Trail", "A narrow trail leading eastward toward the hills, offering scenic views.", "N/A"],
    ["Person of Interest", "Mayor Calin", "A quest giver in the village.", "N/A"],
    ["Person of Interest", "Doug", "Provides information on a quest and another quest giver.", "N/A"]
], columns=["Category", "Name", "Description", "Key Characters"])

# Displaying the table
tools.display_dataframe_to_user(name="Shire Layout", dataframe=shire_layout)
