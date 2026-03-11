import pandas as pd
from typing import Dict, Any

def analyze_data(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Analyzes the sales dataframe and returns key metrics.
    Expected Columns: Date, Product_Category, Region, Units_Sold, Unit_Price, Revenue, Status
    """
    # Force column names to be stripped of whitespace
    df.columns = df.columns.str.strip()

    required_columns = ["Product_Category", "Region", "Units_Sold", "Unit_Price", "Revenue", "Status"]
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns in dataset: {', '.join(missing_columns)}. Make sure your CSV follows standard format.")

    # Data type conversions and clean ups
    df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce').fillna(0)
    df['Units_Sold'] = pd.to_numeric(df['Units_Sold'], errors='coerce').fillna(0)
    
    # Calculate key metrics
    total_revenue = float(df['Revenue'].sum())
    total_units_sold = int(df['Units_Sold'].sum())
    
    # Revenue by region
    revenue_by_region = df.groupby('Region')['Revenue'].sum().to_dict()
    
    # Top selling product category
    top_product_category = ""
    if not df.empty:
        revenue_by_category = df.groupby('Product_Category')['Revenue'].sum()
        if not revenue_by_category.empty:
            top_product_category = str(revenue_by_category.idxmax())

    # Cancelled orders count
    cancelled_orders_count = int(df[df['Status'].str.strip().str.lower() == 'cancelled'].shape[0])
    
    return {
        "Total Revenue": f"${total_revenue:,.2f}",
        "Total Units Sold": f"{total_units_sold:,}",
        "Revenue by Region": {k: f"${v:,.2f}" for k, v in revenue_by_region.items()},
        "Top Selling Product Category": top_product_category,
        "Cancelled Orders Count": cancelled_orders_count
    }
