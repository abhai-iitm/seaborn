# Customer Analytics: Response Time Distribution by Support Channel

**Email:** 21f3001705@ds.study.iitm.ac.in

## Project Overview

This project creates a professional-grade Seaborn visualization for **Schoen Rippin and Wilderman**, a data-driven customer experience company. The visualization analyzes customer support response times across different channels using a violin plot to show distribution density and quartile information.

## Business Context

A major retail client requires a publication-ready visualization for their quarterly business review, executive presentations, and strategic planning documents. The analysis focuses on support efficiency across multiple customer service channels.

## Files in Repository

- `README.md` - This documentation file with contact email
- `chart.py` - Python script using Seaborn to generate the violin plot
- `chart.png` - Generated visualization (512x512 pixels)

## Visualization Features

- **Chart Type:** Violin plot showing response time distributions
- **Data:** Synthetic customer support data across 5 channels
- **Styling:** Professional Seaborn styling suitable for executive presentations
- **Dimensions:** Exactly 512x512 pixels as required
- **Analysis:** Covers 3,500+ support interactions across multiple channels

## Support Channels Analyzed

1. **Live Chat** - Real-time support with fastest response times
2. **Email** - Asynchronous support with moderate response times  
3. **Phone** - Real-time support with quick response times
4. **Social Media** - Variable response times depending on monitoring
5. **Ticket System** - Formal support process with longer response times

## Technical Implementation

The visualization uses:
- `seaborn.violinplot()` for distribution analysis
- Professional color palette and styling
- Statistical quartile overlays
- Executive-ready formatting and annotations

## Usage

Run the Python script to generate the analysis:

```bash
python chart.py
```

This will create `chart.png` with the violin plot visualization and display summary statistics in the console.