import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';

export function ProfilePage() {
  return (
    <div className="space-y-6">
      <div className="grid gap-6 lg:grid-cols-[1fr_0.9fr]">
        <Card className="space-y-4">
          <h2 className="text-xl font-semibold">Personal information</h2>
          <div className="grid gap-3 md:grid-cols-2">
            <input className="rounded-2xl border border-slate-200 bg-white px-4 py-3 dark:border-slate-800 dark:bg-slate-900" placeholder="Full name" />
            <input className="rounded-2xl border border-slate-200 bg-white px-4 py-3 dark:border-slate-800 dark:bg-slate-900" placeholder="Email" />
          </div>
          <Button variant="primary">Save profile</Button>
        </Card>
        <Card className="space-y-4">
          <h2 className="text-xl font-semibold">Security settings</h2>
          <div className="space-y-3">
            <input className="w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 dark:border-slate-800 dark:bg-slate-900" placeholder="Current password" type="password" />
            <input className="w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 dark:border-slate-800 dark:bg-slate-900" placeholder="New password" type="password" />
          </div>
          <Button variant="secondary">Update password</Button>
        </Card>
      </div>
      <Card className="space-y-4">
        <h2 className="text-xl font-semibold">Notification preferences</h2>
        <div className="flex items-center justify-between rounded-2xl bg-slate-100 p-4 dark:bg-slate-800">
          <span>Email alerts</span>
          <input type="checkbox" className="h-4 w-4" defaultChecked />
        </div>
      </Card>
    </div>
  );
}
