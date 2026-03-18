from etl.pipeline import transform
import pandas as pd

def test_transform():
    df = pd.DataFrame({
        "quantity": [2, 3],
        "price": [10, 20]
    })

    result = transform(df)

    assert "total" in result.columns
    assert result["total"].iloc[0] == 20