def display_dataframe_to_user(name: str, dataframe) -> None:
    """
    Displays a formatted DataFrame to the user.
    
    Args:
        name (str): Name of the DataFrame for display purposes
        dataframe (pandas.DataFrame): DataFrame to display
    """
    print(f"\n=== {name} ===\n")
    print(dataframe.to_string(index=False))