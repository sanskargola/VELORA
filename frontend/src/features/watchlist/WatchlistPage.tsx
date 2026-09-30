import { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { SearchBar } from '../../components/ui/SearchBar';
import { Button } from '../../components/ui/Button';

const stocks = ['AAPL', 'MSFT', 'NVDA', 'TSLA', 'AMD'];

export function WatchlistPage() {
  const [query, setQuery] = useState('');
  const filtered = stocks.filter((stock) => stock.toLowerCase().includes(query.toLowerCase()));

  return (
    <div className="space-y-6">
      <div className="flex flex-col gap-3 md:flex-row md:items-center md:justify-between">
        <div>
          <h1 className="text-2xl font-semibold text-slate-900 dark:text-white">Watchlist</h1>
          <p className="text-sm text-slate-500">Search, filter, and manage alert-ready stocks.</p>
        </div>
        <Button variant="primary">Add stock</Button>
      </div>
      <Card className="space-y-4">
        <SearchBar value={query} onChange={setQuery} placeholder="Search watchlist..." />
        <div className="grid gap-3 md:grid-cols-2">
          {filtered.map((stock) => (
            <div key={stock} className="flex items-center justify-between rounded-2xl border border-slate-200 p-4 dark:border-slate-800">
              <div>
                <div className="font-medium">{stock}</div>
                <div className="text-sm text-slate-500">Price alert enabled</div>
              </div>
              <Button variant="secondary">Remove</Button>
            </div>
          ))}
        </div>
      </Card>
    </div>
  );
}
