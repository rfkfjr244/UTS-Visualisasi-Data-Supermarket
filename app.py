
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="Supermarket Sales Dashboard",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Supermarket Sales Performance Dashboard")
st.caption("Analisis penjualan supermarket periode Januari sampai Maret 2019")

# ==========================================
# 2. MEMUAT DATASET
# ==========================================
DATA_PATH = Path("data/processed/supermarket_sales_clean.csv")

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_PATH)
    data["Date"] = pd.to_datetime(data["Date"])
    return data

try:
    df = load_data()
except FileNotFoundError:
    st.error(
        "Dataset tidak ditemukan. Pastikan file berada di "
        "data/processed/supermarket_sales_clean.csv"
    )
    st.stop()

# ==========================================
# 3. SIDEBAR FILTER
# ==========================================
st.sidebar.header("Filter Data")

min_date = df["Date"].min().date()
max_date = df["Date"].max().date()

date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

branches = st.sidebar.multiselect(
    "Pilih Kota",
    options=sorted(df["City"].unique()),
    default=sorted(df["City"].unique())
)

categories = st.sidebar.multiselect(
    "Pilih Kategori Produk",
    options=sorted(df["Product line"].unique()),
    default=sorted(df["Product line"].unique())
)

payments = st.sidebar.multiselect(
    "Pilih Metode Pembayaran",
    options=sorted(df["Payment"].unique()),
    default=sorted(df["Payment"].unique())
)

# ==========================================
# 4. FILTER DATA
# ==========================================
if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date

filtered_df = df[
    (df["Date"].dt.date >= start_date) &
    (df["Date"].dt.date <= end_date) &
    (df["City"].isin(branches)) &
    (df["Product line"].isin(categories)) &
    (df["Payment"].isin(payments))
].copy()

if filtered_df.empty:
    st.warning("Tidak ada data untuk kombinasi filter tersebut.")
    st.stop()

# ==========================================
# 5. KPI
# ==========================================
total_revenue = filtered_df["Total"].sum()
total_transactions = filtered_df["Invoice ID"].nunique()
total_quantity = filtered_df["Quantity"].sum()
average_rating = filtered_df["Rating"].mean()

st.subheader("Ringkasan Penjualan")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Penjualan",
    f"{total_revenue:,.2f}"
)

col2.metric(
    "Total Transaksi",
    f"{total_transactions:,}"
)

col3.metric(
    "Produk Terjual",
    f"{total_quantity:,}"
)

col4.metric(
    "Rata-rata Rating",
    f"{average_rating:.2f} / 10"
)

st.divider()

# ==========================================
# 6. GRAFIK TREN PENJUALAN HARIAN
# ==========================================
st.subheader("Tren Penjualan Harian")

daily_sales = (
    filtered_df.groupby("Date", as_index=False)["Total"]
    .sum()
)

fig_daily = px.line(
    daily_sales,
    x="Date",
    y="Total",
    markers=True,
    title="Perubahan Total Penjualan Harian"
)

fig_daily.update_layout(
    xaxis_title="Tanggal",
    yaxis_title="Total Penjualan"
)

st.plotly_chart(fig_daily, use_container_width=True)

# ==========================================
# 7. GRAFIK KATEGORI PRODUK
# ==========================================
col_left, col_right = st.columns(2)

with col_left:
    category_sales = (
        filtered_df.groupby("Product line", as_index=False)["Total"]
        .sum()
        .sort_values("Total", ascending=True)
    )

    fig_category = px.bar(
        category_sales,
        x="Total",
        y="Product line",
        orientation="h",
        title="Penjualan Berdasarkan Kategori Produk"
    )

    fig_category.update_layout(
        xaxis_title="Total Penjualan",
        yaxis_title="Kategori Produk"
    )

    st.plotly_chart(fig_category, use_container_width=True)

# ==========================================
# 8. GRAFIK PENJUALAN BERDASARKAN KOTA
# ==========================================
with col_right:
    city_sales = (
        filtered_df.groupby("City", as_index=False)["Total"]
        .sum()
        .sort_values("Total", ascending=False)
    )

    fig_city = px.bar(
        city_sales,
        x="City",
        y="Total",
        title="Penjualan Berdasarkan Kota",
        text_auto=".2s"
    )

    fig_city.update_layout(
        xaxis_title="Kota",
        yaxis_title="Total Penjualan"
    )

    st.plotly_chart(fig_city, use_container_width=True)

# ==========================================
# 9. GRAFIK METODE PEMBAYARAN
# ==========================================
col_left, col_right = st.columns(2)

with col_left:
    payment_sales = (
        filtered_df.groupby("Payment", as_index=False)
        .agg(
            Transactions=("Invoice ID", "nunique"),
            Sales=("Total", "sum")
        )
    )

    fig_payment = px.pie(
        payment_sales,
        names="Payment",
        values="Transactions",
        hole=0.4,
        title="Distribusi Transaksi Berdasarkan Pembayaran"
    )

    st.plotly_chart(fig_payment, use_container_width=True)

# ==========================================
# 10. GRAFIK RATING PELANGGAN
# ==========================================
with col_right:
    fig_rating = px.scatter(
        filtered_df,
        x="Rating",
        y="Total",
        color="Customer type",
        title="Rating Pelanggan dan Total Transaksi",
        labels={
            "Rating": "Rating Pelanggan",
            "Total": "Total Transaksi"
        }
    )

    st.plotly_chart(fig_rating, use_container_width=True)

# ==========================================
# 11. INSIGHT OTOMATIS
# ==========================================
st.divider()
st.subheader("Temuan Utama Berdasarkan Filter")

best_category = (
    filtered_df.groupby("Product line")["Total"].sum().idxmax()
)

best_city = (
    filtered_df.groupby("City")["Total"].sum().idxmax()
)

best_payment = (
    filtered_df.groupby("Payment")["Invoice ID"].nunique().idxmax()
)

st.markdown(
    f"""
    1. Kategori produk dengan penjualan tertinggi adalah **{best_category}**.
    2. Kota dengan total penjualan tertinggi adalah **{best_city}**.
    3. Metode pembayaran dengan jumlah transaksi terbanyak adalah **{best_payment}**.
    4. Total penjualan berdasarkan filter saat ini mencapai **{total_revenue:,.2f}**.
    """
)

# ==========================================
# 12. TABEL DATA
# ==========================================
with st.expander("Lihat Data Transaksi"):
    st.dataframe(filtered_df, use_container_width=True)

st.caption(
    "Sumber dataset: Aung Pyae, Supermarket Sales Dataset, Kaggle."
)
