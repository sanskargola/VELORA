import { ReactNode } from 'react';
import { Card } from './Card';

interface MetricCardProps {
  title: string;
  value: string;
  detail?: string;
  icon?: ReactNode;
}

export function MetricCard({ title, value, detail, icon }: MetricCardProps) {
  return (
    <Card className="space-y-3">
      <div className="flex items-center justify-between">
        <p className="text-sm font-medium text-slate-500 dark:text-slate-400">{title}</p>
        {icon}
      </div>
      <p className="text-2xl font-semibold text-slate-900 dark:text-white">{value}</p>
      {detail ? <p className="text-sm text-emerald-500">{detail}</p> : null}
    </Card>
  );
}
