import preswald
from preswald import connect, get_df
from preswald import query
from preswald import table, text
from preswald import plotly
import plotly.express as px

print("Start your project here!")

# Load the dataset
connect()  # Initialize connection to preswald.toml data sources
df = get_df("lottery_numbers")  # Load data

# Query or manipulate the data
sql = "SELECT * FROM lottery_numbers WHERE Multiplier = 2"
filtered_df = query(sql, "lottery_numbers")

# Build an interactive UI
text("Powerball Numbers")
table(filtered_df, title="Filtered Data")


# Create a visualization
fig = px.scatter(df, x="Winning Numbers", y="Draw Date", color="Multiplier")
plotly(fig)