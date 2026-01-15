import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from shared.etl_logic import extract_data, transform_data

def test_etl_pipeline():
    df = extract_data("data/input/user_events.csv")
    result = transform_data(df, ["USA", "IND"])
    assert not result.empty
    print("ETL logic test passed ")

if __name__ == "__main__":
    test_etl_pipeline()
