import { Card } from '../../components/ui/Card';
import { NewsItem } from '../../types';

const news: NewsItem[] = [
  { id: 1, title: 'Markets rally as AI demand strengthens', source: 'Bloomberg', publishedAt: '2h ago', sentiment: 'Positive' },
  { id: 2, title: 'Fed stays steady on rates amid soft landing optimism', source: 'Reuters', publishedAt: '4h ago', sentiment: 'Neutral' },
  { id: 3, title: 'Tech earnings pressure risk sentiment', source: 'CNBC', publishedAt: '6h ago', sentiment: 'Negative' },
];

export function NewsPage() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold text-slate-900 dark:text-white">News intelligence</h1>
        <p className="text-sm text-slate-500">Financial headlines, sentiment, and trending themes.</p>
      </div>
      <div className="grid gap-6 lg:grid-cols-[1.1fr_0.9fr]">
        <Card className="space-y-4">
          <h2 className="text-xl font-semibold">Latest feed</h2>
          <div className="space-y-3">
            {news.map((item) => (
              <div key={item.id} className="rounded-2xl border border-slate-200 p-4 dark:border-slate-800">
                <div className="flex items-center justify-between">
                  <h3 className="font-medium">{item.title}</h3>
                  <span className="text-sm text-slate-500">{item.publishedAt}</span>
                </div>
                <div className="mt-2 text-sm text-slate-500">{item.source} • {item.sentiment}</div>
              </div>
            ))}
          </div>
        </Card>
        <Card className="space-y-4">
          <h2 className="text-xl font-semibold">Trending topics</h2>
          <div className="space-y-3">
            {['AI Semiconductors', 'Fed Policy', 'Banking', 'Energy'].map((topic) => (
              <div key={topic} className="rounded-2xl bg-slate-100 p-4 dark:bg-slate-800">{topic}</div>
            ))}
          </div>
        </Card>
      </div>
    </div>
  );
}
