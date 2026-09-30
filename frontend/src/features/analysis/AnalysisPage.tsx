import { Sparkles } from 'lucide-react';
import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';

export function AnalysisPage() {
  return (
    <div className="space-y-6">
      <div className="flex flex-col gap-3 md:flex-row md:items-center md:justify-between">
        <div>
          <h1 className="text-2xl font-semibold text-slate-900 dark:text-white">Stock analysis</h1>
          <p className="text-sm text-slate-500">Candlestick view, indicators, forecasts, and news sentiment.</p>
        </div>
        <Button variant="primary">Run analysis</Button>
      </div>

      <div className="grid gap-6 lg:grid-cols-[1.2fr_0.8fr]">
        <Card className="space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-slate-500">AAPL</p>
              <h2 className="text-xl font-semibold">Apple Inc.</h2>
            </div>
            <span className="rounded-full bg-emerald-500/10 px-3 py-1 text-sm text-emerald-600">Bullish</span>
          </div>
          <div className="h-56 rounded-3xl bg-gradient-to-br from-slate-900 to-blue-500" />
        </Card>
        <Card className="space-y-4">
          <h3 className="text-lg font-semibold">Prediction card</h3>
          <div className="rounded-2xl bg-slate-100 p-4 dark:bg-slate-800">
            <div className="flex items-center gap-2 text-blue-600"><Sparkles className="h-4 w-4" /> Confidence 84%</div>
            <div className="mt-3 text-3xl font-semibold">$198.34</div>
            <div className="mt-2 text-sm text-slate-500">Recommendation: Buy</div>
          </div>
          <div className="grid gap-3 sm:grid-cols-2">
            <div className="rounded-2xl border border-slate-200 p-4 dark:border-slate-800"><div className="text-sm text-slate-500">RSI</div><div className="text-xl font-semibold">63.8</div></div>
            <div className="rounded-2xl border border-slate-200 p-4 dark:border-slate-800"><div className="text-sm text-slate-500">MACD</div><div className="text-xl font-semibold">+0.42</div></div>
          </div>
        </Card>
      </div>

      <div className="grid gap-6 lg:grid-cols-[0.8fr_1.2fr]">
        <Card className="space-y-4">
          <h3 className="text-lg font-semibold">Company info</h3>
          <div className="space-y-2 text-sm text-slate-600 dark:text-slate-400">
            <p>Sector: Consumer Electronics</p>
            <p>Market Cap: $2.8T</p>
            <p>Dividend Yield: 0.53%</p>
          </div>
        </Card>
        <Card className="space-y-4">
          <h3 className="text-lg font-semibold">Model comparison</h3>
          <div className="grid gap-3 md:grid-cols-3">
            {['LSTM', 'GRU', 'XGBoost'].map((model) => (
              <div key={model} className="rounded-2xl border border-slate-200 p-4 dark:border-slate-800">
                <div className="font-medium">{model}</div>
                <div className="mt-2 text-sm text-slate-500">Accuracy 83%</div>
                <div className="mt-1 text-sm text-emerald-500">Strong signal</div>
              </div>
            ))}
          </div>
        </Card>
      </div>
    </div>
  );
}
