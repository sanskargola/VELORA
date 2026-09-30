import { Card } from '../../components/ui/Card';

export function AdminPage() {
  return (
    <div className="space-y-6">
      <div className="grid gap-4 md:grid-cols-3">
        {[
          ['Users', '1,240'],
          ['Predictions', '48,500'],
          ['System health', '99.9%']
        ].map(([label, value]) => (
          <Card key={label} className="space-y-2">
            <p className="text-sm text-slate-500">{label}</p>
            <p className="text-2xl font-semibold">{value}</p>
          </Card>
        ))}
      </div>
      <Card className="space-y-4">
        <h2 className="text-xl font-semibold">Recent prediction logs</h2>
        <div className="space-y-3">
          {['AAPL • Buy • 84% confidence', 'MSFT • Hold • 72%', 'NVDA • Sell • 68%'].map((log) => (
            <div key={log} className="rounded-2xl bg-slate-100 p-4 dark:bg-slate-800">{log}</div>
          ))}
        </div>
      </Card>
    </div>
  );
}
