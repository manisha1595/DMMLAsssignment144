import json
from datetime import datetime

metrics = {
    "source": "transformed_data.csv",
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "changelog": "Updated dataset version with cleaned data"
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print("metrics.json created successfully!")
