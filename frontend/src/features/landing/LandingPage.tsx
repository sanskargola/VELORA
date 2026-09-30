import { Bot, ShieldCheck, Sparkles, TrendingUp, Zap } from 'lucide-react';
import { motion } from 'framer-motion';
import { Button } from '../../components/ui/Button';
import { Card } from '../../components/ui/Card';
import { SearchBar } from '../../components/ui/SearchBar';

const features = [
  { icon: Sparkles, title: 'AI Forecasting', description: 'Model-driven price forecasts with confidence scoring.' },
  { icon: ShieldCheck, title: 'Secure Workspace', description: 'Encrypted auth flows and secure API integration.' },
  { icon: TrendingUp, title: 'Live Insights', description: 'Real-time portfolio, watchlist, and market sentiment signals.' }
];

const models = ['LSTM', 'GRU', 'Transformer', 'XGBoost', 'Random Forest'];

export function LandingPage() {
  return (
    <div className="space-y-10 pb-16">
      <section className="overflow-hidden rounded-[2rem] border border-slate-200/70 bg-gradient-to-br from-blue-600 via-blue-500 to-cyan-400 p-8 text-white shadow-2xl dark:border-slate-800">
        <div className="grid gap-8 lg:grid-cols-[1.2fr_0.8fr] lg:items-center">
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="space-y-5">
            <div className="inline-flex items-center gap-2 rounded-full bg-white/15 px-3 py-1 text-sm backdrop-blur"> <Bot className="h-4 w-4" /> AI-powered stock intelligence</div>
            <h1 className="text-4xl font-semibold sm:text-5xl">Trade with the clarity of a premium fintech platform.</h1>
            <p className="max-w-2xl text-lg text-blue-50">Monitor markets, compare model forecasts, analyze sentiment, and manage portfolios from one elegant workspace.</p>
            <div className="flex flex-wrap gap-3">
              <Button variant="secondary" className="bg-white text-blue-600 hover:bg-blue-50">Start Free</Button>
              <Button variant="ghost" className="border border-white/30 text-white hover:bg-white/10">Explore Platform</Button>
            </div>
          </motion.div>
          <Card className="space-y-4 border-white/20 bg-slate-950/40 text-white">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-slate-300">Live Market Preview</p>
                <p className="text-2xl font-semibold">NASDAQ +1.24%</p>
              </div>
              <Zap className="h-8 w-8 text-amber-300" />
            </div>
            <SearchBar placeholder="Search symbols ..." />
            <div className="grid gap-3 sm:grid-cols-2">
              {['AAPL', 'MSFT', 'NVDA', 'TSLA'].map((symbol) => (
                <div key={symbol} className="rounded-2xl border border-white/10 bg-white/10 p-3">
                  <div className="text-sm text-slate-300">{symbol}</div>
                  <div className="mt-1 font-semibold">+4.8%</div>
                </div>
              ))}
            </div>
          </Card>
        </div>
      </section>

      <section className="grid gap-4 md:grid-cols-3">
        {features.map(({ icon: Icon, title, description }) => (
          <Card key={title} className="space-y-3">
            <Icon className="h-8 w-8 text-blue-600" />
            <h3 className="text-lg font-semibold text-slate-900 dark:text-white">{title}</h3>
            <p className="text-sm text-slate-600 dark:text-slate-400">{description}</p>
          </Card>
        ))}
      </section>

      <section className="grid gap-4 lg:grid-cols-[0.9fr_1.1fr]">
        <Card className="space-y-4">
          <h2 className="text-2xl font-semibold text-slate-900 dark:text-white">AI model highlights</h2>
          <div className="space-y-3">
            {models.map((model) => (
              <div key={model} className="flex items-center justify-between rounded-2xl bg-slate-100 px-4 py-3 dark:bg-slate-800">
                <span>{model}</span>
                <span className="text-sm text-emerald-500">84% accuracy</span>
              </div>
            ))}
          </div>
        </Card>
        <Card className="space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-2xl font-semibold text-slate-900 dark:text-white">Prediction confidence</h2>
            <span className="rounded-full bg-emerald-500/10 px-3 py-1 text-sm text-emerald-600">Bullish</span>
          </div>
          <div className="h-40 rounded-3xl bg-gradient-to-r from-blue-500 to-emerald-400" />
        </Card>
      </section>

      <section className="rounded-[2rem] border border-slate-200/70 bg-white/80 p-8 dark:border-slate-800 dark:bg-slate-900/80">
        <div className="mb-6 flex items-center justify-between">
          <h2 className="text-2xl font-semibold">What users say</h2>
          <Button variant="secondary">Read stories</Button>
        </div>
        <div className="grid gap-4 md:grid-cols-3">
          {['“It feels like TradingView and a premium AI research desk combined.”', '“The model comparison makes forecasting far easier.”', '“Beautiful UI, helpful signals, and fast insights.”'].map((quote) => (
            <Card key={quote} className="text-sm text-slate-600 dark:text-slate-400">{quote}</Card>
          ))}
        </div>
      </section>

      <section className="grid gap-4 lg:grid-cols-3">
        {[
          { name: 'Starter', price: '$19', features: ['5 daily predictions', 'Basic alerts'] },
          { name: 'Pro', price: '$79', features: ['Advanced ML models', 'Portfolio tracking'] },
          { name: 'Enterprise', price: 'Custom', features: ['Admin dashboards', 'API access'] }
        ].map((plan) => (
          <Card key={plan.name} className="space-y-4">
            <h3 className="text-lg font-semibold">{plan.name}</h3>
            <div className="text-4xl font-semibold">{plan.price}<span className="text-sm text-slate-500">/mo</span></div>
            <ul className="space-y-2 text-sm text-slate-600 dark:text-slate-400">
              {plan.features.map((feature) => <li key={feature}>• {feature}</li>)}
            </ul>
            <Button variant="primary" className="w-full">Choose plan</Button>
          </Card>
        ))}
      </section>
    </div>
  );
}
