import { Activity, ArrowUpRight, AlertTriangle, TrendingUp } from 'lucide-react';
import { Card } from '../../components/ui/Card';
import { MetricCard } from '../../components/ui/MetricCard';
import { Button } from '../../components/ui/Button';
import { StockSummary } from '../../types';

const stocks: StockSummary[] = [
  { symbol: 'AAPL', company: 'Apple', price: 182.4, change: 2.1, volume: '52.3M', sector: 'Consumer Tech' },
  { symbol: 'NVDA', company: 'NVIDIA', price: 121.3, change: 4.9, volume: '38.7M', sector: 'Semiconductors' },
  { symbol: 'MSFT', company: 'Microsoft', price: 412.8, change: -1.1, volume: '21.4M', sector: 'Cloud' },
];

export function DashboardPage() {
  return (
    <div className="space-y-6">
      <div className="grid gap-4 md:grid-cols-3">
        <MetricCard title="Portfolio Value" value="$248,430" detail="+$12.4% today" icon={<Activity className="h-5 w-5 text-blue-600" />} />
        <MetricCard title="Total P/L" value="$18,200" detail="+$1,240 this week" icon={<TrendingUp className="h-5 w-5 text-emerald-600" />} />
        <MetricCard title="Risk Score" value="Low" detail="Balanced allocation" icon={<AlertTriangle className="h-5 w-5 text-amber-600" />} />
      </div>

      <div className="grid gap-6 xl:grid-cols-[1.2fr_0.8fr]">
        <Card className="space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-xl font-semibold text-slate-900 dark:text-white">Top gainers</h2>
            <Button variant="ghost">View all</Button>
          </div>
          <div className="space-y-3">
            {stocks.map((stock) => (
              <div key={stock.symbol} className="flex items-center justify-between rounded-2xl border border-slate-200/70 bg-slate-50 px-4 py-3 dark:border-slate-800 dark:bg-slate-800/50">
                <div>
                  <div className="font-medium">{stock.symbol}</div>
                  <div className="text-sm text-slate-500">{stock.company}</div>
                </div>
                <div className="text-right">
                  <div className="font-medium">${stock.price}</div>
                  <div className={`text-sm ${stock.change > 0 ? 'text-emerald-500' : 'text-red-500'}`}>{stock.change > 0 ? '+' : ''}{stock.change}%</div>
                </div>
              </div>
            ))}
          </div>
        </Card>

        <Card className="space-y-4">
          <h2 className="text-xl font-semibold text-slate-900 dark:text-white">Recent predictions</h2>
          <div className="space-y-3">
            {['AAPL 7D Buy', 'NVDA 30D Hold', 'MSFT 14D Sell'].map((item) => (
              <div key={item} className="rounded-2xl bg-slate-100 p-4 dark:bg-slate-800">
                <div className="flex items-center justify-between">
                  <span className="font-medium">{item}</span>
                  <ArrowUpRight className="h-4 w-4 text-blue-600" />
                </div>
                <p className="mt-2 text-sm text-slate-500">Confidence 84%</p>
              </div>
            ))}
          </div>
        </Card>
      </div>

      <div className="grid gap-6 lg:grid-cols-[1fr_0.8fr]">
        <Card className="space-y-4">
          <h2 className="text-xl font-semibold text-slate-900 dark:text-white">Watchlist</h2>
          <div className="grid gap-3 md:grid-cols-2">
            {['TSLA', 'AMD', 'PLTR', 'SHOP'].map((symbol) => (
              <div key={symbol} className="rounded-2xl border border-slate-200/70 p-4 dark:border-slate-800">
                <div className="flex items-center justify-between">
                  <span className="font-medium">{symbol}</span>
                  <TrendingUp className="h-4 w-4 text-emerald-500" />
                </div>
                <div className="mt-2 text-sm text-slate-500">Momentum strong</div>
              </div>
            ))}
          </div>
        </Card>
        <Card className="space-y-4">
          <h2 className="text-xl font-semibold text-slate-900 dark:text-white">Market news</h2>
          <div className="space-y-3">
            {['Fed signals steady policy', 'AI chip rally continues', 'Energy names rebound'].map((headline) => (
              <div key={headline} className="rounded-2xl bg-slate-100 p-4 dark:bg-slate-800">
                <div className="font-medium">{headline}</div>
                <div className="mt-2 text-sm text-slate-500">Sentiment: Positive</div>
              </div>
            ))}
          </div>
        </Card>
      </div>
    </div>
  );
}
