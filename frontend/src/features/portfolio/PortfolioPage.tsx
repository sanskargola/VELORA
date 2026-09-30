import { Card } from '../../components/ui/Card';
import { PortfolioHolding } from '../../types';

const holdings: PortfolioHolding[] = [
  { symbol: 'AAPL', shares: 32, avgCost: 140.2, currentPrice: 182.4, allocation: 42 },
  { symbol: 'MSFT', shares: 18, avgCost: 388.5, currentPrice: 412.8, allocation: 35 },
  { symbol: 'NVDA', shares: 24, avgCost: 110.4, currentPrice: 121.3, allocation: 23 },
];

export function PortfolioPage() {
  return (
    <div className="space-y-6">
      <div className="grid gap-6 lg:grid-cols-[1fr_0.8fr]">
        <Card className="space-y-4">
          <h2 className="text-xl font-semibold">Holdings</h2>
          <div className="overflow-hidden rounded-2xl border border-slate-200 dark:border-slate-800">
            <table className="min-w-full text-sm">
              <thead className="bg-slate-100 dark:bg-slate-800">
                <tr>
                  <th className="px-4 py-3 text-left">Symbol</th>
                  <th className="px-4 py-3 text-left">Shares</th>
                  <th className="px-4 py-3 text-left">Cost</th>
                  <th className="px-4 py-3 text-left">Value</th>
                </tr>
              </thead>
              <tbody>
                {holdings.map((holding) => (
                  <tr key={holding.symbol} className="border-t border-slate-200 dark:border-slate-800">
                    <td className="px-4 py-3 font-medium">{holding.symbol}</td>
                    <td className="px-4 py-3">{holding.shares}</td>
                    <td className="px-4 py-3">${holding.avgCost}</td>
                    <td className="px-4 py-3">${(holding.currentPrice * holding.shares).toFixed(2)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </Card>
        <Card className="space-y-4">
          <h2 className="text-xl font-semibold">Allocation</h2>
          <div className="h-48 rounded-3xl bg-gradient-to-br from-blue-600 to-emerald-400" />
        </Card>
      </div>
      <Card className="space-y-4">
        <h2 className="text-xl font-semibold">Portfolio growth</h2>
        <div className="h-56 rounded-3xl bg-slate-100 dark:bg-slate-800" />
      </Card>
    </div>
  );
}
