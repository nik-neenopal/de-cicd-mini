from etl.pipeline import transform
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def test_transform():
    df = pd.DataFrame({
        "quantity": [2, 3],
        "price": [10, 20]
    })

    result = transform(df)

    assert "total" in result.columns
    assert result["total"].iloc[0] == 20