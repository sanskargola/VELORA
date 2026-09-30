export interface StockSummary {
  symbol: string;
  company: string;
  price: number;
  change: number;
  volume: string;
  sector: string;
}

export interface PredictionModel {
  name: string;
  accuracy: number;
  confidence: number;
  trend: 'Bullish' | 'Neutral' | 'Bearish';
}

export interface PortfolioHolding {
  symbol: string;
  shares: number;
  avgCost: number;
  currentPrice: number;
  allocation: number;
}

export interface NewsItem {
  id: number;
  title: string;
  source: string;
  publishedAt: string;
  sentiment: 'Positive' | 'Neutral' | 'Negative';
}
