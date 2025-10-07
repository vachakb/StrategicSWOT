import streamlit as st
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path
import subprocess
import sys
from datetime import datetime, date as dt_date  # Rename to avoid conflict
import time

# Page configuration
st.set_page_config(
    page_title="SEC SWOT Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme and professional styling
st.markdown("""
<style>
    .main > div {
        padding-top: 2rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f1419 0%, #1a1d29 100%);
    }
    
    .css-1d391kg {
        background-color: #1e2329;
    }
    
    .stSelectbox > div > div {
        background-color: #2d3748;
        color: white;
    }
    
    .stTextInput > div > div > input {
        background-color: #2d3748;
        color: white;
        border: 1px solid #4a5568;
    }
    
    .stDateInput > div > div > input {
        background-color: #2d3748;
        color: white;
        border: 1px solid #4a5568;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #2d3748 0%, #4a5568 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #4a5568;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        margin: 0.5rem 0;
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        color: #63b3ed;
        margin: 0;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #a0aec0;
        margin: 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .swot-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #63b3ed;
        margin-bottom: 1rem;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #2d3748, #4a5568);
        border-radius: 10px;
        border: 1px solid #4a5568;
    }
    
    .strength-card {
        background: linear-gradient(135deg, #22543d 0%, #2f855a 100%);
        border-left: 5px solid #38a169;
    }
    
    .weakness-card {
        background: linear-gradient(135deg, #742a2a 0%, #c53030 100%);
        border-left: 5px solid #e53e3e;
    }
    
    .opportunity-card {
        background: linear-gradient(135deg, #2a4365 0%, #3182ce 100%);
        border-left: 5px solid #4299e1;
    }
    
    .threat-card {
        background: linear-gradient(135deg, #744210 0%, #d69e2e 100%);
        border-left: 5px solid #ed8936;
    }
    
    .insight-text {
        color: #e2e8f0;
        font-size: 0.95rem;
        line-height: 1.6;
        margin: 0.5rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #3182ce, #4299e1);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #2c5aa0, #3182ce);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(49, 130, 206, 0.4);
    }
    
    .sidebar .stSelectbox > div > div {
        background-color: #2d3748;
    }
    
    .uploadedFile {
        background-color: #2d3748;
        border: 1px solid #4a5568;
        border-radius: 8px;
    }
    
    .stProgress > div > div {
        background-color: #3182ce;
    }
    
    .analysis-summary {
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%);
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid #4a5568;
        margin: 1rem 0;
    }
    
    .executive-summary {
        background: linear-gradient(135deg, #2a4365 0%, #3182ce 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Utility functions
@st.cache_data
def load_analysis_results(output_dir="sec_swot_output"):
    """Load analysis results from output directory"""
    try:
        index_file = Path(output_dir) / "index.json"
        if index_file.exists():
            with open(index_file, 'r') as f:
                return json.load(f)
        return []
    except Exception as e:
        st.error(f"Error loading results: {e}")
        return []

@st.cache_data
def load_swot_report(json_path):
    """Load SWOT report from JSON file"""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading SWOT report: {e}")
        return None

def run_analysis(ticker, start_date, end_date):
    """Run SWOT analysis for given parameters"""
    try:
        # Update config in swot_analysis.py (simplified approach)
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("🔄 Initializing analysis...")
        progress_bar.progress(20)
        
        # Import and run analysis
        import sys
        sys.path.append('.')
        
        status_text.text("📊 Running SWOT analysis...")
        progress_bar.progress(40)
        
        # This would call your existing analysis function
        from swot_analysis import analyze_portfolio
        
        # Configure parameters
        config = {
            'TICKERS': [ticker],
            'FORMS': ["10-K"],
            'DATE_RANGE': (start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")),
            'OUTPUT_DIR': "sec_swot_output",
            'PORTFOLIO_DIR': "sec_portfolio"
        }
        
        status_text.text("🔍 Processing filings...")
        progress_bar.progress(60)
        
        # Run analysis
        analyze_portfolio(
            tickers=config['TICKERS'],
            forms=config['FORMS'],
            date_range=config['DATE_RANGE'],
            output_dir=config['OUTPUT_DIR'],
            portfolio_dir=config['PORTFOLIO_DIR']
        )
        
        status_text.text("✅ Analysis complete!")
        progress_bar.progress(100)
        
        time.sleep(1)
        progress_bar.empty()
        status_text.empty()
        
        return True
        
    except Exception as e:
        st.error(f"Analysis failed: {e}")
        return False

def create_swot_visualization(report_data):
    """Create SWOT visualization charts"""
    
    # Extract counts
    categories = ['Strength', 'Weakness', 'Opportunity', 'Threat']
    counts = [report_data['report'][cat]['count'] for cat in categories]
    colors = ['#38a169', '#e53e3e', '#4299e1', '#ed8936']
    
    # Create pie chart only
    fig = go.Figure()
    
    # Pie chart
    fig.add_trace(
        go.Pie(
            labels=categories,
            values=counts,
            marker_colors=colors,
            hole=0.4,
            textinfo='label+percent+value',
            textfont=dict(color='white', size=14, family='Arial Black'),
            showlegend=True,
            textposition='outside',
            pull=[0.05, 0.05, 0.05, 0.05]  # Slightly separate all slices for better visibility
        )
    )
    
    # Update layout
    fig.update_layout(
        title=dict(
            text="SWOT Analysis Distribution",
            x=0.5,
            font=dict(size=24, color='white', family='Arial Black')
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        height=600,  # Increased height for better visibility of single chart
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.15,
            xanchor="center",
            x=0.5,
            font=dict(color='white', size=12)
        ),
        margin=dict(t=80, b=80, l=50, r=50)  # Better margins for single chart
    )
    
    return fig




def display_swot_category(category, data, card_class):
    """Display SWOT category with professional styling"""
    
    st.markdown(f"""
    <div class="metric-card {card_class}">
        <div class="swot-header">{category}</div>
        <div class="metric-value" style="text-align: center;">{data['count']}</div>
        <div class="metric-label" style="text-align: center;">Indicators Found</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Key themes with minimal height and padding
    if 'key_themes' in data and data['key_themes']:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #1a365d 0%, #2c5aa0 100%); padding: 0.5rem; border-radius: 8px; border-left: 4px solid #4299e1; margin: 0.5rem 0; box-shadow: 0 2px 4px rgba(0,0,0,0.3);">
            <h4 style="color: #63b3ed; margin: 0 0 0.3rem 0; font-size: 1.1rem; font-weight: bold; display: flex; align-items: center;">
                <span style="margin-right: 0.5rem;">🎯</span>Key Themes
            </h4>
            <div style="display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0;">
        """, unsafe_allow_html=True)
        
        # Display themes as highlighted tags
        for theme in data['key_themes']:
            st.markdown(f"""
            <span style="background: rgba(66, 153, 225, 0.2); color: #90cdf4; padding: 0.25rem 0.7rem; border-radius: 20px; font-size: 0.85rem; font-weight: 500; border: 1px solid rgba(66, 153, 225, 0.3); display: inline-block; margin: 0.1rem 0.1rem 0.1rem 0;">
                • {theme}
            </span>
            """, unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Key insights with reduced spacing
    if 'key_insights' in data and data['key_insights']:
        st.markdown("""
        <h4 style="color: #63b3ed; margin: 0.75rem 0 0.5rem 0; font-size: 1.1rem; font-weight: bold; display: flex; align-items: center;">
            <span style="margin-right: 0.5rem;">💡</span>Key Insights
        </h4>
        """, unsafe_allow_html=True)
        
        for insight in data['key_insights']:
            st.markdown(f"""
            <div style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.6; margin: 0.3rem 0 0.3rem 1.5rem; padding-left: 0.5rem; border-left: 2px solid rgba(99, 179, 237, 0.3);">
                • {insight}
            </div>
            """, unsafe_allow_html=True)
    
    # Sample evidence
    if 'top_bullets' in data and data['top_bullets']:
        with st.expander("View Sample Evidence", expanded=False):
            for i, bullet in enumerate(data['top_bullets'][:3], 1):
                st.markdown(f"**{i}.** {bullet}")




def main():
    # Header
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h1 style="color: #63b3ed; font-size: 3rem; margin: 0;">📊 SEC SWOT Analysis</h1>
        <p style="color: #a0aec0; font-size: 1.2rem; margin: 0.5rem 0;">
            Professional Financial Document Analysis Dashboard
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown("## 🎛️ Analysis Configuration")
        
        # Analysis mode
        analysis_mode = st.radio(
            "Analysis Mode",
            ["📈 Quick Analysis", "📋 Upload Documents", "📊 View Results"],
            index=0
        )
        
        if analysis_mode == "📈 Quick Analysis":
            st.markdown("### Company Selection")
            
            # Ticker input
            ticker = st.selectbox(
                "Select Ticker",
                ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA"],
                index=0
            )
            
            # Custom ticker option
            custom_ticker = st.text_input("Or enter custom ticker:")
            if custom_ticker:
                ticker = custom_ticker.upper()
            
            # Date range
            st.markdown("### Date Range")
            col1, col2 = st.columns(2)
            with col1:
                start_date = st.date_input(
                    "Start Date",
                    value=dt_date(2023, 1, 1),
                    min_value=dt_date(2020, 1, 1),
                    max_value=dt_date.today()
                )
            with col2:
                end_date = st.date_input(
                    "End Date",
                    value=dt_date(2024, 12, 31),
                    min_value=start_date,
                    max_value=dt_date(2025, 12, 31)
                )
            
            # Analysis button
            if st.button("🚀 Run Analysis", type="primary"):
                st.session_state.run_analysis = True
                st.session_state.analysis_params = {
                    'ticker': ticker,
                    'start_date': start_date,
                    'end_date': end_date
                }
        
        elif analysis_mode == "📋 Upload Documents":
            st.markdown("### Document Upload")
            uploaded_files = st.file_uploader(
                "Upload SEC Filings",
                type=['txt', 'pdf', 'html'],
                accept_multiple_files=True
            )
            
            if uploaded_files:
                st.success(f"📄 {len(uploaded_files)} files uploaded")
                if st.button("Process Documents", type="primary"):
                    st.info("Document processing feature coming soon!")

    # Main content area based on selected mode
    if analysis_mode == "📈 Quick Analysis":
        # Quick Analysis main content
        if st.session_state.get('run_analysis', False):
            params = st.session_state.get('analysis_params', {})
            
            st.markdown("## 🔄 Running Analysis")
            
            success = run_analysis(
                params['ticker'],
                params['start_date'], 
                params['end_date']
            )
            
            if success:
                st.success("✅ Analysis completed successfully!")
                st.session_state.run_analysis = False
                st.rerun()
            else:
                st.error("❌ Analysis failed. Please try again.")
                st.session_state.run_analysis = False
                return
        else:
            # Quick analysis instructions using Streamlit components
            st.markdown("""
            <div class="analysis-summary">
                <h2 style="color: #63b3ed; text-align: center; margin-top: 0;">
                    📈 Quick Analysis Mode
                </h2>
                <p style="color: #a0aec0; text-align: center; font-size: 1.1rem;">
                    Select a company ticker and date range from the sidebar, then click "Run Analysis" to generate a comprehensive SWOT report.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### How it works:")
            
            # Use Streamlit columns for the workflow
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                <div style="background: #2d3748; padding: 1.5rem; border-radius: 10px; text-align: center; height: 150px; display: flex; flex-direction: column; justify-content: center;">
                    <h4 style="color: #4299e1; margin: 0;">1. Select Company</h4>
                    <p style="color: #a0aec0; font-size: 0.9rem; margin: 0.5rem 0;">Choose from popular tickers or enter a custom one</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div style="background: #2d3748; padding: 1.5rem; border-radius: 10px; text-align: center; height: 150px; display: flex; flex-direction: column; justify-content: center;">
                    <h4 style="color: #4299e1; margin: 0;">2. Set Date Range</h4>
                    <p style="color: #a0aec0; font-size: 0.9rem; margin: 0.5rem 0;">Define the period for SEC filing analysis</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown("""
                <div style="background: #2d3748; padding: 1.5rem; border-radius: 10px; text-align: center; height: 150px; display: flex; flex-direction: column; justify-content: center;">
                    <h4 style="color: #4299e1; margin: 0;">3. Get Insights</h4>
                    <p style="color: #a0aec0; font-size: 0.9rem; margin: 0.5rem 0;">AI analyzes filings and generates SWOT report</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
            <p style="color: #63b3ed; text-align: center; font-size: 1.1rem; margin: 1rem 0;">
                Configure your analysis parameters in the sidebar →
            </p>
            """, unsafe_allow_html=True)
    
    elif analysis_mode == "📋 Upload Documents":
        # Upload Documents main content
        st.markdown("""
        <div class="analysis-summary">
            <h2 style="color: #63b3ed; text-align: center; margin-top: 0;">
                📋 Document Upload Mode
            </h2>
            <p style="color: #a0aec0; text-align: center; font-size: 1.1rem;">
                Upload your own SEC filings or financial documents for SWOT analysis.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Supported Formats:")
        
        # Use Streamlit columns for supported formats
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="background: #2d3748; padding: 1.5rem; border-radius: 10px; text-align: center; height: 120px; display: flex; flex-direction: column; justify-content: center;">
                <h4 style="color: #38a169; margin: 0;">📄 Text Files</h4>
                <p style="color: #a0aec0; font-size: 0.9rem; margin: 0.5rem 0;">.txt format documents</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: #2d3748; padding: 1.5rem; border-radius: 10px; text-align: center; height: 120px; display: flex; flex-direction: column; justify-content: center;">
                <h4 style="color: #e53e3e; margin: 0;">📕 PDF Files</h4>
                <p style="color: #a0aec0; font-size: 0.9rem; margin: 0.5rem 0;">.pdf format documents</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="background: #2d3748; padding: 1.5rem; border-radius: 10px; text-align: center; height: 120px; display: flex; flex-direction: column; justify-content: center;">
                <h4 style="color: #ed8936; margin: 0;">🌐 HTML Files</h4>
                <p style="color: #a0aec0; font-size: 0.9rem; margin: 0.5rem 0;">.html format filings</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.warning("⚠️ **Coming Soon**: Document upload functionality is currently under development. Use Quick Analysis mode to analyze SEC filings automatically.")
        
        st.info("📁 Use the file upload widget in the sidebar to get started")
    
    elif analysis_mode == "📊 View Results":
        # View Results main content (keep the existing code)
        results = load_analysis_results()
        
        if not results:
            st.markdown("""
            <div class="analysis-summary">
                <h3 style="color: #63b3ed; text-align: center;">No Analysis Results Found</h3>
                <p style="color: #a0aec0; text-align: center;">
                    Run an analysis using the Quick Analysis mode to generate SWOT reports.
                </p>
            </div>
            """, unsafe_allow_html=True)
            return
        
        # Results selector
        st.markdown("## 📈 Analysis Results")
        
        # Create options for selectbox
        options = []
        for result in results:
            ticker_name = result['ticker']
            filing_date = result.get('filing_date', 'Unknown Date')
            accession = result['accession'][:12] + "..."
            options.append(f"{ticker_name} - {filing_date} ({accession})")
        
        selected_idx = st.selectbox(
            "Select Report to View",
            range(len(options)),
            format_func=lambda x: options[x]
        )
        
        selected_result = results[selected_idx]
        
        # Load SWOT report
        report_data = load_swot_report(selected_result['json'])
        
        if not report_data:
            st.error("Failed to load SWOT report")
            return
        
        # Display company info
        meta = report_data['meta']
        
        st.markdown(f"""
        <div class="executive-summary">
            <h2 style="margin: 0; color: white;">
                🏢 {meta['ticker']} - SWOT Analysis Report
            </h2>
            <p style="margin: 0.5rem 0; opacity: 0.9;">
                <strong>Filing Date:</strong> {meta.get('filing_date', 'N/A')} | 
                <strong>Accession:</strong> {meta['accession']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Visualization
        fig = create_swot_visualization(report_data)
        st.plotly_chart(fig, use_container_width=True)
        
        # SWOT Categories
        st.markdown("## 📊 Detailed SWOT Analysis")
        
        # Create 2x2 grid for SWOT categories
        col1, col2 = st.columns(2)
        
        with col1:
            display_swot_category(
                "💪 Strengths", 
                report_data['report']['Strength'], 
                "strength-card"
            )
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            display_swot_category(
                "🎯 Opportunities", 
                report_data['report']['Opportunity'], 
                "opportunity-card"
            )
        
        with col2:
            display_swot_category(
                "⚠️ Weaknesses", 
                report_data['report']['Weakness'], 
                "weakness-card"
            )
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            display_swot_category(
                "⚡ Threats", 
                report_data['report']['Threat'], 
                "threat-card"
            )
        
        # Executive Summary (if available)
        if 'executive_overview' in report_data['report']:
            exec_summary = report_data['report']['executive_overview']
            
            st.markdown("## 📋 Executive Summary")
            
            # Metrics row
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-value">{exec_summary.get('total_indicators', 'N/A')}</div>
                    <div class="metric-label">Total Indicators</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-value">{exec_summary.get('dominant_category', 'N/A').title()}</div>
                    <div class="metric-label">Dominant Category</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                analysis_summary = exec_summary.get('analysis_summary', 'N/A')
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-value" style="font-size: 1.2rem;">{analysis_summary[:50]}...</div>
                    <div class="metric-label">Analysis Summary</div>
                </div>
                """, unsafe_allow_html=True)
        
        # Download options
        st.markdown("## 📥 Export Options")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📊 Download CSV", type="secondary"):
                csv_path = selected_result['csv']
                with open(csv_path, 'rb') as f:
                    st.download_button(
                        label="Download Raw Data",
                        data=f.read(),
                        file_name=f"swot_data_{meta['ticker']}.csv",
                        mime="text/csv"
                    )
        
        with col2:
            if st.button("📄 Download JSON", type="secondary"):
                json_data = json.dumps(report_data, indent=2)
                st.download_button(
                    label="Download Report",
                    data=json_data,
                    file_name=f"swot_report_{meta['ticker']}.json",
                    mime="application/json"
                )
        
        with col3:
            if st.button("📈 Generate PDF", type="secondary"):
                st.info("PDF generation feature coming soon!")

if __name__ == "__main__":
    main()