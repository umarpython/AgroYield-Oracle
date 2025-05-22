
import json

# Sample crop yield data (simulated USDA/FAO)
sample_data = [
    {"region": "Iowa", "crop": "Corn", "yield_t_per_hectare": 11.2},
    {"region": "Nebraska", "crop": "Wheat", "yield_t_per_hectare": 3.1},
    {"region": "Punjab", "crop": "Rice", "yield_t_per_hectare": 6.7},
    {"region": "Oyo", "crop": "Cassava", "yield_t_per_hectare": 13.5},
]

oracle_payload = {
    "oracle_name": "AgroYield Oracle",
    "description": "Tracks global crop yield data (tons/hectare) from public sources and makes it available onchain.",
    "data_source": "Simulated from FAO/USDA",
    "data": sample_data,
}

def save_payload():
    with open("agroyield_oracle_output.json", "w") as f:
        json.dump(oracle_payload, f, indent=2)
    print("Oracle output saved to agroyield_oracle_output.json")

if __name__ == "__main__":
    save_payload()