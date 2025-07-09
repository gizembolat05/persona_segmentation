import pandas as pd
import os

def export_dataframe(df: pd.DataFrame, filename: str, folder: str = "output"):

    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)
    df.to_csv(filepath, index=False)
    print(f"[✓] Exported → {filepath}")


if __name__ == "__main__":

    agg_df = pd.read_csv("C:/Users/gizemb/Desktop/agg_df.csv")  # veya main.py'de export ettiğin path

    export_dataframe(agg_df, "persona_segments.csv")

    new_users = agg_df[agg_df["customers_level_based"].isin([
        "BRA_ANDROID_FEMALE_0_18",
        "BRA_ANDROID_FEMALE_19_23"
    ])]

    export_dataframe(new_users, "new_user_predictions.csv")
