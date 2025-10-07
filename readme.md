# SEC SWOT Analysis Dashboard

A comprehensive Python application for analyzing SEC 10-K filings and generating automated SWOT (Strengths, Weaknesses, Opportunities, Threats) reports using natural language processing and machine learning techniques.

## 🌟 Features

- **Automated SEC Filing Analysis**: Download and process 10-K filings directly from the SEC EDGAR database
- **AI-Powered SWOT Classification**: Uses machine learning to classify text into SWOT categories
- **Interactive Dashboard**: Modern Streamlit web interface with dark theme and professional styling
- **Comprehensive Visualizations**: Interactive charts and graphs powered by Plotly
- **Export Options**: Download results in CSV, JSON, and PDF formats
- **Multi-Company Support**: Analyze multiple companies and time periods
- **Real-Time Processing**: Live progress tracking during analysis

## 📊 Dashboard Preview

The application features three main modes:
- **📈 Quick Analysis**: Select a ticker and date range for automated analysis
- **📋 Upload Documents**: Process custom SEC filings (coming soon)
- **📊 View Results**: Browse and visualize previously generated reports

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd nlp-project
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard**:
   ```bash
   streamlit run dashboard.py
   ```

## 📋 Requirements

```txt
streamlit>=1.28.0
plotly>=5.15.0
pandas>=1.5.0
datamule
tqdm
pathlib
```

## 🏗️ Project Structure

```
├── dashboard.py              # Main Streamlit dashboard
├── swot_analysis.ipynb      # Jupyter notebook for SWOT analysis
├── requirements.txt         # Python dependencies
├── sec_10k_sentences.csv   # Raw SEC filing sentences
├── sec_10k_sentences_clean.csv # Cleaned sentences
├── sec_portfolio/          # Downloaded SEC filings
│   ├── 000032019323000106.tar
│   └── 000032019324000123.tar
└── sec_swot_output/        # Analysis results
    ├── index.json          # Master index of reports
    ├── swot_AAPL_*.csv    # Individual SWOT data
    └── swot_report_AAPL_*.json # Structured reports
```

## 🚀 Usage

### Quick Analysis Mode

1. Launch the dashboard: `streamlit run dashboard.py`
2. Select **📈 Quick Analysis** from the sidebar
3. Choose a company ticker (e.g., AAPL, MSFT, GOOGL)
4. Set your desired date range
5. Click **🚀 Run Analysis**
6. View results in the **📊 View Results** section

### Dashboard Navigation

#### 📈 Quick Analysis
- **Company Selection**: Choose from popular tickers (AAPL, MSFT, GOOGL, AMZN, TSLA, META, NVDA) or enter custom ticker
- **Date Range**: Set start and end dates for filing analysis (2020-2025)
- **One-Click Analysis**: Automated processing with real-time progress tracking

#### 📋 Upload Documents (Coming Soon)
- Support for `.txt`, `.pdf`, and `.html` files
- Custom document processing capabilities
- Batch upload functionality

#### 📊 View Results
- Interactive report selector
- Professional SWOT visualizations
- Detailed category breakdowns with key themes and insights
- Export options (CSV, JSON, PDF)

### Jupyter Notebook Analysis

For advanced users and development:

1. Open `swot_analysis.ipynb`
2. Configure parameters:
   ```python
   TICKERS = ["AAPL"]  # Companies to analyze
   FORMS = ["10-K"]    # SEC form types
   DATE_RANGE = ("2023-01-01", "2024-12-31")
   ```
3. Run all cells to perform analysis

## 📈 Output Files

The analysis generates several output files:

- **CSV Files**: Raw SWOT classifications with confidence scores
- **JSON Reports**: Structured reports with key themes and insights
- **Index File**: Master catalog of all generated reports

### Sample JSON Report Structure

```json
{
  "meta": {
    "ticker": "AAPL",
    "accession": "000032019324000123",
    "filing_date": "2024-11-01"
  },
  "report": {
    "Strength": {
      "count": 25,
      "top_bullets": ["Key strength indicators..."],
      "key_themes": ["company", "growth", "innovation"],
      "key_insights": ["Strategic advantages identified..."],
      "summary": "25 strength indicators found"
    },
    "Weakness": { ... },
    "Opportunity": { ... },
    "Threat": { ... }
  }
}
```

## 🎨 Dashboard Features

### Professional Dark Theme
- Gradient backgrounds and modern styling
- Color-coded SWOT categories:
  - 💪 **Strengths**: Green gradient
  - ⚠️ **Weaknesses**: Red gradient  
  - 🎯 **Opportunities**: Blue gradient
  - ⚡ **Threats**: Orange gradient

### Interactive Visualizations
- **Pie Charts**: SWOT category distribution with pull-out effects
- **Key Themes**: Highlighted tag-style display of common topics
- **Sample Evidence**: Expandable sections with filing excerpts
- **Metrics Cards**: Professional summary statistics

### Export Capabilities
- **CSV Export**: Raw classification data for further analysis
- **JSON Export**: Complete structured reports
- **PDF Generation**: Professional report formatting (coming soon)

## 🔧 Key Components

### `dashboard.py`
Main Streamlit application featuring:
- Modern dark theme with professional styling
- Interactive visualizations with Plotly
- Real-time analysis progress tracking
- Multi-format export capabilities
- Responsive design with custom CSS

### `swot_analysis.ipynb`
Core analysis engine providing:
- SEC filing download via datamule
- Text preprocessing and sentence extraction
- ML-based SWOT classification
- Report generation and export

## 🎯 SWOT Classification

The system uses keyword-based weak supervision to classify sentences:

- **Strengths**: Competitive advantages, strong performance metrics, market leadership
- **Weaknesses**: Risk factors, operational challenges, regulatory concerns
- **Opportunities**: Growth potential, market expansion, new technologies
- **Threats**: External risks, competitive pressures, economic factors

## 📊 Visualization Features

### Interactive Charts
- **Distribution Analysis**: Pie charts showing SWOT category proportions
- **Theme Analysis**: Most frequent topics per category
- **Evidence Display**: Representative sentences for each category
- **Executive Metrics**: Key performance indicators and summaries

### Professional Styling
- **Dark Theme**: Modern gradient backgrounds
- **Color Coding**: Intuitive category identification
- **Responsive Layout**: Adapts to different screen sizes
- **Professional Typography**: Clean, readable font choices

## 🔍 Data Sources

- **SEC EDGAR Database**: Official 10-K filings
- **Supported Companies**: All publicly traded US companies
- **Time Range**: 2020-present (configurable)
- **Filing Types**: 10-K annual reports (expandable)

## 🚧 Roadmap

### Near Term
- [ ] PDF document upload support
- [ ] Enhanced text preprocessing
- [ ] Batch analysis capabilities
- [ ] PDF report generation

### Medium Term
- [ ] Advanced NLP models (BERT, GPT)
- [ ] Comparative analysis across companies
- [ ] Trend analysis over time
- [ ] Email notification system

### Long Term
- [ ] Multi-language support
- [ ] Real-time market integration
- [ ] Automated report scheduling
- [ ] API development

## 🎮 Getting Started

1. **First Time Setup**:
   ```bash
   git clone <repository-url>
   cd nlp-project
   pip install -r requirements.txt
   ```

2. **Launch Dashboard**:
   ```bash
   streamlit run dashboard.py
   ```

3. **Run Your First Analysis**:
   - Navigate to "Quick Analysis" mode
   - Select "AAPL" from the ticker dropdown
   - Set date range to last year
   - Click "Run Analysis"
   - View results in "View Results" mode

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Bug Reports

Please use the GitHub Issues tab to report bugs. Include:
- Python version
- Streamlit version
- Error messages
- Steps to reproduce

## 📝 License

This project is licensed under the MIT License. See LICENSE file for details.

## 🙏 Acknowledgments

- **datamule**: For SEC filing download and processing
- **Streamlit**: For the interactive web interface framework
- **Plotly**: For advanced data visualizations
- **SEC EDGAR**: For providing public access to corporate filings

## 📞 Support

- 📧 Email: [your-email@domain.com]
- 🐛 Issues: [GitHub Issues Page]
- 📖 Docs: [Documentation Link]

---

**⚠️ Disclaimer**: This tool is for educational and research purposes. Always verify results with original SEC filings before making investment decisions. The analysis is based on automated text processing and may contain inaccuracies.

**🔒 Data Privacy**: All analysis is performed locally. No data is transmitted to external servers unless explicitly configured.