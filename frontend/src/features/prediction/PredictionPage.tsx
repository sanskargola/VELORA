import { Download, Sparkles } from 'lucide-react';
import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';

export function PredictionPage() {
  return (
    <div className="space-y-6">
      <div className="flex flex-col gap-3 md:flex-row md:items-center md:justify-between">
        <div>
          <h1 className="text-2xl font-semibold text-slate-900 dark:text-white">Prediction studio</h1>
          <p className="text-sm text-slate-500">Select a symbol, timeframe, and model to generate a projection.</p>
        </div>
        <Button variant="primary" className="flex items-center gap-2"><Download className="h-4 w-4" /> Download report</Button>
      </div>

      <div className="grid gap-6 lg:grid-cols-[0.8fr_1.2fr]">
        <Card className="space-y-4">
          <label className="block text-sm font-medium">Stock</label>
          <select className="w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 dark:border-slate-800 dark:bg-slate-900">
            <option>AAPL</option><option>MSFT</option><option>NVDA</option>
          </select>
          <label className="block text-sm font-medium">Timeframe</label>
          <select className="w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 dark:border-slate-800 dark:bg-slate-900">
            <option>7 Days</option><option>30 Days</option><option>90 Days</option>
          </select>
          <label className="block text-sm font-medium">Model</label>
          <select className="w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 dark:border-slate-800 dark:bg-slate-900">
            <option>LSTM</option><option>GRU</option><option>XGBoost</option>
          </select>
        </Card>
        <Card className="space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-slate-500">Projected price</p>
              <p className="text-3xl font-semibold">$198.34</p>
            </div>
            <div className="rounded-full bg-emerald-500/10 p-3 text-emerald-600"><Sparkles className="h-5 w-5" /></div>
          </div>
          <div className="h-56 rounded-3xl bg-gradient-to-br from-blue-600 to-cyan-400" />
          <div className="grid gap-3 md:grid-cols-3">
            {['MAE 1.31', 'RMSE 1.98', 'R² 0.91'].map((metric) => <div key={metric} className="rounded-2xl border border-slate-200 p-4 text-center text-sm dark:border-slate-800">{metric}</div>)}
          </div>
        </Card>
      </div>
    </div>
  );
}
